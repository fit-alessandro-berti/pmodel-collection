# Generated from: a7c6b397-5c50-4fc1-9524-1ac62acc999a.json
# Description: This process outlines the artisanal cheese supply chain from raw milk sourcing to final retail distribution. It involves sourcing milk from local farms, quality testing, traditional cheese curdling, aging under controlled conditions, packaging using eco-friendly materials, coordinating with niche retailers, managing seasonal demand fluctuations, and ensuring traceability through blockchain-based records. Each step requires meticulous attention to maintain flavor profiles and comply with health regulations while minimizing environmental impact and supporting local economies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_milk_sourcing   = Transition(label='Milk Sourcing')
t_quality_testing = Transition(label='Quality Testing')
t_pasteurize      = Transition(label='Milk Pasteurize')
t_curd            = Transition(label='Curd Formation')
t_whey            = Transition(label='Whey Separation')
t_inoculation     = Transition(label='Mold Inoculation')
t_aging           = Transition(label='Cheese Aging')
t_humidity        = Transition(label='Humidity Control')
t_flavor          = Transition(label='Flavor Profiling')
t_packaging       = Transition(label='Eco Packaging')
t_traceability    = Transition(label='Traceability Log')
t_regulation      = Transition(label='Regulation Check')
t_demand          = Transition(label='Demand Forecast')
t_audit           = Transition(label='Inventory Audit')
t_order           = Transition(label='Order Processing')
t_retail          = Transition(label='Retail Coordination')

# Concurrent aging sub-process
aging_group = StrictPartialOrder(nodes=[t_aging, t_humidity, t_flavor])
# (no internal order between these three; all follow inoculation)

# Inventory-to-retail subprocess (sequential)
inventory_group = StrictPartialOrder(nodes=[t_audit, t_order, t_retail])
inventory_group.order.add_edge(t_audit, t_order)
inventory_group.order.add_edge(t_order, t_retail)

# Loop for seasonal demand/retail coordination
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_demand, inventory_group]
)

# Build the main process model
root = StrictPartialOrder(nodes=[
    t_milk_sourcing, t_quality_testing, t_pasteurize,
    t_curd, t_whey, t_inoculation,
    aging_group,
    t_packaging, t_traceability, t_regulation,
    seasonal_loop
])

# Define the main partial order
root.order.add_edge(t_milk_sourcing,   t_quality_testing)
root.order.add_edge(t_quality_testing, t_pasteurize)
root.order.add_edge(t_pasteurize,      t_curd)
root.order.add_edge(t_curd,            t_whey)
root.order.add_edge(t_whey,            t_inoculation)
# after inoculation, start aging sub-process
root.order.add_edge(t_inoculation,     aging_group)
# after aging completes, move to packaging
root.order.add_edge(aging_group,       t_packaging)
# ensure traceability and regulation check after packaging
root.order.add_edge(t_packaging,       t_traceability)
root.order.add_edge(t_traceability,    t_regulation)
# after compliance checks, enter seasonal demand loop
root.order.add_edge(t_regulation,      seasonal_loop)