# Generated from: 61002564-02e9-43ca-8a29-ee1bd7d81e06.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating automated hydroponics, AI-driven climate control, and real-time crop health analytics. Starting from seed selection, the farm leverages sensor networks and robotic systems to optimize nutrient delivery and light exposure. Periodic data analysis guides pruning and harvesting schedules, while waste is recycled through on-site composting. Market demand forecasts inform planting decisions, and harvested produce undergoes quality checks before distribution. The cycle also includes maintenance of mechanical systems and continuous improvement protocols based on yield performance and resource efficiency metrics, ensuring sustainable urban agriculture within limited city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mixing')
planting = Transition(label='Planting Setup')
climate = Transition(label='Climate Control')
sensor = Transition(label='Sensor Calibration')
data_coll = Transition(label='Data Collection')
growth = Transition(label='Growth Monitoring')
pruning = Transition(label='Pruning Schedule')
pest = Transition(label='Pest Detection')
harvest = Transition(label='Harvest Planning')
quality = Transition(label='Quality Check')
waste = Transition(label='Waste Recycling')
market = Transition(label='Market Forecast')
distribution = Transition(label='Distribution Prep')
maintenance = Transition(label='System Maintenance')
yield_analysis = Transition(label='Yield Analysis')

# Concurrency of climate control and sensor calibration (A part of loop)
A_cycle = StrictPartialOrder(nodes=[climate, sensor])
# no edges => they can run in parallel

# Choice between pruning and pest detection during growth cycle
prune_or_pest = OperatorPOWL(operator=Operator.XOR, children=[pruning, pest])

# Body of the loop: the periodic operational cycle (B part of loop)
B_cycle = StrictPartialOrder(nodes=[
    data_coll,
    growth,
    prune_or_pest,
    harvest,
    quality,
    distribution,
    waste,
    market,
    maintenance,
    yield_analysis
])
# Define the sequential order in the cycle
B_cycle.order.add_edge(data_coll, growth)
B_cycle.order.add_edge(growth, prune_or_pest)
B_cycle.order.add_edge(prune_or_pest, harvest)
B_cycle.order.add_edge(harvest, quality)
B_cycle.order.add_edge(quality, distribution)
B_cycle.order.add_edge(distribution, waste)
B_cycle.order.add_edge(waste, market)
B_cycle.order.add_edge(market, maintenance)
B_cycle.order.add_edge(maintenance, yield_analysis)

# Main loop: first climate+sensor, then repeat B_cycle and A_cycle
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_cycle, B_cycle])

# Prefix: seed selection -> nutrient mixing -> planting setup -> enter main loop
root = StrictPartialOrder(nodes=[seed, nutrient, planting, main_loop])
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, planting)
root.order.add_edge(planting, main_loop)