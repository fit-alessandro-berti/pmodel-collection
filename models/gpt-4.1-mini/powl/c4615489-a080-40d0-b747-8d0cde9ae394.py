# Generated from: c4615489-a080-40d0-b747-8d0cde9ae394.json
# Description: This process outlines the comprehensive setup of an urban vertical farming facility within a repurposed industrial building. It involves site analysis, structural modification, environmental control installation, hydroponic system integration, crop selection, and staff training. The process ensures sustainable resource use, maximizes yield per square foot, and incorporates IoT-based monitoring to optimize growth conditions. Regulatory compliance, community engagement, and market launch strategies are also included to create a resilient urban agriculture business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Permit_Filing = Transition(label='Permit Filing')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Set_Lighting = Transition(label='Set Lighting')
Build_Racks = Transition(label='Build Racks')
Install_Hydroponics = Transition(label='Install Hydroponics')
Configure_Sensors = Transition(label='Configure Sensors')
Select_Crops = Transition(label='Select Crops')
Seed_Planting = Transition(label='Seed Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Staff_Training = Transition(label='Staff Training')
Market_Launch = Transition(label='Market Launch')
Waste_Recycling = Transition(label='Waste Recycling')
Customer_Onboarding = Transition(label='Customer Onboarding')

# Create partial orders for groupings with dependencies

# Initial site analysis and regulatory
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Structural_Audit, Permit_Filing])
initial_PO.order.add_edge(Site_Survey, Structural_Audit)
initial_PO.order.add_edge(Structural_Audit, Permit_Filing)

# Design and structural modification activities, starts after Permit_Filing
design_PO = StrictPartialOrder(nodes=[Design_Layout, Install_HVAC, Set_Lighting, Build_Racks])
design_PO.order.add_edge(Design_Layout, Install_HVAC)
design_PO.order.add_edge(Design_Layout, Set_Lighting)
design_PO.order.add_edge(Design_Layout, Build_Racks)

# Hydroponic system installation and environmental controls (all after design_PO)
install_PO = StrictPartialOrder(nodes=[Install_Hydroponics, Configure_Sensors, Nutrient_Mixing])
install_PO.order.add_edge(Install_Hydroponics, Configure_Sensors)
install_PO.order.add_edge(Install_Hydroponics, Nutrient_Mixing)

# Crop activities start after hydroponics and install_PO
crop_PO = StrictPartialOrder(nodes=[Select_Crops, Seed_Planting, Monitor_Growth])
crop_PO.order.add_edge(Select_Crops, Seed_Planting)
crop_PO.order.add_edge(Seed_Planting, Monitor_Growth)

# Staff training can run concurrently with crop monitoring
training_PO = StrictPartialOrder(nodes=[Staff_Training])

# Waste recycling and customer onboarding concurrent with market launch
post_PO = StrictPartialOrder(nodes=[Market_Launch, Waste_Recycling, Customer_Onboarding])

# Build a big partial order that combines all with order edges reflecting dependencies

root = StrictPartialOrder(
    nodes=[initial_PO, design_PO, install_PO, crop_PO, training_PO, post_PO]
)

# Link partial orders with dependencies

# initial_PO --> design_PO
root.order.add_edge(initial_PO, design_PO)

# design_PO --> install_PO
root.order.add_edge(design_PO, install_PO)

# install_PO --> crop_PO
root.order.add_edge(install_PO, crop_PO)

# crop_PO --> training_PO (They can run concurrently, but crop_PO needs to start first;
# to reflect training can start once crop_PO started (partial order), we omit strict edge)

# crop_PO --> post_PO
root.order.add_edge(crop_PO, post_PO)

# training_PO concurrent with crop_PO and post_PO (no edges added, concurrent)

# Summary:
# The partial orders reflect the main phases:
# initial_PO (site survey etc)
# then design_PO
# then install_PO
# then crop_PO
# training_PO concurrent with crop_PO and post_PO
# post_PO last phase with market launch etc.
