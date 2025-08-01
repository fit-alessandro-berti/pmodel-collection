# Generated from: 0a7372d4-2250-44df-ba41-9ac62e4df5b3.json
# Description: This process outlines the comprehensive steps required to establish an urban rooftop farming operation in a densely populated city environment. It involves assessing the rooftop's structural integrity, obtaining necessary permits, designing modular planting systems, sourcing sustainable materials, installing irrigation and sensor networks, selecting crop varieties suited for microclimates, implementing pest management strategies, training local staff, and initiating a phased planting schedule. The process also includes continuous monitoring for environmental conditions and crop health, adaptive maintenance routines, harvesting logistics, and planning for seasonal crop rotation to maximize yield and sustainability within limited urban space constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
site_survey = Transition(label="Site Survey")
load_testing = Transition(label="Load Testing")
permit_request = Transition(label="Permit Request")
design_layout = Transition(label="Design Layout")
material_sourcing = Transition(label="Material Sourcing")
irrigation_setup = Transition(label="Irrigation Setup")
sensor_install = Transition(label="Sensor Install")
staff_training = Transition(label="Staff Training")

crop_selection = Transition(label="Crop Selection")
soil_prep = Transition(label="Soil Prep")
planting_phase = Transition(label="Planting Phase")
growth_monitor = Transition(label="Growth Monitor")
pest_control = Transition(label="Pest Control")
harvest_plan = Transition(label="Harvest Plan")
waste_manage = Transition(label="Waste Manage")
season_rotate = Transition(label="Season Rotate")

# Define the continuous monitoring loop: Growth Monitor then Pest Control
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Define one seasonal cycle (select -> prep -> plant -> monitor loop -> harvest -> waste)
season_sequence = StrictPartialOrder(nodes=[
    crop_selection,
    soil_prep,
    planting_phase,
    monitor_loop,
    harvest_plan,
    waste_manage
])
# ordering within a season
season_sequence.order.add_edge(crop_selection, soil_prep)
season_sequence.order.add_edge(soil_prep, planting_phase)
season_sequence.order.add_edge(planting_phase, monitor_loop)
season_sequence.order.add_edge(monitor_loop, harvest_plan)
season_sequence.order.add_edge(harvest_plan, waste_manage)

# Define the seasonal rotation loop: execute one season then optionally rotate and repeat
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[season_sequence, season_rotate]
)

# Build the main workflow partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_testing,
    permit_request,
    design_layout,
    material_sourcing,
    irrigation_setup,
    sensor_install,
    staff_training,
    seasonal_loop
])

# Structural assessment and permitting
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, permit_request)
root.order.add_edge(permit_request, design_layout)

# Design and sourcing
root.order.add_edge(design_layout, material_sourcing)

# Installation in parallel
root.order.add_edge(material_sourcing, irrigation_setup)
root.order.add_edge(material_sourcing, sensor_install)

# Training after both installations
root.order.add_edge(irrigation_setup, staff_training)
root.order.add_edge(sensor_install, staff_training)

# After training, begin seasonal cycles
root.order.add_edge(staff_training, seasonal_loop)