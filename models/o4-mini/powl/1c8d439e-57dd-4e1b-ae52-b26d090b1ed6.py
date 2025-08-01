# Generated from: 1c8d439e-57dd-4e1b-ae52-b26d090b1ed6.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm, integrating advanced hydroponics, IoT sensor networks, renewable energy sources, and automated harvesting systems. The process begins with site assessment and feasibility studies, followed by modular structure design tailored for limited urban spaces. Next, installation of climate control systems and nutrient delivery networks ensures optimal plant growth conditions. Integration of AI-driven monitoring and predictive maintenance reduces downtime and maximizes yield. Subsequent stages include staff training on system operations, trial planting phases to calibrate environmental parameters, and establishing logistics for produce distribution within city markets. This atypical yet realistic process requires coordination between architects, engineers, agronomists, and supply chain managers, highlighting the multidisciplinary nature of sustainable urban agriculture ventures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess       = Transition(label='Site Assess')
design_module     = Transition(label='Design Module')
install_hydro     = Transition(label='Install Hydroponics')
setup_sensors     = Transition(label='Setup Sensors')
configure_climate = Transition(label='Configure Climate')
install_lighting  = Transition(label='Install Lighting')
connect_energy    = Transition(label='Connect Energy')
program_ai        = Transition(label='Program AI')
test_systems      = Transition(label='Test Systems')
train_staff       = Transition(label='Train Staff')
trial_planting    = Transition(label='Trial Planting')
monitor_growth    = Transition(label='Monitor Growth')
adjust_nutrients  = Transition(label='Adjust Nutrients')
schedule_harvest  = Transition(label='Schedule Harvest')
plan_logistics    = Transition(label='Plan Logistics')
distribute_prod   = Transition(label='Distribute Produce')

# Loop for trial-planting calibration: do (trial planting -> monitor growth), then decide to exit or adjust nutrients and repeat
body = StrictPartialOrder(nodes=[trial_planting, monitor_growth])
body.order.add_edge(trial_planting, monitor_growth)
redo = adjust_nutrients
trial_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# Build the full partial order
root = StrictPartialOrder(nodes=[
    site_assess, design_module,
    install_hydro, setup_sensors, configure_climate, install_lighting, connect_energy,
    program_ai, test_systems, train_staff,
    trial_loop,
    schedule_harvest, plan_logistics, distribute_prod
])

# Define the control-flow relations
root.order.add_edge(site_assess, design_module)
# After design, installations can proceed in parallel
for step in [install_hydro, setup_sensors, configure_climate, install_lighting, connect_energy]:
    root.order.add_edge(design_module, step)
    root.order.add_edge(step, program_ai)
# AI programming and testing
root.order.add_edge(program_ai, test_systems)
# Staff training before calibration
root.order.add_edge(test_systems, train_staff)
# Enter trial loop
root.order.add_edge(train_staff, trial_loop)
# After calibration loop, schedule and distribute
root.order.add_edge(trial_loop, schedule_harvest)
root.order.add_edge(schedule_harvest, plan_logistics)
root.order.add_edge(plan_logistics, distribute_prod)