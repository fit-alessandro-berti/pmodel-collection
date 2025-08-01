# Generated from: b692e74c-a887-4025-91a2-f3266ebcb373.json
# Description: This process outlines the comprehensive cycle of urban vertical farming operations, integrating advanced hydroponic systems with AI-driven environmental controls and community engagement initiatives. It begins with seed selection based on local climate data, followed by nutrient solution preparation and precise planting schedules. Throughout growth, AI monitors plant health and adjusts light, humidity, and nutrient delivery to optimize yield. Periodic pest detection employs bio-control agents to maintain organic standards. Harvesting is synchronized with demand forecasts to minimize waste. Post-harvest, produce undergoes quality grading and packaging using sustainable materials. The cycle concludes with data analytics to refine future crops and community workshops to promote urban agriculture awareness, creating a resilient, eco-friendly food production loop within city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Setup = Transition(label='Plant Setup')

# Loop body: AI Monitor, Env Adjust, Pest Detect, Bio Control, Growth Audit
# Pest Detect leads to Bio Control (sequence), others concurrent except this dependency
AI_Monitor = Transition(label='AI Monitor')
Env_Adjust = Transition(label='Env Adjust')
Pest_Detect = Transition(label='Pest Detect')
Bio_Control = Transition(label='Bio Control')
Growth_Audit = Transition(label='Growth Audit')

# Loop condition to exit: Demand Sync, Harvest Plan, Quality Check, Eco Package
Demand_Sync = Transition(label='Demand Sync')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Eco_Package = Transition(label='Eco Package')

# After loop: Data Review, Crop Forecast, Community Train, Waste Manage
Data_Review = Transition(label='Data Review')
Crop_Forecast = Transition(label='Crop Forecast')
Community_Train = Transition(label='Community Train')
Waste_Manage = Transition(label='Waste Manage')

# Construct partial order for loop body
body_nodes = [AI_Monitor, Env_Adjust, Pest_Detect, Bio_Control, Growth_Audit]
body_po = StrictPartialOrder(nodes=body_nodes)
# Pest Detect --> Bio Control
body_po.order.add_edge(Pest_Detect, Bio_Control)
# All others can be concurrent, no other dependencies needed

# Construct partial order for loop condition (the choice after body)
condition_nodes = [Demand_Sync, Harvest_Plan, Quality_Check, Eco_Package]
condition_po = StrictPartialOrder(nodes=condition_nodes)
# No dependencies given, treat concurrent

# Loop node: execute body, then choose to exit (condition) or do condition then body again
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_po, condition_po])

# Initial sequence: Seed Select --> Nutrient Mix --> Plant Setup --> loop
start_po = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix, Plant_Setup, loop])
start_po.order.add_edge(Seed_Select, Nutrient_Mix)
start_po.order.add_edge(Nutrient_Mix, Plant_Setup)
start_po.order.add_edge(Plant_Setup, loop)

# After loop completes, perform final partial order with Data Review, Crop Forecast, Community Train, Waste Manage
final_nodes = [Data_Review, Crop_Forecast, Community_Train, Waste_Manage]

final_po = StrictPartialOrder(nodes=final_nodes)
# No internal order, concurrent

# Full model nodes: start_po (includes loop) and final_po nodes
root = StrictPartialOrder(nodes=[start_po] + final_nodes)
# start_po --> all final nodes (all start after loop done)
for node in final_nodes:
    root.order.add_edge(start_po, node)