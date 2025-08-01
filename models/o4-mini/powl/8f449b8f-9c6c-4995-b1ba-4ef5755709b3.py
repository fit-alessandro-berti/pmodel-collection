# Generated from: 8f449b8f-9c6c-4995-b1ba-4ef5755709b3.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental control system design, hydroponic installation, crop cycle planning, nutrient solution optimization, and integration of IoT monitoring devices. Additional activities cover pest management strategies, staff training on automated systems, marketing of fresh produce to local businesses, and ongoing data analysis for yield improvement. The process ensures sustainable urban agriculture by maximizing space efficiency, reducing water usage, and promoting local food production in an atypical but realistic business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL Transitions
site_assess       = Transition(label='Site Assess')
design_hvac       = Transition(label='Design HVAC')
install_hydro     = Transition(label='Install Hydroponics')
setup_lighting    = Transition(label='Setup Lighting')
plan_crops        = Transition(label='Plan Crops')
mix_nutrients     = Transition(label='Mix Nutrients')
calibrate_sensors = Transition(label='Calibrate Sensors')
deploy_iot        = Transition(label='Deploy IoT')
train_staff       = Transition(label='Train Staff')
start_cult        = Transition(label='Start Cultivation')
pest_control      = Transition(label='Pest Control')
harvest_crops     = Transition(label='Harvest Crops')
quality_check     = Transition(label='Quality Check')
package_goods     = Transition(label='Package Goods')
distribute_produce= Transition(label='Distribute Produce')
analyze_data      = Transition(label='Analyze Data')

# Loop: cultivation phase, where after starting cultivation we may do pest control
cultivation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[start_cult, pest_control]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    design_hvac, install_hydro, setup_lighting,
    plan_crops, mix_nutrients, calibrate_sensors, deploy_iot, train_staff,
    cultivation_loop,
    harvest_crops, quality_check, package_goods, distribute_produce, analyze_data
])

# 1) After site assessment, set up environment (can be concurrent)
for env in [design_hvac, install_hydro, setup_lighting]:
    root.order.add_edge(site_assess, env)

# 2) Once environment is ready, do planning, nutrient mixing, sensor & IoT setup, and staff training
prep_tasks = [plan_crops, mix_nutrients, calibrate_sensors, deploy_iot, train_staff]
for env in [design_hvac, install_hydro, setup_lighting]:
    for task in prep_tasks:
        root.order.add_edge(env, task)

# 3) After all prep tasks, enter the cultivation & pest‐control loop
for task in prep_tasks:
    root.order.add_edge(task, cultivation_loop)

# 4) After exiting the loop, proceed to harvest and downstream activities
root.order.add_edge(cultivation_loop, harvest_crops)
root.order.add_edge(harvest_crops, quality_check)
root.order.add_edge(quality_check, package_goods)
root.order.add_edge(package_goods, distribute_produce)
root.order.add_edge(distribute_produce, analyze_data)