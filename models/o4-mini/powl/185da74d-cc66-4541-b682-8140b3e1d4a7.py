# Generated from: 185da74d-cc66-4541-b682-8140b3e1d4a7.json
# Description: This process manages the sourcing, creation, and distribution of handcrafted artisanal goods from remote rural communities to urban boutique retailers. It involves identifying unique raw materials, coordinating with local artisans, ensuring quality control through multi-stage inspections, handling complex logistics in regions with limited infrastructure, and maintaining traceability for ethical certification. Additionally, the process integrates real-time feedback loops from customers to adapt designs and production methods, while balancing sustainability goals and fair trade principles with market demand fluctuations and seasonal variations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic transitions
ms = Transition(label='Material Sourcing')
asel = Transition(label='Artisan Selection')
dr = Transition(label='Design Review')
pb = Transition(label='Prototype Build')
qi = Transition(label='Quality Inspect')
bs = Transition(label='Batch Scheduling')
lp = Transition(label='Logistics Plan')
cc = Transition(label='Customs Clearance')
ic = Transition(label='Inventory Check')
ps = Transition(label='Packaging Setup')
ma = Transition(label='Market Analysis')
df = Transition(label='Demand Forecast')
op = Transition(label='Order Processing')
st = Transition(label='Shipment Track')
pr = Transition(label='Payment Reconcile')
sa = Transition(label='Sustainability Audit')
fg = Transition(label='Feedback Gather')

# Silent transition for loops
skip = SilentTransition()

# Loop for multi-stage quality inspection: do Quality Inspect, then decide to exit or inspect again
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[qi, skip])

# XOR between Market Analysis and Demand Forecast to adapt to market/seasonal variations
demand_choice = OperatorPOWL(operator=Operator.XOR, children=[ma, df])

# Loop for real-time customer feedback feeding back into design review
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fg, dr])

# Build the top‐level partially ordered workflow
root = StrictPartialOrder(nodes=[
    ms, asel, dr, pb, quality_loop, bs,
    demand_choice,
    lp, cc, ic, ps, op, st, pr, sa,
    feedback_loop
])

# Define the control‐flow dependencies
root.order.add_edge(ms,   asel)
root.order.add_edge(asel, dr)
root.order.add_edge(dr,   pb)
root.order.add_edge(pb,   quality_loop)
root.order.add_edge(quality_loop, bs)
root.order.add_edge(bs,   demand_choice)
root.order.add_edge(demand_choice, lp)
root.order.add_edge(lp,   cc)
root.order.add_edge(cc,   ic)
root.order.add_edge(ic,   ps)
root.order.add_edge(ps,   op)
root.order.add_edge(op,   st)
root.order.add_edge(st,   pr)
root.order.add_edge(pr,   sa)
root.order.add_edge(sa,  feedback_loop)
root.order.add_edge(feedback_loop, dr)