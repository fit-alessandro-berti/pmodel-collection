# Generated from: e01de5dc-964d-49a5-8d9b-25e36abc0945.json
# Description: This process outlines the end-to-end management of an urban vertical farming system that integrates automated nutrient delivery, climate control, pest management, and crop harvesting within a multi-level indoor environment. The cycle begins with seed selection and germination under controlled light spectrums, followed by transplanting seedlings into hydroponic towers. Nutrient mixing and precise pH balancing ensure optimal growth conditions, while AI-powered sensors continuously monitor humidity, temperature, and CO2 levels. Pest detection triggers environmentally friendly interventions, avoiding chemical use. Harvesting is scheduled by maturity models and robots collect produce for packaging. Waste is composted on-site and water is recycled to minimize resource use, closing the loop for sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Select = Transition(label='Seed Select')
Germinate_Seeds = Transition(label='Germinate Seeds')
Transplant_Seedlings = Transition(label='Transplant Seedlings')
Mix_Nutrients = Transition(label='Mix Nutrients')
Adjust_pH = Transition(label='Adjust pH')
Monitor_Climate = Transition(label='Monitor Climate')
Control_Humidity = Transition(label='Control Humidity')
CO2_Regulation = Transition(label='CO2 Regulation')
Detect_Pests = Transition(label='Detect Pests')
Deploy_Biocontrols = Transition(label='Deploy Biocontrols')
Schedule_Harvest = Transition(label='Schedule Harvest')
Automate_Picking = Transition(label='Automate Picking')
Package_Produce = Transition(label='Package Produce')
Compost_Waste = Transition(label='Compost Waste')
Recycle_Water = Transition(label='Recycle Water')
Data_Logging = Transition(label='Data Logging')
System_Maintenance = Transition(label='System Maintenance')

# Climate monitoring partial order (concurrent monitoring of three sensors)
climate_monitoring = StrictPartialOrder(
    nodes=[Monitor_Climate, Control_Humidity, CO2_Regulation]
)
# No order between these three, so concurrent

# Pest management choice: either pest detected and biocontrol deployed or no pest detected (silent)
skip = SilentTransition()
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[Deploy_Biocontrols, skip])

# Pest handling subtree: Detect Pests -> (Deploy Biocontrols or skip)
pest_handling = StrictPartialOrder(nodes=[Detect_Pests, pest_choice])
pest_handling.order.add_edge(Detect_Pests, pest_choice)

# Nutrient management partial order: Mix Nutrients then Adjust pH (sequential)
nutrient_management = StrictPartialOrder(
    nodes=[Mix_Nutrients, Adjust_pH]
)
nutrient_management.order.add_edge(Mix_Nutrients, Adjust_pH)

# Harvesting partial order: Schedule Harvest -> Automate Picking -> Package Produce
harvest_seq = StrictPartialOrder(
    nodes=[Schedule_Harvest, Automate_Picking, Package_Produce]
)
harvest_seq.order.add_edge(Schedule_Harvest, Automate_Picking)
harvest_seq.order.add_edge(Automate_Picking, Package_Produce)

# Waste management concurrent with harvest completion: Compost Waste and Recycle Water concurrent
waste_management = StrictPartialOrder(
    nodes=[Compost_Waste, Recycle_Water]
)
# Concurrent, no order between Compost_Waste and Recycle_Water

# Data Logging and System Maintenance done concurrently with waste management and harvest
# We'll put Data Logging and System Maintenance concurrent too at the end

# Combine Harvest, Waste, Data Logging and System Maintenance into one partial order:
finalization_nodes = [harvest_seq, waste_management, Data_Logging, System_Maintenance]

finalization = StrictPartialOrder(nodes=finalization_nodes)
# harvest_seq before waste_management, Data Logging and System Maintenance can be done concurrently with waste management
# From description, harvesting schedules and robots collect produce, then waste composted and water recycled,
# data logging and maintenance ongoing.
# We'll order harvest_seq before waste_management, and make Data_Logging and System_Maintenance independent (concurrent)

finalization.order.add_edge(harvest_seq, waste_management)
# No edges to/from Data_Logging and System_Maintenance -> concurrently done

# Initial part: Seed Select -> Germinate Seeds -> Transplant Seedlings -> Nutrient Management -> Climate Monitoring -> Pest Handling -> Finalization

root = StrictPartialOrder(
    nodes=[
        Seed_Select,
        Germinate_Seeds,
        Transplant_Seedlings,
        nutrient_management,
        climate_monitoring,
        pest_handling,
        finalization
    ]
)

# Define the process order edges:

root.order.add_edge(Seed_Select, Germinate_Seeds)
root.order.add_edge(Germinate_Seeds, Transplant_Seedlings)
root.order.add_edge(Transplant_Seedlings, nutrient_management)
root.order.add_edge(nutrient_management, climate_monitoring)
root.order.add_edge(climate_monitoring, pest_handling)
root.order.add_edge(pest_handling, finalization)