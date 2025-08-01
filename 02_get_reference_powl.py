#!/usr/bin/env python3

import os
import sys
import json
import threading
import queue
import argparse
import traceback
import requests
import pm4py
import time
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Environment
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: OPENAI_API_KEY not set", file=sys.stderr)
    sys.exit(1)

# Parse model argument first to use it for default paths
parser = argparse.ArgumentParser(description="Generate POWL models and Petri nets from textual descriptions.")
parser.add_argument("--model", type=str, default="gpt-4.1-mini", help="OpenAI model to use")

# Parse just the model argument first
args, remaining_argv = parser.parse_known_args()
model_name = args.model

# Now add the remaining arguments with defaults based on the model
parser.add_argument("--input-dir", type=str, default="models/textual_descriptions", help="Directory of input JSON files")
parser.add_argument("--max-threads", type=int, default=50, help="Max concurrent threads")
parser.add_argument("--powl-dir", type=str, default=f"models/{model_name}/powl", help="Directory to save generated POWL Python files")
parser.add_argument("--vis-dir", type=str, default=f"models/{model_name}/visualization", help="Directory to save Petri net visualizations")
parser.add_argument("--max-global-retries", type=int, default=10, help="Maximum number of global retry attempts")
parser.add_argument("--retry-delay", type=int, default=5, help="Delay in seconds between global retries")

# Parse all arguments
args = parser.parse_args()

INPUT_DIR = args.input_dir
POWL_DIR = args.powl_dir
VIS_DIR = args.vis_dir
MAX_THREADS = args.max_threads
MODEL = args.model
MAX_GLOBAL_RETRIES = args.max_global_retries
RETRY_DELAY = args.retry_delay

# Prepare directories
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(POWL_DIR, exist_ok=True)
os.makedirs(VIS_DIR, exist_ok=True)

# Track failed files for retry
failed_files = set()
lock = threading.Lock()

# Worker function
def worker(file_queue, processed_counter, error_counter, total_files):
    thread_name = threading.current_thread().name
    
    while True:
        try:
            fname = file_queue.get_nowait()
        except queue.Empty:
            break
            
        base = fname[:-5]
        print(f"{thread_name}: Processing {fname}")
        
        try:
            # Load descriptor
            input_path = os.path.join(INPUT_DIR, fname)
            with open(input_path, 'r', encoding='utf-8') as f:
                desc_json = json.load(f)
                
            description = desc_json.get('description')
            activities = desc_json.get('activities')
            
            if not description or not activities:
                raise ValueError('Missing description or activities in JSON')

            # Build comprehensive prompt
            prompt = (
                "Generate a POWL model for the following process, saving the final result in the variable 'root'.\n"
                "A partially ordered workflow language (POWL) is a partially ordered graph representation of a process, extended with control-flow operators for modeling choice and loop structures. There are four types of POWL models:\n"
                "- an activity (identified by its label, e.g., 'M' identifies the activity M). Silent activities with empty labels (tau labels) are also supported.\n"
                "- a choice of other POWL models (exclusive choice: X(A, B)).\n"
                "- a loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit.\n"
                "- a partial order: PO=(nodes={...}, order={...}), where order is a set of source-->target dependencies; unconnected nodes are concurrent.\n"
                "Example 1: PO=(nodes={NODE1, NODE2}, order={})\n"
                "Example 2: PO=(nodes={NODE1, NODE2}, order={NODE1-->NODE2})\n"
                "Example 3: PO=(nodes={NODE1, NODE2, NODE3, X(NODE4, NODE5)}, order={NODE1-->NODE2, NODE1-->X(NODE4, NODE5), NODE2-->X(NODE4, NODE5)})\n"
                "POWL classes in pm4py.objects.powl.obj:\n"
                "- SilentTransition(): silent transition\n"
                "- Transition(label): labeled transition\n"
                "- StrictPartialOrder(nodes=[...]) with .order.add_edge(src, tgt)\n"
                "- OperatorPOWL(operator=Operator.XOR or Operator.LOOP, children=[...])\n"
                "Example code:\n"
                "import pm4py\n"
                "from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition\n"
                "from pm4py.objects.process_tree.obj import Operator\n"
                "A = Transition(label='A')\n"
                "B = Transition(label='B')\n"
                "C = Transition(label='C')\n"
                "skip = SilentTransition()\n"
                "loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])\n"
                "xor = OperatorPOWL(operator=Operator.XOR, children=[C, skip])\n"
                "root = StrictPartialOrder(nodes=[loop, xor])\n"
                "root.order.add_edge(loop, xor)\n"
                f"NOW, generate the POWL model for the process below.\n"
                f"DESCRIPTION: {description}\n"
                f"ACTIVITIES (use these exactly, same names): {activities}\n"
                "Respond with valid Python code only, defining 'root'."
            )

            payload = {
                'model': MODEL,
                'messages': [{'role': 'user', 'content': prompt}],
                'max_completion_tokens': 8000,
            }
            
            # API call with retry logic
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    resp = requests.post(
                        API_URL, 
                        headers={
                            'Authorization': f"Bearer {API_KEY}", 
                            'Content-Type': 'application/json'
                        }, 
                        json=payload, 
                        timeout=120  # 2 minutes timeout
                    )
                    resp.raise_for_status()
                    break
                except requests.exceptions.RequestException as e:
                    if attempt == max_retries - 1:
                        raise
                    print(f"{thread_name}: API request failed (attempt {attempt + 1}/{max_retries}): {e}")
                    time.sleep(2)  # Brief delay before retry
                    
            response_json = resp.json()
            if 'choices' not in response_json or len(response_json['choices']) == 0:
                raise ValueError("Invalid API response: no choices returned")
                
            code = response_json['choices'][0]['message']['content'].strip()
            
            # Strip code fences if present
            if code.startswith('```'):
                lines = code.split('\n')
                if lines[0].startswith('```'):
                    lines = lines[1:]
                if lines[-1] == '```':
                    lines = lines[:-1]
                code = '\n'.join(lines)

            # Execute code in a controlled environment
            local_env = {
                'pm4py': pm4py,
                'StrictPartialOrder': StrictPartialOrder,
                'OperatorPOWL': OperatorPOWL,
                'Transition': Transition,
                'SilentTransition': SilentTransition,
                'Operator': Operator
            }
            
            exec(code, local_env, local_env)
            powl_model = local_env.get('root')
            
            if powl_model is None:
                raise ValueError("Generated code did not set 'root' variable")

            # Convert to Petri net
            net, im, fm = pm4py.convert_to_petri_net(powl_model)
            
            # Validate activities
            visible_transitions = [t for t in net.transitions if t.label is not None]
            generated_labels = set(t.label for t in visible_transitions)
            expected_labels = set(activities)
            
            if expected_labels != generated_labels:
                raise ValueError(
                    f"Activity set mismatch:\n"
                    f"  Expected: {sorted(expected_labels)}\n"
                    f"  Generated: {sorted(generated_labels)}\n"
                    f"  Missing: {sorted(expected_labels - generated_labels)}\n"
                    f"  Extra: {sorted(generated_labels - expected_labels)}"
                )

            # Save Python code
            powl_path = os.path.join(POWL_DIR, base + '.py')
            with open(powl_path, 'w', encoding='utf-8') as f:
                f.write(f"# Generated from: {fname}\n")
                f.write(f"# Description: {description}\n\n")
                f.write("import pm4py\n")
                f.write("from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition\n")
                f.write("from pm4py.objects.process_tree.obj import Operator\n\n")
                f.write(code)

            # Save visualization
            svg_path = os.path.join(VIS_DIR, base + '.svg')
            pm4py.save_vis_petri_net(net, im, fm, svg_path)

            with lock:
                processed_counter[0] += 1
                # Remove from failed files if it was there
                failed_files.discard(fname)
                print(f"{thread_name}: [{processed_counter[0]}/{total_files}] Success: {base}")
                
        except Exception as e:
            with lock:
                error_counter[0] += 1
                failed_files.add(fname)
                print(f"{thread_name}: Error processing {fname}: {str(e)}")
                if args.max_threads == 1:  # Only print full traceback in single-threaded mode
                    traceback.print_exc()
        finally:
            file_queue.task_done()
            
    print(f"{thread_name} exiting.")

