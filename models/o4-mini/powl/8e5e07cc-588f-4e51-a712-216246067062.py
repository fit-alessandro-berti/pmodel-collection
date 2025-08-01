# Generated from: 8e5e07cc-588f-4e51-a712-216246067062.json
# Description: This process outlines the steps involved in managing a custom art commission from initial client inquiry through final delivery and post-sale support. It begins with gathering detailed client requirements and concept approval, followed by iterative design drafts and revisions. After client confirmation, the artist proceeds with production using specialized materials and techniques. Quality checks ensure adherence to client specifications before packaging. The process concludes with shipment logistics and a feedback collection phase to maintain client satisfaction and improve future commissions. This atypical process incorporates creative, logistical, and customer service tasks in a cohesive workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ci = Transition(label='Client Inquiry')
rg = Transition(label='Requirement Gather')
concept = Transition(label='Concept Sketch')
design_rev = Transition(label='Design Revise')
client_rev = Transition(label='Client Review')
mat = Transition(label='Material Select')
prod = Transition(label='Production Start')
mid = Transition(label='Midway Check')
qr = Transition(label='Quality Review')
fa = Transition(label='Final Approval')
pp = Transition(label='Packaging Prep')
sa = Transition(label='Shipment Arrange')
dc = Transition(label='Delivery Confirm')
fc = Transition(label='Feedback Collect')
ac = Transition(label='Aftercare Support')

# Build the loop for iterative design (Concept Sketch → (Design Revise → Client Review)* )
rev_cycle = StrictPartialOrder(nodes=[design_rev, client_rev])
rev_cycle.order.add_edge(design_rev, client_rev)

design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[concept, rev_cycle]
)

# Assemble the full workflow in a strict partial order
root = StrictPartialOrder(nodes=[
    ci, rg,             # inquiry & requirements
    design_loop,        # concept & revision loop
    mat,                # material selection
    prod,               # production start
    mid,                # midway check
    qr,                 # quality review
    fa,                 # final approval
    pp, sa, dc,         # packaging, shipment, delivery
    fc, ac              # feedback & aftercare
])

# Define the control-flow dependencies
root.order.add_edge(ci, rg)
root.order.add_edge(rg, design_loop)
root.order.add_edge(design_loop, mat)
root.order.add_edge(mat, prod)
root.order.add_edge(prod, mid)
root.order.add_edge(mid, qr)
root.order.add_edge(qr, fa)
root.order.add_edge(fa, pp)
root.order.add_edge(pp, sa)
root.order.add_edge(sa, dc)
root.order.add_edge(dc, fc)
root.order.add_edge(fc, ac)