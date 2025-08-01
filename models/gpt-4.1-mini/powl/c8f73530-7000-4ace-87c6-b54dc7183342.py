# Generated from: c8f73530-7000-4ace-87c6-b54dc7183342.json
# Description: This process describes the complex supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by controlled fermentation, artisanal aging, quality sensory evaluation, bespoke packaging design, and finally customized distribution to niche gourmet markets. Each step involves detailed coordination with local farmers, microbiologists, master cheesemakers, packaging designers, and logistics partners to maintain quality and authenticity. The process also includes managing seasonal variations, regulatory compliance, and customer feedback integration to continuously refine product offerings and meet evolving market demands, ensuring a unique and premium cheese experience for connoisseurs worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_inoculate = Transition(label='Culture Inoculate')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
aging_control = Transition(label='Aging Control')
sensory_audit = Transition(label='Sensory Audit')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_customization = Transition(label='Order Customization')
logistics_plan = Transition(label='Logistics Plan')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')
regulatory_check = Transition(label='Regulatory Check')

# Build partial orders for milk processing stages (fermentation etc)
milk_processing_nodes = [
    quality_testing,
    milk_pasteurize,
    culture_inoculate,
    coagulation,
    curd_cutting,
    whey_drain,
    pressing,
    salting
]
milk_processing = StrictPartialOrder(nodes=milk_processing_nodes)
milk_processing.order.add_edge(quality_testing, milk_pasteurize)
milk_processing.order.add_edge(milk_pasteurize, culture_inoculate)
milk_processing.order.add_edge(culture_inoculate, coagulation)
milk_processing.order.add_edge(coagulation, curd_cutting)
milk_processing.order.add_edge(curd_cutting, whey_drain)
milk_processing.order.add_edge(whey_drain, pressing)
milk_processing.order.add_edge(pressing, salting)

# Aging and sensory evaluation in partial order (sensory audit after aging control)
aging_and_audit = StrictPartialOrder(nodes=[aging_control, sensory_audit])
aging_and_audit.order.add_edge(aging_control, sensory_audit)

# Packaging steps partial order (packaging design then label approval)
packaging = StrictPartialOrder(nodes=[packaging_design, label_approval])
packaging.order.add_edge(packaging_design, label_approval)

# Distribution steps partial order (order customization, logistics planning, market delivery)
distribution = StrictPartialOrder(nodes=[order_customization, logistics_plan, market_delivery])
distribution.order.add_edge(order_customization, logistics_plan)
distribution.order.add_edge(logistics_plan, market_delivery)

# Final feedback and regulatory compliance as concurrent nodes (can happen anytime after market delivery)
feedback_regulatory = StrictPartialOrder(nodes=[customer_feedback, regulatory_check])

# Build full production sequence:
# Milk sourcing -> Milk processing -> Aging and audit -> Packaging -> Distribution
production_seq_nodes = [
    milk_sourcing,
    milk_processing,
    aging_and_audit,
    packaging,
    distribution,
    feedback_regulatory
]
root = StrictPartialOrder(nodes=production_seq_nodes)

root.order.add_edge(milk_sourcing, milk_processing)
root.order.add_edge(milk_processing, aging_and_audit)
root.order.add_edge(aging_and_audit, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, feedback_regulatory)