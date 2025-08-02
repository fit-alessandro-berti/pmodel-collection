# Generated from: 52a6d27b-3efc-4e35-8ae8-d9c321b29c6e.json
# Description: This process outlines the multi-phase establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular structure design, environmental control integration, and crop selection tailored to vertical growth. The workflow includes compliance with city zoning laws, installation of hydroponic systems, automation setup for lighting and irrigation, and continuous monitoring using IoT sensors. Post-installation, staff training and community engagement initiatives ensure sustainable operation. The process culminates in phased crop harvesting and distribution, maximizing yield while minimizing resource consumption in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Zoning_Review = Transition(label='Zoning Review')
Compliance_Check = Transition(label='Compliance Check')
Structure_Design = Transition(label='Structure Design')
System_Planning = Transition(label='System Planning')
Hydro_Setup = Transition(label='Hydro Setup')
Lighting_Install = Transition(label='Lighting Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Automation_Config = Transition(label='Automation Config')
Crop_Select = Transition(label='Crop Select')
Staff_Training = Transition(label='Staff Training')
Community_Outreach = Transition(label='Community Outreach')
Trial_Harvest = Transition(label='Trial Harvest')
Yield_Analysis = Transition(label='Yield Analysis')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Compliance branch: Zoning Review then Compliance Check
compliance_po = StrictPartialOrder(nodes=[Zoning_Review, Compliance_Check])
compliance_po.order.add_edge(Zoning_Review, Compliance_Check)

# System install partial order: Hydro Setup, Lighting Install, Irrigation Setup (concurrent), 
# all after System Planning, then Sensor Deploy and Automation Config in order

# concurrency among Hydro Setup, Lighting Install, Irrigation Setup
install_po = StrictPartialOrder(nodes=[Hydro_Setup, Lighting_Install, Irrigation_Setup])
# No edges among them --> concurrent

# After System Planning, the install_po executes
system_planning_branch = StrictPartialOrder(nodes=[System_Planning, install_po])
system_planning_branch.order.add_edge(System_Planning, install_po)

# sensor deploy then automation config after install
sensor_automation_po = StrictPartialOrder(nodes=[Sensor_Deploy, Automation_Config])
sensor_automation_po.order.add_edge(Sensor_Deploy, Automation_Config)

# Combine install_po and sensor_automation_po:
# after install (Hydro, Lighting, Irrigation) in parallel, then sensor deploy, then automation config
install_sensor_po = StrictPartialOrder(nodes=[install_po, sensor_automation_po])
install_sensor_po.order.add_edge(install_po, sensor_automation_po)

# Combine System Planning + install + sensor_automation
system_full_po = StrictPartialOrder(nodes=[System_Planning, install_po, sensor_automation_po])
system_full_po.order.add_edge(System_Planning, install_po)
system_full_po.order.add_edge(install_po, sensor_automation_po)

# Alternatively, use system_planning_branch order structure:
# But to keep it simpler and consistent, let's keep system_full_po as the combined order:
# This models System Planning -> (Hydro, Lighting, Irrigation concurrent) -> Sensor Deploy -> Automation Config

# Overall structure design and system planning phases:
structure_system_po = StrictPartialOrder(nodes=[Structure_Design, system_full_po])
structure_system_po.order.add_edge(Structure_Design, system_full_po)

# First phase: Site Survey then (compliance branch and structure_system branch) concurrent
# So Site Survey --> compliance_po and Site Survey --> structure_system_po
first_phase = StrictPartialOrder(nodes=[Site_Survey, compliance_po, structure_system_po])
first_phase.order.add_edge(Site_Survey, compliance_po)
first_phase.order.add_edge(Site_Survey, structure_system_po)

# Crop Select after full system ready (i.e. after structure + system planning phase)
# Add Crop Select depends on structure_system_po (and indirectly on Site Survey)
crop_select_po = StrictPartialOrder(nodes=[structure_system_po, Crop_Select])
crop_select_po.order.add_edge(structure_system_po, Crop_Select)

# After Crop Select comes Staff Training and Community Outreach concurrent
staff_community_po = StrictPartialOrder(nodes=[Staff_Training, Community_Outreach])
# no edges = concurrent

crop_staff_community_po = StrictPartialOrder(nodes=[Crop_Select, staff_community_po])
crop_staff_community_po.order.add_edge(Crop_Select, staff_community_po)

# Final phase: Trial Harvest -> Yield Analysis -> Maintenance Plan
harvest_po = StrictPartialOrder(nodes=[Trial_Harvest, Yield_Analysis, Maintenance_Plan])
harvest_po.order.add_edge(Trial_Harvest, Yield_Analysis)
harvest_po.order.add_edge(Yield_Analysis, Maintenance_Plan)

# Combine all: first phase -> Crop Select -> Staff & Community -> Harvest phase
full_process = StrictPartialOrder(nodes=[first_phase, Crop_Select, staff_community_po, harvest_po])
full_process.order.add_edge(first_phase, Crop_Select)
full_process.order.add_edge(Crop_Select, staff_community_po)
full_process.order.add_edge(staff_community_po, harvest_po)

root = full_process