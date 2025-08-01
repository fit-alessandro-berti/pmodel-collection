# Generated from: 4028487d-1108-4d1c-9aff-80f9e09a6b2f.json
# Description: This process outlines the end-to-end supply chain management for an urban vertical farming operation that integrates advanced hydroponic cultivation with local distribution. Starting from seed procurement, the process includes nutrient mix optimization, climate monitoring, iterative growth adjustments, pest bio-control application, and automated harvesting. Post-harvest, fresh produce undergoes quality inspection, packaging with biodegradable materials, and dynamic inventory allocation based on real-time demand analytics. The distribution phase involves route optimization for electric delivery vehicles, last-mile cold chain maintenance, and direct-to-consumer subscription management. Additionally, waste biomass recycling and data feedback loops for continuous process improvement are integral to ensure sustainability and operational efficiency within constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Check = Transition(label='Climate Check')
Growth_Adjust = Transition(label='Growth Adjust')
Pest_Control = Transition(label='Pest Control')
Harvest_Cycle = Transition(label='Harvest Cycle')
Quality_Scan = Transition(label='Quality Scan')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Sort = Transition(label='Inventory Sort')
Demand_Forecast = Transition(label='Demand Forecast')
Route_Plan = Transition(label='Route Plan')
Cold_Chain = Transition(label='Cold Chain')
Delivery_Track = Transition(label='Delivery Track')
Subscription_Mgmt = Transition(label='Subscription Mgmt')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Feedback = Transition(label='Data Feedback')

# Loop: iterative growth adjustment after Climate Check
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Adjust, Pest_Control])

# Partial order for the growth phase: Nutrient Mix --> Climate Check --> loop of Growth_Adjust and Pest_Control --> Harvest Cycle
growth_phase = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Check, growth_loop, Harvest_Cycle])
growth_phase.order.add_edge(Nutrient_Mix, Climate_Check)
growth_phase.order.add_edge(Climate_Check, growth_loop)
growth_phase.order.add_edge(growth_loop, Harvest_Cycle)

# Post-harvest quality and packaging sequence
post_harvest = StrictPartialOrder(nodes=[Quality_Scan, Eco_Packaging])
post_harvest.order.add_edge(Quality_Scan, Eco_Packaging)

# Inventory phase where Demand Forecast and Inventory Sort are concurrent (real-time analytics and sorting)
inventory_phase = StrictPartialOrder(nodes=[Inventory_Sort, Demand_Forecast])

# Distribution phase: Route Plan --> Cold Chain --> Delivery Track --> Subscription Mgmt
distribution_phase = StrictPartialOrder(nodes=[Route_Plan, Cold_Chain, Delivery_Track, Subscription_Mgmt])
distribution_phase.order.add_edge(Route_Plan, Cold_Chain)
distribution_phase.order.add_edge(Cold_Chain, Delivery_Track)
distribution_phase.order.add_edge(Delivery_Track, Subscription_Mgmt)

# Waste recycling and data feedback happen concurrently with distribution and possibly the rest; 
# we place them concurrent at top level for sustainability & continuous improvement
sustainability_phase = StrictPartialOrder(nodes=[Waste_Recycle, Data_Feedback])

# Assemble all main phases (Seed Sourcing first)
# Seed Sourcing --> growth phase --> Harvest Cycle finished in growth_phase
# then post_harvest
# followed by inventory_phase and distribution_phase concurrently
root = StrictPartialOrder(nodes=[Seed_Sourcing, growth_phase, post_harvest, inventory_phase, distribution_phase, sustainability_phase])
root.order.add_edge(Seed_Sourcing, growth_phase)
root.order.add_edge(growth_phase, post_harvest)
root.order.add_edge(post_harvest, inventory_phase)
root.order.add_edge(post_harvest, distribution_phase)

# Waste_Recycle and Data_Feedback run concurrently with inventory and distribution,
# so no order edges connected to sustainability_phase (parallel)
