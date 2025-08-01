# Generated from: 8f8dad2d-a43b-413f-8154-b9a85aaac586.json
# Description: This process describes a complex urban farming system that integrates aquaponics, renewable energy, and real-time data analytics to optimize crop yield and resource efficiency. The cycle begins with environmental sensing and seed selection, followed by adaptive nutrient balancing and automated pest control. It incorporates waste recycling from local sources, energy management through solar and wind inputs, and dynamic scheduling based on weather predictions. Continuous monitoring ensures plant health, while machine learning algorithms adjust growth parameters. Harvesting is synchronized with market demand forecasts, and post-harvest processing includes packaging and distribution using sustainable logistics. The process closes with community feedback integration and system maintenance to enhance future cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# atomic activities
seed = Transition(label='Seed Select')
env = Transition(label='Env Sensing')
waste = Transition(label='Waste Collect')
water_filter = Transition(label='Water Filter')
nutrient = Transition(label='Nutrient Mix')
pest = Transition(label='Pest Control')
energy = Transition(label='Energy Charge')
data_monitor = Transition(label='Data Monitor')
growth_adjust = Transition(label='Growth Adjust')
health_check = Transition(label='Health Check')
market_sync = Transition(label='Market Sync')
harvest = Transition(label='Harvest Crop')
package_goods = Transition(label='Package Goods')
logistics = Transition(label='Logistics Plan')
feedback = Transition(label='Feedback Loop')
maintain = Transition(label='System Maintain')

# loop for continuous monitoring & adjustment:
#   A = Data Monitor
#   B = (Growth Adjust -> Health Check)
b = StrictPartialOrder(nodes=[growth_adjust, health_check])
b.order.add_edge(growth_adjust, health_check)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, b])

# root partial order assembling the full process
root = StrictPartialOrder(nodes=[
    seed, env,
    waste, water_filter, nutrient, pest,
    energy,
    monitor_loop,
    market_sync, harvest,
    package_goods, logistics,
    feedback, maintain
])

# ordering constraints
# initial concurrent sensing & selection → waste recycling
root.order.add_edge(seed, waste)
root.order.add_edge(env, waste)

# waste recycling → water filter → nutrient mixing → pest control
root.order.add_edge(waste, water_filter)
root.order.add_edge(water_filter, nutrient)
root.order.add_edge(nutrient, pest)

# pest control → energy management → monitoring loop
root.order.add_edge(pest, energy)
root.order.add_edge(energy, monitor_loop)

# exit monitoring loop → market sync → harvest → packaging → logistics → feedback → maintenance
root.order.add_edge(monitor_loop, market_sync)
root.order.add_edge(market_sync, harvest)
root.order.add_edge(harvest, package_goods)
root.order.add_edge(package_goods, logistics)
root.order.add_edge(logistics, feedback)
root.order.add_edge(feedback, maintain)