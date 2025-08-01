# Generated from: 1b4b65a2-799b-406b-8a13-744384d4c512.json
# Description: This process orchestrates the development of breakthrough innovations by integrating multiple industry perspectives, combining technological scouting, cross-sector brainstorming, rapid prototyping, and iterative validation with external ecosystem partners. It involves continuous feedback loops between R&D, market analysis, and legal compliance to ensure novel solutions meet regulatory standards and market needs. The workflow emphasizes adaptive resource allocation, risk assessment, and knowledge transfer across departments to accelerate time-to-market while maintaining quality and sustainability standards, ultimately fostering a culture of collaborative creativity within complex organizational structures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Tech_Scouting = Transition(label='Tech Scouting')
Idea_Harvest = Transition(label='Idea Harvest')
Partner_Align = Transition(label='Partner Align')
Concept_Sketch = Transition(label='Concept Sketch')
Resource_Map = Transition(label='Resource Map')
Risk_Assess = Transition(label='Risk Assess')
Prototype_Build = Transition(label='Prototype Build')
User_Testing = Transition(label='User Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Legal_Review = Transition(label='Legal Review')
Market_Scan = Transition(label='Market Scan')
Budget_Adjust = Transition(label='Budget Adjust')
Knowledge_Share = Transition(label='Knowledge Share')
Iterate_Design = Transition(label='Iterate Design')
Launch_Prep = Transition(label='Launch Prep')
Post_Launch = Transition(label='Post Launch')
Sustain_Audit = Transition(label='Sustain Audit')

# Model continuous feedback loop between R&D (Prototype_Build), Market Scan, Legal Review and Feedback Loop
# Loop(A,B): A then (exit or B then A again)
# Here:
#   A = StrictPartialOrder with Prototype_Build, User_Testing, Feedback_Loop in partial order
#   B = Parallel branches of Market_Scan, Legal_Review feeding back to feedback loop

# R&D core sequence:
rnd_core = StrictPartialOrder(nodes=[Prototype_Build, User_Testing, Feedback_Loop])
rnd_core.order.add_edge(Prototype_Build, User_Testing)
rnd_core.order.add_edge(User_Testing, Feedback_Loop)

# Feedback sub-loop activities: Market_Scan, Legal_Review concurrent before feeding back
feedback_proc = StrictPartialOrder(nodes=[Market_Scan, Legal_Review, Feedback_Loop])
# To model feedback: Market_Scan and Legal_Review before Feedback_Loop -> loop restart
feedback_proc.order.add_edge(Market_Scan, Feedback_Loop)
feedback_proc.order.add_edge(Legal_Review, Feedback_Loop)

# Loop node: main loop of prototype testing and feedback iteration
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[rnd_core, feedback_proc])

# Initial idea generation and alignment phases with partial order and some concurrency
init_generation = StrictPartialOrder(nodes=[Tech_Scouting, Idea_Harvest, Partner_Align, Concept_Sketch])
init_generation.order.add_edge(Tech_Scouting, Idea_Harvest)
init_generation.order.add_edge(Idea_Harvest, Partner_Align)
init_generation.order.add_edge(Partner_Align, Concept_Sketch)

# Resource allocation, risk assessment and budget adjustment concurrent after concept sketch
res_risk_budget = StrictPartialOrder(
    nodes=[Resource_Map, Risk_Assess, Budget_Adjust]
)
# Concurrency: no edges -> all concurrent

# Enforce Concept_Sketch precedes these three
res_risk_budget.order.add_edge(Resource_Map, Risk_Assess)  # Set some order to avoid full concurrency cycle
res_risk_budget.order.add_edge(Resource_Map, Budget_Adjust)
# Actually to allow concurrency among Resource_Map, Risk_Assess, Budget_Adjust, remove edges
# But POWL strictly needs partial order: no edges means all concurrent
# So remove edges to allow concurrency:
res_risk_budget = StrictPartialOrder(
    nodes=[Resource_Map, Risk_Assess, Budget_Adjust]
)
# Add Concept_Sketch --> Resource_Map, Concept_Sketch --> Risk_Assess, Concept_Sketch --> Budget_Adjust via a partial order combining both

pre_loop = StrictPartialOrder(
    nodes=[Concept_Sketch, Resource_Map, Risk_Assess, Budget_Adjust]
)
pre_loop.order.add_edge(Concept_Sketch, Resource_Map)
pre_loop.order.add_edge(Concept_Sketch, Risk_Assess)
pre_loop.order.add_edge(Concept_Sketch, Budget_Adjust)

# Knowledge Share concurrent with above phases but before next iteration
knowledge_phase = Knowledge_Share

# Iterate Design is part of loop continuation after feedback loop; connects to feedback_loop via iterate design
iterate_design = Iterate_Design

# Compose loop exit and continuation sequence after feedback_loop:
# After feedback_loop finished, transition to Iterate Design then loop again or exit to launch prep

# Model a LOOP of (feedback_loop) with (iterate_design) as B in loop, but we've modeled feedback_loop as big loop already.
# Instead model:
# X(Launch Prep, Loop again with iterate design leading back to feedback loop)

# Loop for iterative design and feedback again before launch prep
# Outer loop:
outer_loop_body = StrictPartialOrder(nodes=[iterate_design, feedback_loop])
outer_loop_body.order.add_edge(iterate_design, feedback_loop)  # finish iterate design then restart feedback loop

outer_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, outer_loop_body])

# Launch Prep after outer loop exits
launch_prep = Launch_Prep

# Post Launch and Sustain Audit after launch prep, sequential
post_proc = StrictPartialOrder(nodes=[Post_Launch, Sustain_Audit])
post_proc.order.add_edge(Post_Launch, Sustain_Audit)

# Build whole process partial order:
# Start: init_generation -> pre_loop -> knowledge_share (parallel with pre_loop) -> outer_loop -> launch_prep -> post_proc

# knowledge_share concurrent with pre_loop nodes
start_phase = StrictPartialOrder(
    nodes=[init_generation, pre_loop, knowledge_phase]
)
# link init_generation --> pre_loop
start_phase.order.add_edge(init_generation, pre_loop)
# knowledge_share concurrent with pre_loop, but comes after init_generation roughly:
start_phase.order.add_edge(init_generation, knowledge_phase)

# combine start_phase with outer_loop and launch_prep and post_proc

root = StrictPartialOrder(
    nodes=[start_phase, outer_loop, launch_prep, post_proc]
)
root.order.add_edge(start_phase, outer_loop)
root.order.add_edge(outer_loop, launch_prep)
root.order.add_edge(launch_prep, post_proc)