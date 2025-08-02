# Generated from: 749248a6-464c-46f5-8ef7-e327b481a336.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It encompasses site assessment, environmental control system design, selecting crop varieties optimized for vertical growth, and integrating IoT sensors for continuous monitoring. The process also involves securing permits, designing hydroponic and aeroponic systems, training staff on sustainable farming techniques, and establishing a supply chain for distribution. Emphasis is placed on energy efficiency, waste recycling, and community engagement to ensure both economic viability and social impact in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Permit_Apply = Transition(label='Permit Apply')
Crop_Select = Transition(label='Crop Select')
System_Design = Transition(label='System Design')
Sensor_Deploy = Transition(label='Sensor Deploy')
Energy_Audit = Transition(label='Energy Audit')
Waste_Plan = Transition(label='Waste Plan')
Staff_Train = Transition(label='Staff Train')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Aeroponic_Install = Transition(label='Aeroponic Install')
Irrigation_Test = Transition(label='Irrigation Test')
Climate_Control = Transition(label='Climate Control')
Supply_Chain = Transition(label='Supply Chain')
Quality_Check = Transition(label='Quality Check')
Community_Meet = Transition(label='Community Meet')
Launch_Event = Transition(label='Launch Event')

# Step 1: Site Survey --> Permit Apply
step1 = StrictPartialOrder(nodes=[Site_Survey, Permit_Apply])
step1.order.add_edge(Site_Survey, Permit_Apply)

# Step 2: Crop Select after Permit Apply
step2 = StrictPartialOrder(nodes=[Permit_Apply, Crop_Select])
step2.order.add_edge(Permit_Apply, Crop_Select)

# Step 3: System Design after Crop Select
step3 = StrictPartialOrder(nodes=[Crop_Select, System_Design])
step3.order.add_edge(Crop_Select, System_Design)

# Step 4: Sensor Deploy after System Design
step4 = StrictPartialOrder(nodes=[System_Design, Sensor_Deploy])
step4.order.add_edge(System_Design, Sensor_Deploy)

# Step 5: Energy Audit and Waste Plan are concurrent, both after Sensor Deploy
energy_waste = StrictPartialOrder(nodes=[Sensor_Deploy, Energy_Audit, Waste_Plan])
energy_waste.order.add_edge(Sensor_Deploy, Energy_Audit)
energy_waste.order.add_edge(Sensor_Deploy, Waste_Plan)

# Step 6: After Energy Audit and Waste Plan, Staff Train
staff_train = StrictPartialOrder(nodes=[Energy_Audit, Waste_Plan, Staff_Train])
staff_train.order.add_edge(Energy_Audit, Staff_Train)
staff_train.order.add_edge(Waste_Plan, Staff_Train)

# Step 7: Hydroponic Setup and Aeroponic Install are concurrent after Staff Train
hydro_aero = StrictPartialOrder(nodes=[Staff_Train, Hydroponic_Setup, Aeroponic_Install])
hydro_aero.order.add_edge(Staff_Train, Hydroponic_Setup)
hydro_aero.order.add_edge(Staff_Train, Aeroponic_Install)

# Step 8: Irrigation Test and Climate Control concurrent after both Hydroponic Setup and Aeroponic Install
irrigation_climate = StrictPartialOrder(
    nodes=[Hydroponic_Setup, Aeroponic_Install, Irrigation_Test, Climate_Control]
)
irrigation_climate.order.add_edge(Hydroponic_Setup, Irrigation_Test)
irrigation_climate.order.add_edge(Aeroponic_Install, Irrigation_Test)
irrigation_climate.order.add_edge(Hydroponic_Setup, Climate_Control)
irrigation_climate.order.add_edge(Aeroponic_Install, Climate_Control)

# Step 9: Supply Chain after Irrigation Test and Climate Control
supply_chain = StrictPartialOrder(
    nodes=[Irrigation_Test, Climate_Control, Supply_Chain])
supply_chain.order.add_edge(Irrigation_Test, Supply_Chain)
supply_chain.order.add_edge(Climate_Control, Supply_Chain)

