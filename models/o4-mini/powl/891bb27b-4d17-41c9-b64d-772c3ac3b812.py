# Generated from: 891bb27b-4d17-41c9-b64d-772c3ac3b812.json
# Description: This process involves the meticulous examination and validation of antique artifacts to establish their authenticity and provenance. Specialists conduct multi-layered inspections including material analysis, historical cross-referencing, and forensic imaging. The process integrates expert consultations, database verification, and environmental impact assessments to ensure each item’s legitimacy. It also includes restoration feasibility studies, market valuation, and legal compliance checks related to cultural heritage protections before final certification and archival documentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ir = Transition(label='Initial Review')
ms = Transition(label='Material Scan')
pc = Transition(label='Provenance Check')
hm = Transition(label='Historical Match')
fi = Transition(label='Forensic Imaging')
ec = Transition(label='Expert Consult')
db = Transition(label='Database Search')
cr = Transition(label='Condition Report')
rp = Transition(label='Restoration Plan')
mv = Transition(label='Market Valuation')
lr = Transition(label='Legal Review')
ca = Transition(label='Cultural Audit')
et = Transition(label='Environmental Test')
cert = Transition(label='Certification')
ae = Transition(label='Archival Entry')
fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ir, ms, pc, hm, fi, ec, db, cr, rp, mv, lr, ca, et, cert, ae, fa
])

# Initial review precedes all inspection tasks
root.order.add_edge(ir, ms)
root.order.add_edge(ir, pc)
root.order.add_edge(ir, fi)

# Provenance check feeds into historical match
root.order.add_edge(pc, hm)

# All inspections feed into expert consult, database search, and environmental test
for prep in (ms, hm, fi):
    root.order.add_edge(prep, ec)
    root.order.add_edge(prep, db)
    root.order.add_edge(prep, et)

# Consult, DB search, and environmental test precede the condition report
root.order.add_edge(ec, cr)
root.order.add_edge(db, cr)
root.order.add_edge(et, cr)

# Condition report leads to restoration planning and market valuation
root.order.add_edge(cr, rp)
root.order.add_edge(cr, mv)

# Restoration plan and market valuation lead to legal review and cultural audit
for prev in (rp, mv):
    root.order.add_edge(prev, lr)
    root.order.add_edge(prev, ca)

# Legal review and cultural audit both lead to certification
root.order.add_edge(lr, cert)
root.order.add_edge(ca, cert)

# Certification is followed by archival entry and final approval
root.order.add_edge(cert, ae)
root.order.add_edge(ae, fa)