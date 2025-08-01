# Generated from: 17397a8e-90c1-415e-8e3b-0671db45bf79.json
# Description: This process outlines the comprehensive steps required to establish a sustainable urban rooftop farm. It involves evaluating roof conditions, securing permits, designing modular growing units, sourcing organic soil and seeds, installing irrigation and lighting systems, implementing pest control measures, training local staff, and creating a distribution framework for fresh produce. The workflow ensures compliance with safety regulations, maximizes space utilization, and promotes community engagement through workshops and seasonal events. Continuous monitoring and maintenance guarantee optimal plant growth and yield, supporting urban food security and environmental benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
roof_survey      = Transition(label="Roof Survey")
permit_check     = Transition(label="Permit Check")
design_layout    = Transition(label="Design Layout")
module_build     = Transition(label="Module Build")
soil_sourcing    = Transition(label="Soil Sourcing")
seed_selection   = Transition(label="Seed Selection")
irrigation_install = Transition(label="Irrigation Install")
lighting_setup   = Transition(label="Lighting Setup")
pest_control     = Transition(label="Pest Control")
staff_training   = Transition(label="Staff Training")
safety_audit1    = Transition(label="Safety Audit")
planting_phase   = Transition(label="Planting Phase")
growth_monitor   = Transition(label="Growth Monitor")
safety_audit2    = Transition(label="Safety Audit")
harvest_plan     = Transition(label="Harvest Plan")
community_event  = Transition(label="Community Event")
produce_delivery = Transition(label="Produce Delivery")
skip             = SilentTransition()

# Parallel sourcing of soil and seeds
soil_seed_parallel = StrictPartialOrder(nodes=[soil_sourcing, seed_selection])

# Parallel install of irrigation and lighting
install_parallel = StrictPartialOrder(nodes=[irrigation_install, lighting_setup])

# Parallel pre‐planting tasks: pest control measures & staff training
training_parallel = StrictPartialOrder(nodes=[pest_control, staff_training])

# Monitoring & safety loop: do Growth Monitor, then either exit or do Safety Audit then repeat
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, safety_audit2])

# Optional community event
community_xor = OperatorPOWL(operator=Operator.XOR, children=[community_event, skip])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    roof_survey,
    permit_check,
    design_layout,
    module_build,
    soil_seed_parallel,
    install_parallel,
    training_parallel,
    safety_audit1,
    planting_phase,
    monitor_loop,
    harvest_plan,
    produce_delivery,
    community_xor
])

# Define the control‐flow dependencies
root.order.add_edge(roof_survey, permit_check)
root.order.add_edge(permit_check, design_layout)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, soil_seed_parallel)
root.order.add_edge(soil_seed_parallel, install_parallel)
root.order.add_edge(install_parallel, training_parallel)
root.order.add_edge(training_parallel, safety_audit1)
root.order.add_edge(safety_audit1, planting_phase)
root.order.add_edge(planting_phase, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, produce_delivery)
root.order.add_edge(harvest_plan, community_xor)