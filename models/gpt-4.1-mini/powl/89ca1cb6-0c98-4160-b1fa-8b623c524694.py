# Generated from: 89ca1cb6-0c98-4160-b1fa-8b623c524694.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a dense city environment. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, and community integration strategies. The process requires coordinating multidisciplinary teams to address challenges such as limited space, energy efficiency, waste management, and crop selection tailored for vertical growth. Continuous monitoring and adaptive adjustments ensure sustainable yield and environmental compliance, ultimately fostering local food production in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Cycle = Transition(label='Water Cycle')
Crop_Select = Transition(label='Crop Select')
Lighting_Tune = Transition(label='Lighting Tune')
Energy_Audit = Transition(label='Energy Audit')
Waste_Plan = Transition(label='Waste Plan')
Pollination_Aid = Transition(label='Pollination Aid')
Pest_Control = Transition(label='Pest Control')
Data_Monitor = Transition(label='Data Monitor')
Yield_Review = Transition(label='Yield Review')
Community_Meet = Transition(label='Community Meet')
Regulation_Check = Transition(label='Regulation Check')
Supply_Chain = Transition(label='Supply Chain')

# Structure:
# Site Survey --> Design Layout --> System Build
po1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, System_Build])
po1.order.add_edge(Site_Survey, Design_Layout)
po1.order.add_edge(Design_Layout, System_Build)

# Climate Setup --> Nutrient Mix --> Water Cycle form a PO (some steps concurrent)
# Nutrient Mix and Water Cycle can run concurrently after Climate Setup
po2 = StrictPartialOrder(
    nodes=[Climate_Setup, Nutrient_Mix, Water_Cycle]
)
po2.order.add_edge(Climate_Setup, Nutrient_Mix)
po2.order.add_edge(Climate_Setup, Water_Cycle)

# After Water Cycle and Nutrient Mix, Crop Select and Lighting Tune can run in parallel
po3 = StrictPartialOrder(
    nodes=[Crop_Select, Lighting_Tune]
)
# They are concurrent, no edges

# Energy Audit --> Waste Plan (sequential)
po4 = StrictPartialOrder(
    nodes=[Energy_Audit, Waste_Plan]
)
po4.order.add_edge(Energy_Audit, Waste_Plan)

# Pollination Aid and Pest Control can be done concurrently after Waste Plan
po5 = StrictPartialOrder(
    nodes=[Pollination_Aid, Pest_Control]
)
# concurrent, no edges

# Loop for monitoring and adjusting: Data Monitor followed by Yield Review,
# then choice to exit or repeat Data Monitor (loop between Data Monitor and Yield Review)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP, children=[Data_Monitor, Yield_Review]
)

# Community Meet --> Regulation Check --> Supply Chain (sequential)
po6 = StrictPartialOrder(
    nodes=[Community_Meet, Regulation_Check, Supply_Chain]
)
po6.order.add_edge(Community_Meet, Regulation_Check)
po6.order.add_edge(Regulation_Check, Supply_Chain)

# Compose the large partial order:

# po1 (Site Survey to System Build)
# then po2 (Climate Setup + Nutrient Mix + Water Cycle)
# then po3 (Crop Select, Lighting Tune)
# then po4 (Energy Audit --> Waste Plan)
# then po5 (Pollination Aid, Pest Control)
# then monitor_loop
# then po6 (Community Meet --> Regulation Check --> Supply Chain)
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5, monitor_loop, po6]
)

# Add the edges to define partial order among these blocks
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, po4)
root.order.add_edge(po4, po5)
root.order.add_edge(po5, monitor_loop)
root.order.add_edge(monitor_loop, po6)