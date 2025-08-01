# Generated from: c37e68ef-2601-41c3-97b1-ee12581c44be.json
# Description: This process covers the end-to-end supply chain for artisan cheese production, starting from raw milk sourcing through quality verification, fermentation control, and aging management. It includes packaging design customization, niche market distribution, and feedback integration for continuous product refinement. The process also involves regulatory compliance checks, seasonal inventory adjustments, and collaborative marketing campaigns to strengthen brand presence in specialty food markets. Stakeholder coordination ensures timely deliveries while maintaining product integrity throughout transit and storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_press = Transition(label='Molding Press')
fermentation_control = Transition(label='Fermentation Control')
aging_setup = Transition(label='Aging Setup')
humidity_check = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_scheduling = Transition(label='Order Scheduling')
market_delivery = Transition(label='Market Delivery')
feedback_review = Transition(label='Feedback Review')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')

# Partial order 1: Milk Processing sequence
milk_processing = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_prep,
    curd_cutting,
    whey_draining,
    molding_press
])
milk_processing.order.add_edge(milk_sourcing, quality_testing)
milk_processing.order.add_edge(quality_testing, starter_prep)
milk_processing.order.add_edge(starter_prep, curd_cutting)
milk_processing.order.add_edge(curd_cutting, whey_draining)
milk_processing.order.add_edge(whey_draining, molding_press)

# Partial order 2: Fermentation and Aging, Humidity check concurrent with Aging Setup
fermentation_aging = StrictPartialOrder(nodes=[
    fermentation_control,
    aging_setup,
    humidity_check
])
fermentation_aging.order.add_edge(fermentation_control, aging_setup)
# humidity_check concurrent with aging_setup (no edge)

# Packaging design and label approval (sequence)
packaging = StrictPartialOrder(nodes=[packaging_design, label_approval])
packaging.order.add_edge(packaging_design, label_approval)

# Inventory audit and order scheduling (sequence)
inventory = StrictPartialOrder(nodes=[inventory_audit, order_scheduling])
inventory.order.add_edge(inventory_audit, order_scheduling)

# Market delivery, feedback review, compliance check and marketing sync (concurrent)
delivery_feedback_compliance_marketing = StrictPartialOrder(nodes=[
    market_delivery,
    feedback_review,
    compliance_check,
    marketing_sync
])
# no internal ordering, all concurrent

# Combine inventory and delivery_feedback_compliance_marketing, order scheduling before delivery
inv_del = StrictPartialOrder(nodes=[inventory, delivery_feedback_compliance_marketing])
# The nodes inventory and delivery_feedback_compliance_marketing are themselves StrictPartialOrders,
# need to flatten nodes and edges inside inv_del

# To merge StrictPartialOrders properly, we create one StrictPartialOrder with all nodes and edges:

all_nodes = [
    milk_processing,
    fermentation_aging,
    packaging,
    inventory,
    delivery_feedback_compliance_marketing
]

# The top-level partial order: milk_processing --> fermentation_aging --> packaging --> inventory --> delivery_feedback_compliance_marketing
root = StrictPartialOrder(
    nodes=[
        milk_sourcing, quality_testing, starter_prep, curd_cutting, whey_draining, molding_press,
        fermentation_control, aging_setup, humidity_check,
        packaging_design, label_approval,
        inventory_audit, order_scheduling,
        market_delivery, feedback_review, compliance_check, marketing_sync
    ]
)

# Add milk processing edges
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_press)

# milk_processing --> fermentation_aging: milk_processing completes before fermentation_control starts
root.order.add_edge(molding_press, fermentation_control)

# fermentation_aging edges
root.order.add_edge(fermentation_control, aging_setup)
# humidity_check concurrent with aging_setup: no edge

# fermentation_aging --> packaging: aging_setup completes before packaging_design
root.order.add_edge(aging_setup, packaging_design)

# packaging edges
root.order.add_edge(packaging_design, label_approval)

# packaging --> inventory
root.order.add_edge(label_approval, inventory_audit)

# inventory edges
root.order.add_edge(inventory_audit, order_scheduling)

# inventory --> market_delivery, feedback_review, compliance_check, marketing_sync
root.order.add_edge(order_scheduling, market_delivery)
root.order.add_edge(order_scheduling, feedback_review)
root.order.add_edge(order_scheduling, compliance_check)
root.order.add_edge(order_scheduling, marketing_sync)

# No ordering among market_delivery, feedback_review, compliance_check, marketing_sync (concurrent)

# Final root
# root variable is already defined as StrictPartialOrder named root