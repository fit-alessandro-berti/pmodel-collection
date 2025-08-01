# Generated from: 9e7b05a8-8913-4f72-8c77-856d03f789c3.json
# Description: This process manages the complete operational cycle of an urban vertical farm specializing in multi-layer hydroponic crop production. It begins with seed selection based on climate and market demand, followed by nutrient optimization customized per plant type. Automated climate control adjusts humidity, temperature, and light spectra to maximize growth efficiency. Continuous pest monitoring uses AI-driven image recognition to detect early infestations, triggering targeted biocontrol interventions. Wastewater recycling incorporates filtration and mineral rebalancing before reuse. Harvest scheduling synchronizes with local distribution networks to ensure freshness and reduce carbon footprint. Additionally, real-time data analytics inform adaptive planting strategies, while employee training on advanced farming technologies maintains operational excellence. The process concludes with system maintenance and seasonal recalibration to prepare for subsequent cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Adjust = Transition(label='Climate Adjust')
Light_Control = Transition(label='Light Control')
Pest_Scan = Transition(label='Pest Scan')
Biocontrol_Use = Transition(label='Biocontrol Use')
Water_Filter = Transition(label='Water Filter')
Mineral_Rebalance = Transition(label='Mineral Rebalance')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Analyze = Transition(label='Data Analyze')
Harvest_Plan = Transition(label='Harvest Plan')
Logistics_Sync = Transition(label='Logistics Sync')
Employee_Train = Transition(label='Employee Train')
System_Maintain = Transition(label='System Maintain')
Cycle_Recalibrate = Transition(label='Cycle Recalibrate')
Waste_Process = Transition(label='Waste Process')
Inventory_Check = Transition(label='Inventory Check')

# 1. Seed Select → Nutrient Mix (customized per plant type)
# 2. Automated climate control adjusts humidity, temperature, and light spectra:
#    - Climate Adjust and Light Control are concurrent after Nutrient Mix
# We'll model Climate Adjust and Light Control as concurrent.

# After Climate Adjust & Light Control, Continuous Pest Monitoring:
# Pest Scan → if infestation detected, Biocontrol Use (choice)
# model choice: XOR(Pest Scan only, Pest Scan → Biocontrol Use)

# Wastewater recycling: Water Filter → Mineral Rebalance → Waste Process
# This can be concurrent with pest control and growth monitoring.

# Growth Monitor and Data Analyze are concurrent with Pest control and Wastewater recycling.

# Harvest scheduling: Harvest Plan → Logistics Sync

# Employee Train happens parallel to other operational activities

# System Maintenance and Cycle Recalibrate conclude the process (serial)

# Breakdown the concurrency groups:
# Group A: Seed Select → Nutrient Mix → parallel (Climate Adjust, Light Control)
# Group B: Pest monitoring loop:
# Pest Scan → XOR(skip, Biocontrol Use)
# Group C: Wastewater recycling: Water Filter → Mineral Rebalance → Waste Process
# Group D: Growth Monitor and Data Analyze concurrent
# Group E: Harvest Plan → Logistics Sync
# Group F: Employee Train (concurrent)
# Group G: Inventory Check (can be concurrent with others, preparation step)
# Finally: System Maintain → Cycle Recalibrate

# Build Pest monitoring choice:
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[SilentTransition(), Biocontrol_Use])
pest_monitor = StrictPartialOrder(nodes=[Pest_Scan, pest_choice])
pest_monitor.order.add_edge(Pest_Scan, pest_choice)

# Build Wastewater recycling sequence
wastewater = StrictPartialOrder(nodes=[Water_Filter, Mineral_Rebalance, Waste_Process])
wastewater.order.add_edge(Water_Filter, Mineral_Rebalance)
wastewater.order.add_edge(Mineral_Rebalance, Waste_Process)

# Climate Adjust and Light Control concurrent partial order
climate_light = StrictPartialOrder(nodes=[Climate_Adjust, Light_Control])

# Group after Nutrient Mix: concurrency of (Climate_Adjust, Light_Control, Pest Monitoring, Wastewater,
# Growth Monitor & Data Analyze, Employee Train, Inventory Check)
# Growth Monitor and Data Analyze concurrent
growth_data = StrictPartialOrder(nodes=[Growth_Monitor, Data_Analyze])

# All concurrency after Nutrient Mix:
after_nutrient_nodes = [
    climate_light,
    pest_monitor,
    wastewater,
    growth_data,
    Employee_Train,
    Inventory_Check,
]

# Make a PO with those nodes concurrent:
after_nutrient = StrictPartialOrder(nodes=after_nutrient_nodes)

# Harvest Plan → Logistics Sync sequence
harvest = StrictPartialOrder(nodes=[Harvest_Plan, Logistics_Sync])
harvest.order.add_edge(Harvest_Plan, Logistics_Sync)

# Combine after_nutrient concurrency with harvest sequence and Seed Select/Nutrient Mix sequence all in order
# Seed Select → Nutrient Mix → after_nutrient concurrency → harvest → System Maintain → Cycle Recalibrate

# Seed_Select to Nutrient_Mix sequence
seed_nutrient = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix])
seed_nutrient.order.add_edge(Seed_Select, Nutrient_Mix)

# After Nutrient Mix, order to after_nutrient concurrency nodes (concurrent nodes start after Nutrient Mix)
# So add edges Nutrient_Mix → each node in after_nutrient_nodes

# We do this by building a new StrictPartialOrder with all nodes:
nodes_all = [Seed_Select, Nutrient_Mix]
# flatten after_nutrient nodes:
for node in after_nutrient_nodes:
    if isinstance(node, StrictPartialOrder) or isinstance(node, OperatorPOWL):
        nodes_all.append(node)
    else:
        nodes_all.append(node)
nodes_all.append(harvest)
nodes_all.append(System_Maintain)
nodes_all.append(Cycle_Recalibrate)

root = StrictPartialOrder(nodes=nodes_all)

# order edges:
# Seed_Select → Nutrient_Mix
root.order.add_edge(Seed_Select, Nutrient_Mix)
# Nutrient_Mix → each node in after_nutrient concurrency group
for n in after_nutrient_nodes:
    root.order.add_edge(Nutrient_Mix, n)
# after_nutrient concurrency has internal orders already
# after_nutrient nodes are concurrent among each other

# Nutrient_Mix → Harvest sequence (harvest should start after all concurrency or in parallel?)
# The description says: Harvest scheduling synchronizes with local distribution networks to ensure freshness and reduce footprint.
# This suggests it depends on growth etc., so start after concurrency ends.
# We'll model that Harvest start after all concurrency nodes.

# So, add edges from all concurrency nodes to harvest
for n in after_nutrient_nodes:
    root.order.add_edge(n, harvest)

# Harvest sequence's internal order already exists
harvest.order.add_edge(Harvest_Plan, Logistics_Sync)

# Harvest → System Maintain → Cycle Recalibrate
root.order.add_edge(harvest, System_Maintain)
root.order.add_edge(System_Maintain, Cycle_Recalibrate)

# No explicit order for Employee_Train and Inventory_Check except after Nutrient_Mix
# which is already modeled.

# Return root