# Generated from: 8de9f34d-102a-44eb-bdae-4766ff4f5fa1.json
# Description: This process details the end-to-end supply chain for artisan cheese production and distribution, involving unique steps like raw milk sourcing from specific breeds, microbial culture selection, seasonal aging conditions, and quality validation through sensory panels. It integrates traditional craftsmanship with modern logistics, ensuring traceability from farm to boutique stores. Activities include milk testing, starter prep, curd cutting, whey drainage, pressing, salting, controlled aging, flavor profiling, packaging design, cold chain management, boutique allocation, seasonal forecasting, customer feedback, and artisanal marketing strategies to optimize both quality and market reach while maintaining the cheese’s unique regional character.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
milk_sourcing = Transition(label='Milk Sourcing')
microbe_selection = Transition(label='Microbe Selection')
starter_prep = Transition(label='Starter Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_drainage = Transition(label='Whey Drainage')
cheese_pressing = Transition(label='Cheese Pressing')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
flavor_profiling = Transition(label='Flavor Profiling')
quality_testing = Transition(label='Quality Testing')
package_design = Transition(label='Package Design')
cold_storage = Transition(label='Cold Storage')
boutique_allocation = Transition(label='Boutique Allocation')
market_forecast = Transition(label='Market Forecast')

# Construct partial order
# Milk Sourcing --> Microbe Selection --> Starter Prep --> Milk Pasteurize
# After pasteurize: Curd Cutting --> Whey Drainage --> Cheese Pressing --> Salt Application
# Then Controlled Aging --> Quality Testing
# After Quality Testing, parallel packaging & marketing logistics:
# Packaging branch: Package Design --> Cold Storage --> Boutique Allocation
# Marketing branch: Market Forecast
# Flavor Profiling happens concurrently with Quality Testing (to profile flavors while testing)
# Controlled Aging must finish before Flavor Profiling and Quality Testing
# Boutique Allocation depends on Cold Storage
# Market Forecast is concurrent with Packaging pipeline but happens after Quality Testing

root = StrictPartialOrder(nodes=[
    milk_sourcing,
    microbe_selection,
    starter_prep,
    milk_pasteurize,
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

order = root.order
# Linear chain for initial milk processing sequence
order.add_edge(milk_sourcing, microbe_selection)
order.add_edge(microbe_selection, starter_prep)
order.add_edge(starter_prep, milk_pasteurize)

# Milk pasteurize leads to curd cutting line
order.add_edge(milk_pasteurize, curd_cutting)
order.add_edge(curd_cutting, whey_drainage)
order.add_edge(whey_drainage, cheese_pressing)
order.add_edge(cheese_pressing, salt_application)

# Salt application precedes controlled aging
order.add_edge(salt_application, controlled_aging)

# Controlled aging precedes both flavor profiling and quality testing (concurrent)
order.add_edge(controlled_aging, flavor_profiling)
order.add_edge(controlled_aging, quality_testing)

# Flavor profiling and quality testing concurrent - no edges between them

# Quality testing precedes packaging and marketing branches
order.add_edge(quality_testing, package_design)
order.add_edge(quality_testing, market_forecast)

# Packaging pipeline
order.add_edge(package_design, cold_storage)
order.add_edge(cold_storage, boutique_allocation)

# Market forecast is concurrent with packaging pipeline (starts after quality testing)

# No edges between market_forecast and packaging nodes except from quality_testing

# This models concurrency between packaging branch and marketing branch

# No other edges needed, they remain concurrent where no edge present

# root variable holds the final POWL model