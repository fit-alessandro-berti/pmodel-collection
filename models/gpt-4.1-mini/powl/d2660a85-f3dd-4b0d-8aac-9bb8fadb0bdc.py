# Generated from: d2660a85-f3dd-4b0d-8aac-9bb8fadb0bdc.json
# Description: This process details the comprehensive setup of an urban vertical farming operation within a repurposed industrial building. It involves site assessment, modular infrastructure design, environmental control configuration, crop selection tailored to urban microclimates, integration of automated irrigation and nutrient delivery systems, installation of energy-efficient LED lighting optimized for photosynthesis, establishment of remote monitoring capabilities via IoT sensors, staff training on hydroponic techniques, implementation of pest management protocols emphasizing biological controls, and launch of supply chain logistics to deliver fresh produce directly to local markets, all while ensuring sustainability and regulatory compliance throughout the operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition nodes
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
set_controls = Transition(label='Set Controls')
select_crops = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
setup_lighting = Transition(label='Setup Lighting')
deploy_sensors = Transition(label='Deploy Sensors')
train_staff = Transition(label='Train Staff')
start_cultivation = Transition(label='Start Cultivation')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
harvest_crops = Transition(label='Harvest Crops')
pack_produce = Transition(label='Pack Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define the sequence orderings reflecting the described process flow:
# Site Survey --> Design Layout --> Install Modules --> Set Controls --> Select Crops
# --> Configure Irrigation --> Setup Lighting --> Deploy Sensors --> Train Staff
# --> Start Cultivation --> Monitor Growth --> Manage Pests --> Harvest Crops
# --> Pack Produce --> Distribute Goods

root = StrictPartialOrder(
    nodes=[
        site_survey, design_layout, install_modules, set_controls, select_crops,
        configure_irrigation, setup_lighting, deploy_sensors, train_staff,
        start_cultivation, monitor_growth, manage_pests, harvest_crops,
        pack_produce, distribute_goods
    ]
)

root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, select_crops)
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(configure_irrigation, setup_lighting)
root.order.add_edge(setup_lighting, deploy_sensors)
root.order.add_edge(deploy_sensors, train_staff)
root.order.add_edge(train_staff, start_cultivation)
root.order.add_edge(start_cultivation, monitor_growth)
root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(manage_pests, harvest_crops)
root.order.add_edge(harvest_crops, pack_produce)
root.order.add_edge(pack_produce, distribute_goods)