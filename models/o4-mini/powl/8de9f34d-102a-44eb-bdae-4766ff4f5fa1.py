# Generated from: 8de9f34d-102a-44eb-bdae-4766ff4f5fa1.json
# Description: This process details the end-to-end supply chain for artisan cheese production and distribution, involving unique steps like raw milk sourcing from specific breeds, microbial culture selection, seasonal aging conditions, and quality validation through sensory panels. It integrates traditional craftsmanship with modern logistics, ensuring traceability from farm to boutique stores. Activities include milk testing, starter prep, curd cutting, whey drainage, pressing, salting, controlled aging, flavor profiling, packaging design, cold chain management, boutique allocation, seasonal forecasting, customer feedback, and artisanal marketing strategies to optimize both quality and market reach while maintaining the cheese’s unique regional character.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
milk_sourcing       = Transition(label="Milk Sourcing")
microbe_selection   = Transition(label="Microbe Selection")
milk_pasteurize     = Transition(label="Milk Pasteurize")
starter_prep        = Transition(label="Starter Prep")
curd_cutting        = Transition(label="Curd Cutting")
whey_drainage       = Transition(label="Whey Drainage")
cheese_pressing     = Transition(label="Cheese Pressing")
salt_application    = Transition(label="Salt Application")
controlled_aging    = Transition(label="Controlled Aging")
flavor_profiling    = Transition(label="Flavor Profiling")
quality_testing     = Transition(label="Quality Testing")
package_design      = Transition(label="Package Design")
cold_storage        = Transition(label="Cold Storage")
boutique_allocation = Transition(label="Boutique Allocation")
market_forecast     = Transition(label="Market Forecast")

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    microbe_selection,
    milk_pasteurize,
    starter_prep,
    curd_cutting,
    whey_drainage,
    cheese_pressing,
    salt_application,
    controlled_aging,
    flavor_profiling,
    quality_testing,
    package_design,
    cold_storage,
    boutique_allocation,
    market_forecast
])

# Add the precedence relations
root.order.add_edge(milk_sourcing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, starter_prep)
root.order.add_edge(microbe_selection, starter_prep)

root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, whey_drainage)
root.order.add_edge(whey_drainage, cheese_pressing)
root.order.add_edge(cheese_pressing, salt_application)

root.order.add_edge(salt_application, controlled_aging)
root.order.add_edge(controlled_aging, flavor_profiling)
root.order.add_edge(flavor_profiling, quality_testing)

root.order.add_edge(quality_testing, package_design)
root.order.add_edge(package_design, cold_storage)
root.order.add_edge(cold_storage, boutique_allocation)

# Market forecast informs packaging and allocation downstream
root.order.add_edge(market_forecast, package_design)
root.order.add_edge(market_forecast, boutique_allocation)