# Generated from: c8efee69-7aee-415a-a6ea-559e0439e363.json
# Description: This process manages the complete lifecycle of producing and distributing artisan cheese from small-scale farms to niche gourmet retailers. It includes raw milk sourcing, quality testing, artisan fermentation, aging control, packaging customization, and cold-chain logistics. The workflow ensures traceability, compliance with regional food safety laws, and adaptive inventory management based on seasonal production variations. Additionally, it integrates direct consumer feedback loops through digital platforms to adjust future batches and marketing strategies, while coordinating limited batch releases and specialty event planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
curd_cutting = Transition(label='Curd Cutting')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
humidity_check = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
inventory_audit = Transition(label='Inventory Audit')
cold_storage = Transition(label='Cold Storage')
order_processing = Transition(label='Order Processing')
logistics_planning = Transition(label='Logistics Planning')
retail_delivery = Transition(label='Retail Delivery')
consumer_feedback = Transition(label='Consumer Feedback')
batch_adjustment = Transition(label='Batch Adjustment')
event_coordination = Transition(label='Event Coordination')

# Define loops and choices based on description

# Loop for aging with humidity checks: (Aging Control followed by choice)
# Loop: execute aging_control, then choose to exit or execute humidity_check then aging_control etc.
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, humidity_check])

# Loop for consumer feedback adjustment cycle:
# Consumer Feedback -> Batch Adjustment -> (loop back to consumer_feedback or exit)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, batch_adjustment])

# Packaging customization: packaging_design and label_printing can run concurrently, then merged by a XOR skip choice for simplification
# Actually, they are parallel; packaging_design and label_printing probably happen concurrently.
packaging_po = StrictPartialOrder(nodes=[packaging_design, label_printing],)
# no order between these two for concurrency

# Inventory audit and cold storage happen after packaging and before order processing
# So packaging -> inventory_audit -> cold_storage -> order_processing
packaging_to_inventory_order = StrictPartialOrder(
    nodes=[packaging_po, inventory_audit, cold_storage, order_processing]
)
packaging_to_inventory_order.order.add_edge(packaging_po, inventory_audit)
packaging_to_inventory_order.order.add_edge(inventory_audit, cold_storage)
packaging_to_inventory_order.order.add_edge(cold_storage, order_processing)

# Logistics planning and retail delivery happen after order processing
# event coordination and specialty event planning runs after retail delivery (somewhat independent)
event_coordination_node = event_coordination

# Order processing -> logistics planning -> retail delivery
post_order_po = StrictPartialOrder(nodes=[order_processing, logistics_planning, retail_delivery, event_coordination_node])
post_order_po.order.add_edge(order_processing, logistics_planning)
post_order_po.order.add_edge(logistics_planning, retail_delivery)
post_order_po.order.add_edge(retail_delivery, event_coordination_node)

# Core production chain: Milk Sourcing -> Quality Testing -> Starter Prep -> Curd Cutting -> Molding Cheese -> Salting Process
core_production_po = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, starter_prep, curd_cutting, molding_cheese, salting_process
])
core_production_po.order.add_edge(milk_sourcing, quality_testing)
core_production_po.order.add_edge(quality_testing, starter_prep)
core_production_po.order.add_edge(starter_prep, curd_cutting)
core_production_po.order.add_edge(curd_cutting, molding_cheese)
core_production_po.order.add_edge(molding_cheese, salting_process)

# Combine core production with aging loop
core_and_aging_po = StrictPartialOrder(nodes=[core_production_po, aging_loop])
core_and_aging_po.order.add_edge(core_production_po, aging_loop)

# Combine packaging with batch feedback loop:
# packaging_po (concurrent nodes) -> inventory audit etc (packaging_to_inventory_order) -> feedback loop (feedback_loop)
# Combine also the post order steps after packaging_to_inventory_order and feedback.
# Feedback loop can be done concurrently with event coordination (marketing/special events)
packaging_and_feedback_po = StrictPartialOrder(nodes=[packaging_to_inventory_order, feedback_loop])
packaging_and_feedback_po.order.add_edge(packaging_to_inventory_order, feedback_loop)

# Total upper chain: packaging_and_feedback -> post order
full_post_production_po = StrictPartialOrder(nodes=[packaging_and_feedback_po, post_order_po])
full_post_production_po.order.add_edge(packaging_and_feedback_po, post_order_po)

# Now, top-level process: core_and_aging_po (production, aging) -> full_post_production_po (packaging, inventory, feedback, delivery)
root = StrictPartialOrder(nodes=[core_and_aging_po, full_post_production_po])
root.order.add_edge(core_and_aging_po, full_post_production_po)