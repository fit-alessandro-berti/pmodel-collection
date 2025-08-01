# Generated from: 2f34c772-00ed-43d1-8712-79a31f2bde92.json
# Description: This process outlines the detailed steps for establishing a bespoke urban farming system in densely populated city environments. It involves site analysis, modular design customization, integration of IoT sensors for real-time monitoring, adaptive irrigation scheduling based on microclimate data, community engagement for crop selection, and iterative yield optimization through data analytics. Additional activities include local regulatory compliance, vertical structure assembly, soil-less media preparation, renewable energy sourcing, pest management using bio-controls, and final harvest logistics coordination to ensure fresh produce delivery directly to consumers with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
site_survey = Transition(label='Site Survey')
design_draft = Transition(label='Design Draft')
sensor_setup = Transition(label='Sensor Setup')
microclimate_map = Transition(label='Microclimate Map')
irrigation_plan = Transition(label='Irrigation Plan')
crop_selection = Transition(label='Crop Selection')
regulation_check = Transition(label='Regulation Check')
structure_build = Transition(label='Structure Build')
media_prep = Transition(label='Media Prep')
energy_setup = Transition(label='Energy Setup')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
data_analysis = Transition(label='Data Analysis')
yield_adjust = Transition(label='Yield Adjust')
harvest_plan = Transition(label='Harvest Plan')
delivery_coord = Transition(label='Delivery Coord')

# Create partial order for initial site analysis and design customization:
# Site Survey --> Design Draft
site_design = StrictPartialOrder(nodes=[site_survey, design_draft])
site_design.order.add_edge(site_survey, design_draft)

# Sensor Setup depends on Design Draft
sensor_on_design = StrictPartialOrder(nodes=[sensor_setup, design_draft])
sensor_on_design.order.add_edge(design_draft, sensor_setup)

# Microclimate Map depends on Sensor Setup
microclimate = StrictPartialOrder(nodes=[sensor_setup, microclimate_map])
microclimate.order.add_edge(sensor_setup, microclimate_map)

# Irrigation Plan depends on Microclimate Map
irrigation = StrictPartialOrder(nodes=[microclimate_map, irrigation_plan])
irrigation.order.add_edge(microclimate_map, irrigation_plan)

# Crop Selection and Community Meet are related and likely concurrent but Crop Selection likely depends on Community Meet (engagement)
crop_comm_meet = StrictPartialOrder(nodes=[community_meet, crop_selection])
crop_comm_meet.order.add_edge(community_meet, crop_selection)

# Regulation Check can occur after Design Draft in parallel with community activities
reg_check_design = StrictPartialOrder(nodes=[design_draft, regulation_check])
reg_check_design.order.add_edge(design_draft, regulation_check)

# Structure Build, Media Prep, Energy Setup, Pest Control are preparation activities,
# some can be executed in parallel, but all depend on Regulation Check and Design Draft
prep_activities = StrictPartialOrder(nodes=[
    structure_build,
    media_prep,
    energy_setup,
    pest_control,
    regulation_check,
    design_draft
])
prep_activities.order.add_edge(design_draft, regulation_check)
prep_activities.order.add_edge(regulation_check, structure_build)
prep_activities.order.add_edge(regulation_check, media_prep)
prep_activities.order.add_edge(regulation_check, energy_setup)
prep_activities.order.add_edge(regulation_check, pest_control)

# Data Analysis and Yield Adjust form a loop - iterative yield optimization:
# LOOP( Data Analysis, Yield Adjust )
loop_yield_opt = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, yield_adjust])

# Harvest Plan depends on Yield Adjust (final step of optimization)
harvest = StrictPartialOrder(nodes=[yield_adjust, harvest_plan])
harvest.order.add_edge(yield_adjust, harvest_plan)

# Delivery Coord depends on Harvest Plan
delivery = StrictPartialOrder(nodes=[harvest_plan, delivery_coord])
delivery.order.add_edge(harvest_plan, delivery_coord)

# Combine partial order for monitoring and irrigation scheduling steps
monitor_irrigation = StrictPartialOrder(nodes=[sensor_setup, microclimate_map, irrigation_plan])
monitor_irrigation.order.add_edge(sensor_setup, microclimate_map)
monitor_irrigation.order.add_edge(microclimate_map, irrigation_plan)

# Combine community engagement and crop selection with monitoring and irrigation concurrently after design draft
comm_crop_monitor_irrig = StrictPartialOrder(nodes=[crop_comm_meet, monitor_irrigation])
# No order edges between crop_comm_meet and monitor_irrigation => concurrent

# Combine site analysis/design with community, monitoring/irrigation, and preparation activities
site_design_extended = StrictPartialOrder(nodes=[site_design, comm_crop_monitor_irrig, prep_activities])
site_design_extended.order.add_edge(site_design, comm_crop_monitor_irrig)
site_design_extended.order.add_edge(site_design, prep_activities)

# Combine loop and harvest/delivery in sequence
loop_and_harvest = StrictPartialOrder(nodes=[loop_yield_opt, harvest, delivery])
loop_and_harvest.order.add_edge(loop_yield_opt, harvest)
loop_and_harvest.order.add_edge(harvest, delivery)

# Final combination: the phases
root = StrictPartialOrder(nodes=[site_design_extended, loop_and_harvest])
root.order.add_edge(site_design_extended, loop_and_harvest)