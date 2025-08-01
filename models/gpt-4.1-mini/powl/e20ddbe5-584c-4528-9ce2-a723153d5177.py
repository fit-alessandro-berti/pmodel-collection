# Generated from: e20ddbe5-584c-4528-9ce2-a723153d5177.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a metropolitan environment. It begins with site analysis and structural assessment to ensure roof load capacity and sunlight exposure. Next, soil-less medium selection and hydroponic system design are conducted to optimize water and nutrient delivery. Procurement involves sourcing organic seeds and eco-friendly materials, followed by installation of irrigation and climate control systems. Planting schedules are created based on seasonal cycles, alongside pest management planning using integrated pest management strategies. Regular monitoring includes data collection on plant growth, moisture levels, and system performance, while adapting to weather fluctuations through automated controls. Harvesting and packaging protocols prioritize freshness and minimal waste. Finally, community engagement and educational workshops are organized to promote urban agriculture awareness and sustainability practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Load_Test = Transition(label='Load Test')
Sunlight_Map = Transition(label='Sunlight Map')
Medium_Select = Transition(label='Medium Select')
Hydro_Design = Transition(label='Hydro Design')
Procure_Seeds = Transition(label='Procure Seeds')
Install_Irrigation = Transition(label='Install Irrigation')
Setup_Climate = Transition(label='Setup Climate')
Create_Schedule = Transition(label='Create Schedule')
Pest_Control = Transition(label='Pest Control')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Systems = Transition(label='Adjust Systems')
Harvest_Crops = Transition(label='Harvest Crops')
Package_Produce = Transition(label='Package Produce')
Engage_Community = Transition(label='Engage Community')
Host_Workshops = Transition(label='Host Workshops')

# Step 1: Site analysis and structural assessment
# Site Analysis --> Load Test and Sunlight Map (concurrent)
step1 = StrictPartialOrder(
    nodes=[Site_Analysis, Load_Test, Sunlight_Map]
)
step1.order.add_edge(Site_Analysis, Load_Test)
step1.order.add_edge(Site_Analysis, Sunlight_Map)

# Step 2: Medium selection and hydroponic design (concurrent after step 1)
step2 = StrictPartialOrder(
    nodes=[Medium_Select, Hydro_Design]
)

# Overall after step1 --> step2
phase1_2 = StrictPartialOrder(
    nodes=[step1, step2]
)
phase1_2.order.add_edge(step1, step2)

# Step 3: Procurement 
phase3 = Procure_Seeds

# Step 4: Installation of irrigation and climate control (concurrent)
step4 = StrictPartialOrder(
    nodes=[Install_Irrigation, Setup_Climate]
)

# Step 5: Scheduling and pest control (concurrent)
step5 = StrictPartialOrder(
    nodes=[Create_Schedule, Pest_Control]
)

# Step 6: Monitoring and adjustment (Monitor Growth --> Adjust Systems)
step6 = StrictPartialOrder(
    nodes=[Monitor_Growth, Adjust_Systems]
)
step6.order.add_edge(Monitor_Growth, Adjust_Systems)

# Step 7: Harvesting and packaging (Harvest Crops --> Package Produce)
step7 = StrictPartialOrder(
    nodes=[Harvest_Crops, Package_Produce]
)
step7.order.add_edge(Harvest_Crops, Package_Produce)

# Step 8: Community engagement and workshops (concurrent)
step8 = StrictPartialOrder(
    nodes=[Engage_Community, Host_Workshops]
)

# Combine installation and scheduling and monitoring phases
phase4_5_6 = StrictPartialOrder(
    nodes=[step4, step5, step6]
)
# Installation --> Scheduling & Pest Control
phase4_5_6.order.add_edge(step4, step5)
# Scheduling & Pest Control --> Monitoring & Adjustment
phase4_5_6.order.add_edge(step5, step6)

# Combine harvesting with community engagement/workshops
phase7_8 = StrictPartialOrder(
    nodes=[step7, step8]
)

# Harvest/package --> community/workshops order implied by text? 
# They happen last, community engagement probably after harvest
# We'll add edge harvest/package --> community/workshops
phase7_8.order.add_edge(step7, step8)

# Full process:
# phase1_2 --> phase3 --> phase4_5_6 --> phase7_8

root = StrictPartialOrder(
    nodes=[phase1_2, phase3, phase4_5_6, phase7_8]
)
root.order.add_edge(phase1_2, phase3)
root.order.add_edge(phase3, phase4_5_6)
root.order.add_edge(phase4_5_6, phase7_8)