# Generated from: 808a64a4-a89e-473b-8423-3e1418a72c01.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, environmental control calibration, nutrient solution preparation, seed selection, and automated planting. Continuous monitoring of plant growth, pest detection using AI, and adaptive lighting adjustments are essential. The process also includes waste recycling, data analytics for yield optimization, and community engagement for local distribution. Finally, the system undergoes periodic maintenance and scalability evaluation to ensure sustainable production and economic viability in a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Env_Calibration = Transition(label='Env Calibration')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Prep = Transition(label='Nutrient Prep')
Automated_Plant = Transition(label='Automated Plant')
Pest_Detection = Transition(label='Pest Detection')
Lighting_Adjust = Transition(label='Lighting Adjust')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analyze = Transition(label='Data Analyze')
Yield_Optimize = Transition(label='Yield Optimize')
Community_Engage = Transition(label='Community Engage')
System_Maintain = Transition(label='System Maintain')
Scale_Evaluate = Transition(label='Scale Evaluate')

# Step 1: Initial sequence - Site Survey -> System Design -> Env Calibration
initial_seq = StrictPartialOrder(nodes=[Site_Survey, System_Design, Env_Calibration])
initial_seq.order.add_edge(Site_Survey, System_Design)
initial_seq.order.add_edge(System_Design, Env_Calibration)

# Step 2: Parallel branch after Env Calibration:
# One branch: Nutrient Prep -> Seed Selection -> Automated Plant
nutrient_branch = StrictPartialOrder(nodes=[Nutrient_Prep, Seed_Selection, Automated_Plant])
nutrient_branch.order.add_edge(Nutrient_Prep, Seed_Selection)
nutrient_branch.order.add_edge(Seed_Selection, Automated_Plant)

# The other branch represents the continuous monitoring loop:
# The "monitoring" loop consists of Growth Monitor -> Pest Detection -> Lighting Adjust repeating
# Implemented as loop: LOOP(body=A, redo=B)
monitor_body = Growth_Monitor
monitor_redo = StrictPartialOrder(nodes=[Pest_Detection, Lighting_Adjust])
monitor_redo.order.add_edge(Pest_Detection, Lighting_Adjust)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, monitor_redo])

# Step 3: The monitoring loop and nutrient branch run in parallel after Env Calibration
parallel_monitor_nutrient = StrictPartialOrder(nodes=[nutrient_branch, monitor_loop])

# Step 4: After the parallel activities, add Waste Recycle, Data Analyze, Yield Optimize in sequence
post_parallel_seq = StrictPartialOrder(nodes=[Waste_Recycle, Data_Analyze, Yield_Optimize])
post_parallel_seq.order.add_edge(Waste_Recycle, Data_Analyze)
post_parallel_seq.order.add_edge(Data_Analyze, Yield_Optimize)

# Step 5: Community Engage happens after Yield Optimize
community = Community_Engage

# Step 6: Finally, System Maintain -> Scale Evaluate in sequence
final_maintenance = StrictPartialOrder(nodes=[System_Maintain, Scale_Evaluate])
final_maintenance.order.add_edge(System_Maintain, Scale_Evaluate)

# Now connect all parts respecting the partial order:

# Start by putting initial_seq and parallel_monitor_nutrient and post_parallel_seq and community and final_maintenance into one PO
nodes_main = [initial_seq, parallel_monitor_nutrient, post_parallel_seq, community, final_maintenance]
root = StrictPartialOrder(nodes=nodes_main)

# Order: initial_seq finishes before parallel_monitor_nutrient
root.order.add_edge(initial_seq, parallel_monitor_nutrient)
# parallel_monitor_nutrient finishes before post_parallel_seq
root.order.add_edge(parallel_monitor_nutrient, post_parallel_seq)
# post_parallel_seq before community
root.order.add_edge(post_parallel_seq, community)
# community before final_maintenance
root.order.add_edge(community, final_maintenance)