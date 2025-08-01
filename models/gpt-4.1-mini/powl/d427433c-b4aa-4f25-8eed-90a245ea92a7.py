# Generated from: d427433c-b4aa-4f25-8eed-90a245ea92a7.json
# Description: This process outlines the complex supply chain for artisanal cheese production, starting from raw milk collection from multiple small farms, followed by quality testing, milk blending, and fermentation monitoring. The process involves aging control, packaging customization based on regional demand, cold-chain logistics coordination, regulatory compliance checks, and finally, distribution to niche gourmet retailers. Throughout, traceability is maintained via blockchain recording, while dynamic pricing models are applied based on market trends and seasonal variations. Customer feedback loops are integrated to adjust future batches and optimize flavor profiles, ensuring a premium product that balances tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
milk_collection = Transition(label='Milk Collection')
quality_testing = Transition(label='Quality Testing')
milk_blending = Transition(label='Milk Blending')
starter_culture = Transition(label='Starter Culture')
fermentation_check = Transition(label='Fermentation Check')
curd_cutting = Transition(label='Curd Cutting')
whey_separation = Transition(label='Whey Separation')
molding_press = Transition(label='Molding Press')
salting_stage = Transition(label='Salting Stage')
aging_control = Transition(label='Aging Control')
packaging_design = Transition(label='Packaging Design')
cold_shipping = Transition(label='Cold Shipping')
compliance_audit = Transition(label='Compliance Audit')
blockchain_log = Transition(label='Blockchain Log')
market_pricing = Transition(label='Market Pricing')
order_fulfillment = Transition(label='Order Fulfillment')
feedback_review = Transition(label='Feedback Review')

skip = SilentTransition()

# Partial order for Milk Collection from multiple farms (concurrent assumed).
# The description doesn't specify multiple activities for this explicitly,
# so we consider Milk Collection as a single activity starting the process.

# Core production steps in order:
# Milk Collection --> Quality Testing --> Milk Blending
# Milk Blending --> Starter Culture and Fermentation Check (partially ordered: fermentation check after starter culture)
# Then Curd Cutting, Whey Separation, Molding Press, Salting Stage in order
# Aging Control is a loop with Feedback Review before it (customer feedback loops)
# Packaging Design and Cold Shipping depend on Aging Control
# Compliance Audit and Blockchain Log are concurrent and happen after Packaging Design but before Market Pricing
# Market Pricing before Order Fulfillment

# Define the fermentation sub-process partial order: Starter Culture --> Fermentation Check
fermentation_po = StrictPartialOrder(nodes=[starter_culture, fermentation_check])
fermentation_po.order.add_edge(starter_culture, fermentation_check)

# Define the cheese forming steps partial order:
cheese_forming_po = StrictPartialOrder(
    nodes=[curd_cutting, whey_separation, molding_press, salting_stage]
)
cheese_forming_po.order.add_edge(curd_cutting, whey_separation)
cheese_forming_po.order.add_edge(whey_separation, molding_press)
cheese_forming_po.order.add_edge(molding_press, salting_stage)

# Feedback loop: loop over Aging Control and Feedback Review
# Loop structure: execute Aging Control; then choose to exit or execute Feedback Review and repeat
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_control, feedback_review]
)

# Packaging Design and Cold Shipping run in parallel after feedback loop.
packaging_and_shipping = StrictPartialOrder(
    nodes=[packaging_design, cold_shipping]
)
# no order edges => concurrent

# Compliance Audit and Blockchain Log run concurrently but after packaging_and_shipping
compliance_and_blockchain = StrictPartialOrder(
    nodes=[compliance_audit, blockchain_log]
)
# no order edges => concurrent

# Market Pricing depends on Compliance Audit and Blockchain Log
# Order Fulfillment after Market Pricing
final_steps = StrictPartialOrder(
    nodes=[market_pricing, order_fulfillment]
)
final_steps.order.add_edge(market_pricing, order_fulfillment)

# Now impose the global process order and dependencies:
# Milk Collection --> Quality Testing --> Milk Blending --> fermentation_po
# fermentation_po --> cheese_forming_po
# cheese_forming_po --> feedback_loop
# feedback_loop --> packaging_and_shipping
# packaging_and_shipping --> compliance_and_blockchain
# compliance_and_blockchain --> final_steps

root = StrictPartialOrder(
    nodes=[
        milk_collection,
        quality_testing,
        milk_blending,
        fermentation_po,
        cheese_forming_po,
        feedback_loop,
        packaging_and_shipping,
        compliance_and_blockchain,
        final_steps,
    ]
)

# Adding edges for sequence between major stages
root.order.add_edge(milk_collection, quality_testing)
root.order.add_edge(quality_testing, milk_blending)
root.order.add_edge(milk_blending, fermentation_po)
root.order.add_edge(fermentation_po, cheese_forming_po)
root.order.add_edge(cheese_forming_po, feedback_loop)
root.order.add_edge(feedback_loop, packaging_and_shipping)
root.order.add_edge(packaging_and_shipping, compliance_and_blockchain)
root.order.add_edge(compliance_and_blockchain, final_steps)