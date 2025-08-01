# Generated from: 3fcba11c-d263-44a0-95cf-9991d5c50dd4.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm that integrates sustainable practices, IoT monitoring, and community engagement. It begins with seed selection based on climate data and market trends, followed by nutrient optimization using hydroponic systems. Continuous environmental adjustments ensure optimal growth, while real-time data analytics predict harvest times. Post-harvest, crops undergo quality assessment and packaging tailored for local distribution. The cycle incorporates waste recycling through composting and energy recovery. Finally, the process concludes with customer feedback integration and adaptive planning for subsequent planting cycles, ensuring both ecological balance and economic viability within an urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Seed_Select = Transition(label='Seed Select')
Climate_Analyze = Transition(label='Climate Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
System_Calibrate = Transition(label='System Calibrate')
Planting_Setup = Transition(label='Planting Setup')
Growth_Monitor = Transition(label='Growth Monitor')
Environment_Adjust = Transition(label='Environment Adjust')
Data_Analyze = Transition(label='Data Analyze')
Pest_Inspect = Transition(label='Pest Inspect')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Harvest = Transition(label='Crop Harvest')
Quality_Check = Transition(label='Quality Check')
Package_Prepare = Transition(label='Package Prepare')
Waste_Process = Transition(label='Waste Process')
Energy_Recover = Transition(label='Energy Recover')
Distribute_Local = Transition(label='Distribute Local')
Feedback_Collect = Transition(label='Feedback Collect')
Cycle_Review = Transition(label='Cycle Review')

# Build partial orders based on the process description

# Initial preparation: Seed_Select -> Climate_Analyze -> Nutrient_Mix -> System_Calibrate -> Planting_Setup
prep = StrictPartialOrder(nodes=[Seed_Select, Climate_Analyze, Nutrient_Mix, System_Calibrate, Planting_Setup])
prep.order.add_edge(Seed_Select, Climate_Analyze)
prep.order.add_edge(Climate_Analyze, Nutrient_Mix)
prep.order.add_edge(Nutrient_Mix, System_Calibrate)
prep.order.add_edge(System_Calibrate, Planting_Setup)

# Growth phase with loops: growth_monitoring and environmental adjustment with pest inspection in parallel
# The growth phase is iterative and continuous environmental adjustments + pest inspections
# Model Growth_Monitor and Environment_Adjust as concurrent with Pest_Inspect following Growth_Monitor
growth_adjust = StrictPartialOrder(nodes=[Growth_Monitor, Environment_Adjust, Pest_Inspect])
growth_adjust.order.add_edge(Growth_Monitor, Pest_Inspect)  # Pest inspection after monitoring
# Environment_Adjust concurrent (no order added)

# Loop on growth_adjust: after pest inspection, it can loop back to Growth_Monitor or exit (via loop operator)
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, OperatorPOWL(operator=Operator.XOR, children=[Environment_Adjust, Pest_Inspect])])
# However, PM4Py loop expects children = [body, redo]
# We'll model the loop as: body = growth cycle (Growth_Monitor + Environment_Adjust + Pest_Inspect), redo = silent exit or continue
# This is complex, so instead break down:

# Loop body: Growth_Monitor -> Environment_Adjust and Pest_Inspect after Growth_Monitor
growth_body = StrictPartialOrder(nodes=[Growth_Monitor, Environment_Adjust, Pest_Inspect])
growth_body.order.add_edge(Growth_Monitor, Environment_Adjust)
growth_body.order.add_edge(Growth_Monitor, Pest_Inspect)

# Pest_Inspect and Environment_Adjust concurrent after Growth_Monitor => remove ordering between Environment_Adjust and Pest_Inspect
# We have environment_adjust and pest_inspect concurrent after growth_monitor

# To model concurrency of Environment_Adjust and Pest_Inspect, don't add edge between them
# But both after Growth_Monitor:
growth_body = StrictPartialOrder(nodes=[Growth_Monitor, Environment_Adjust, Pest_Inspect])
growth_body.order.add_edge(Growth_Monitor, Environment_Adjust)
growth_body.order.add_edge(Growth_Monitor, Pest_Inspect)

# Loop redo branch: none or silent transition (exit)
skip = SilentTransition()

# Loop node with body growth_body and redo skip
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_body, skip])

# After growth loop, proceed to Data Analyze and Harvest Plan sequential
harvest_plan_order = StrictPartialOrder(nodes=[Data_Analyze, Harvest_Plan])
harvest_plan_order.order.add_edge(Data_Analyze, Harvest_Plan)

# Harvest activities: Crop Harvest -> Quality Check -> Package Prepare
harvest = StrictPartialOrder(nodes=[Crop_Harvest, Quality_Check, Package_Prepare])
harvest.order.add_edge(Crop_Harvest, Quality_Check)
harvest.order.add_edge(Quality_Check, Package_Prepare)

# Waste and Energy recovery in parallel, then join before Distribute Local
waste_energy = StrictPartialOrder(nodes=[Waste_Process, Energy_Recover])
# No edges for concurrency

# Distribution after waste + energy recovery
distribution = StrictPartialOrder(nodes=[Distribute_Local])
# Edges from both waste and energy to distribution
waste_energy_dist = StrictPartialOrder(nodes=[Waste_Process, Energy_Recover, Distribute_Local])
waste_energy_dist.order.add_edge(Waste_Process, Distribute_Local)
waste_energy_dist.order.add_edge(Energy_Recover, Distribute_Local)

# Feedback and review after distribution sequentially
feedback_review = StrictPartialOrder(nodes=[Feedback_Collect, Cycle_Review])
feedback_review.order.add_edge(Feedback_Collect, Cycle_Review)

# Compose the full linear partial order:
# Prep -> loop_growth -> harvest_plan_order -> harvest -> waste_energy_dist -> feedback_review

nodes_all = [
    prep,
    loop_growth,
    harvest_plan_order,
    harvest,
    waste_energy_dist,
    feedback_review
]

root = StrictPartialOrder(nodes=nodes_all)
root.order.add_edge(prep, loop_growth)
root.order.add_edge(loop_growth, harvest_plan_order)
root.order.add_edge(harvest_plan_order, harvest)
root.order.add_edge(harvest, waste_energy_dist)
root.order.add_edge(waste_energy_dist, feedback_review)