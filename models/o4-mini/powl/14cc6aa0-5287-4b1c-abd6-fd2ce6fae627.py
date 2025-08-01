# Generated from: 14cc6aa0-5287-4b1c-abd6-fd2ce6fae627.json
# Description: This process outlines the establishment of a fully automated urban vertical farm designed to optimize space and resource efficiency in metropolitan areas. It involves site analysis, modular structure assembly, IoT sensor integration for real-time monitoring, adaptive lighting calibration, hydroponic nutrient cycling, AI-driven pest detection, and dynamic crop rotation scheduling. The workflow also includes local community collaboration for produce distribution, sustainability compliance checks, energy consumption optimization, and post-harvest quality assurance to ensure fresh, pesticide-free yield year-round within confined urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
structure_build  = Transition(label='Structure Build')
install_sensors  = Transition(label='Install Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
setup_hydroponics= Transition(label='Setup Hydroponics')
nutrient_mix     = Transition(label='Nutrient Mix')
deploy_ai        = Transition(label='Deploy AI')
pest_monitor     = Transition(label='Pest Monitor')
crop_rotate      = Transition(label='Crop Rotate')
energy_audit     = Transition(label='Energy Audit')
community_meet   = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
harvest_test     = Transition(label='Harvest Test')
quality_review   = Transition(label='Quality Review')
distribute_produce = Transition(label='Distribute Produce')

# Model the repeating processes as loops
# Nutrient cycling loop
nutrient_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[nutrient_mix, nutrient_mix]
)

# Pest monitoring loop
pest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_monitor, pest_monitor]
)

# Crop rotation loop
crop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_rotate, crop_rotate]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    install_sensors,
    calibrate_lights,
    setup_hydroponics,
    nutrient_loop,
    deploy_ai,
    pest_loop,
    crop_loop,
    energy_audit,
    community_meet,
    compliance_check,
    harvest_test,
    quality_review,
    distribute_produce
])

# Define the control‐flow dependencies (-->)
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    structure_build)
root.order.add_edge(structure_build,  install_sensors)
root.order.add_edge(install_sensors,  calibrate_lights)
root.order.add_edge(calibrate_lights, setup_hydroponics)

# Hydroponics to nutrient cycling
root.order.add_edge(setup_hydroponics, nutrient_loop)
root.order.add_edge(nutrient_loop,     deploy_ai)

# AI deployment to pest monitoring
root.order.add_edge(deploy_ai, pest_loop)

# Pest monitoring to crop rotation
root.order.add_edge(pest_loop, crop_loop)

# After crop rotation, run community engagement, compliance and energy audit in parallel
root.order.add_edge(crop_loop, community_meet)
root.order.add_edge(crop_loop, compliance_check)
root.order.add_edge(crop_loop, energy_audit)

# All three must complete before harvest testing
root.order.add_edge(community_meet,   harvest_test)
root.order.add_edge(compliance_check, harvest_test)
root.order.add_edge(energy_audit,     harvest_test)

# Final steps: harvest → quality review → distribution
root.order.add_edge(harvest_test,   quality_review)
root.order.add_edge(quality_review, distribute_produce)