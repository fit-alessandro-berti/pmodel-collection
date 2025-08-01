# Generated from: 52a6d27b-3efc-4e35-8ae8-d9c321b29c6e.json
# Description: This process outlines the multi-phase establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular structure design, environmental control integration, and crop selection tailored to vertical growth. The workflow includes compliance with city zoning laws, installation of hydroponic systems, automation setup for lighting and irrigation, and continuous monitoring using IoT sensors. Post-installation, staff training and community engagement initiatives ensure sustainable operation. The process culminates in phased crop harvesting and distribution, maximizing yield while minimizing resource consumption in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
zoning_review = Transition(label='Zoning Review')
compliance_check = Transition(label='Compliance Check')
structure_design = Transition(label='Structure Design')
system_planning = Transition(label='System Planning')
hydro_setup = Transition(label='Hydro Setup')
lighting_install = Transition(label='Lighting Install')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_deploy = Transition(label='Sensor Deploy')
automation_config = Transition(label='Automation Config')
crop_select = Transition(label='Crop Select')
staff_training = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')
trial_harvest = Transition(label='Trial Harvest')
yield_analysis = Transition(label='Yield Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the monitoring & harvesting loop: execute harvest+analysis, then either exit or do maintenance and repeat
phaseA = StrictPartialOrder(nodes=[trial_harvest, yield_analysis])
phaseA.order.add_edge(trial_harvest, yield_analysis)
loop = OperatorPOWL(operator=Operator.LOOP, children=[phaseA, maintenance_plan])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    site_survey, zoning_review, compliance_check,
    structure_design, system_planning,
    hydro_setup, lighting_install, irrigation_setup,
    sensor_deploy, automation_config, crop_select,
    staff_training, community_outreach,
    loop
])

# Pre-installation sequence
root.order.add_edge(site_survey, zoning_review)
root.order.add_edge(zoning_review, compliance_check)
root.order.add_edge(compliance_check, structure_design)
root.order.add_edge(structure_design, system_planning)

# Installation in parallel
root.order.add_edge(system_planning, hydro_setup)
root.order.add_edge(system_planning, lighting_install)
root.order.add_edge(system_planning, irrigation_setup)

# Environmental control integration
root.order.add_edge(hydro_setup, sensor_deploy)
root.order.add_edge(lighting_install, sensor_deploy)
root.order.add_edge(irrigation_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, automation_config)

# Crop selection and post-installation activities
root.order.add_edge(automation_config, crop_select)
root.order.add_edge(crop_select, staff_training)
root.order.add_edge(crop_select, community_outreach)

# Enter the continuous monitoring & harvesting loop
root.order.add_edge(staff_training, loop)
root.order.add_edge(community_outreach, loop)