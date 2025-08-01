# Generated from: a95ea33f-1da5-41ed-b52f-8001b96b79bb.json
# Description: This process outlines the intricate supply chain management of a niche artisan goods company specializing in handcrafted luxury items. It involves sourcing rare raw materials from remote locations, coordinating with local craftspeople, ensuring quality through multi-stage inspections, managing bespoke orders, and integrating sustainable packaging solutions. The process demands close collaboration between procurement, production, design, and logistics teams to maintain authenticity, meet custom client specifications, and adhere to strict environmental standards while optimizing delivery timelines and cost efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ms = Transition(label='Material Sourcing')
sv = Transition(label='Supplier Vetting')
st = Transition(label='Sample Testing')
oc = Transition(label='Order Customization')
cap = Transition(label='Client Approval')
ca = Transition(label='Craft Allocation')
pt = Transition(label='Production Tracking')
qa = Transition(label='Quality Audit')
sc = Transition(label='Sustainability Check')
pd = Transition(label='Packaging Design')
inv_sync = Transition(label='Inventory Sync')
lp = Transition(label='Logistics Planning')
sp = Transition(label='Shipment Prep')
dm = Transition(label='Delivery Monitoring')
fc = Transition(label='Feedback Collection')
reorder = Transition(label='Reorder Forecast')

# Loop for client-driven rework of the customization
customization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[oc, cap]
)

# Main partial order for one end-to-end cycle (up to feedback)
main_cycle = StrictPartialOrder(nodes=[
    ms, sv, st,
    customization_loop,
    ca, pt, qa, sc,
    pd, inv_sync, lp,
    sp, dm, fc
])
# Define the control-flow dependencies
main_cycle.order.add_edge(ms, sv)
main_cycle.order.add_edge(sv, st)
main_cycle.order.add_edge(st, customization_loop)
main_cycle.order.add_edge(customization_loop, ca)
main_cycle.order.add_edge(ca, pt)
main_cycle.order.add_edge(pt, qa)
main_cycle.order.add_edge(pt, sc)
main_cycle.order.add_edge(sc, pd)
main_cycle.order.add_edge(pt, inv_sync)
main_cycle.order.add_edge(pd, lp)
main_cycle.order.add_edge(inv_sync, lp)
main_cycle.order.add_edge(lp, sp)
main_cycle.order.add_edge(sp, dm)
main_cycle.order.add_edge(dm, fc)

# Top‐level loop for handling future reorders
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_cycle, reorder]
)