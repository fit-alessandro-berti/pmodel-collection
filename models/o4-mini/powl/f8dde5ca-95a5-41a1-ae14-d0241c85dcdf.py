# Generated from: f8dde5ca-95a5-41a1-ae14-d0241c85dcdf.json
# Description: This process involves a multi-disciplinary approach to authenticate rare artifacts sourced from various global locations. It begins with preliminary provenance checks, followed by advanced material analysis using spectrometry and radiocarbon dating. Specialists then perform stylistic comparisons against extensive historical databases. Concurrently, blockchain registration is prepared to ensure traceability. Legal consultants review ownership legitimacy while conservators assess preservation needs. Finally, a comprehensive report is compiled, validated by an expert panel, and submitted to both the client and relevant cultural heritage authorities to ensure compliance and facilitate potential acquisition or exhibition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
pc = Transition(label="Provenance Check")
ms = Transition(label="Material Scan")
rt = Transition(label="Radiocarbon Test")
sc = Transition(label="Style Compare")
dq = Transition(label="Database Query")
bp = Transition(label="Blockchain Prep")
lr = Transition(label="Legal Review")
oa = Transition(label="Ownership Audit")
cp = Transition(label="Conservation Plan")
rd = Transition(label="Report Draft")
ep = Transition(label="Expert Panel")
cr = Transition(label="Client Review")
asb = Transition(label="Authority Submit")
es = Transition(label="Exhibit Setup")
fa = Transition(label="Final Approval")

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    pc, ms, rt,
    sc, dq, bp,
    lr, oa, cp,
    rd, ep,
    cr, asb,
    es, fa
])

# 1) Preliminary provenance check precedes both material‐analysis tasks
root.order.add_edge(pc, ms)
root.order.add_edge(pc, rt)

# 2) Material Scan and Radiocarbon Test must finish before stylistic/database/blockchain tasks
for src in (ms, rt):
    root.order.add_edge(src, sc)
    root.order.add_edge(src, dq)
    root.order.add_edge(src, bp)

# 3) Style Compare, Database Query, Blockchain Prep all precede the legal/ownership/conservation reviews
for src in (sc, dq, bp):
    root.order.add_edge(src, lr)
    root.order.add_edge(src, oa)
    root.order.add_edge(src, cp)

# 4) Legal Review, Ownership Audit, Conservation Plan all precede Report Draft
for src in (lr, oa, cp):
    root.order.add_edge(src, rd)

# 5) Report Draft → Expert Panel
root.order.add_edge(rd, ep)

# 6) Expert Panel → parallel client and authority submission
root.order.add_edge(ep, cr)
root.order.add_edge(ep, asb)

# 7) Both submissions precede Exhibit Setup
root.order.add_edge(cr, es)
root.order.add_edge(asb, es)

# 8) Exhibit Setup → Final Approval
root.order.add_edge(es, fa)