# Generated from: f5fe2cd7-bbd4-45ef-a60b-a2c18794f20e.json
# Description: This process outlines the intricate steps involved in authenticating historical artifacts for museum acquisition. It begins with initial provenance research, followed by material analysis using spectrometry and radiocarbon dating. Expert consultations are conducted to verify stylistic elements and historical context. Legal documentation is reviewed to ensure acquisition legitimacy. If discrepancies arise, re-examination or alternative sourcing is pursued. The process concludes with final approval by the acquisitions committee and secure cataloging for exhibit planning. This workflow ensures both scientific and legal rigor in artifact authentication, minimizing the risk of forgery or misattribution in cultural heritage collections.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
prov     = Transition(label='Provenance Check')
ms       = Transition(label='Material Scan')
rc       = Transition(label='Radiocarbon Test')
sr       = Transition(label='Stylistic Review')
ec       = Transition(label='Expert Consult')
da       = Transition(label='Document Audit')
lv       = Transition(label='Legal Verify')
cr       = Transition(label='Condition Report')
df       = Transition(label='Discrepancy Flag')
reexam   = Transition(label='Re-examination')
alt      = Transition(label='Alternative Source')
acq      = Transition(label='Acquisition Vote')
cat      = Transition(label='Catalog Entry')
exh      = Transition(label='Exhibit Plan')
fa       = Transition(label='Final Approval')

# Body of the loop: material & dating analysis, expert reviews, legal checks, condition report
A = StrictPartialOrder(nodes=[ms, rc, sr, ec, da, lv, cr])
A.order.add_edge(ms, sr)
A.order.add_edge(ms, ec)
A.order.add_edge(rc, sr)
A.order.add_edge(rc, ec)
A.order.add_edge(sr, da)
A.order.add_edge(ec, da)
A.order.add_edge(da, lv)
A.order.add_edge(lv, cr)

# Guard for the loop: flag discrepancy then choose re‐exam or alt source
choice = OperatorPOWL(operator=Operator.XOR, children=[reexam, alt])
B = StrictPartialOrder(nodes=[df, choice])
B.order.add_edge(df, choice)

# Loop: execute A, then either exit or execute B and repeat A
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Full process: provenance check → looping analysis/checks → acquisition vote → cataloging → exhibit planning → final approval
root = StrictPartialOrder(nodes=[prov, loop, acq, cat, exh, fa])
root.order.add_edge(prov, loop)
root.order.add_edge(loop, acq)
root.order.add_edge(acq, cat)
root.order.add_edge(cat, exh)
root.order.add_edge(exh, fa)