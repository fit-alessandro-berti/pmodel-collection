# Generated from: 6bad82af-7ac5-4a26-8c72-b41a104f557e.json
# Description: This process details the complex steps involved in exporting artisanal cheese from small-scale farms to international gourmet markets. It begins with milk sourcing from specific breed cows, followed by precise curdling and aging under controlled conditions. The cheese is then carefully packaged with temperature monitoring and compliance with diverse export regulations. Logistics coordination includes cold chain management, customs clearance, and distribution to boutique retailers. The process requires continuous quality testing and feedback loops with producers to maintain product integrity and meet varying consumer tastes across regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
breed_selection = Transition(label='Breed Selection')
curd_formation = Transition(label='Curd Formation')
pressing_cheese = Transition(label='Pressing Cheese')
aging_process = Transition(label='Aging Process')
quality_testing = Transition(label='Quality Testing')
packaging_prep = Transition(label='Packaging Prep')
temp_monitoring = Transition(label='Temp Monitoring')
label_compliance = Transition(label='Label Compliance')
export_documentation = Transition(label='Export Documentation')
cold_chain = Transition(label='Cold Chain')
customs_clearance = Transition(label='Customs Clearance')
shipping_booking = Transition(label='Shipping Booking')
retail_coordination = Transition(label='Retail Coordination')
feedback_review = Transition(label='Feedback Review')

# Quality testing and feedback loop:
# loop = *(Quality Testing, Feedback Review)
quality_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, feedback_review])

# Milk sourcing and breed selection happen sequentially:
milk_breed_po = StrictPartialOrder(nodes=[milk_sourcing, breed_selection])
milk_breed_po.order.add_edge(milk_sourcing, breed_selection)

# After breed selection, curd formation then pressing cheese then aging process:
curd_press_aging_po = StrictPartialOrder(
    nodes=[curd_formation, pressing_cheese, aging_process, quality_feedback_loop]
)
curd_press_aging_po.order.add_edge(curd_formation, pressing_cheese)
curd_press_aging_po.order.add_edge(pressing_cheese, aging_process)
# Quality testing and feedback loop runs in parallel with aging process since it's continuous
curd_press_aging_po.order.add_edge(aging_process, quality_feedback_loop)

# Packaging prep, temp monitoring and label compliance run sequentially after aging process ends and quality feedback:
packaging_po = StrictPartialOrder(nodes=[packaging_prep, temp_monitoring, label_compliance])
packaging_po.order.add_edge(packaging_prep, temp_monitoring)
packaging_po.order.add_edge(temp_monitoring, label_compliance)

# Export documentation after packaging sequence:
export_po = StrictPartialOrder(nodes=[label_compliance, export_documentation])
export_po.order.add_edge(label_compliance, export_documentation)

# Logistics coordination: cold chain, customs clearance, shipping booking, retail coordination sequentially:
logistics_po = StrictPartialOrder(
    nodes=[cold_chain, customs_clearance, shipping_booking, retail_coordination]
)
logistics_po.order.add_edge(cold_chain, customs_clearance)
logistics_po.order.add_edge(customs_clearance, shipping_booking)
logistics_po.order.add_edge(shipping_booking, retail_coordination)

# Combine export doc and logistics coordination in partial order (export_documentation before cold_chain):
export_logistics_po = StrictPartialOrder(
    nodes=[export_documentation, cold_chain, customs_clearance, shipping_booking, retail_coordination]
)
export_logistics_po.order.add_edge(export_documentation, cold_chain)
export_logistics_po.order.add_edge(cold_chain, customs_clearance)
export_logistics_po.order.add_edge(customs_clearance, shipping_booking)
export_logistics_po.order.add_edge(shipping_booking, retail_coordination)

# Connect packaging sequence to export + logistics
packaging_export_logistics_po = StrictPartialOrder(
    nodes=[packaging_prep, temp_monitoring, label_compliance,
           export_documentation, cold_chain, customs_clearance, shipping_booking, retail_coordination]
)
packaging_export_logistics_po.order.add_edge(packaging_prep, temp_monitoring)
packaging_export_logistics_po.order.add_edge(temp_monitoring, label_compliance)
packaging_export_logistics_po.order.add_edge(label_compliance, export_documentation)
packaging_export_logistics_po.order.add_edge(export_documentation, cold_chain)
packaging_export_logistics_po.order.add_edge(cold_chain, customs_clearance)
packaging_export_logistics_po.order.add_edge(customs_clearance, shipping_booking)
packaging_export_logistics_po.order.add_edge(shipping_booking, retail_coordination)

# Now combine the aging + quality loop and packaging onwards:
aging_quality_packaging_po = StrictPartialOrder(
    nodes=[aging_process, quality_feedback_loop,
           packaging_prep, temp_monitoring, label_compliance,
           export_documentation, cold_chain, customs_clearance, shipping_booking, retail_coordination]
)
aging_quality_packaging_po.order.add_edge(aging_process, quality_feedback_loop)
aging_quality_packaging_po.order.add_edge(aging_process, packaging_prep)
aging_quality_packaging_po.order.add_edge(quality_feedback_loop, packaging_prep)
aging_quality_packaging_po.order.add_edge(packaging_prep, temp_monitoring)
aging_quality_packaging_po.order.add_edge(temp_monitoring, label_compliance)
aging_quality_packaging_po.order.add_edge(label_compliance, export_documentation)
aging_quality_packaging_po.order.add_edge(export_documentation, cold_chain)
aging_quality_packaging_po.order.add_edge(cold_chain, customs_clearance)
aging_quality_packaging_po.order.add_edge(customs_clearance, shipping_booking)
aging_quality_packaging_po.order.add_edge(shipping_booking, retail_coordination)

# Finally, combine all with initial Milk Sourcing and Breed Selection nodes
root = StrictPartialOrder(
    nodes=[milk_sourcing, breed_selection,
           curd_formation, pressing_cheese,
           aging_process, quality_feedback_loop,
           packaging_prep, temp_monitoring, label_compliance,
           export_documentation, cold_chain, customs_clearance, shipping_booking, retail_coordination]
)

root.order.add_edge(milk_sourcing, breed_selection)
root.order.add_edge(breed_selection, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, aging_process)
root.order.add_edge(aging_process, quality_feedback_loop)
root.order.add_edge(aging_process, packaging_prep)
root.order.add_edge(quality_feedback_loop, packaging_prep)
root.order.add_edge(packaging_prep, temp_monitoring)
root.order.add_edge(temp_monitoring, label_compliance)
root.order.add_edge(label_compliance, export_documentation)
root.order.add_edge(export_documentation, cold_chain)
root.order.add_edge(cold_chain, customs_clearance)
root.order.add_edge(customs_clearance, shipping_booking)
root.order.add_edge(shipping_booking, retail_coordination)