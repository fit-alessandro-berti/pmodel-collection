# Generated from: b8cdaeba-0004-4dcd-b3db-03f6c89616a1.json
# Description: This process governs the acquisition, authentication, preservation, and exchange of rare cultural artifacts between international museums and private collectors. It involves multi-layered verification steps including provenance research, scientific testing, and diplomatic clearance. The process ensures legal compliance with cultural heritage laws, ethical considerations, and optimal preservation methodologies. Stakeholders coordinate through multiple channels to negotiate terms, arrange secure transportation, and manage insurance policies. Additionally, public exhibition planning and educational outreach are integrated to maximize cultural impact and accessibility while respecting ownership rights and international treaties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
asrc = Transition(label='Artifact Sourcing')
pc   = Transition(label='Provenance Check')
st   = Transition(label='Scientific Test')
dc   = Transition(label='Diplomatic Clear')
lr   = Transition(label='Legal Review')
ea   = Transition(label='Ethics Approval')
on   = Transition(label='Owner Negotiation')
cd   = Transition(label='Contract Draft')
ins  = Transition(label='Insurance Setup')
stt  = Transition(label='Secure Transit')
cr   = Transition(label='Condition Report')
pp   = Transition(label='Preservation Plan')
ed   = Transition(label='Exhibit Design')
po   = Transition(label='Public Outreach')
ot   = Transition(label='Ownership Transfer')
ca   = Transition(label='Compliance Audit')
fc   = Transition(label='Feedback Collect')

# Verification body: scientific test → diplomatic clear
verification_body = StrictPartialOrder(nodes=[st, dc])
verification_body.order.add_edge(st, dc)

# Loop over provenance check then (scientific test → diplomatic clear) until exit
ver_loop = OperatorPOWL(operator=Operator.LOOP, children=[pc, verification_body])

# Build the full partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        asrc, ver_loop, lr, ea, on, cd, ins, stt,
        cr, pp, ed, po, ot, ca, fc
    ]
)

# Set up the dependencies (→ means precedes)
root.order.add_edge(asrc, ver_loop)
root.order.add_edge(ver_loop, lr)
root.order.add_edge(ver_loop, ea)
root.order.add_edge(lr, on)
root.order.add_edge(ea, on)
root.order.add_edge(on, cd)
root.order.add_edge(cd, ins)
root.order.add_edge(ins, stt)
root.order.add_edge(stt, cr)
root.order.add_edge(stt, pp)
root.order.add_edge(cr, ed)
root.order.add_edge(pp, ed)
root.order.add_edge(cr, po)
root.order.add_edge(pp, po)
root.order.add_edge(ed, ot)
root.order.add_edge(po, ot)
root.order.add_edge(ot, ca)
root.order.add_edge(ca, fc)