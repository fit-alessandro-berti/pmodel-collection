# Generated from: cd6499c7-8028-40f1-8829-93b4b96b3a64.json
# Description: This process outlines the detailed supply chain management for artisan cheese production and distribution. It begins with sourcing rare milk varieties from small-scale farms, followed by quality testing and fermentation control. The process includes custom aging schedules based on cheese type, packaging with eco-friendly materials, and coordinating limited batch shipments to niche markets. It also involves managing seasonal variations, vendor relations, and compliance with regional food safety regulations, ensuring traceability from farm to customer while maintaining artisanal integrity and minimizing waste through adaptive inventory management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing     = Transition(label="Milk Sourcing")
quality_testing   = Transition(label="Quality Testing")
starter_prep      = Transition(label="Starter Prep")
milk_pasteurize   = Transition(label="Milk Pasteurize")
curd_formation    = Transition(label="Curd Formation")
whey_drain        = Transition(label="Whey Drain")
cheese_press      = Transition(label="Cheese Press")
salting_process   = Transition(label="Salting Process")
aging_setup       = Transition(label="Aging Setup")
temperature_ctrl  = Transition(label="Temperature Control")
batch_labeling    = Transition(label="Batch Labeling")
eco_packaging     = Transition(label="Eco Packaging")
inventory_audit   = Transition(label="Inventory Audit")
order_coord       = Transition(label="Order Coordination")
vendor_liaison    = Transition(label="Vendor Liaison")
regulatory_check  = Transition(label="Regulatory Check")
shipment_planning = Transition(label="Shipment Planning")
waste_reduction   = Transition(label="Waste Reduction")

# Loop for adaptive inventory management (audit -> optionally waste reduction -> repeat)
inventory_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inventory_audit, waste_reduction]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, starter_prep,
    milk_pasteurize, curd_formation, whey_drain,
    cheese_press, salting_process, aging_setup,
    temperature_ctrl, batch_labeling, eco_packaging,
    inventory_loop, order_coord, vendor_liaison,
    regulatory_check, shipment_planning
])

# Add the main sequential flow
root.order.add_edge(milk_sourcing,   quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep,    milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation,  whey_drain)
root.order.add_edge(whey_drain,      cheese_press)
root.order.add_edge(cheese_press,    salting_process)
root.order.add_edge(salting_process, aging_setup)
root.order.add_edge(aging_setup,     temperature_ctrl)
root.order.add_edge(temperature_ctrl, batch_labeling)
root.order.add_edge(batch_labeling,  eco_packaging)

# Inventory management loop inserted after packaging
root.order.add_edge(eco_packaging, inventory_loop)
root.order.add_edge(inventory_loop, order_coord)

# Parallel handling of vendor relations and regulatory compliance
root.order.add_edge(order_coord,      vendor_liaison)
root.order.add_edge(order_coord,      regulatory_check)
root.order.add_edge(vendor_liaison,   shipment_planning)
root.order.add_edge(regulatory_check, shipment_planning)