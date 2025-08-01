# Generated from: 0a7372d4-2250-44df-ba41-9ac62e4df5b3.json
# Description: This process outlines the comprehensive steps required to establish an urban rooftop farming operation in a densely populated city environment. It involves assessing the rooftop's structural integrity, obtaining necessary permits, designing modular planting systems, sourcing sustainable materials, installing irrigation and sensor networks, selecting crop varieties suited for microclimates, implementing pest management strategies, training local staff, and initiating a phased planting schedule. The process also includes continuous monitoring for environmental conditions and crop health, adaptive maintenance routines, harvesting logistics, and planning for seasonal crop rotation to maximize yield and sustainability within limited urban space constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
permit_request = Transition(label='Permit Request')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
crop_selection = Transition(label='Crop Selection')
soil_prep = Transition(label='Soil Prep')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_manage = Transition(label='Waste Manage')
season_rotate = Transition(label='Season Rotate')

# Phase 1: Assess rooftop and get permits (Site Survey -> Load Testing -> Permit Request)
assessment = StrictPartialOrder(nodes=[site_survey, load_testing, permit_request])
assessment.order.add_edge(site_survey, load_testing)
assessment.order.add_edge(load_testing, permit_request)

# Phase 2: Design and source materials (Design Layout -> Material Sourcing)
design_and_source = StrictPartialOrder(nodes=[design_layout, material_sourcing])
design_and_source.order.add_edge(design_layout, material_sourcing)

# Phase 3: Installation (Irrigation and Sensor Install concurrently after materials)
installation = StrictPartialOrder(nodes=[irrigation_setup, sensor_install])
# concurrent, no edges needed

# Phase 4: Crop preparation (Crop Selection -> Soil Prep)
prep = StrictPartialOrder(nodes=[crop_selection, soil_prep])
prep.order.add_edge(crop_selection, soil_prep)

# Phase 5: Planting phase including pest control and staff training in parallel
planting_related = StrictPartialOrder(
    nodes=[planting_phase, pest_control, staff_training])
planting_related.order.add_edge(planting_phase, pest_control)
planting_related.order.add_edge(planting_phase, staff_training)
# pest_control and staff_training concurrent after planting_phase

# Phase 6: Monitoring loop for Growth Monitor with adaptive maintenance (Waste Manage)
# Loop: Growth Monitor then choose to exit or do Waste Manage then Growth Monitor again

loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, waste_manage])

# Phase 7: Harvest plans and season rotate after monitoring loop
harvest_and_rotate = StrictPartialOrder(nodes=[harvest_plan, season_rotate])
harvest_and_rotate.order.add_edge(harvest_plan, season_rotate)

# Build overall process partial order

# Start with assessment followed by permit_request completed
# Then design_and_source
# Then installation (irrigation_setup and sensor_install in parallel)
# Then prep 
# Then planting_related
# Then monitoring loop
# Then harvest and rotate

nodes = [
    assessment,
    design_and_source,
    installation,
    prep,
    planting_related,
    loop_monitor,
    harvest_and_rotate
]

root = StrictPartialOrder(nodes=nodes)

# Establish phase order dependencies
root.order.add_edge(assessment, design_and_source)
root.order.add_edge(design_and_source, installation)
root.order.add_edge(installation, prep)
root.order.add_edge(prep, planting_related)
root.order.add_edge(planting_related, loop_monitor)
root.order.add_edge(loop_monitor, harvest_and_rotate)