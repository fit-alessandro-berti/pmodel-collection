#!/usr/bin/env python3

import os
import threading
import uuid
import json
import requests
import argparse
import sys

# Base API settings
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: The OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
    sys.exit(1)

# Command-line arguments
parser = argparse.ArgumentParser(
    description="Generate business process descriptions using OpenAI API."
)
parser.add_argument(
    "--count", type=int, default=1000,
    help="Number of process descriptions to generate (default: 1000)"
)
parser.add_argument(
    "--max-threads", type=int, default=30,
    help="Maximum number of concurrent threads (default: 30)"
)
parser.add_argument(
    "--output-dir", type=str, default="models",
    help="Base output directory (default: models)"
)
args = parser.parse_args()

TARGET_COUNT = args.count
MAX_THREADS = args.max_threads
BASE_OUTPUT_DIR = args.output_dir
SUBDIR = "textual_descriptions"
FULL_OUTPUT_DIR = os.path.join(BASE_OUTPUT_DIR, SUBDIR)
os.makedirs(FULL_OUTPUT_DIR, exist_ok=True)

# Thread-safe counter and lock
lock = threading.Lock()
created_count = 0

# Check activity name constraints
def activity_valid(name):
    if not isinstance(name, str):
        return False
    if len(name) > 20:
        return False
    # Count words by splitting on whitespace
    if len(name.split()) > 2:
        return False
    return True

# Function to call the OpenAI API and validate the response
def generate_process():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    prompt = (
        "Please provide a complex business process description that is atypical but still realistic. "
        "Each activity name must be short (max 2 words, max 20 characters). "
        "Return the result in JSON format with the following structure:\n"
        "{\n"
        '  "title": "A short title for the process",\n'
        '  "description": "The description of the process with >= 300 characters",\n'
        '  "activities": [/* at least 15 different activities, each max 2 words and 20 chars */]\n'
        "}\n"
        "Respond with valid JSON only and no additional text."
    )
    payload = {
        "model": "gpt-4.1-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{threading.current_thread().name}: Request error: {e}", file=sys.stderr)
        return None

    try:
        text = response.json()["choices"][0]["message"]["content"].strip()
    except (KeyError, ValueError) as e:
        print(f"{threading.current_thread().name}: Failed to parse API response: {e}", file=sys.stderr)
        return None

    # Strip markdown fences if present
    if text.startswith("```"):
        text = text.strip("```json").strip("```")

    try:
        result = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"{threading.current_thread().name}: Invalid JSON: {e}", file=sys.stderr)
        return None

    # Validation
    desc = result.get("description", "")
    acts = result.get("activities", [])
    valid = (
        isinstance(result, dict)
        and "title" in result
        and isinstance(desc, str)
        and len(desc) >= 300
        and isinstance(acts, list)
        and len(acts) >= 15
        and all(activity_valid(a) for a in acts)
    )
    if valid:
        return result

    # Log validation failure details
    print(f"{threading.current_thread().name}: Validation failed - \
          Title present: {'title' in result}, \
          Description length: {len(desc)}, \
          Activities count: {len(acts)}, \
          Activities valid: {all(activity_valid(a) for a in acts)}", file=sys.stderr)
    return None

# Worker thread function
def worker():
    global created_count
    thread_name = threading.current_thread().name
    print(f"{thread_name} started.")
    while True:
        with lock:
            if created_count >= TARGET_COUNT:
                break
        process = generate_process()
        if process:
            guid = str(uuid.uuid4())
            file_path = os.path.join(FULL_OUTPUT_DIR, f"{guid}.json")
            try:
                with open(file_path, "w") as f:
                    json.dump(process, f, indent=2)
                with lock:
                    created_count += 1
                    current = created_count
                print(f"{thread_name}: [{current}/{TARGET_COUNT}] Saved: {file_path}")
            except IOError as e:
                print(f"{thread_name}: File write error: {e}", file=sys.stderr)
        else:
            print(f"{thread_name}: Invalid response or validation failed, retrying...")
    print(f"{thread_name} exiting.")

# Main execution
print(f"Launching generation: {TARGET_COUNT} processes with up to {MAX_THREADS} threads.")
threads = []
for i in range(MAX_THREADS):
    t = threading.Thread(target=worker, name=f"Worker-{i+1}")
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Completed: Generated {created_count} processes. Files are in '{FULL_OUTPUT_DIR}'.")
