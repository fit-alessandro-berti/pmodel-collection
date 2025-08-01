# Generated from: 5e54199e-bea2-48c8-8f99-b28d65e07dd8.json
# Description: This process involves the establishment and operational integration of an urban vertical farm within a multi-use commercial building. It includes site assessment, environmental control setup, crop selection tailored for vertical growth, automation of irrigation and nutrient delivery, integration with building energy systems for sustainability, continuous crop monitoring through IoT sensors, pest management without chemicals, harvest scheduling aligned with market demand, waste recycling through composting, employee training on unique vertical farming techniques, product packaging with traceability features, distribution logistics optimized for urban delivery, customer feedback incorporation for crop improvement, and periodic system upgrades to enhance efficiency and output while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_assess = Transition(label='Site Assess')
env_setup = Transition(label='Env Setup')
crop_select = Transition(label='Crop Select')
irrigation_auto = Transition(label='Irrigation Auto')
energy_sync = Transition(label='Energy Sync')
sensor_deploy = Transition(label='Sensor Deploy')
pest_manage = Transition(label='Pest Manage')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
staff_train = Transition(label='Staff Train')
pack_product = Transition(label='Pack Product')
logistics_plan = Transition(label='Logistics Plan')
feedback_loop = Transition(label='Feedback Loop')
system_upgrade = Transition(label='System Upgrade')
market_align = Transition(label='Market Align')

# Model the main partial order structure:

# Logical sequence of initial setup activities
# Site Assess --> Env Setup (environment preparation)
# Env Setup --> Crop Select
# Crop Select --> Irrigation Auto and Energy Sync can be done concurrently after Crop Select
# Irrigation Auto and Energy Sync --> Sensor Deploy
# Sensor Deploy --> Pest Manage
# Pest Manage --> Harvest Plan

# After Harvest Plan, Waste Recycle and Staff Train can proceed concurrently
# Then: Pack Product --> Logistics Plan --> Market Align

# Feedback Loop and System Upgrade form a loop after Market Align
# The loop: execute Feedback Loop, then either exit or do System Upgrade and Feedback Loop again

# Create the partial order nodes including transitions and operators

# LOOP for feedback and upgrades: *(Feedback Loop, System Upgrade)
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, system_upgrade])

# Define partial order nodes
nodes = [
    site_assess,
    env_setup,
    crop_select,
    irrigation_auto,
    energy_sync,
    sensor_deploy,
    pest_manage,
    harvest_plan,
    waste_recycle,
    staff_train,
    pack_product,
    logistics_plan,
    market_align,
    loop_feedback
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for the partial order dependencies
root.order.add_edge(site_assess, env_setup)
root.order.add_edge(env_setup, crop_select)

root.order.add_edge(crop_select, irrigation_auto)
root.order.add_edge(crop_select, energy_sync)

root.order.add_edge(irrigation_auto, sensor_deploy)
root.order.add_edge(energy_sync, sensor_deploy)

root.order.add_edge(sensor_deploy, pest_manage)
root.order.add_edge(pest_manage, harvest_plan)

root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(harvest_plan, staff_train)

root.order.add_edge(waste_recycle, pack_product)
root.order.add_edge(staff_train, pack_product)

root.order.add_edge(pack_product, logistics_plan)
root.order.add_edge(logistics_plan, market_align)

root.order.add_edge(market_align, loop_feedback)