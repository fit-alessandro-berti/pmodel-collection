# Generated from: 8f8fb025-50ef-4f8b-83f0-8b2b7ca18b7e.json
# Description: This process manages the end-to-end supply chain of artisanal cheese, beginning with sourcing rare milk varieties from local farms, followed by specialized fermentation and aging phases conducted in controlled environments. Quality inspections occur at multiple stages, including raw material intake, mid-fermentation checks, and pre-shipment assessment. Unique packaging is designed to preserve flavor and freshness, incorporating biodegradable materials. Distribution involves coordinating with niche gourmet retailers and direct-to-consumer channels, ensuring traceability and adherence to organic certifications throughout. Seasonal demand fluctuations require dynamic inventory adjustment and flexible logistics planning. Customer feedback loops influence future batch recipes and supply decisions, creating a continuous improvement cycle for this specialized product line.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing      = Transition(label='Milk Sourcing')
quality_check      = Transition(label='Quality Check')
fermentation_start = Transition(label='Fermentation Start')
mid_check          = Transition(label='Mid-Check')
aging_control      = Transition(label='Aging Control')
flavor_testing     = Transition(label='Flavor Testing')
packaging_design   = Transition(label='Packaging Design')
eco_packaging      = Transition(label='Eco Packaging')
inventory_update   = Transition(label='Inventory Update')
order_processing   = Transition(label='Order Processing')
logistics_plan     = Transition(label='Logistics Plan')
retail_coordination= Transition(label='Retail Coordination')
direct_shipping    = Transition(label='Direct Shipping')
customer_feedback  = Transition(label='Customer Feedback')
recipe_adjust      = Transition(label='Recipe Adjust')

# 1) Distribution choice: either Retail Coordination or Direct Shipping
distribution_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[retail_coordination, direct_shipping]
)

# 2) Seasonal loop for Inventory Update and Logistics Plan
inv_logistics_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inventory_update, logistics_plan]
)

# 3) Core supply‐chain process as a partial order
core_nodes = [
    milk_sourcing, quality_check, fermentation_start, mid_check,
    aging_control, flavor_testing, packaging_design, eco_packaging,
    distribution_choice, order_processing, inv_logistics_loop
]
core_process = StrictPartialOrder(nodes=core_nodes)
core = core_process.order
core.add_edge(milk_sourcing,      quality_check)
core.add_edge(quality_check,      fermentation_start)
core.add_edge(fermentation_start, mid_check)
core.add_edge(mid_check,          aging_control)
core.add_edge(aging_control,      flavor_testing)
core.add_edge(flavor_testing,     packaging_design)
core.add_edge(packaging_design,   eco_packaging)
core.add_edge(eco_packaging,      distribution_choice)
core.add_edge(distribution_choice,order_processing)
core.add_edge(order_processing,   inv_logistics_loop)

# 4) Feedback loop for continuous improvement
feedback_nodes = [customer_feedback, recipe_adjust]
feedback_process = StrictPartialOrder(nodes=feedback_nodes)
fb = feedback_process.order
fb.add_edge(customer_feedback, recipe_adjust)

# 5) Top‐level loop: run core_process, then optionally feedback & repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[core_process, feedback_process]
)