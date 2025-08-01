# Generated from: c4e042a6-4225-4679-9c2f-0ce00a84a9d7.json
# Description: This process outlines the intricate supply chain management for a bespoke artisan goods company specializing in handcrafted musical instruments. It involves sourcing rare organic materials from remote regions, verifying artisan credentials, coordinating small batch production, managing custom design approvals, and synchronizing global shipping with strict quality inspections. The process integrates real-time artisan feedback loops, adaptive inventory adjustments, and niche marketing strategies to ensure exclusivity while maintaining transparency and sustainability throughout the supply chain lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Audit = Transition(label='Supplier Audit')
Credential_Verify = Transition(label='Credential Verify')
Design_Concept = Transition(label='Design Concept')
Prototype_Build = Transition(label='Prototype Build')
Quality_Review = Transition(label='Quality Review')
Artisan_Assign = Transition(label='Artisan Assign')
Batch_Scheduling = Transition(label='Batch Scheduling')
Custom_Approvals = Transition(label='Custom Approvals')
Inventory_Adjust = Transition(label='Inventory Adjust')
Production_Sync = Transition(label='Production Sync')
Shipping_Plan = Transition(label='Shipping Plan')
Compliance_Check = Transition(label='Compliance Check')
Feedback_Loop = Transition(label='Feedback Loop')
Market_Target = Transition(label='Market Target')
Order_Fulfill = Transition(label='Order Fulfill')
Sustainability = Transition(label='Sustainability')
Customer_Engage = Transition(label='Customer Engage')

# Loop node: Real-time artisan feedback loop and adaptive inventory adjustments
# Loop(A, B) with A=Feedback_Loop, B=Inventory_Adjust
feedback_inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Inventory_Adjust])

# Choice node: Custom Approvals or skip (silent)
skip = SilentTransition()
custom_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[Custom_Approvals, skip])

# Partial Orders

# Early sourcing and verification (Material Sourcing --> Supplier Audit --> Credential Verify)
early_verification = StrictPartialOrder(nodes=[Material_Sourcing, Supplier_Audit, Credential_Verify])
early_verification.order.add_edge(Material_Sourcing, Supplier_Audit)
early_verification.order.add_edge(Supplier_Audit, Credential_Verify)

# Production preparation: Design Concept --> Prototype Build --> Quality Review --> Artisan Assign --> Batch Scheduling
production_preparation = StrictPartialOrder(nodes=[Design_Concept, Prototype_Build, Quality_Review, Artisan_Assign, Batch_Scheduling])
production_preparation.order.add_edge(Design_Concept, Prototype_Build)
production_preparation.order.add_edge(Prototype_Build, Quality_Review)
production_preparation.order.add_edge(Quality_Review, Artisan_Assign)
production_preparation.order.add_edge(Artisan_Assign, Batch_Scheduling)

# Production execution: Batch Scheduling --> (custom approvals choice) --> Production Sync
production_execution = StrictPartialOrder(nodes=[Batch_Scheduling, custom_approval_xor, Production_Sync])
production_execution.order.add_edge(Batch_Scheduling, custom_approval_xor)
production_execution.order.add_edge(custom_approval_xor, Production_Sync)

# Post-production: Production Sync --> Shipping Plan --> Compliance Check
post_production = StrictPartialOrder(nodes=[Production_Sync, Shipping_Plan, Compliance_Check])
post_production.order.add_edge(Production_Sync, Shipping_Plan)
post_production.order.add_edge(Shipping_Plan, Compliance_Check)

# Final fulfillment and market engagement: Compliance Check --> Order Fulfill --> Sustainability & Market Target --> Customer Engage

# Sustainability and Market Target are concurrent before Customer Engage
final_marketing = StrictPartialOrder(nodes=[Sustainability, Market_Target, Customer_Engage])
final_marketing.order.add_edge(Sustainability, Customer_Engage)
final_marketing.order.add_edge(Market_Target, Customer_Engage)

fulfillment_flow = StrictPartialOrder(nodes=[Compliance_Check, Order_Fulfill, final_marketing])
# Compliance_Check --> Order_Fulfill --> final_marketing (represented as nodes in fulfillment_flow)
fulfillment_flow.order.add_edge(Compliance_Check, Order_Fulfill)
fulfillment_flow.order.add_edge(Order_Fulfill, final_marketing)

# Now build the top-level partial order linking everything

# All major subprocesses nodes:
# early_verification, production_preparation, production_execution, feedback_inventory_loop, post_production, fulfillment_flow

# Top-level: 
# early_verification --> production_preparation --> production_execution --> feedback_inventory_loop (loops internally), and post_production

# production_execution and feedback_inventory_loop are concurrent after production_preparation (feedback loop is real-time/opportunistic)
# post_production depends on production_execution completion

top_level_nodes = [
    early_verification,
    production_preparation,
    production_execution,
    feedback_inventory_loop,
    post_production,
    fulfillment_flow
]

root = StrictPartialOrder(nodes=top_level_nodes)

# Order edges for top-level flow
root.order.add_edge(early_verification, production_preparation)
root.order.add_edge(production_preparation, production_execution)
root.order.add_edge(production_execution, post_production)
root.order.add_edge(post_production, fulfillment_flow)

# Additionally, the feedback_inventory_loop may be used concurrently with production_execution and post_production,
# reflecting ongoing adaptation.

# To model this concurrency, no ordering edges between feedback_inventory_loop and production_execution/post_production.

# The model "integrates real-time artisan feedback loops, adaptive inventory adjustments,"
# so feedback_inventory_loop comes after production_preparation (start after preparation)
root.order.add_edge(production_preparation, feedback_inventory_loop)

# No further edges needed for concurrency.
