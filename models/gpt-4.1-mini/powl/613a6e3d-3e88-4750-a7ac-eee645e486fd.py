# Generated from: 613a6e3d-3e88-4750-a7ac-eee645e486fd.json
# Description: This process details the complex cycle of managing an urban vertical farm that integrates hydroponics and AI-driven environmental controls to optimize crop yield in limited city spaces. The process includes seed selection based on market demand, automated nutrient mixing, real-time climate adjustments, pest detection through machine vision, and dynamic harvesting schedules. It also incorporates waste recycling from plant residue into biofertilizers, energy management through solar and battery systems, and data analysis for continuous improvement. The cycle ends with distribution logistics tailored for last-mile urban delivery, ensuring freshness and minimal carbon footprint while maintaining regulatory compliance and consumer feedback integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Setup = Transition(label='Plant Setup')
Climate_Tune = Transition(label='Climate Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Scan = Transition(label='Pest Scan')
Water_Supply = Transition(label='Water Supply')
Light_Adjust = Transition(label='Light Adjust')
Bio_Waste = Transition(label='Bio Waste')
Energy_Manage = Transition(label='Energy Manage')
Harvest_Plan = Transition(label='Harvest Plan')
Crop_Pick = Transition(label='Crop Pick')
Pack_Order = Transition(label='Pack Order')
Delivery_Route = Transition(label='Delivery Route')
Feedback_Log = Transition(label='Feedback Log')
Data_Analyze = Transition(label='Data Analyze')

# Build partial orders and loops according to the process description

# 1. Seed selection based on market demand -> Nutrient Mix -> Plant Setup
setup_po = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix, Plant_Setup])
setup_po.order.add_edge(Seed_Select, Nutrient_Mix)
setup_po.order.add_edge(Nutrient_Mix, Plant_Setup)

# 2. Climate Tune, Water Supply, Light Adjust are concurrent preparatory adjustments after plant setup
environment_po = StrictPartialOrder(
    nodes=[Climate_Tune, Water_Supply, Light_Adjust]
)
# No order edges: concurrent

# 3. Growth Monitor runs alongside Pest Scan (parallel monitoring)
monitor_po = StrictPartialOrder(
    nodes=[Growth_Monitor, Pest_Scan]
)
# No order: concurrent

# 4. Bio Waste and Energy Manage are waste recycling and energy management, can be done concurrently anytime after Plant Setup
waste_energy_po = StrictPartialOrder(
    nodes=[Bio_Waste, Energy_Manage]
)
# No order edges: concurrent

# 5. Harvest Plan loops with Crop Pick and Pack Order - planning the harvesting schedule, picking crops, packing orders repeated with updates
harvest_loop_body = StrictPartialOrder(
    nodes=[Crop_Pick, Pack_Order]
)
harvest_loop_body.order.add_edge(Crop_Pick, Pack_Order)

harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Plan, harvest_loop_body])

# 6. Delivery Route - logistic distribution stage after packing
# 7. Feedback Log and Data Analyze run concurrently after Delivery Route for continuous improvement
post_deliver_po = StrictPartialOrder(
    nodes=[Delivery_Route, Feedback_Log, Data_Analyze]
)
post_deliver_po.order.add_edge(Delivery_Route, Feedback_Log)
post_deliver_po.order.add_edge(Delivery_Route, Data_Analyze)

# Compose the whole partial order structure

# After Plant Setup, run environment tuning, monitoring, waste/energy, and the harvest loop concurrently
post_setup_nodes = [environment_po, monitor_po, waste_energy_po, harvest_loop]
post_setup_po = StrictPartialOrder(nodes=post_setup_nodes)
# No explicit order edges among them so they are concurrent

# Finally link setup -> post_setup -> post_deliver
root = StrictPartialOrder(nodes=[setup_po, post_setup_po, post_deliver_po])
root.order.add_edge(setup_po, post_setup_po)
root.order.add_edge(post_setup_po, post_deliver_po)