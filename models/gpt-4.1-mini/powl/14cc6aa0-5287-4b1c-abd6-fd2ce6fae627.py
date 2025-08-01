# Generated from: 14cc6aa0-5287-4b1c-abd6-fd2ce6fae627.json
# Description: This process outlines the establishment of a fully automated urban vertical farm designed to optimize space and resource efficiency in metropolitan areas. It involves site analysis, modular structure assembly, IoT sensor integration for real-time monitoring, adaptive lighting calibration, hydroponic nutrient cycling, AI-driven pest detection, and dynamic crop rotation scheduling. The workflow also includes local community collaboration for produce distribution, sustainability compliance checks, energy consumption optimization, and post-harvest quality assurance to ensure fresh, pesticide-free yield year-round within confined urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
install_sensors = Transition(label='Install Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
setup_hydroponics = Transition(label='Setup Hydroponics')
nutrient_mix = Transition(label='Nutrient Mix')
deploy_ai = Transition(label='Deploy AI')
pest_monitor = Transition(label='Pest Monitor')
crop_rotate = Transition(label='Crop Rotate')
energy_audit = Transition(label='Energy Audit')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
harvest_test = Transition(label='Harvest Test')
distribute_produce = Transition(label='Distribute Produce')
quality_review = Transition(label='Quality Review')

# Hydroponic nutrient cycling loop: Nutrient Mix (B) repeated between Setup Hydroponics (A)
hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_hydroponics, nutrient_mix])

# AI pest detection loop: Pest Monitor (B) repeated between Deploy AI (A)
pest_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[deploy_ai, pest_monitor])

# Partial order:
# Site Survey --> Design Layout --> Structure Build --> Install Sensors --> Calibrate Lights --> hydroponic_loop --> pest_detection_loop --> Crop Rotate
# Crop Rotate and Energy Audit run concurrently after pest_detection_loop
# Then Community Meet and Compliance Check run concurrently
# Then Harvest Test --> Distribute Produce --> Quality Review

root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        structure_build,
        install_sensors,
        calibrate_lights,
        hydroponic_loop,
        pest_detection_loop,
        crop_rotate,
        energy_audit,
        community_meet,
        compliance_check,
        harvest_test,
        distribute_produce,
        quality_review
    ]
)

# Define partial order edges

# Linear sequence up to hydroponic loop
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, install_sensors)
root.order.add_edge(install_sensors, calibrate_lights)
root.order.add_edge(calibrate_lights, hydroponic_loop)

# hydroponic loop to pest detection loop
root.order.add_edge(hydroponic_loop, pest_detection_loop)

# pest detection loop to crop rotate and energy audit (concurrent)
root.order.add_edge(pest_detection_loop, crop_rotate)
root.order.add_edge(pest_detection_loop, energy_audit)

# crop rotate and energy audit to community meet and compliance check (both concurrent)
root.order.add_edge(crop_rotate, community_meet)
root.order.add_edge(crop_rotate, compliance_check)
root.order.add_edge(energy_audit, community_meet)
root.order.add_edge(energy_audit, compliance_check)

# community meet and compliance check to harvest test
root.order.add_edge(community_meet, harvest_test)
root.order.add_edge(compliance_check, harvest_test)

# harvest test linear to distribute produce and then quality review
root.order.add_edge(harvest_test, distribute_produce)
root.order.add_edge(distribute_produce, quality_review)