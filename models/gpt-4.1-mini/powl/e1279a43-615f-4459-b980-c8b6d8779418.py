# Generated from: e1279a43-615f-4459-b980-c8b6d8779418.json
# Description: This process describes the comprehensive cycle of an urban vertical farming operation, integrating technology, resource management, and distribution logistics. It begins with site analysis and infrastructure setup, followed by seed selection and nutrient calibration. Real-time monitoring and climate adjustment optimize plant growth, while automated harvesting and quality inspection ensure produce standards. Post-harvest, products undergo packaging and cold storage before distribution via eco-friendly channels. Waste recycling and system maintenance close the loop, promoting sustainability in an atypical yet realistic agricultural business model embedded within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')

planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')

harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')

packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')

waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

# Define a loop for the Planting Cycle with Growth Monitoring and Climate Adjust & Pest Control
# Loop body B contains Climate Adjust, Growth Monitor, Pest Control
monitoring = StrictPartialOrder(nodes=[climate_adjust, growth_monitor, pest_control])
monitoring.order.add_edge(climate_adjust, growth_monitor)
monitoring.order.add_edge(climate_adjust, pest_control)
# climate_adjust before growth_monitor and pest_control; growth_monitor and pest_control concurrent

loop_body = monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, loop_body])

# Pre-loop partial order: Site Analysis --> Infrastructure Setup --> Seed Selection --> Nutrient Mix --> Loop
pre_loop = StrictPartialOrder(nodes=[site_analysis, infrastructure_setup, seed_selection, nutrient_mix, loop])
pre_loop.order.add_edge(site_analysis, infrastructure_setup)
pre_loop.order.add_edge(infrastructure_setup, seed_selection)
pre_loop.order.add_edge(seed_selection, nutrient_mix)
pre_loop.order.add_edge(nutrient_mix, loop)

# Post-harvest partial order: Harvesting Mode --> Quality Check --> Packaging Phase --> Cold Storage --> Order Dispatch
post_harvest = StrictPartialOrder(nodes=[
    harvesting_mode,
    quality_check,
    packaging_phase,
    cold_storage,
    order_dispatch
])
post_harvest.order.add_edge(harvesting_mode, quality_check)
post_harvest.order.add_edge(quality_check, packaging_phase)
post_harvest.order.add_edge(packaging_phase, cold_storage)
post_harvest.order.add_edge(cold_storage, order_dispatch)

# Closing loop with Waste Recycling and System Maintain concurrent
closing = StrictPartialOrder(nodes=[waste_recycling, system_maintain])
# No order edges: concurrent

# Combine all parts into root partial order, order edges:
# pre_loop --> post_harvest --> closing
root = StrictPartialOrder(
    nodes=[pre_loop, post_harvest, closing]
)
root.order.add_edge(pre_loop, post_harvest)
root.order.add_edge(post_harvest, closing)