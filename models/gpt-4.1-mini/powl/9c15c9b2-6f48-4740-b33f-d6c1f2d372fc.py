# Generated from: 9c15c9b2-6f48-4740-b33f-d6c1f2d372fc.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm within a densely populated city. It includes site analysis, structural assessment, soil and water testing, regulatory approvals, system design, installation of hydroponic or soil beds, irrigation setup, crop selection, pest management planning, community engagement, staff training, monitoring systems installation, initial seeding, growth tracking, and finally harvest scheduling. The process requires collaboration between engineers, agronomists, city officials, and local communities to ensure environmental compliance, optimize yield, and promote urban green spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Sample = Transition(label='Soil Sample')
Water_Check = Transition(label='Water Check')
Permit_Apply = Transition(label='Permit Apply')
Design_Plan = Transition(label='Design Plan')
Bed_Install = Transition(label='Bed Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Select = Transition(label='Crop Select')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Staff_Train = Transition(label='Staff Train')
Sensor_Install = Transition(label='Sensor Install')
Seed_Plant = Transition(label='Seed Plant')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')

# Site analysis partial order: Site Survey --> (Load Test, Soil Sample, Water Check) concurrently
site_analysis = StrictPartialOrder(
    nodes=[Site_Survey, Load_Test, Soil_Sample, Water_Check]
)
site_analysis.order.add_edge(Site_Survey, Load_Test)
site_analysis.order.add_edge(Site_Survey, Soil_Sample)
site_analysis.order.add_edge(Site_Survey, Water_Check)

# Structural & regulatory partial order: Load Test --> Permit Apply, Permit Apply after Water_Check and Soil_Sample too
structural_reg = StrictPartialOrder(
    nodes=[Load_Test, Soil_Sample, Water_Check, Permit_Apply]
)
structural_reg.order.add_edge(Load_Test, Permit_Apply)
structural_reg.order.add_edge(Soil_Sample, Permit_Apply)
structural_reg.order.add_edge(Water_Check, Permit_Apply)

# Design after permit
design = StrictPartialOrder(nodes=[Permit_Apply, Design_Plan])
design.order.add_edge(Permit_Apply, Design_Plan)

# Installation setup partial order: Design Plan --> (Bed Install, Irrigation Setup) concurrently
install_setup = StrictPartialOrder(nodes=[Design_Plan, Bed_Install, Irrigation_Setup])
install_setup.order.add_edge(Design_Plan, Bed_Install)
install_setup.order.add_edge(Design_Plan, Irrigation_Setup)

# Crop and pest partial order: Crop Select --> Pest Control
crop_pest = StrictPartialOrder(nodes=[Crop_Select, Pest_Control])
crop_pest.order.add_edge(Crop_Select, Pest_Control)

# Community and staff partial order: Community Meet --> Staff Train
community_staff = StrictPartialOrder(nodes=[Community_Meet, Staff_Train])
community_staff.order.add_edge(Community_Meet, Staff_Train)

# Monitoring setup partial order: Staff Train --> Sensor Install --> Seed Plant
monitoring_setup = StrictPartialOrder(nodes=[Staff_Train, Sensor_Install, Seed_Plant])
monitoring_setup.order.add_edge(Staff_Train, Sensor_Install)
monitoring_setup.order.add_edge(Sensor_Install, Seed_Plant)

# Growth and harvest partial order: Seed Plant --> Growth Monitor --> Harvest Plan
growth_harvest = StrictPartialOrder(nodes=[Seed_Plant, Growth_Monitor, Harvest_Plan])
growth_harvest.order.add_edge(Seed_Plant, Growth_Monitor)
growth_harvest.order.add_edge(Growth_Monitor, Harvest_Plan)

# Combine crop_pest and community_staff concurrently before monitoring setup
pre_monitoring = StrictPartialOrder(
    nodes=[crop_pest, community_staff]
)
# No explicit order between these two concurrently

# Now combine pre_monitoring and install_setup concurrently: They occur after design
# The design partial order already leads to install_setup, so we'll build a big PO merging these

# Step 1: Combine crop_pest and community_staff concurrently
crop_community = StrictPartialOrder(
    nodes=[crop_pest, community_staff]
)

# Step 2: Add Install Setup, concurrency between crop_community and install_setup
mid_part = StrictPartialOrder(
    nodes=[install_setup, crop_community]
)

# Step 3: Then monitoring_setup after both install_setup and crop_community
monitoring_big = StrictPartialOrder(
    nodes=[mid_part, monitoring_setup]
)
monitoring_big.order.add_edge(mid_part, monitoring_setup)

# Step 4: Combine growth_harvest after monitoring_setup
final_part = StrictPartialOrder(
    nodes=[monitoring_big, growth_harvest]
)
final_part.order.add_edge(monitoring_big, growth_harvest)

# Step 5: Combine site_analysis, structural_reg, design, and final_part in order
# site_analysis --> structural_reg --> design --> final_part

step1 = StrictPartialOrder(
    nodes=[site_analysis, structural_reg]
)
step1.order.add_edge(site_analysis, structural_reg)

step2 = StrictPartialOrder(
    nodes=[step1, design]
)
step2.order.add_edge(step1, design)

step3 = StrictPartialOrder(
    nodes=[step2, final_part]
)
step3.order.add_edge(step2, final_part)

root = step3