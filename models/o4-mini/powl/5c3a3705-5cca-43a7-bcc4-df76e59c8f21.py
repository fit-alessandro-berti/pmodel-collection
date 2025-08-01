# Generated from: 5c3a3705-5cca-43a7-bcc4-df76e59c8f21.json
# Description: This process outlines the end-to-end supply chain management for an urban vertical farming operation that integrates local produce cultivation with smart logistics and sustainability practices. Starting with seed procurement, it includes controlled environment monitoring, nutrient blending, crop growth tracking, automated harvesting, quality inspection, packaging customization, cold chain management, dynamic route planning for delivery via electric vehicles, real-time inventory updates, consumer feedback integration, waste recycling, and data analytics for yield optimization. The process ensures fresh, eco-friendly produce reaches urban consumers efficiently, minimizing carbon footprint while maintaining product freshness and maximizing resource utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed = Transition(label='Seed Sourcing')
env = Transition(label='Env Monitoring')
nut = Transition(label='Nutrient Blend')
track = Transition(label='Crop Tracking')
harvest = Transition(label='Automated Harvest')
inspect = Transition(label='Quality Inspect')
pack = Transition(label='Pack Customize')
cold = Transition(label='Cold Storage')
plan = Transition(label='Route Planning')
dispatch = Transition(label='EV Dispatch')
inventory = Transition(label='Inventory Update')
feedback = Transition(label='Customer Feedback')
waste = Transition(label='Waste Recycle')
analytics = Transition(label='Data Analytics')
optimize = Transition(label='Yield Optimize')

# Continuous environment monitoring with nutrient blending as a loop
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env, nut]
)

# Data analytics followed by yield optimization
da_sequence = StrictPartialOrder(nodes=[analytics, optimize])
da_sequence.order.add_edge(analytics, optimize)

# Build the overall partially ordered workflow
root = StrictPartialOrder(nodes=[
    seed,
    loop_monitor,
    track,
    harvest,
    inspect,
    pack,
    cold,
    plan,
    dispatch,
    inventory,
    feedback,
    da_sequence,
    waste
])

# Define the control-flow relations
root.order.add_edge(seed, loop_monitor)
root.order.add_edge(loop_monitor, track)
root.order.add_edge(track, harvest)
root.order.add_edge(harvest, inspect)
root.order.add_edge(inspect, pack)
root.order.add_edge(pack, cold)
root.order.add_edge(cold, plan)
root.order.add_edge(plan, dispatch)
root.order.add_edge(dispatch, inventory)
root.order.add_edge(inventory, feedback)
# After customer feedback, branch into waste recycle and data analytics+yield optimize
root.order.add_edge(feedback, waste)
root.order.add_edge(feedback, da_sequence)