# Generated from: b2f8042b-9ed1-4376-9f37-8518d05aef9f.json
# Description: This process involves sourcing small-batch artisan cheeses from regional farms, ensuring quality through sensory evaluation and microbial testing, then coordinating cold-chain logistics to specialty retailers. It includes seasonal inventory adjustments based on production cycles, managing compliance with local food regulations, and fostering relationships with cheesemakers for exclusive varieties. Marketing focuses on storytelling and provenance, while feedback loops from retailers guide product selection and promotional strategies to maximize shelf-life and customer satisfaction in niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
farm_sourcing = Transition(label='Farm Sourcing')
quality_check = Transition(label='Quality Check')
microbial_test = Transition(label='Microbial Test')
sample_panel = Transition(label='Sample Panel')
inventory_audit = Transition(label='Inventory Audit')
order_forecast = Transition(label='Order Forecast')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
regulation_review = Transition(label='Regulation Review')
retail_outreach = Transition(label='Retail Outreach')
sales_training = Transition(label='Sales Training')
marketing_campaign = Transition(label='Marketing Campaign')
feedback_gather = Transition(label='Feedback Gather')
stock_rotation = Transition(label='Stock Rotation')
supplier_meeting = Transition(label='Supplier Meeting')
customer_support = Transition(label='Customer Support')
sales_analysis = Transition(label='Sales Analysis')

# Source & quality sub-process (Farm Sourcing -> Quality Check + Microbial Test + Sample Panel in parallel with quality_check before microbial_test and sample_panel)
# Partial order reflecting: Quality Check precedes Microbial Test and Sample Panel; Microbial Test and Sample Panel concurrent after Quality Check
quality_subprocess = StrictPartialOrder(
    nodes=[quality_check, microbial_test, sample_panel]
)
quality_subprocess.order.add_edge(quality_check, microbial_test)
quality_subprocess.order.add_edge(quality_check, sample_panel)

# Supply Chain:
# Cold Storage and Logistics Plan after Quality Subprocess, concurrent
supply_chain = StrictPartialOrder(
    nodes=[cold_storage, logistics_plan]
)

# Inventory adjustments:
# Inventory Audit and Order Forecast concurrent
inventory_management = StrictPartialOrder(
    nodes=[inventory_audit, order_forecast]
)

# Compliance:
# Regulation Review standalone
compliance = regulation_review

# Relationship fostering:
# Supplier Meeting standalone
supplier_relations = supplier_meeting

# Marketing focus:
# Marketing Campaign concurrent with Sales Training
marketing = StrictPartialOrder(
    nodes=[marketing_campaign, sales_training]
)

# Retail feedback loop:
# Feedback Gather precedes Sales Analysis and Customer Support (which are concurrent)
feedback_loop = StrictPartialOrder(
    nodes=[feedback_gather, sales_analysis, customer_support]
)
feedback_loop.order.add_edge(feedback_gather, sales_analysis)
feedback_loop.order.add_edge(feedback_gather, customer_support)

# Stock rotation standalone
stock_management = stock_rotation

# Overall process PO:
# 1. Farm Sourcing -> quality_subprocess
# 2. quality_subprocess -> supply_chain and inventory_management
# 3. supply_chain and inventory_management -> compliance
# 4. compliance -> supplier_relations
# 5. supplier_relations -> marketing and retail outreach (Retail Outreach concurrent with marketing)
# 6. marketing and retail outreach -> feedback_loop
# 7. feedback_loop -> stock management

root = StrictPartialOrder(
    nodes=[
        farm_sourcing,
        quality_subprocess,
        supply_chain,
        inventory_management,
        compliance,
        supplier_relations,
        marketing,
        retail_outreach,
        feedback_loop,
        stock_management
    ]
)

# Define order edges according to above sequencing:

# 1. Farm Sourcing -> quality_subprocess
root.order.add_edge(farm_sourcing, quality_subprocess)

# 2a. quality_subprocess -> supply_chain
root.order.add_edge(quality_subprocess, supply_chain)
# 2b. quality_subprocess -> inventory_management
root.order.add_edge(quality_subprocess, inventory_management)

# 3. supply_chain -> compliance
root.order.add_edge(supply_chain, compliance)
# 3b. inventory_management -> compliance
root.order.add_edge(inventory_management, compliance)

# 4. compliance -> supplier_relations
root.order.add_edge(compliance, supplier_relations)

# 5a. supplier_relations -> marketing
root.order.add_edge(supplier_relations, marketing)
# 5b. supplier_relations -> retail_outreach
root.order.add_edge(supplier_relations, retail_outreach)

# 6a. marketing -> feedback_loop
root.order.add_edge(marketing, feedback_loop)
# 6b. retail_outreach -> feedback_loop
root.order.add_edge(retail_outreach, feedback_loop)

# 7. feedback_loop -> stock_management
root.order.add_edge(feedback_loop, stock_management)