# Step 10: Quality Check after Supply Chain
quality_check = StrictPartialOrder(nodes=[Supply_Chain, Quality_Check])
quality_check.order.add_edge(Supply_Chain, Quality_Check)

# Step 11: Community Meet concurrent with Quality Check (to emphasize community engagement during quality)
community_quality = StrictPartialOrder(nodes=[Quality_Check, Community_Meet])
# no order edge => concurrent

# Step 12: Launch Event after Quality Check and Community Meet both complete
launch = StrictPartialOrder(nodes=[Quality_Check, Community_Meet, Launch_Event])
launch.order.add_edge(Quality_Check, Launch_Event)
launch.order.add_edge(Community_Meet, Launch_Event)

# Compose the full model step by step

# Combine step1 to step2
part1 = StrictPartialOrder(nodes=[step1, Crop_Select])
part1.order.add_edge(step1, Crop_Select)

# Actually step1 and step2 both contain Permit_Apply and Crop_Select; to avoid duplicate, let's build bottom-up

# Instead, combine the sequence in one chain for the first few sequential tasks:
init_seq = StrictPartialOrder(nodes=[
    Site_Survey, Permit_Apply, Crop_Select, System_Design, Sensor_Deploy])
init_seq.order.add_edge(Site_Survey, Permit_Apply)
init_seq.order.add_edge(Permit_Apply, Crop_Select)
init_seq.order.add_edge(Crop_Select, System_Design)
init_seq.order.add_edge(System_Design, Sensor_Deploy)

# Then add energy_waste after Sensor Deploy
phase1 = StrictPartialOrder(nodes=[init_seq, Energy_Audit, Waste_Plan])
# init_seq ends with Sensor_Deploy inside, but Sensor_Deploy node repeated?
# To properly link, let's flatten nodes properly and use unique objects only once.

# Better to create the entire partial order with all nodes and edges carefully:

root = StrictPartialOrder(
    nodes=[
        Site_Survey, Permit_Apply, Crop_Select, System_Design, Sensor_Deploy,
        Energy_Audit, Waste_Plan, Staff_Train,
        Hydroponic_Setup, Aeroponic_Install,
        Irrigation_Test, Climate_Control,
        Supply_Chain, Quality_Check, Community_Meet, Launch_Event
    ]
)

# Define order edges according to design:

# Step 1-4 (sequence)
root.order.add_edge(Site_Survey, Permit_Apply)
root.order.add_edge(Permit_Apply, Crop_Select)
root.order.add_edge(Crop_Select, System_Design)
root.order.add_edge(System_Design, Sensor_Deploy)

# Step 5 (energy and waste concurrent after Sensor Deploy)
root.order.add_edge(Sensor_Deploy, Energy_Audit)
root.order.add_edge(Sensor_Deploy, Waste_Plan)

# Step 6 Staff Train after both energy and waste
root.order.add_edge(Energy_Audit, Staff_Train)
root.order.add_edge(Waste_Plan, Staff_Train)

# Step 7 Hydroponic and Aeroponic concurrent after Staff Train
root.order.add_edge(Staff_Train, Hydroponic_Setup)
root.order.add_edge(Staff_Train, Aeroponic_Install)

# Step 8 Irrigation Test and Climate Control concurrent after both Hydroponic and Aeroponic
root.order.add_edge(Hydroponic_Setup, Irrigation_Test)
root.order.add_edge(Aeroponic_Install, Irrigation_Test)
root.order.add_edge(Hydroponic_Setup, Climate_Control)
root.order.add_edge(Aeroponic_Install, Climate_Control)

# Step 9 Supply Chain after Irrigation Test and Climate Control
root.order.add_edge(Irrigation_Test, Supply_Chain)
root.order.add_edge(Climate_Control, Supply_Chain)

# Step 10 Quality Check after Supply Chain
root.order.add_edge(Supply_Chain, Quality_Check)

# Step 12 Launch Event after Quality Check and Community Meet (Community Meet concurrent with Quality Check)
root.order.add_edge(Quality_Check, Launch_Event)
root.order.add_edge(Community_Meet, Launch_Event)

# Community Meet concurrent with Quality Check => no edges between them

# The final model is stored in root