# Generated from: 15809ac8-07e3-4d8f-bebd-4a4719499500.json
# Description: This process manages the sourcing, crafting, and distribution of unique artisan goods which involve coordinating with local craftsmen, verifying material authenticity, customizing orders based on client preferences, and ensuring timely delivery while maintaining sustainability standards and minimizing waste throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Source_Materials = Transition(label='Source Materials')
Verify_Authenticity = Transition(label='Verify Authenticity')
Negotiate_Price = Transition(label='Negotiate Price')
Order_Custom = Transition(label='Order Custom')
Design_Prototype = Transition(label='Design Prototype')
Approve_Design = Transition(label='Approve Design')
Craft_Item = Transition(label='Craft Item')
Quality_Inspect = Transition(label='Quality Inspect')
Package_Goods = Transition(label='Package Goods')
Schedule_Pickup = Transition(label='Schedule Pickup')
Arrange_Transport = Transition(label='Arrange Transport')
Track_Shipment = Transition(label='Track Shipment')
Confirm_Delivery = Transition(label='Confirm Delivery')
Collect_Feedback = Transition(label='Collect Feedback')
Restock_Inventory = Transition(label='Restock Inventory')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Building the main partial order structure considering dependencies and concurrency

# First phase: sourcing materials and verifying authenticity happen sequentially
source_phase = StrictPartialOrder(
    nodes=[Source_Materials, Verify_Authenticity, Negotiate_Price]
)
source_phase.order.add_edge(Source_Materials, Verify_Authenticity)
source_phase.order.add_edge(Verify_Authenticity, Negotiate_Price)

# Design & ordering phase: Order Custom -> Design Prototype -> Approve Design sequence
design_phase = StrictPartialOrder(
    nodes=[Order_Custom, Design_Prototype, Approve_Design]
)
design_phase.order.add_edge(Order_Custom, Design_Prototype)
design_phase.order.add_edge(Design_Prototype, Approve_Design)

# Crafting phase depends on approved design
craft_phase = StrictPartialOrder(nodes=[Craft_Item, Quality_Inspect])
craft_phase.order.add_edge(Craft_Item, Quality_Inspect)

# Packaging and arranging shipment go after quality inspect
package_and_shipping = StrictPartialOrder(
    nodes=[Package_Goods, Schedule_Pickup, Arrange_Transport, Track_Shipment, Confirm_Delivery]
)
# Package before scheduling pickup
package_and_shipping.order.add_edge(Package_Goods, Schedule_Pickup)
# Pickup before transport arrangement
package_and_shipping.order.add_edge(Schedule_Pickup, Arrange_Transport)
# Transport before tracking
package_and_shipping.order.add_edge(Arrange_Transport, Track_Shipment)
# Tracking before confirmation
package_and_shipping.order.add_edge(Track_Shipment, Confirm_Delivery)

# Collect Feedback and Restock Inventory happen after delivery confirmation, can run in parallel
feedback_and_restock = StrictPartialOrder(nodes=[Collect_Feedback, Restock_Inventory])

# Sustainability Audit can be done throughout but model it as a concurrent node that can run anytime
# Here, modeled concurrent to entire main flow
sustainability_audit = Sustainability_Audit

# Combine phases into one big PO

# Intermediate nodes to combine:
# source_phase -> design_phase -> craft_phase -> package_and_shipping -> feedback_and_restock
phases = StrictPartialOrder(
    nodes=[source_phase, design_phase, craft_phase, package_and_shipping, feedback_and_restock, sustainability_audit]
)

# Add edges between phases to represent flow sequence
phases.order.add_edge(source_phase, design_phase)
phases.order.add_edge(design_phase, craft_phase)
phases.order.add_edge(craft_phase, package_and_shipping)
phases.order.add_edge(package_and_shipping, feedback_and_restock)

# sustainability_audit is concurrent with everything, so no edges connected -> concurrent execution

root = phases