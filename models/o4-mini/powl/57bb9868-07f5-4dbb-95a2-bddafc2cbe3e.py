# Generated from: 57bb9868-07f5-4dbb-95a2-bddafc2cbe3e.json
# Description: This process outlines the complex logistics and operational steps involved in managing an urban vertical farming supply chain. It begins with seed procurement and genetic selection, followed by environmental calibration and hydroponic setup. Continuous monitoring of nutrient levels and pest control ensures optimal plant growth. Harvesting is scheduled based on data analytics predicting peak freshness. Post-harvest processing includes automated packaging and quality inspection. The produce is then routed through cold-chain logistics and distributed via micro-fulfillment centers to local retailers and direct-to-consumer platforms. Feedback loops from sales data influence future crop planning and resource allocation, creating a dynamic, sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Sourcing')
genetic = Transition(label='Genetic Select')
env_cal = Transition(label='Env Calibration')
hydro = Transition(label='Hydro Setup')
nutrient = Transition(label='Nutrient Monitor')
pest = Transition(label='Pest Control')
analytics = Transition(label='Growth Analytics')
harvest = Transition(label='Harvest Plan')
pack = Transition(label='Automated Pack')
quality = Transition(label='Quality Check')
cold = Transition(label='Cold Storage')
route = Transition(label='Logistics Route')
micro = Transition(label='Micro Fulfill')
retail = Transition(label='Retail Supply')
consumer = Transition(label='Consumer Ship')
sales = Transition(label='Sales Feedback')
adjust = Transition(label='Crop Adjust')

# Silent skip for loops
skip = SilentTransition()

# Monitoring loop: Nutrient Monitor and Pest Control repeat until exit
monitor_body = StrictPartialOrder(nodes=[nutrient, pest])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, skip])

# Main body of the workflow
body = StrictPartialOrder(nodes=[
    seed, genetic, env_cal, hydro,
    monitor_loop,
    analytics, harvest,
    pack, quality,
    cold, route,
    micro, retail, consumer
])
body.order.add_edge(seed, genetic)
body.order.add_edge(genetic, env_cal)
body.order.add_edge(env_cal, hydro)
body.order.add_edge(hydro, monitor_loop)
body.order.add_edge(monitor_loop, analytics)
body.order.add_edge(analytics, harvest)
body.order.add_edge(harvest, pack)
body.order.add_edge(pack, quality)
body.order.add_edge(quality, cold)
body.order.add_edge(cold, route)
body.order.add_edge(route, micro)
body.order.add_edge(micro, retail)
body.order.add_edge(micro, consumer)

# Feedback loop: Sales Feedback -> Crop Adjust
redo = StrictPartialOrder(nodes=[sales, adjust])
redo.order.add_edge(sales, adjust)

# Top-level loop integrating feedback into the main body
root = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])