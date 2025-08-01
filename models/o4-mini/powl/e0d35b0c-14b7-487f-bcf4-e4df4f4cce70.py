# Generated from: e0d35b0c-14b7-487f-bcf4-e4df4f4cce70.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm, integrating advanced hydroponic technology with local community engagement. It begins with site analysis and structural assessment to ensure safety and viability. Subsequent steps include resource sourcing, installation of modular grow systems, and environmental control setup such as lighting and irrigation. Parallel activities involve stakeholder coordination, training of local volunteers, and compliance with urban agricultural regulations. The process concludes with iterative crop monitoring, data collection for yield optimization, and community harvest events to promote urban food resilience and social cohesion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
site_survey       = Transition(label='Site Survey')
struct_check      = Transition(label='Structural Check')
resource_source   = Transition(label='Resource Sourcing')
system_install    = Transition(label='System Install')
lighting_setup    = Transition(label='Lighting Setup')
irrigation_setup  = Transition(label='Irrigation Setup')
stakeholder_meet  = Transition(label='Stakeholder Meet')
volunteer_train   = Transition(label='Volunteer Train')
regulation_review = Transition(label='Regulation Review')
crop_selection    = Transition(label='Crop Selection')
planting_phase    = Transition(label='Planting Phase')
climate_control   = Transition(label='Climate Control')
growth_monitor    = Transition(label='Growth Monitor')
data_logging      = Transition(label='Data Logging')
harvest_event     = Transition(label='Harvest Event')
waste_manage      = Transition(label='Waste Manage')
feedback_collect  = Transition(label='Feedback Collect')

# Build the iterative monitoring & logging loop
loop_body = StrictPartialOrder(nodes=[growth_monitor, data_logging])
loop_body.order.add_edge(growth_monitor, data_logging)
skip = SilentTransition()
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Build the overall POWL
root = StrictPartialOrder(nodes=[
    site_survey, struct_check,
    resource_source, system_install,
    lighting_setup, irrigation_setup,
    stakeholder_meet, volunteer_train, regulation_review,
    crop_selection, planting_phase, climate_control,
    monitoring_loop, harvest_event, waste_manage, feedback_collect
])

# Define the sequential & concurrent dependencies
root.order.add_edge(site_survey, struct_check)
root.order.add_edge(struct_check, resource_source)
root.order.add_edge(resource_source, system_install)

# After installation, run environmental control and community engagement in parallel
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, stakeholder_meet)
root.order.add_edge(system_install, volunteer_train)
root.order.add_edge(system_install, regulation_review)

# Join all of the above before crop selection
for prev in [lighting_setup, irrigation_setup, stakeholder_meet, volunteer_train, regulation_review]:
    root.order.add_edge(prev, crop_selection)

# Continue with planting and climate control
root.order.add_edge(crop_selection, planting_phase)
root.order.add_edge(planting_phase, climate_control)

# Enter the monitoring & logging loop, then harvest and wrap‐up
root.order.add_edge(climate_control, monitoring_loop)
root.order.add_edge(monitoring_loop, harvest_event)
root.order.add_edge(harvest_event, waste_manage)
root.order.add_edge(waste_manage, feedback_collect)