# Generated from: cd6499c7-8028-40f1-8829-93b4b96b3a64.json
# Description: This process outlines the detailed supply chain management for artisan cheese production and distribution. It begins with sourcing rare milk varieties from small-scale farms, followed by quality testing and fermentation control. The process includes custom aging schedules based on cheese type, packaging with eco-friendly materials, and coordinating limited batch shipments to niche markets. It also involves managing seasonal variations, vendor relations, and compliance with regional food safety regulations, ensuring traceability from farm to customer while maintaining artisanal integrity and minimizing waste through adaptive inventory management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_drain = Transition(label='Whey Drain')
cheese_press = Transition(label='Cheese Press')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
temperature_control = Transition(label='Temperature Control')
batch_labeling = Transition(label='Batch Labeling')
eco_packaging = Transition(label='Eco Packaging')
inventory_audit = Transition(label='Inventory Audit')
order_coordination = Transition(label='Order Coordination')
regulatory_check = Transition(label='Regulatory Check')
shipment_planning = Transition(label='Shipment Planning')
vendor_liaison = Transition(label='Vendor Liaison')
waste_reduction = Transition(label='Waste Reduction')

# Define partial orders for fermentation and aging control (Starter Prep -> Milk Pasteurize)
fermentation_po = StrictPartialOrder(nodes=[starter_prep, milk_pasteurize])
fermentation_po.order.add_edge(starter_prep, milk_pasteurize)

# Define partial order for cheesemaking steps after pasteurize
cheese_making_po = StrictPartialOrder(
    nodes=[curd_formation, whey_drain, cheese_press, salting_process]
)
cheese_making_po.order.add_edge(curd_formation, whey_drain)
cheese_making_po.order.add_edge(whey_drain, cheese_press)
cheese_making_po.order.add_edge(cheese_press, salting_process)

# Aging control loop: Aging Setup then Temperature Control repeated with loop
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_setup, temperature_control]
)

# Packaging partial order (Batch Labeling then Eco Packaging)
packaging_po = StrictPartialOrder(
    nodes=[batch_labeling, eco_packaging]
)
packaging_po.order.add_edge(batch_labeling, eco_packaging)

# Administrative partial order: Inventory Audit, Order Coordination, Regulatory Check, Shipment Planning, Vendor Liaison, Waste Reduction
admin_po = StrictPartialOrder(
    nodes=[inventory_audit, order_coordination, regulatory_check,
           shipment_planning, vendor_liaison, waste_reduction]
)
# Partial order only constraining some dependencies, e.g., Regulatory Check before Shipment Planning
admin_po.order.add_edge(regulatory_check, shipment_planning)
# Vendor Liaison before Order Coordination (to reflect vendor relations influencing orders)
admin_po.order.add_edge(vendor_liaison, order_coordination)
# Inventory Audit before Waste Reduction (adaptive inventory management influences waste reduction)
admin_po.order.add_edge(inventory_audit, waste_reduction)

# Main sequence start: Milk Sourcing -> Quality Testing -> fermentation_po -> cheese_making_po
# Build top level partial order nodes:
# Nodes include: milk_sourcing, quality_testing, fermentation_po, cheese_making_po, aging_loop, packaging_po, admin_po
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        fermentation_po,
        cheese_making_po,
        aging_loop,
        packaging_po,
        admin_po,
    ]
)

# Add edges according to process flow
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, fermentation_po)
root.order.add_edge(fermentation_po, cheese_making_po)
root.order.add_edge(cheese_making_po, aging_loop)
root.order.add_edge(aging_loop, packaging_po)
root.order.add_edge(packaging_po, admin_po)