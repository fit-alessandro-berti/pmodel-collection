# Generated from: 97030c7f-5355-4ece-8743-41ac91ff79a5.json
# Description: This process outlines the complete operational cycle of an urban vertical farm, integrating advanced IoT monitoring, automated nutrient delivery, and energy-efficient lighting adjustments. It involves crop selection based on market trends, seed germination in controlled chambers, continuous environmental data collection, adaptive irrigation, pest detection through AI imaging, yield forecasting, and post-harvest quality analysis. This atypical business process blends agricultural science with smart technology to optimize crop production in limited urban spaces while minimizing resource consumption and ensuring consistent product quality for local distribution networks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
t_trend = Transition(label='Trend Analysis')
t_chamber = Transition(label='Chamber Setup')
t_seed = Transition(label='Seed Germination')
t_env = Transition(label='Env Monitoring')
t_irrigation = Transition(label='Irrigation Control')
t_nutrient = Transition(label='Nutrient Mix')
t_lighting = Transition(label='Lighting Adjust')
t_climate = Transition(label='Climate Adjust')
t_pest = Transition(label='Pest Detection')
t_growth = Transition(label='Growth Tracking')
t_yield_forecast = Transition(label='Yield Forecast')
t_harvest = Transition(label='Harvest Plan')
t_quality = Transition(label='Quality Check')
t_packaging = Transition(label='Packaging Prep')
t_delivery = Transition(label='Delivery Schedule')

# Build the monitoring-and-control cycle as a loop
cycle_tasks = StrictPartialOrder(nodes=[
    t_env, t_irrigation, t_nutrient, t_lighting,
    t_climate, t_pest, t_growth, t_yield_forecast
])
cycle_tasks.order.add_edge(t_env, t_irrigation)
cycle_tasks.order.add_edge(t_irrigation, t_nutrient)
cycle_tasks.order.add_edge(t_nutrient, t_lighting)
cycle_tasks.order.add_edge(t_lighting, t_climate)
cycle_tasks.order.add_edge(t_climate, t_pest)
cycle_tasks.order.add_edge(t_pest, t_growth)
cycle_tasks.order.add_edge(t_growth, t_yield_forecast)

# Define the loop operator: repeat the cycle until exit
cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_tasks, cycle_tasks])

# Assemble the full process
root = StrictPartialOrder(nodes=[
    t_trend,
    t_chamber,
    t_seed,
    cycle_loop,
    t_harvest,
    t_quality,
    t_packaging,
    t_delivery
])
root.order.add_edge(t_trend, t_chamber)
root.order.add_edge(t_chamber, t_seed)
root.order.add_edge(t_seed, cycle_loop)
root.order.add_edge(cycle_loop, t_harvest)
root.order.add_edge(t_harvest, t_quality)
root.order.add_edge(t_quality, t_packaging)
root.order.add_edge(t_packaging, t_delivery)