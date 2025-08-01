# Generated from: 92edc857-826f-4e36-86eb-17062eccc3a1.json
# Description: This process outlines the complete operational cycle of an urban vertical farming system that integrates hydroponics, AI-driven environmental controls, and real-time market analytics. The cycle starts with seed selection based on predictive demand, moves through nutrient calibration and climate optimization, incorporates pest monitoring using drones, and involves staggered harvesting coordinated with automated packaging. Post-harvest, produce quality is assessed by computer vision systems, and inventory levels are updated in cloud-based supply chain software. Finally, waste materials are processed into biofertilizers, closing the loop in a sustainable urban agriculture ecosystem designed to maximize yield and minimize resource consumption within constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Demand_Forecast = Transition(label='Demand Forecast')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Adjust = Transition(label='Climate Adjust')
Plant_Monitor = Transition(label='Plant Monitor')
Drone_Inspect = Transition(label='Drone Inspect')
Pest_Control = Transition(label='Pest Control')
Growth_Track = Transition(label='Growth Track')
Harvest_Plan = Transition(label='Harvest Plan')
Automate_Pack = Transition(label='Automate Pack')
Quality_Scan = Transition(label='Quality Scan')
Inventory_Update = Transition(label='Inventory Update')
Market_Sync = Transition(label='Market Sync')
Waste_Process = Transition(label='Waste Process')
Biofertilizer = Transition(label='Biofertilizer')

# Loop over pest monitoring: Plant Monitor then Drone Inspect then Pest Control repeated until exit
pest_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Plant_Monitor,
    OperatorPOWL(operator=Operator.XOR, children=[Drone_Inspect, Pest_Control])
])

# The main process flow:
# Seed Select -> Demand Forecast -> Nutrient Mix -> Climate Adjust -> pest_monitor_loop -> Growth Track -> Harvest Plan -> Automate Pack -> Quality Scan -> Inventory Update -> Market Sync -> Waste_Process -> Biofertilizer
nodes = [Seed_Select, Demand_Forecast, Nutrient_Mix, Climate_Adjust, pest_monitor_loop,
         Growth_Track, Harvest_Plan, Automate_Pack, Quality_Scan, Inventory_Update,
         Market_Sync, Waste_Process, Biofertilizer]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Seed_Select, Demand_Forecast)
root.order.add_edge(Demand_Forecast, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Climate_Adjust)
root.order.add_edge(Climate_Adjust, pest_monitor_loop)
root.order.add_edge(pest_monitor_loop, Growth_Track)
root.order.add_edge(Growth_Track, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Automate_Pack)
root.order.add_edge(Automate_Pack, Quality_Scan)
root.order.add_edge(Quality_Scan, Inventory_Update)
root.order.add_edge(Inventory_Update, Market_Sync)
root.order.add_edge(Market_Sync, Waste_Process)
root.order.add_edge(Waste_Process, Biofertilizer)