def process_files():
    """Process all unprocessed files and return the number of errors"""
    # Queue of files to process
    file_queue = queue.Queue()
    
    # Find unprocessed files
    for fname in os.listdir(INPUT_DIR):
        if not fname.endswith('.json'):
            continue
        base = fname[:-5]
        powl_file = os.path.join(POWL_DIR, base + '.py')
        if not os.path.exists(powl_file):
            file_queue.put(fname)
    
    total = file_queue.qsize()
    if total == 0:
        return 0
    
    print(f"\nFound {total} unprocessed descriptors. Launching up to {MAX_THREADS} threads.")
    
    # Counters
    processed_counter = [0]  # Using list to make it mutable in threads
    error_counter = [0]
    
    # Launch threads
    threads = []
    num_threads = min(MAX_THREADS, total)
    
    for i in range(num_threads):
        t = threading.Thread(
            target=worker, 
            args=(file_queue, processed_counter, error_counter, total),
            name=f"Worker-{i+1}"
        )
        t.start()
        threads.append(t)
    
    # Wait for completion
    for t in threads:
        t.join()
    
    print(f"Iteration complete. Successfully processed {processed_counter[0]}/{total} files.")
    if error_counter[0] > 0:
        print(f"Encountered errors in {error_counter[0]} files.")
    
    return error_counter[0]

# Main loop - repeat until no errors
attempt = 0
while attempt < MAX_GLOBAL_RETRIES:
    attempt += 1
    print(f"\n{'='*60}")
    print(f"GLOBAL ATTEMPT {attempt}/{MAX_GLOBAL_RETRIES}")
    print(f"{'='*60}")
    
    # Clear the failed files set at the start of each attempt
    failed_files.clear()
    
    errors = process_files()
    
    if errors == 0:
        print("\n✅ All files processed successfully!")
        sys.exit(0)
    
    if attempt < MAX_GLOBAL_RETRIES:
        print(f"\n⚠️  {errors} files failed. Retrying in {RETRY_DELAY} seconds...")
        time.sleep(RETRY_DELAY)
    else:
        print(f"\n❌ Failed to process all files after {MAX_GLOBAL_RETRIES} attempts.")
        print(f"Failed files: {sorted(failed_files)}")
        sys.exit(1)