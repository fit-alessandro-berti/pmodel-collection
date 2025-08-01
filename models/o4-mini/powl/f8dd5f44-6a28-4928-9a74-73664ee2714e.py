# Generated from: f8dd5f44-6a28-4928-9a74-73664ee2714e.json
# Description: This process outlines the end-to-end operations of an urban vertical farming supply chain, integrating advanced hydroponics, automated harvesting, and AI-driven demand forecasting. It begins with seed selection and nutrient formulation, followed by controlled environment monitoring and pest detection using IoT sensors. Crops are then harvested via robotic arms, quality-checked by computer vision systems, and packaged in biodegradable containers. Distribution leverages micro-fulfillment centers to enable rapid delivery to local markets while minimizing carbon footprint. Feedback loops from consumer preferences inform adaptive crop planning and resource allocation, ensuring sustainability and profitability in a complex urban agricultural ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
env = Transition(label='Environment Setup')
sensor = Transition(label='Sensor Deployment')
monitoring = Transition(label='Growth Monitoring')
pest = Transition(label='Pest Detection')
harvest = Transition(label='Automated Harvest')
quality = Transition(label='Quality Check')
prep = Transition(label='Packaging Prep')
pack = Transition(label='Biodegradable Pack')
inv = Transition(label='Inventory Sync')
demand = Transition(label='Demand Forecast')
micro = Transition(label='Micro Fulfillment')
local = Transition(label='Local Dispatch')
feedback = Transition(label='Consumer Feedback')
adjust = Transition(label='Crop Adjustment')

# Main workflow partial order (A)
full_flow = StrictPartialOrder(nodes=[
    seed, nutrient, env, sensor, monitoring, pest,
    harvest, quality, prep, pack, inv, demand, micro, local
])
full_flow.order.add_edge(seed, nutrient)
full_flow.order.add_edge(nutrient, env)
full_flow.order.add_edge(env, sensor)
full_flow.order.add_edge(sensor, monitoring)
full_flow.order.add_edge(monitoring, pest)
full_flow.order.add_edge(pest, harvest)
full_flow.order.add_edge(harvest, quality)
full_flow.order.add_edge(quality, prep)
full_flow.order.add_edge(prep, pack)
full_flow.order.add_edge(pack, inv)
full_flow.order.add_edge(inv, demand)
full_flow.order.add_edge(demand, micro)
full_flow.order.add_edge(micro, local)

# Adaptive feedback partial order (B)
adjustment = StrictPartialOrder(nodes=[feedback, adjust])
adjustment.order.add_edge(feedback, adjust)

# Loop: execute full_flow, then optionally do adjustment and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[full_flow, adjustment])