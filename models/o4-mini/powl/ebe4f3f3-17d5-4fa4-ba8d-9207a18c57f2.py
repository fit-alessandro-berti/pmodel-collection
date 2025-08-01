# Generated from: ebe4f3f3-17d5-4fa4-ba8d-9207a18c57f2.json
# Description: This process describes the end-to-end supply chain management of artisan cheese production, involving unique sourcing of raw milk from local farms, quality assessment of milk, traditional cheese crafting techniques, aging control, custom packaging, and distribution to specialized retailers. The process integrates seasonal variations in milk supply, artisan scheduling, compliance with food safety standards, and direct communication with boutique shops for demand forecasting to ensure freshness and authenticity. It also includes customer feedback loops for continuous product refinement and limited edition release planning to maintain exclusivity and market differentiation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing       = Transition(label='Milk Sourcing')
farm_audit          = Transition(label='Farm Audit')
milk_testing        = Transition(label='Milk Testing')
batch_forming       = Transition(label='Batch Forming')
curd_cutting        = Transition(label='Curd Cutting')
molding_cheese      = Transition(label='Molding Cheese')
salting_process     = Transition(label='Salting Process')
aging_control       = Transition(label='Aging Control')
quality_check       = Transition(label='Quality Check')
packaging_design    = Transition(label='Packaging Design')
label_printing      = Transition(label='Label Printing')
inventory_update    = Transition(label='Inventory Update')
order_receiving     = Transition(label='Order Receiving')
retail_coordination = Transition(label='Retail Coordination')
shipping_prep       = Transition(label='Shipping Prep')
customer_feedback   = Transition(label='Customer Feedback')
demand_forecast     = Transition(label='Demand Forecast')
limited_release     = Transition(label='Limited Release')

# Core production partial order
prod = StrictPartialOrder(nodes=[
    milk_sourcing, farm_audit, milk_testing,
    batch_forming, curd_cutting, molding_cheese,
    salting_process, aging_control, quality_check,
    packaging_design, label_printing, inventory_update,
    order_receiving, retail_coordination, shipping_prep
])

# Add ordering constraints for core production
prod_edges = [
    (milk_sourcing, farm_audit),
    (farm_audit, milk_testing),
    (milk_testing, batch_forming),
    (batch_forming, curd_cutting),
    (curd_cutting, molding_cheese),
    (molding_cheese, salting_process),
    (salting_process, aging_control),
    (aging_control, quality_check),
    (quality_check, packaging_design),
    (packaging_design, label_printing),
    (label_printing, inventory_update),
    (inventory_update, order_receiving),
    (order_receiving, retail_coordination),
    (retail_coordination, shipping_prep)
]
for src, tgt in prod_edges:
    prod.order.add_edge(src, tgt)

# Feedback & refinement partial order
feedback = StrictPartialOrder(nodes=[
    customer_feedback, demand_forecast, limited_release
])
feedback.order.add_edge(customer_feedback, demand_forecast)
feedback.order.add_edge(demand_forecast, limited_release)

# Loop: run production, then optionally do feedback & repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prod, feedback]
)