# Generated from: 1528ad7c-bd53-464f-94b3-4c36be12f57d.json
# Description: This process describes the complex and atypical steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It encompasses site assessment, modular structure design, climate control calibration, advanced hydroponic system installation, sensor network deployment for real-time monitoring, and integration with renewable energy sources. The process also includes staff training on specialized equipment, compliance with urban agriculture regulations, yield forecasting using AI analytics, and establishing distribution channels targeting local markets. This ensures sustainable food production in limited city spaces while optimizing resource efficiency and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label="Site Survey")
design_modules   = Transition(label="Design Modules")
install_framework= Transition(label="Install Framework")
setup_hvac       = Transition(label="Setup HVAC")
configure_light  = Transition(label="Configure Lighting")
deploy_sensors   = Transition(label="Deploy Sensors")
install_hydro    = Transition(label="Install Hydroponics")
energy_integration = Transition(label="Energy Integration")
staff_training   = Transition(label="Staff Training")
compliance_check = Transition(label="Compliance Check")
system_testing   = Transition(label="System Testing")
ai_forecasting   = Transition(label="AI Forecasting")
optimize_workflow= Transition(label="Optimize Workflow")
market_setup     = Transition(label="Market Setup")
launch_operations= Transition(label="Launch Operations")

# Build the loop for testing & forecasting, allowing re-optimization
# A-part: system testing -> AI forecasting
loop_body = StrictPartialOrder(nodes=[system_testing, ai_forecasting])
loop_body.order.add_edge(system_testing, ai_forecasting)
# B-part: optimize workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, optimize_workflow])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_modules, install_framework,
    setup_hvac, configure_light,
    deploy_sensors, install_hydro,
    energy_integration, staff_training,
    compliance_check, loop,
    market_setup, launch_operations
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,       design_modules)
root.order.add_edge(design_modules,    install_framework)

# After framework install, HVAC and lighting can proceed in parallel
root.order.add_edge(install_framework, setup_hvac)
root.order.add_edge(install_framework, configure_light)

# Both HVAC & lighting must finish before sensors & hydroponics
root.order.add_edge(setup_hvac,        deploy_sensors)
root.order.add_edge(setup_hvac,        install_hydro)
root.order.add_edge(configure_light,   deploy_sensors)
root.order.add_edge(configure_light,   install_hydro)

# Sensors & hydroponics in parallel, then energy integration
root.order.add_edge(deploy_sensors,    energy_integration)
root.order.add_edge(install_hydro,     energy_integration)

# Then staff training, compliance, looping, market setup, and launch
root.order.add_edge(energy_integration, staff_training)
root.order.add_edge(staff_training,     compliance_check)
root.order.add_edge(compliance_check,   loop)
root.order.add_edge(loop,               market_setup)
root.order.add_edge(market_setup,       launch_operations)