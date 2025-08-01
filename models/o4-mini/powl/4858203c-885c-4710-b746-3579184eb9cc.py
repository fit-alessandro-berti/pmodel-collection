# Generated from: 4858203c-885c-4710-b746-3579184eb9cc.json
# Description: This process involves the intricate validation and certification of rare historical artifacts before they are auctioned to collectors worldwide. It begins with provenance research, followed by material composition analysis using advanced spectroscopy. Next, expert forensic imaging is performed to detect any restoration or forgery attempts. The artifact then undergoes environmental impact testing to ensure preservation standards. Legal clearance checks confirm ownership legitimacy, while digital 3D modeling creates an archival record. The process also includes coordination with customs for export permits, insurance valuation, and final certification issuance. The entire workflow ensures authenticity, legality, and preservation compliance for high-value cultural items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
fi = Transition(label='Forensic Imaging')
rd = Transition(label='Restoration Detect')
it = Transition(label='Impact Testing')
lr = Transition(label='Legal Review')
ov = Transition(label='Ownership Verify')
dm = Transition(label='3D Modeling')
cl = Transition(label='Customs Liaison')
iq = Transition(label='Insurance Quote')
vr = Transition(label='Valuation Review')
cf = Transition(label='Certification')
au = Transition(label='Archival Upload')
ep = Transition(label='Export Permit')
fa = Transition(label='Final Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    pc, ms, fi, rd, it,
    lr, ov, dm,
    cl, iq, vr,
    cf, au, ep, fa
])

# Sequential dependencies at the start
root.order.add_edge(pc, ms)
root.order.add_edge(ms, fi)
root.order.add_edge(fi, rd)
root.order.add_edge(rd, it)

# After impact testing, three tasks can run in parallel
root.order.add_edge(it, lr)
root.order.add_edge(it, ov)
root.order.add_edge(it, dm)

# Once legal, ownership and 3D modeling are done, coordination tasks can start
for prev in [lr, ov, dm]:
    root.order.add_edge(prev, cl)
    root.order.add_edge(prev, iq)
    root.order.add_edge(prev, vr)

# All coordination tasks must finish before certification
for prev in [cl, iq, vr]:
    root.order.add_edge(prev, cf)

# Final linear steps
root.order.add_edge(cf, au)
root.order.add_edge(au, ep)
root.order.add_edge(ep, fa)