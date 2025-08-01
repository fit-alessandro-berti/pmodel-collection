# Generated from: 39f719ae-3b71-4c93-adf3-f776109a8ead.json
# Description: This process outlines the complex, atypical workflow of managing an urban vertical farm that integrates hydroponics, AI-driven climate control, and automated harvesting. Starting with seed selection based on predictive analytics, it includes nutrient solution calibration, multi-layer crop monitoring, pest bio-control deployment, and dynamic light spectrum adjustment. The cycle further incorporates waste recycling into compost, energy consumption optimization, and real-time data reporting to stakeholders. This holistic approach ensures sustainable production, maximizes yield within confined urban spaces, and adapts continuously to environmental changes and market demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Solution_Mix = Transition(label='Solution Mix')
Climate_Setup = Transition(label='Climate Setup')
Light_Tuning = Transition(label='Light Tuning')
Crop_Monitoring = Transition(label='Crop Monitoring')
Pest_Control = Transition(label='Pest Control')
Growth_Analysis = Transition(label='Growth Analysis')
Energy_Audit = Transition(label='Energy Audit')
Water_Recycling = Transition(label='Water Recycling')
Nutrient_Refill = Transition(label='Nutrient Refill')
Waste_Compost = Transition(label='Waste Compost')
Harvest_Prep = Transition(label='Harvest Prep')
Automated_Pick = Transition(label='Automated Pick')
Data_Reporting = Transition(label='Data Reporting')
Market_Sync = Transition(label='Market Sync')
Equipment_Check = Transition(label='Equipment Check')
System_Update = Transition(label='System Update')

# PO1: Initial sequence: Seed Selection -> Solution Mix
PO1 = StrictPartialOrder(nodes=[Seed_Selection, Solution_Mix])
PO1.order.add_edge(Seed_Selection, Solution_Mix)

# PO2: Climate Setup and Light Tuning run concurrently after Solution Mix
PO2 = StrictPartialOrder(nodes=[Climate_Setup, Light_Tuning])
# no edges: concurrent

# PO3: Crop Monitoring -> Pest Control
PO3 = StrictPartialOrder(nodes=[Crop_Monitoring, Pest_Control])
PO3.order.add_edge(Crop_Monitoring, Pest_Control)

# PO4: Growth Analysis, Energy Audit, Water Recycling run concurrently after Pest Control
PO4 = StrictPartialOrder(nodes=[Growth_Analysis, Energy_Audit, Water_Recycling])
# no edges: concurrent

# PO5: After Water Recycling -> Nutrient Refill -> Waste Compost sequence
PO5 = StrictPartialOrder(nodes=[Water_Recycling, Nutrient_Refill, Waste_Compost])
PO5.order.add_edge(Water_Recycling, Nutrient_Refill)
PO5.order.add_edge(Nutrient_Refill, Waste_Compost)

# PO6: Harvest Prep -> Automated Pick sequence
PO6 = StrictPartialOrder(nodes=[Harvest_Prep, Automated_Pick])
PO6.order.add_edge(Harvest_Prep, Automated_Pick)

# PO7: Data Reporting -> Market Sync
PO7 = StrictPartialOrder(nodes=[Data_Reporting, Market_Sync])
PO7.order.add_edge(Data_Reporting, Market_Sync)

# PO8: Equipment Check -> System Update
PO8 = StrictPartialOrder(nodes=[Equipment_Check, System_Update])
PO8.order.add_edge(Equipment_Check, System_Update)

# After Solution Mix, dependencies:
# Solution Mix --> { Climate Setup, Light Tuning }
# Climate Setup, Light Tuning --> Crop Monitoring
PO2_and_PO3 = StrictPartialOrder(
    nodes=[Climate_Setup, Light_Tuning, Crop_Monitoring, Pest_Control]
)
PO2_and_PO3.order.add_edge(Climate_Setup, Crop_Monitoring)
PO2_and_PO3.order.add_edge(Light_Tuning, Crop_Monitoring)
PO2_and_PO3.order.add_edge(Crop_Monitoring, Pest_Control)

# PO4 and PO5 integration:
# Pest Control --> Growth Analysis, Energy Audit, Water Recycling
# Growth Analysis, Energy Audit concurrent with Water Recycling, but Water Recycling precedes Nutrient Refill -> Waste Compost
PO4_PO5 = StrictPartialOrder(
    nodes=[Growth_Analysis, Energy_Audit, Water_Recycling, Nutrient_Refill, Waste_Compost]
)
# Pest Control precedes PO4 nodes: edges added in main combined PO
# within PO4_PO5:
PO4_PO5.order.add_edge(Water_Recycling, Nutrient_Refill)
PO4_PO5.order.add_edge(Nutrient_Refill, Waste_Compost)

# Combine PO4_PO5 and PO6:
# Waste Compost precedes Harvest Prep (so harvesting happens after waste handling)
PO6_nodes = [Harvest_Prep, Automated_Pick]

# PO7 (data reporting -> market sync) happens after Automated Pick
# PO8 (equipment check -> system update) runs concurrently but likely after Market Sync (or can be concurrent)
# For simplicity, treat PO8 concurrent with PO7

# Build the big PO stepwise:

# Start from PO1: Seed_Selection -> Solution_Mix
# Then Solution_Mix precedes Climate_Setup and Light_Tuning (PO2)
# Climate_Setup & Light_Tuning -> Crop_Monitoring -> Pest_Control (PO2_and_PO3)
# Pest_Control -> Growth_Analysis, Energy_Audit, Water_Recycling (PO4_PO5)
# Water_Recycling -> Nutrient_Refill -> Waste_Compost
# Waste_Compost -> Harvest_Prep -> Automated_Pick
# Automated_Pick -> Data_Reporting -> Market_Sync
# Market_Sync concurrent with Equipment_Check -> System_Update

root = StrictPartialOrder(
    nodes=[
        Seed_Selection, Solution_Mix,
        Climate_Setup, Light_Tuning,
        Crop_Monitoring, Pest_Control,
        Growth_Analysis, Energy_Audit, Water_Recycling,
        Nutrient_Refill, Waste_Compost,
        Harvest_Prep, Automated_Pick,
        Data_Reporting, Market_Sync,
        Equipment_Check, System_Update
    ]
)

# Define order edges
root.order.add_edge(Seed_Selection, Solution_Mix)

root.order.add_edge(Solution_Mix, Climate_Setup)
root.order.add_edge(Solution_Mix, Light_Tuning)

root.order.add_edge(Climate_Setup, Crop_Monitoring)
root.order.add_edge(Light_Tuning, Crop_Monitoring)

root.order.add_edge(Crop_Monitoring, Pest_Control)

root.order.add_edge(Pest_Control, Growth_Analysis)
root.order.add_edge(Pest_Control, Energy_Audit)
root.order.add_edge(Pest_Control, Water_Recycling)

root.order.add_edge(Water_Recycling, Nutrient_Refill)
root.order.add_edge(Nutrient_Refill, Waste_Compost)

root.order.add_edge(Waste_Compost, Harvest_Prep)
root.order.add_edge(Harvest_Prep, Automated_Pick)

root.order.add_edge(Automated_Pick, Data_Reporting)
root.order.add_edge(Data_Reporting, Market_Sync)

root.order.add_edge(Equipment_Check, System_Update)
# Equipment_Check and Market_Sync run concurrently (no edge between Market_Sync and Equipment_Check)