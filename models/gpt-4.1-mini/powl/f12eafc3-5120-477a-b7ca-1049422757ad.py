# Generated from: f12eafc3-5120-477a-b7ca-1049422757ad.json
# Description: This process outlines the complex and highly specialized steps involved in exporting artisanal cheese from a small-scale farm to international gourmet markets. It begins with milk selection and quality testing, followed by traditional cheese crafting and aging under controlled conditions. The matured cheese then undergoes sensory evaluation and packaging using custom materials to preserve flavor and texture. Regulatory compliance checks for export documentation and customs clearance are conducted before the product is shipped via temperature-controlled logistics. Post-shipment tracking and customer feedback analysis complete the cycle, ensuring continuous improvement and market adaptation for this niche product.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Selection = Transition(label='Milk Selection')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Cheese_Crafting = Transition(label='Cheese Crafting')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Review = Transition(label='Sensory Review')
Custom_Packaging = Transition(label='Custom Packaging')
Label_Printing = Transition(label='Label Printing')
Export_Licensing = Transition(label='Export Licensing')
Documentation_Prep = Transition(label='Documentation Prep')
Customs_Clearance = Transition(label='Customs Clearance')
Cold_Shipping = Transition(label='Cold Shipping')
Delivery_Tracking = Transition(label='Delivery Tracking')
Feedback_Review = Transition(label='Feedback Review')
Market_Analysis = Transition(label='Market Analysis')

# First part: milk selection -> quality testing -> pasteurize -> cheese crafting -> controlled aging
po1 = StrictPartialOrder(
    nodes=[Milk_Selection, Quality_Testing, Milk_Pasteurize, Cheese_Crafting, Controlled_Aging]
)
po1.order.add_edge(Milk_Selection, Quality_Testing)
po1.order.add_edge(Quality_Testing, Milk_Pasteurize)
po1.order.add_edge(Milk_Pasteurize, Cheese_Crafting)
po1.order.add_edge(Cheese_Crafting, Controlled_Aging)

# Next: sensory review after controlled aging, then custom packaging and label printing concurrently
packaging_po = StrictPartialOrder(
    nodes=[Custom_Packaging, Label_Printing]
)
# no order between Custom_Packaging and Label_Printing -> concurrent

po2 = StrictPartialOrder(
    nodes=[Sensory_Review, packaging_po]
)
po2.order.add_edge(Sensory_Review, packaging_po)

# Combine export license and documentation prep as concurrent preparatory activities
export_prep = StrictPartialOrder(
    nodes=[Export_Licensing, Documentation_Prep]
)
# no order between Export_Licensing and Documentation_Prep (concurrent)

# Export compliance checks: export prep -> customs clearance
export_checks = StrictPartialOrder(
    nodes=[export_prep, Customs_Clearance]
)
export_checks.order.add_edge(export_prep, Customs_Clearance)

# Shipping after customs clearance
shipping = StrictPartialOrder(
    nodes=[Cold_Shipping]
)

# Post shipment tracking and feedback review concurrent, followed by market analysis
post_shipment = StrictPartialOrder(
    nodes=[Delivery_Tracking, Feedback_Review]
)
# delivery tracking and feedback review concurrent

post_and_analysis = StrictPartialOrder(
    nodes=[post_shipment, Market_Analysis]
)
post_and_analysis.order.add_edge(post_shipment, Market_Analysis)

# Assemble the full sequence:
# po1 -> po2 -> export_checks -> shipping -> post_and_analysis

root = StrictPartialOrder(
    nodes=[po1, po2, export_checks, shipping, post_and_analysis]
)
root.order.add_edge(po1, po2)
root.order.add_edge(po2, export_checks)
root.order.add_edge(export_checks, shipping)
root.order.add_edge(shipping, post_and_analysis)