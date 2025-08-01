# Generated from: 116f1951-d22e-4894-b79a-c17cfb4df786.json
# Description: This process outlines the end-to-end operations of an urban vertical farming facility that integrates automated hydroponics, AI-driven environmental control, and community-supported agriculture. Starting from seed selection, the cycle includes nutrient mixing, lighting calibration, pest monitoring via drones, and adaptive harvesting schedules. Post-harvest, produce undergoes smart packaging and local distribution using electric vehicles. The system continuously collects data on growth patterns and energy consumption to optimize future yields and reduce environmental impact. Additionally, the process incorporates community engagement through workshops and feedback loops, ensuring sustainable urban agriculture development.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as Transitions
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Setup = Transition(label='Lighting Setup')
Drone_Scan = Transition(label='Drone Scan')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Water_Recycle = Transition(label='Water Recycle')
Climate_Adjust = Transition(label='Climate Adjust')
Harvest_Schedule = Transition(label='Harvest Schedule')
Smart_Packing = Transition(label='Smart Packing')
Quality_Check = Transition(label='Quality Check')
Local_Dispatch = Transition(label='Local Dispatch')
Data_Analysis = Transition(label='Data Analysis')
Energy_Audit = Transition(label='Energy Audit')
Community_Meet = Transition(label='Community Meet')
Feedback_Loop = Transition(label='Feedback Loop')

# Define loops for continuous monitoring and improvement activities:
# Loop for Growth Monitoring and Water Recycle (system continuously collects data)
Growth_Monitor_Loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, Water_Recycle]
)

# Loop for Climate Adjustment and Energy Audit (environmental control and energy optimization)
Climate_Energy_Loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Climate_Adjust, Energy_Audit]
)

# Loop for Community Engagement: Community_Meet and Feedback_Loop repeated
Community_Engagement_Loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Community_Meet, Feedback_Loop]
)

# Choice after Drone Scan: either Pest Control or skip pest control (not explicitly stated, but pest control is a step after drone scan)
Pest_Control_Choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[Pest_Control, SilentTransition()]
)

# Nutrient mixing and lighting calibration happen after seed selection (sequential)
# Drone scan happens after lighting setup
# Pest control choice after drone scan
# Adaptive harvesting schedules after pest control
# Post-harvest: Smart Packing then Quality Check then Local Dispatch
# Data Analysis is concurrent with Energy Audit loop, but both logically post-harvest
# Combine data analysis & loops logically concurrent with community engagement

# Construct partial order of initial cycle:
initial_PO = StrictPartialOrder(nodes=[
    Seed_Selection,
    Nutrient_Mix,
    Lighting_Setup,
    Drone_Scan,
    Pest_Control_Choice,
    Harvest_Schedule
])
initial_PO.order.add_edge(Seed_Selection, Nutrient_Mix)
initial_PO.order.add_edge(Nutrient_Mix, Lighting_Setup)
initial_PO.order.add_edge(Lighting_Setup, Drone_Scan)
initial_PO.order.add_edge(Drone_Scan, Pest_Control_Choice)
initial_PO.order.add_edge(Pest_Control_Choice, Harvest_Schedule)

# Post-harvest sequence:
post_harvest_PO = StrictPartialOrder(nodes=[
    Smart_Packing,
    Quality_Check,
    Local_Dispatch
])
post_harvest_PO.order.add_edge(Smart_Packing, Quality_Check)
post_harvest_PO.order.add_edge(Quality_Check, Local_Dispatch)

# Data analysis and loops combined into one PO:
analysis_PO = StrictPartialOrder(nodes=[
    Data_Analysis,
    Climate_Energy_Loop,
    Growth_Monitor_Loop
])
# Data analysis concurrent with both loops, no edges needed

# Community engagement concurrent to above analysis activities
community_PO = Community_Engagement_Loop

# Combine post-harvest, analysis, and community engagement concurrently:
final_PO = StrictPartialOrder(nodes=[
    post_harvest_PO,
    analysis_PO,
    community_PO
])
# All three groups run concurrently, no edges between them

# Root model: initial sequence then final concurrent activities
root = StrictPartialOrder(nodes=[
    initial_PO,
    final_PO
])
root.order.add_edge(initial_PO, final_PO)