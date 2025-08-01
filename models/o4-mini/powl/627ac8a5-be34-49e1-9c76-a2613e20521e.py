# Generated from: 627ac8a5-be34-49e1-9c76-a2613e20521e.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics, AI-driven environmental control, and community engagement. It begins with seed sourcing and germination, followed by automated nutrient mixing and lighting adjustments. Continuous monitoring through sensors feeds data into an AI system that optimizes growth conditions dynamically. Periodic pest control using eco-friendly methods ensures plant health without chemicals. Harvesting is coordinated with packaging customized for urban delivery logistics. Additionally, the process includes waste recycling via composting and water reuse mechanisms. Community workshops and data sharing foster urban agricultural literacy and participation, closing the loop between production and consumption in a sustainable, tech-enabled ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
seed = Transition(label='Seed Sourcing')
germination = Transition(label='Germination Start')
nutrient = Transition(label='Nutrient Mix')
light = Transition(label='Light Adjust')
sensor = Transition(label='Sensor Check')
ai_opt = Transition(label='AI Optimization')
growth_scan = Transition(label='Growth Scan')
pest = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
crop_picking = Transition(label='Crop Picking')
pack_assemble = Transition(label='Pack Assemble')
delivery_sync = Transition(label='Delivery Sync')
waste_sort = Transition(label='Waste Sort')
water_reuse = Transition(label='Water Reuse')
workshop = Transition(label='Workshop Host')
data_share = Transition(label='Data Share')

# Build the monitoring & pest‐control loop: A = sensor → ai → scan ; B = pest control
A_loop = StrictPartialOrder(nodes=[sensor, ai_opt, growth_scan])
A_loop.order.add_edge(sensor, ai_opt)
A_loop.order.add_edge(ai_opt, growth_scan)

loop_model = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A_loop, pest]
)

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    seed, germination, nutrient, light,
    loop_model,
    harvest_plan, crop_picking, pack_assemble, delivery_sync,
    waste_sort, water_reuse, workshop, data_share
])

# Sequential flow up to loop
root.order.add_edge(seed, germination)
root.order.add_edge(germination, nutrient)
root.order.add_edge(nutrient, light)
root.order.add_edge(light, loop_model)

# After exiting the loop: harvest & delivery
root.order.add_edge(loop_model, harvest_plan)
root.order.add_edge(harvest_plan, crop_picking)
root.order.add_edge(crop_picking, pack_assemble)
root.order.add_edge(pack_assemble, delivery_sync)

# Post‐harvest concurrent tasks: waste & water recycling, community engagement
root.order.add_edge(delivery_sync, waste_sort)
root.order.add_edge(delivery_sync, water_reuse)
root.order.add_edge(delivery_sync, workshop)
root.order.add_edge(delivery_sync, data_share)