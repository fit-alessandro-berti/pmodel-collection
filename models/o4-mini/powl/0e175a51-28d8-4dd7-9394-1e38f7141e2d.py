# Generated from: 0e175a51-28d8-4dd7-9394-1e38f7141e2d.json
# Description: This process outlines the end-to-end supply chain management for a specialty artisan coffee company that sources unique coffee beans from remote farms, manages bespoke roasting profiles, and delivers personalized subscription packages to niche market customers. It includes activities such as farmer collaboration, quality cupping, custom roasting, packaging innovation, logistics coordination, and customer feedback integration to ensure a highly tailored coffee experience that balances sustainability, quality, and exclusivity across multiple global regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
Farm         = Transition(label='Farm Selection')
Harvest      = Transition(label='Bean Harvest')
Sorting      = Transition(label='Initial Sorting')
Cupping      = Transition(label='Quality Cupping')
Feedback     = Transition(label='Farmer Feedback')
Profiling    = Transition(label='Roast Profiling')
Roasting     = Transition(label='Batch Roasting')
Testing      = Transition(label='Flavor Testing')
Packaging    = Transition(label='Custom Packaging')
Subscription = Transition(label='Subscription Setup')
OrderProc    = Transition(label='Order Processing')
Logistics    = Transition(label='Logistics Planning')
Tracking     = Transition(label='Shipment Tracking')
Support      = Transition(label='Customer Support')
Analysis     = Transition(label='Feedback Analysis')
Audit        = Transition(label='Inventory Audit')

# Loop for quality cupping and farmer feedback
qc_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Cupping, Feedback]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    Farm, Harvest, Sorting, qc_loop,
    Profiling, Roasting, Testing,
    Packaging, Subscription, OrderProc,
    Logistics, Tracking, Support,
    Analysis, Audit
])

# Define the control‐flow edges
root.order.add_edge(Farm,         Harvest)
root.order.add_edge(Harvest,      Sorting)
root.order.add_edge(Sorting,      qc_loop)
root.order.add_edge(qc_loop,      Profiling)
root.order.add_edge(Profiling,    Roasting)
root.order.add_edge(Roasting,     Testing)
root.order.add_edge(Testing,      Packaging)
root.order.add_edge(Testing,      Subscription)
root.order.add_edge(Packaging,    OrderProc)
root.order.add_edge(Subscription, OrderProc)
root.order.add_edge(OrderProc,    Logistics)
root.order.add_edge(Logistics,    Tracking)
root.order.add_edge(Tracking,     Support)
root.order.add_edge(Support,      Analysis)
root.order.add_edge(Tracking,     Audit)