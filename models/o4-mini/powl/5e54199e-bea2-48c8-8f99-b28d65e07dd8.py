# Generated from: 5e54199e-bea2-48c8-8f99-b28d65e07dd8.json
# Description: This process involves the establishment and operational integration of an urban vertical farm within a multi-use commercial building. It includes site assessment, environmental control setup, crop selection tailored for vertical growth, automation of irrigation and nutrient delivery, integration with building energy systems for sustainability, continuous crop monitoring through IoT sensors, pest management without chemicals, harvest scheduling aligned with market demand, waste recycling through composting, employee training on unique vertical farming techniques, product packaging with traceability features, distribution logistics optimized for urban delivery, customer feedback incorporation for crop improvement, and periodic system upgrades to enhance efficiency and output while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_assess    = Transition(label='Site Assess')
env_setup      = Transition(label='Env Setup')
crop_select    = Transition(label='Crop Select')
irrigation_auto= Transition(label='Irrigation Auto')
energy_sync    = Transition(label='Energy Sync')
sensor_deploy  = Transition(label='Sensor Deploy')
pest_manage    = Transition(label='Pest Manage')
harvest_plan   = Transition(label='Harvest Plan')
market_align   = Transition(label='Market Align')
waste_recycle  = Transition(label='Waste Recycle')
staff_train    = Transition(label='Staff Train')
pack_product   = Transition(label='Pack Product')
logistics_plan = Transition(label='Logistics Plan')
feedback_loop  = Transition(label='Feedback Loop')
system_upgrade = Transition(label='System Upgrade')

# Build the LOOP operator: after logistics, execute Feedback Loop,
# then either exit or do System Upgrade and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, system_upgrade])

# Construct the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_assess, env_setup, crop_select,
    irrigation_auto, energy_sync, sensor_deploy,
    pest_manage, harvest_plan, market_align,
    waste_recycle, staff_train, pack_product,
    logistics_plan, loop
])

# Define the control‐flow / precedence relations
root.order.add_edge(site_assess,    env_setup)
root.order.add_edge(env_setup,      crop_select)

# After crop selection, set up irrigation, energy sync and sensors in parallel
root.order.add_edge(crop_select,    irrigation_auto)
root.order.add_edge(crop_select,    energy_sync)
root.order.add_edge(crop_select,    sensor_deploy)

# Pest management requires sensors
root.order.add_edge(sensor_deploy,  pest_manage)

# Harvest planning follows pest management
root.order.add_edge(pest_manage,    harvest_plan)

# Align harvest with market demand
root.order.add_edge(harvest_plan,   market_align)

# After market alignment, do waste recycling
root.order.add_edge(market_align,   waste_recycle)

# Then train staff on the vertical farming techniques
root.order.add_edge(waste_recycle,  staff_train)

# Packaging and then logistics
root.order.add_edge(staff_train,    pack_product)
root.order.add_edge(pack_product,   logistics_plan)

# After logistics, enter the feedback & upgrade loop
root.order.add_edge(logistics_plan, loop)