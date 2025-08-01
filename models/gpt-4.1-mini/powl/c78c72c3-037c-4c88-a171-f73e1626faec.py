# Generated from: c78c72c3-037c-4c88-a171-f73e1626faec.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, environmental controls installation, nutrient cycling optimization, crop selection, automated irrigation setup, pest monitoring, energy management, waste recycling, and market integration. The process integrates advanced IoT sensors and AI-driven analytics to maximize yield while minimizing resource consumption. Additionally, it includes community engagement and educational program development to promote urban agriculture awareness and sustainability. The approach balances technological innovation with social impact in a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Install_Sensors = Transition(label='Install Sensors')
Set_Controls = Transition(label='Set Controls')
Test_Modules = Transition(label='Test Modules')
Select_Crops = Transition(label='Select Crops')
Configure_Irrigation = Transition(label='Configure Irrigation')
Deploy_AI = Transition(label='Deploy AI')
Monitor_Pests = Transition(label='Monitor Pests')
Manage_Energy = Transition(label='Manage Energy')
Recycle_Waste = Transition(label='Recycle Waste')
Train_Staff = Transition(label='Train Staff')
Launch_Market = Transition(label='Launch Market')
Engage_Community = Transition(label='Engage Community')

# Build partial orders reflecting the process flows and concurrency

# Initial planning phase
planning_phase = StrictPartialOrder(
    nodes=[Site_Survey, Design_Layout]
)
planning_phase.order.add_edge(Site_Survey, Design_Layout)

# Construction and setup phase - sequential: System Build -> Install Sensors -> Set Controls -> Test Modules
construction_phase = StrictPartialOrder(
    nodes=[System_Build, Install_Sensors, Set_Controls, Test_Modules]
)
construction_phase.order.add_edge(System_Build, Install_Sensors)
construction_phase.order.add_edge(Install_Sensors, Set_Controls)
construction_phase.order.add_edge(Set_Controls, Test_Modules)

# Crop preparation and irrigation configuration in parallel to AI deployment and monitoring
crop_irrigation = StrictPartialOrder(
    nodes=[Select_Crops, Configure_Irrigation]
)  # concurrent, no order edges between these two

ai_monitoring = StrictPartialOrder(
    nodes=[Deploy_AI, Monitor_Pests]
)
ai_monitoring.order.add_edge(Deploy_AI, Monitor_Pests)

# Resource management and waste recycling concurrently with training and market launch
resource_management = StrictPartialOrder(
    nodes=[Manage_Energy, Recycle_Waste]
)  # concurrent, no order edges

training_market = StrictPartialOrder(
    nodes=[Train_Staff, Launch_Market]
)
training_market.order.add_edge(Train_Staff, Launch_Market)

# Community engagement is last, independent (can run concurrently with training_market or could follow)
# To reflect integration and social impact, put Engage Community after Launch Market
community_phase = StrictPartialOrder(
    nodes=[Launch_Market, Engage_Community]
)
community_phase.order.add_edge(Launch_Market, Engage_Community)

# Combine training_market and community_phase replacing Launch_Market with a single node to keep order
training_to_community = StrictPartialOrder(
    nodes=[Train_Staff, Launch_Market, Engage_Community]
)
training_to_community.order.add_edge(Train_Staff, Launch_Market)
training_to_community.order.add_edge(Launch_Market, Engage_Community)

# Now combine resource_management with training_to_community concurrently
resource_and_training = StrictPartialOrder(
    nodes=[resource_management, training_to_community]
)  # concurrent, no edges between them

# Now combine crop_irrigation with ai_monitoring concurrently
crop_and_ai = StrictPartialOrder(
    nodes=[crop_irrigation, ai_monitoring]
)  # concurrent, no edges

# Combine all build/setup phases together sequentially:
# planning_phase -> construction_phase -> (crop_and_ai & resource_and_training concurrently)
intermediate = StrictPartialOrder(
    nodes=[planning_phase, construction_phase, crop_and_ai, resource_and_training]
)
intermediate.order.add_edge(planning_phase, construction_phase)
intermediate.order.add_edge(construction_phase, crop_and_ai)
intermediate.order.add_edge(construction_phase, resource_and_training)

root = intermediate