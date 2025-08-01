# Generated from: c9594868-fcfe-440b-8018-7879f54f1e4c.json
# Description: This process outlines the atypical business workflow for establishing a sustainable urban rooftop farm on commercial buildings. It involves site evaluation, structural assessment, soil and hydroponic system design, regulatory compliance checks, sourcing eco-friendly materials, community engagement, installation, crop selection tailored to urban climate, ongoing monitoring with IoT sensors, pest management using organic methods, harvest scheduling, and finally, direct-to-consumer distribution through local markets and digital platforms, ensuring a closed-loop, environmentally conscious urban agriculture initiative.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
soil_prep = Transition(label='Soil Prep')
hydroponic_setup = Transition(label='Hydroponic Setup')
community_meet = Transition(label='Community Meet')
crop_select = Transition(label='Crop Select')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
feedback_collect = Transition(label='Feedback Collect')

# Construct a partial order which reflects the described workflow:
root = StrictPartialOrder(
    nodes=[
        site_survey, load_test, permit_review, design_layout, material_sourcing,
        soil_prep, hydroponic_setup, community_meet, crop_select, sensor_install,
        water_testing, pest_control, growth_monitor, harvest_plan, market_launch,
        feedback_collect
    ]
)

order = root.order
# Site evaluation branch
order.add_edge(site_survey, load_test)
order.add_edge(load_test, permit_review)
# Design and sourcing after permit review
order.add_edge(permit_review, design_layout)
order.add_edge(design_layout, material_sourcing)
# Preparation and setup after material sourcing
order.add_edge(material_sourcing, soil_prep)
order.add_edge(soil_prep, hydroponic_setup)
# Community engagement independent, but after permit_review (assumed)
order.add_edge(permit_review, community_meet)
# Crop selection after design layout to tailor the farm
order.add_edge(design_layout, crop_select)
# Installation steps depend on hydroponic setup and community meet (can be parallel, but model installation after both)
order.add_edge(hydroponic_setup, sensor_install)
order.add_edge(community_meet, sensor_install)
# Water Testing is part of ongoing monitoring setup after sensor install
order.add_edge(sensor_install, water_testing)
# Pest control and growth monitoring depend on water testing
order.add_edge(water_testing, pest_control)
order.add_edge(water_testing, growth_monitor)
# Harvest planning after growth monitor & pest control
order.add_edge(pest_control, harvest_plan)
order.add_edge(growth_monitor, harvest_plan)
# Market launch after harvest plan
order.add_edge(harvest_plan, market_launch)
# Feedback collection after market launch
order.add_edge(market_launch, feedback_collect)