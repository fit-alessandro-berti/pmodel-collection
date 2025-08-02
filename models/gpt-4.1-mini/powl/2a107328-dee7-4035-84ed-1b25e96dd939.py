# Generated from: 2a107328-dee7-4035-84ed-1b25e96dd939.json
# Description: This process manages the entire supply chain of an urban vertical farming operation, integrating agricultural production, resource optimization, real-time environmental monitoring, crop harvesting, packaging, and distribution to local markets. It involves synchronous coordination between AI-driven climate control, automated nutrient delivery, pest management using bioagents, yield prediction, and dynamic order fulfillment. The process also addresses sustainability goals by recycling water and organic waste, while adapting to fluctuating demand patterns in densely populated urban areas. Each activity ensures minimal resource waste and maximizes freshness and quality through a digitally connected ecosystem of sensors, robots, and logistics partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Recycling = Transition(label='Water Recycling')
Pest_Control = Transition(label='Pest Control')
Growth_Monitoring = Transition(label='Growth Monitoring')
Yield_Forecast = Transition(label='Yield Forecast')
Automated_Harvest = Transition(label='Automated Harvest')
Crop_Sorting = Transition(label='Crop Sorting')
Packaging_Prep = Transition(label='Packaging Prep')
Order_Processing = Transition(label='Order Processing')
Delivery_Routing = Transition(label='Delivery Routing')
Waste_Management = Transition(label='Waste Management')
Energy_Tracking = Transition(label='Energy Tracking')
Market_Feedback = Transition(label='Market Feedback')

# Core agriculture production partial order:
# Seed Selection --> Climate Setup --> Nutrient Mix
production = StrictPartialOrder(nodes=[Seed_Selection, Climate_Setup, Nutrient_Mix])
production.order.add_edge(Seed_Selection, Climate_Setup)
production.order.add_edge(Climate_Setup, Nutrient_Mix)

# Sustainability part (Water Recycling, Waste Management, Energy Tracking) run mostly concurrent and synced with core production nutrient mix
sustainability = StrictPartialOrder(nodes=[Water_Recycling, Waste_Management, Energy_Tracking])
# No order edges -> concurrent

# Pest Control and Growth Monitoring run concurrently after Nutrient Mix is ready
pest_and_growth = StrictPartialOrder(nodes=[Pest_Control, Growth_Monitoring])
# No order edge -> concurrent

# Yield Forecast depends on Growth Monitoring
yield_part = StrictPartialOrder(nodes=[Growth_Monitoring, Yield_Forecast])
yield_part.order.add_edge(Growth_Monitoring, Yield_Forecast)

# Harvest and sorting follow Yield Forecast
harvest_sort = StrictPartialOrder(nodes=[Yield_Forecast, Automated_Harvest, Crop_Sorting])
harvest_sort.order.add_edge(Yield_Forecast, Automated_Harvest)
harvest_sort.order.add_edge(Automated_Harvest, Crop_Sorting)

# Packaging and order processing run sequentially after Sorting
pack_order = StrictPartialOrder(nodes=[Crop_Sorting, Packaging_Prep, Order_Processing])
pack_order.order.add_edge(Crop_Sorting, Packaging_Prep)
pack_order.order.add_edge(Packaging_Prep, Order_Processing)

# Delivery routing after order processing
delivery = StrictPartialOrder(nodes=[Order_Processing, Delivery_Routing])
delivery.order.add_edge(Order_Processing, Delivery_Routing)

# Market feedback runs concurrently with sustainability and after Delivery Routing
feedback = Market_Feedback

# Assemble partial orders reflecting the high-level process sequencing and concurrency
# After production Nutrient Mix, pest_and_growth, sustainability start concurrently
# Then Yield Forecast, then harvest/sorting, packaging/order, delivery,
# and feedback runs concurrently with sustainability and after delivery

# First grouping pest_and_growth and production in partial order:
prod_pest_growth = StrictPartialOrder(nodes=[production, pest_and_growth, sustainability])
prod_pest_growth.order.add_edge(production, pest_and_growth)
prod_pest_growth.order.add_edge(production, sustainability)

# Yield forecast depends on Growth Monitoring inside pest_and_growth, 
# but for high-level order, we connect pest_and_growth --> yield_part
high_level = StrictPartialOrder(nodes=[prod_pest_growth, yield_part])
high_level.order.add_edge(prod_pest_growth, yield_part)

# Harvest/sort depends on yield_part
high_level2 = StrictPartialOrder(nodes=[high_level, harvest_sort])
high_level2.order.add_edge(high_level, harvest_sort)

# Packaging/order depends on harvest_sort
high_level3 = StrictPartialOrder(nodes=[high_level2, pack_order])
high_level3.order.add_edge(high_level2, pack_order)

# Delivery depends on packaging/order
high_level4 = StrictPartialOrder(nodes=[high_level3, delivery])
high_level4.order.add_edge(high_level3, delivery)

# Feedback concurrent with sustainability, after delivery
final_root = StrictPartialOrder(nodes=[high_level4, feedback])
final_root.order.add_edge(high_level4, feedback)

root = final_root