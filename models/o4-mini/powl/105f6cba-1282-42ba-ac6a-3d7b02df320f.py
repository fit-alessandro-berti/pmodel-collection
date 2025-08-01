# Generated from: 105f6cba-1282-42ba-ac6a-3d7b02df320f.json
# Description: This process outlines the establishment of an urban vertical farming system designed to optimize limited city space for sustainable food production. It integrates advanced hydroponic techniques, IoT sensor deployment, and automated nutrient delivery to ensure optimal plant growth. The process involves site analysis, modular infrastructure assembly, climate control calibration, and continuous data monitoring to maximize yield and reduce resource consumption. Additionally, it incorporates waste recycling from urban sources and energy-efficient lighting installation. The process aims to create a scalable, eco-friendly farming solution that minimizes environmental impact while addressing urban food security challenges through innovative technology and precise operational workflows.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
procure_modules    = Transition(label='Procure Modules')
install_frames     = Transition(label='Install Frames')
setup_hydroponics  = Transition(label='Setup Hydroponics')
deploy_sensors     = Transition(label='Deploy Sensors')
configure_climate  = Transition(label='Configure Climate')
calibrate_lighting = Transition(label='Calibrate Lighting')
install_automation = Transition(label='Install Automation')
implement_recycling= Transition(label='Implement Recycling')
test_systems       = Transition(label='Test Systems')
plant_seeding      = Transition(label='Plant Seeding')
monitor_growth     = Transition(label='Monitor Growth')
adjust_nutrients   = Transition(label='Adjust Nutrients')
harvest_crop       = Transition(label='Harvest Crop')
analyze_data       = Transition(label='Analyze Data')
report_metrics     = Transition(label='Report Metrics')

# Loop for continuous monitoring and nutrient adjustment
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_nutrients])

# Build the strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    install_frames,
    setup_hydroponics,
    deploy_sensors,
    configure_climate,
    calibrate_lighting,
    install_automation,
    implement_recycling,
    test_systems,
    plant_seeding,
    loop_monitoring,
    harvest_crop,
    analyze_data,
    report_metrics
])

# Define the control-flow order
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, procure_modules)
root.order.add_edge(procure_modules, install_frames)
root.order.add_edge(install_frames, setup_hydroponics)
root.order.add_edge(setup_hydroponics, deploy_sensors)
root.order.add_edge(deploy_sensors, configure_climate)
root.order.add_edge(configure_climate, calibrate_lighting)
root.order.add_edge(calibrate_lighting, install_automation)
root.order.add_edge(install_automation, implement_recycling)
root.order.add_edge(implement_recycling, test_systems)
root.order.add_edge(test_systems, plant_seeding)
root.order.add_edge(plant_seeding, loop_monitoring)
root.order.add_edge(loop_monitoring, harvest_crop)
root.order.add_edge(harvest_crop, analyze_data)
root.order.add_edge(analyze_data, report_metrics)