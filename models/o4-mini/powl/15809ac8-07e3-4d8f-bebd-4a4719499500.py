# Generated from: 15809ac8-07e3-4d8f-bebd-4a4719499500.json
# Description: This process manages the sourcing, crafting, and distribution of unique artisan goods which involve coordinating with local craftsmen, verifying material authenticity, customizing orders based on client preferences, and ensuring timely delivery while maintaining sustainability standards and minimizing waste throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
source_materials     = Transition(label="Source Materials")
verify_authenticity  = Transition(label="Verify Authenticity")
negotiate_price      = Transition(label="Negotiate Price")
order_custom         = Transition(label="Order Custom")
design_prototype     = Transition(label="Design Prototype")
approve_design       = Transition(label="Approve Design")
craft_item           = Transition(label="Craft Item")
quality_inspect      = Transition(label="Quality Inspect")
package_goods        = Transition(label="Package Goods")
schedule_pickup      = Transition(label="Schedule Pickup")
arrange_transport    = Transition(label="Arrange Transport")
track_shipment       = Transition(label="Track Shipment")
confirm_delivery     = Transition(label="Confirm Delivery")
collect_feedback     = Transition(label="Collect Feedback")
sustainability_audit = Transition(label="Sustainability Audit")
restock_inventory    = Transition(label="Restock Inventory")

# A silent skip for optional customization
skip = SilentTransition()

# Optional custom‐order choice: either Order Custom or skip
custom_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[order_custom, skip]
)

# Main production + distribution partial order
production_and_distribution = StrictPartialOrder(nodes=[
    source_materials,
    verify_authenticity,
    negotiate_price,
    custom_xor,
    design_prototype,
    approve_design,
    craft_item,
    quality_inspect,
    package_goods,
    schedule_pickup,
    arrange_transport,
    track_shipment,
    confirm_delivery,
    collect_feedback
])
po = production_and_distribution.order
po.add_edge(source_materials,    verify_authenticity)
po.add_edge(verify_authenticity, negotiate_price)
po.add_edge(negotiate_price,     custom_xor)
po.add_edge(custom_xor,          design_prototype)
po.add_edge(design_prototype,    approve_design)
po.add_edge(approve_design,      craft_item)
po.add_edge(craft_item,          quality_inspect)
po.add_edge(quality_inspect,     package_goods)
po.add_edge(package_goods,       schedule_pickup)
po.add_edge(schedule_pickup,     arrange_transport)
po.add_edge(arrange_transport,   track_shipment)
po.add_edge(track_shipment,      confirm_delivery)
po.add_edge(confirm_delivery,    collect_feedback)

# Sustainability audit and restock sequence
audit_and_restock = StrictPartialOrder(nodes=[
    sustainability_audit,
    restock_inventory
])
ar_po = audit_and_restock.order
ar_po.add_edge(sustainability_audit, restock_inventory)

# Loop: run production+distribution, then optionally audit+restock and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[production_and_distribution, audit_and_restock]
)