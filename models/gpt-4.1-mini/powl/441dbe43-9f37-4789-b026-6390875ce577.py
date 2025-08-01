# Generated from: 441dbe43-9f37-4789-b026-6390875ce577.json
# Description: This process involves sourcing rare raw materials from remote locations, verifying artisan credentials, custom-designing product prototypes, coordinating multi-vendor collaboration, managing quality inspections at various stages, handling bespoke packaging, and organizing niche market distribution. Additionally, it includes real-time artisan feedback integration, dynamic inventory allocation, and adaptive pricing strategies based on limited-edition demand fluctuations, ensuring a seamless blend of tradition and innovation in a highly specialized supply chain network.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Material_Sourcing = Transition(label='Material Sourcing')
Credential_Check = Transition(label='Credential Check')
Prototype_Design = Transition(label='Prototype Design')
Vendor_Sync = Transition(label='Vendor Sync')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Design = Transition(label='Packaging Design')
Market_Analysis = Transition(label='Market Analysis')
Inventory_Allocate = Transition(label='Inventory Allocate')
Demand_Forecast = Transition(label='Demand Forecast')
Price_Adjust = Transition(label='Price Adjust')
Order_Processing = Transition(label='Order Processing')
Shipping_Plan = Transition(label='Shipping Plan')
Feedback_Collect = Transition(label='Feedback Collect')
Data_Review = Transition(label='Data Review')
Sales_Report = Transition(label='Sales Report')

# Build sub-processes reflecting the process description

# Loop for Quality Inspect possibly repeated after Vendor Sync and Packaging Design
quality_loop_body = StrictPartialOrder(
    nodes=[Vendor_Sync, Packaging_Design],
)
quality_loop_body.order.add_edge(Vendor_Sync, Packaging_Design)

quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Inspect, quality_loop_body])

# Feedback integration loop: Feedback Collect followed by Data Review, repeat or exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Collect, Data_Review])

# Pricing strategy: Demand Forecast and Price Adjust in sequence
pricing_seq = StrictPartialOrder(nodes=[Demand_Forecast, Price_Adjust])
pricing_seq.order.add_edge(Demand_Forecast, Price_Adjust)

# Inventory allocation depends on Feedback integration and pricing strategy; these can concur
inventory_and_pricing = StrictPartialOrder(nodes=[Inventory_Allocate, pricing_seq, feedback_loop])

# Market Analysis before inventory and pricing
market_and_inventory = StrictPartialOrder(nodes=[Market_Analysis, inventory_and_pricing])
market_and_inventory.order.add_edge(Market_Analysis, inventory_and_pricing)

# After Prototype Design, go to Vendor Sync and then quality loop
design_to_quality = StrictPartialOrder(nodes=[Prototype_Design, quality_loop])
design_to_quality.order.add_edge(Prototype_Design, quality_loop)

# Sourcing followed by Credential Check, then Prototype Design
initial_seq = StrictPartialOrder(nodes=[Material_Sourcing, Credential_Check, design_to_quality])
initial_seq.order.add_edge(Material_Sourcing, Credential_Check)
initial_seq.order.add_edge(Credential_Check, design_to_quality)

# Packaging design after quality loop
quality_to_packaging = StrictPartialOrder(nodes=[quality_loop, Packaging_Design])
quality_to_packaging.order.add_edge(quality_loop, Packaging_Design)

# After Packaging Design and market_and_inventory, proceed to order processing and shipping plan in partial order
post_pack_order_shipping = StrictPartialOrder(
    nodes=[Order_Processing, Shipping_Plan, Sales_Report]
)
# Sales Report last
post_pack_order_shipping.order.add_edge(Order_Processing, Shipping_Plan)
post_pack_order_shipping.order.add_edge(Shipping_Plan, Sales_Report)

# Combine Packaging followed by market analysis & inventory/pricing/feedback integration
packaging_and_market = StrictPartialOrder(nodes=[Packaging_Design, market_and_inventory])
packaging_and_market.order.add_edge(Packaging_Design, market_and_inventory)

# Full model combining from initial sequence to packaging and market, then order processing/shipping
root = StrictPartialOrder(
    nodes=[initial_seq, packaging_and_market, post_pack_order_shipping]
)
root.order.add_edge(initial_seq, packaging_and_market)
root.order.add_edge(packaging_and_market, post_pack_order_shipping)