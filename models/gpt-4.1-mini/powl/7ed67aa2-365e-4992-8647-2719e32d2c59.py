# Generated from: 7ed67aa2-365e-4992-8647-2719e32d2c59.json
# Description: This process details the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site evaluation, structural modification, environmental system installation, crop selection, automated irrigation setup, data analytics integration, pest management protocols, nutrient cycling optimization, energy consumption monitoring, and community engagement programs. The process ensures sustainable urban agriculture by combining advanced technology with local ecosystem considerations, aiming to maximize yield in limited space while minimizing environmental impact and fostering social responsibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Permit_Filing = Transition(label='Permit Filing')
Design_Layout = Transition(label='Design Layout')
Install_Racks = Transition(label='Install Racks')
Setup_Lighting = Transition(label='Setup Lighting')
Configure_HVAC = Transition(label='Configure HVAC')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Integration = Transition(label='Sensor Integration')
Select_Crops = Transition(label='Select Crops')
Plant_Seeding = Transition(label='Plant Seeding')
Data_Calibration = Transition(label='Data Calibration')
Pest_Control = Transition(label='Pest Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Harvest_Planning = Transition(label='Harvest Planning')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Tracking = Transition(label='Energy Tracking')
Community_Outreach = Transition(label='Community Outreach')

# Build partial orders reflecting the described process

# Phase 1: Site evaluation and approvals
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structural_Audit, Permit_Filing])
phase1.order.add_edge(Site_Survey, Structural_Audit)
phase1.order.add_edge(Structural_Audit, Permit_Filing)

# Phase 2: Design and structural modification
phase2 = StrictPartialOrder(nodes=[Design_Layout, Install_Racks, Setup_Lighting, Configure_HVAC])
phase2.order.add_edge(Design_Layout, Install_Racks)
phase2.order.add_edge(Install_Racks, Setup_Lighting)
phase2.order.add_edge(Install_Racks, Configure_HVAC)
phase2.order.add_edge(Setup_Lighting, Configure_HVAC)

# Phase 3: Installation of irrigation and sensors
phase3 = StrictPartialOrder(nodes=[Irrigation_Install, Sensor_Integration])
phase3.order.add_edge(Irrigation_Install, Sensor_Integration)

# Phase 4: Crop management
# Selecting crops then seeding, with data calibration in parallel (partial order)
crop_and_data = StrictPartialOrder(nodes=[Select_Crops, Plant_Seeding, Data_Calibration])
crop_and_data.order.add_edge(Select_Crops, Plant_Seeding)
# Data Calibration can be concurrent with seeding (no order edge)

# Phase 5: Maintenance and monitoring in parallel
maintenance = StrictPartialOrder(
    nodes=[Pest_Control, Nutrient_Mix, Harvest_Planning, Waste_Recycling, Energy_Tracking, Community_Outreach]
)
# No edges inside maintenance for concurrency

# Compose the full process with all phases partially ordered
# The general sequence:
# phase1 -> phase2 -> phase3 -> crop_and_data -> maintenance (where maintenance activities run in parallel)

# Nodes in root are all phases (POWLs)
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, crop_and_data, maintenance]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, crop_and_data)
root.order.add_edge(crop_and_data, maintenance)