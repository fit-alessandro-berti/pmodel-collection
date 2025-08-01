# Generated from: 54605b3b-6be2-4509-82e7-f8d8d2fbb835.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It includes site evaluation, environmental control system design, crop selection based on local climate and market demand, installation of hydroponic or aeroponic systems, integration of IoT sensors for real-time monitoring, staff training for automated maintenance, and implementation of a supply chain for delivering fresh produce directly to urban consumers. The process also covers sustainability assessments, waste recycling protocols, and iterative optimization of growth parameters to maximize yield and minimize resource consumption, ensuring a scalable and profitable urban agriculture operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
crop_select = Transition(label='Crop Select')
system_design = Transition(label='System Design')

iot_setup = Transition(label='IoT Setup')

install_racks = Transition(label='Install Racks')
install_lighting = Transition(label='Install Lighting')
install_pumps = Transition(label='Install Pumps')

sensor_deploy = Transition(label='Sensor Deploy')
software_config = Transition(label='Software Config')

staff_train = Transition(label='Staff Train')
test_run = Transition(label='Test Run')

waste_plan = Transition(label='Waste Plan')
yield_assess = Transition(label='Yield Assess')

market_link = Transition(label='Market Link')

optimize_growth = Transition(label='Optimize Growth')

supply_dispatch = Transition(label='Supply Dispatch')

# Construct partial orders:

# Site evaluation and system design group (site survey -> climate study -> crop select -> system design)
site_porder = StrictPartialOrder(
    nodes=[site_survey, climate_study, crop_select, system_design]
)
site_porder.order.add_edge(site_survey, climate_study)
site_porder.order.add_edge(climate_study, crop_select)
site_porder.order.add_edge(crop_select, system_design)

# Installation of infrastructure components concurrently (racks, lighting, pumps)
install_porder = StrictPartialOrder(
    nodes=[install_racks, install_lighting, install_pumps]
)
# no order => concurrent

# IoT setup and sensor deployment (iot_setup -> sensor_deploy -> software_config)
iot_porder = StrictPartialOrder(
    nodes=[iot_setup, sensor_deploy, software_config]
)
iot_porder.order.add_edge(iot_setup, sensor_deploy)
iot_porder.order.add_edge(sensor_deploy, software_config)

# Staff training and test run (staff_train -> test_run)
train_porder = StrictPartialOrder(
    nodes=[staff_train, test_run]
)
train_porder.order.add_edge(staff_train, test_run)

# Sustainability and yield assessment (waste_plan and yield_assess concurrent)
sustain_porder = StrictPartialOrder(
    nodes=[waste_plan, yield_assess]
)
# no edges => concurrent

# Market linking and supply dispatch (market_link -> supply_dispatch)
market_porder = StrictPartialOrder(
    nodes=[market_link, supply_dispatch]
)
market_porder.order.add_edge(market_link, supply_dispatch)

# Loop for iterative optimization: 
# Loop with body = optimize_growth, redo = silent transition (exit)
loop_opt = OperatorPOWL(operator=Operator.LOOP, children=[optimize_growth, SilentTransition()])

# Build the overall process as partial order
# Order dependency map (logical from description):
# site_porder -> system_design -> install_porder and iot_porder (in parallel)
# iot_porder and install_porder must finish before staff training and test run
# sustainability assessments (sustain_porder) can run concurrently with staff_train/test_run
# after that, market_link and supply_dispatch
# finally the optimization loop repeats the yield_assess then optimize_growth ?

# To model the dependency from system_design to install_porder and iot_porder, 
# these two partial orders must start after system_design.

# Create a higher-level PO with all nodes as follows
# We use operators or just nodes at high level:
# Nodes: site_porder, install_porder, iot_porder, train_porder, sustain_porder, market_porder, loop_opt

# Note that the nodes themselves are POWL models, so we can embed them.

# Construct root partial order
root = StrictPartialOrder(
    nodes=[site_porder, install_porder, iot_porder, train_porder, sustain_porder, market_porder, loop_opt]
)

# Add orders
# site_porder finishes before install and iot setup start
root.order.add_edge(site_porder, install_porder)
root.order.add_edge(site_porder, iot_porder)

# install and iot finish before training
root.order.add_edge(install_porder, train_porder)
root.order.add_edge(iot_porder, train_porder)

# training and sustainability can run concurrently, but to wait for training finish before market
root.order.add_edge(train_porder, market_porder)

# no strict order between sustain_porder and train_porder (concurrent)

# market_porder before the optimization loop
root.order.add_edge(market_porder, loop_opt)

# Loop involves optimize_growth, but optimize_growth node is inside loop_opt children,
# so no explicit edge needed here.

# Optional: Make yield_assess part of the loop to simulate iterative optimization:
# But no direct loop back defined; we keep as is with existing structure.

# This matches the description well:
# Site survey -> design -> install & iot in parallel -> training -> market linking -> loop optimization
