# Generated from: 42de4269-da18-4ed4-91b4-770bbc470b42.json
# Description: This process outlines the complex and multifaceted approach to establishing a vertical farming operation in an urban environment. It involves site selection based on sunlight and infrastructure availability, modular farm design to maximize space efficiency, integration of IoT sensors for real-time monitoring, automated nutrient delivery systems, climate control calibration, regulatory compliance checks including zoning and agricultural permits, staff training on hydroponic systems, implementation of AI-driven crop health analysis, waste recycling protocols, marketing strategy development targeting local consumers, and continuous performance optimization through data analytics. This atypical business process combines agriculture, technology, urban planning, and sustainability to create a scalable and efficient urban farm that meets the demand for fresh produce within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Tune = Transition(label='Climate Tune')
Permit_Review = Transition(label='Permit Review')
Staff_Onboard = Transition(label='Staff Onboard')
AI_Training = Transition(label='AI Training')
Crop_Monitor = Transition(label='Crop Monitor')
Waste_Setup = Transition(label='Waste Setup')
Market_Plan = Transition(label='Market Plan')
Data_Review = Transition(label='Data Review')
Harvest_Plan = Transition(label='Harvest Plan')
Supply_Chain = Transition(label='Supply Chain')
Feedback_Loop = Transition(label='Feedback Loop')

# Define loops and choices according to process description

# Loop 1: Continuous "Feedback Loop" driving "Data Review" and then possibly looping back
# We'll model loop: *(Feedback_Loop, Data_Review)
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Data_Review])

# Market plan depends on completed regulatory compliance (Permit Review) and Waste Setup
# Staff onboarding and AI Training depend on permit review (regulatory compliance + training)
# Crop Monitoring depends on AI Training and Sensor Install
# Harvest Plan and Supply Chain depend on Crop Monitor and Nutrient Mix, Climate Tune

# Define partial order nodes for initial setup steps
initial_setup_nodes = [Site_Survey, Design_Layout]

# After Site_Survey and Design_Layout, Sensor_Install and Nutrient_Mix can happen concurrently,
# Climate_Tune follows Nutrient_Mix
# Permit_Review follows Site_Survey (infrastructure + zoning)
# Staff_Onboard after Permit_Review
# AI_Training after Staff_Onboard
# Crop_Monitor after AI_Training and Sensor_Install
# Waste_Setup can be concurrent with Crop Monitoring
# Market Plan after Waste_Setup and Permit_Review
# Harvest_Plan after Crop Monitor and Climate Tune
# Supply_Chain after Harvest_Plan
# Finally the feedback loop happens

root = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Sensor_Install,
    Nutrient_Mix,
    Climate_Tune,
    Permit_Review,
    Staff_Onboard,
    AI_Training,
    Crop_Monitor,
    Waste_Setup,
    Market_Plan,
    Harvest_Plan,
    Supply_Chain,
    loop_feedback,
])

# Add control flow edges modeling dependencies

# Site Survey --> Design Layout (survey precedes design)
root.order.add_edge(Site_Survey, Design_Layout)

# Site Survey --> Permit Review (need site info before permits)
root.order.add_edge(Site_Survey, Permit_Review)

# Design Layout --> Sensor Install (design before installing sensors)
root.order.add_edge(Design_Layout, Sensor_Install)

# Design Layout --> Nutrient Mix (design before nutrient system)
root.order.add_edge(Design_Layout, Nutrient_Mix)

# Nutrient Mix --> Climate Tune (nutrient mix then climate tuning)
root.order.add_edge(Nutrient_Mix, Climate_Tune)

# Permit Review --> Staff Onboard (permits before staff training)
root.order.add_edge(Permit_Review, Staff_Onboard)

# Staff Onboard --> AI Training (staff trained before AI training)
root.order.add_edge(Staff_Onboard, AI_Training)

# AI Training and Sensor Install --> Crop Monitor (both needed before crop monitor)
root.order.add_edge(AI_Training, Crop_Monitor)
root.order.add_edge(Sensor_Install, Crop_Monitor)

# Waste Setup concurrent but Market Plan depends on Waste Setup and Permit Review
root.order.add_edge(Waste_Setup, Market_Plan)
root.order.add_edge(Permit_Review, Market_Plan)

# Crop Monitor and Climate Tune --> Harvest Plan
root.order.add_edge(Crop_Monitor, Harvest_Plan)
root.order.add_edge(Climate_Tune, Harvest_Plan)

# Harvest Plan --> Supply Chain
root.order.add_edge(Harvest_Plan, Supply_Chain)

# Supply Chain --> Feedback Loop (loop start)
root.order.add_edge(Supply_Chain, loop_feedback)

# Data Review inside loop (child of loop_feedback), loop edges handled internally

root