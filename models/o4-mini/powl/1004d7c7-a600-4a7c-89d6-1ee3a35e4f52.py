# Generated from: 1004d7c7-a600-4a7c-89d6-1ee3a35e4f52.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes assessing structural integrity, designing modular growing units, integrating IoT sensors for climate control, selecting crop varieties optimized for vertical growth, installing hydroponic systems, and implementing automated nutrient delivery. The process further involves regulatory compliance checks, staff training on specialized farming techniques, continuous environmental monitoring, and establishing supply chain logistics for fresh produce distribution to local markets. Emphasis is placed on sustainability and energy efficiency throughout the setup.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey        = Transition(label="Site Survey")
structural_check   = Transition(label="Structural Check")
design_layout      = Transition(label="Design Layout")
crop_selection     = Transition(label="Crop Selection")
sensor_setup       = Transition(label="Sensor Setup")
hydroponics_install= Transition(label="Hydroponics Install")
compliance_review  = Transition(label="Compliance Review")
staff_training     = Transition(label="Staff Training")
system_testing     = Transition(label="System Testing")
data_integration   = Transition(label="Data Integration")
climate_control    = Transition(label="Climate Control")
nutrient_mix       = Transition(label="Nutrient Mix")
harvest_planning   = Transition(label="Harvest Planning")
packaging_setup    = Transition(label="Packaging Setup")
logistics_setup    = Transition(label="Logistics Setup")
market_launch      = Transition(label="Market Launch")

# Build the loop body for continuous environmental monitoring:
# Data Integration -> Climate Control -> Nutrient Mix
body = StrictPartialOrder(nodes=[data_integration, climate_control, nutrient_mix])
body.order.add_edge(data_integration, climate_control)
body.order.add_edge(climate_control, nutrient_mix)

# Define the LOOP: first do System Testing, then either exit or
# execute (body) and System Testing again, repeating until exit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[system_testing, body]
)

# Build the top‐level partial order of the setup process
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    design_layout,
    crop_selection,
    sensor_setup,
    hydroponics_install,
    compliance_review,
    staff_training,
    monitor_loop,
    harvest_planning,
    packaging_setup,
    logistics_setup,
    market_launch
])

# Add the control‐flow dependencies
root.order.add_edge(site_survey,        structural_check)
root.order.add_edge(structural_check,   design_layout)

# After design, perform crop selection, sensor setup, hydroponic install in parallel
root.order.add_edge(design_layout,      crop_selection)
root.order.add_edge(design_layout,      sensor_setup)
root.order.add_edge(design_layout,      hydroponics_install)

# Once installations are in place, do the compliance review
root.order.add_edge(crop_selection,     compliance_review)
root.order.add_edge(sensor_setup,       compliance_review)
root.order.add_edge(hydroponics_install,compliance_review)

# Then staff training before entering monitoring loop
root.order.add_edge(compliance_review,  staff_training)
root.order.add_edge(staff_training,     monitor_loop)

# After exiting the loop, proceed to harvest planning and launch chain
root.order.add_edge(monitor_loop,       harvest_planning)
root.order.add_edge(harvest_planning,   packaging_setup)
root.order.add_edge(packaging_setup,    logistics_setup)
root.order.add_edge(logistics_setup,    market_launch)