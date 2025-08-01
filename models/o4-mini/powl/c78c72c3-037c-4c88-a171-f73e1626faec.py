# Generated from: c78c72c3-037c-4c88-a171-f73e1626faec.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, environmental controls installation, nutrient cycling optimization, crop selection, automated irrigation setup, pest monitoring, energy management, waste recycling, and market integration. The process integrates advanced IoT sensors and AI-driven analytics to maximize yield while minimizing resource consumption. Additionally, it includes community engagement and educational program development to promote urban agriculture awareness and sustainability. The approach balances technological innovation with social impact in a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
system_build       = Transition(label='System Build')
install_sensors    = Transition(label='Install Sensors')
set_controls       = Transition(label='Set Controls')
test_modules       = Transition(label='Test Modules')
select_crops       = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
deploy_ai          = Transition(label='Deploy AI')
monitor_pests      = Transition(label='Monitor Pests')
manage_energy      = Transition(label='Manage Energy')
recycle_waste      = Transition(label='Recycle Waste')
train_staff        = Transition(label='Train Staff')
launch_market      = Transition(label='Launch Market')
engage_community   = Transition(label='Engage Community')

# Silent transition for loop entry/exit
skip = SilentTransition()

# Loop for continuous monitoring: monitor pests, manage energy, recycle waste
loop_body = StrictPartialOrder(nodes=[monitor_pests, manage_energy, recycle_waste])
loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, loop_body])

# Build the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_build,
    install_sensors, set_controls, test_modules,
    select_crops, configure_irrigation,
    deploy_ai, loop,
    train_staff, launch_market, engage_community
])

# Sequence dependencies for the main line
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build)
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(install_sensors, set_controls)
root.order.add_edge(set_controls, test_modules)

# Parallel branches start after testing modules
root.order.add_edge(test_modules, select_crops)
root.order.add_edge(test_modules, configure_irrigation)
root.order.add_edge(test_modules, deploy_ai)
root.order.add_edge(test_modules, loop)
root.order.add_edge(test_modules, train_staff)

# Sequence within branches
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(train_staff, launch_market)
root.order.add_edge(launch_market, engage_community)