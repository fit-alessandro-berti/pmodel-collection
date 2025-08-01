# Generated from: 54605b3b-6be2-4509-82e7-f8d8d2fbb835.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It includes site evaluation, environmental control system design, crop selection based on local climate and market demand, installation of hydroponic or aeroponic systems, integration of IoT sensors for real-time monitoring, staff training for automated maintenance, and implementation of a supply chain for delivering fresh produce directly to urban consumers. The process also covers sustainability assessments, waste recycling protocols, and iterative optimization of growth parameters to maximize yield and minimize resource consumption, ensuring a scalable and profitable urban agriculture operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
climate_study   = Transition(label='Climate Study')
crop_select     = Transition(label='Crop Select')
system_design   = Transition(label='System Design')

install_racks    = Transition(label='Install Racks')
install_lighting = Transition(label='Install Lighting')
install_pumps    = Transition(label='Install Pumps')

iot_setup       = Transition(label='IoT Setup')
sensor_deploy   = Transition(label='Sensor Deploy')
software_config = Transition(label='Software Config')

staff_train      = Transition(label='Staff Train')
test_run         = Transition(label='Test Run')
optimize_growth  = Transition(label='Optimize Growth')

waste_plan     = Transition(label='Waste Plan')
yield_assess   = Transition(label='Yield Assess')
market_link    = Transition(label='Market Link')
supply_dispatch = Transition(label='Supply Dispatch')

# Sequence for equipment installation: racks -> lighting -> pumps
deploy_seq = StrictPartialOrder(nodes=[install_racks, install_lighting, install_pumps])
deploy_seq.order.add_edge(install_racks, install_lighting)
deploy_seq.order.add_edge(install_lighting, install_pumps)

# Sequence for IoT integration: setup -> deploy sensors -> configure software
iot_seq = StrictPartialOrder(nodes=[iot_setup, sensor_deploy, software_config])
iot_seq.order.add_edge(iot_setup, sensor_deploy)
iot_seq.order.add_edge(sensor_deploy, software_config)

# Loop for iterative optimization: perform Test Run, then optionally Optimize Growth and repeat
optimization_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_run, optimize_growth])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    climate_study,
    crop_select,
    system_design,
    deploy_seq,
    iot_seq,
    staff_train,
    optimization_loop,
    waste_plan,
    yield_assess,
    market_link,
    supply_dispatch
])

# Add control‐flow/order edges
root.order.add_edge(site_survey,   climate_study)
root.order.add_edge(climate_study, crop_select)
root.order.add_edge(crop_select,   system_design)

# After system design, installation and IoT tasks can proceed in parallel
root.order.add_edge(system_design, deploy_seq)
root.order.add_edge(system_design, iot_seq)

# Both streams must finish before staff training
root.order.add_edge(deploy_seq,    staff_train)
root.order.add_edge(iot_seq,       staff_train)

# Staff training precedes the optimization loop
root.order.add_edge(staff_train,   optimization_loop)

# After exiting the loop, continue with waste plan, yield assessment, market linking, and dispatch
root.order.add_edge(optimization_loop, waste_plan)
root.order.add_edge(waste_plan,         yield_assess)
root.order.add_edge(yield_assess,       market_link)
root.order.add_edge(market_link,        supply_dispatch)