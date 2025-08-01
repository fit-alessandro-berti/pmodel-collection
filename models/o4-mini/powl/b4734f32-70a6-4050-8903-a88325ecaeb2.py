# Generated from: b4734f32-70a6-4050-8903-a88325ecaeb2.json
# Description: This process involves the planning, setup, and operational launch of an urban rooftop farming initiative in a densely populated city. It includes site assessment, structural analysis, resource procurement, soil testing, microclimate evaluation, installation of irrigation and lighting systems, selection of crops, community engagement, and finally, the first planting and ongoing monitoring phases. The process is complex due to the constraints of urban infrastructure, regulatory compliance, sustainability goals, and integration with local community programs to ensure long-term viability and social impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey       = Transition(label='Site Survey')
load_analysis     = Transition(label='Load Analysis')
permit_request    = Transition(label='Permit Request')
soil_sampling     = Transition(label='Soil Sampling')
microclimate_map  = Transition(label='Microclimate Map')
system_design     = Transition(label='System Design')
supplier_sourcing = Transition(label='Supplier Sourcing')
irrigation_setup  = Transition(label='Irrigation Setup')
lighting_install  = Transition(label='Lighting Install')
crop_selection    = Transition(label='Crop Selection')
community_meet    = Transition(label='Community Meet')
planting_day      = Transition(label='Planting Day')

# Define the monitoring & feedback activities
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
harvest_plan   = Transition(label='Harvest Plan')
waste_manage   = Transition(label='Waste Manage')
feedback_loop  = Transition(label='Feedback Loop')

# Build the loop body for Monitoring → Pest Control → Waste Manage → Harvest Plan → Feedback Loop
body = StrictPartialOrder(nodes=[pest_control, waste_manage, harvest_plan, feedback_loop])
body.order.add_edge(pest_control, waste_manage)
body.order.add_edge(waste_manage, harvest_plan)
body.order.add_edge(harvest_plan, feedback_loop)

# Create the LOOP operator: do Growth Monitor, then either exit or do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, body])

# Build the root partial order of the entire process
root = StrictPartialOrder(nodes=[
    site_survey, load_analysis, permit_request,
    soil_sampling, microclimate_map, system_design,
    supplier_sourcing, irrigation_setup, lighting_install,
    crop_selection, community_meet, planting_day,
    loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, load_analysis)
root.order.add_edge(load_analysis, permit_request)

root.order.add_edge(site_survey, soil_sampling)
root.order.add_edge(site_survey, microclimate_map)

root.order.add_edge(permit_request, system_design)
root.order.add_edge(soil_sampling,   system_design)
root.order.add_edge(microclimate_map, system_design)

root.order.add_edge(permit_request,    supplier_sourcing)

root.order.add_edge(system_design,    irrigation_setup)
root.order.add_edge(supplier_sourcing, irrigation_setup)
root.order.add_edge(system_design,    lighting_install)
root.order.add_edge(supplier_sourcing, lighting_install)

root.order.add_edge(system_design,    crop_selection)
root.order.add_edge(crop_selection,   community_meet)

root.order.add_edge(irrigation_setup, planting_day)
root.order.add_edge(lighting_install, planting_day)
root.order.add_edge(community_meet,   planting_day)

# After planting, enter the monitoring-loop
root.order.add_edge(planting_day, loop)