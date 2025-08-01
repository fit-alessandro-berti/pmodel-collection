# Generated from: 5cd9afa1-f3b2-4635-9461-133844387a9c.json
# Description: This process involves the intricate validation and certification of rare cultural artifacts using a multi-disciplinary approach. It begins with provenance review, followed by material analysis using advanced spectroscopy. Next, experts conduct stylistic and historical cross-referencing. Digital watermarking is applied for future tracking. Legal clearances are obtained through international heritage law offices. Finally, a tamper-evident seal is issued and logged in a decentralized ledger, ensuring authenticity and preventing illicit trade. The entire workflow requires coordination across legal, scientific, and archival domains to maintain integrity and trust in the artifact authentication process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
pr = Transition(label='Provenance Review')
ms = Transition(label='Material Scan')
st = Transition(label='Spectral Test')
sc = Transition(label='Style Check')
hc = Transition(label='Historical Crossref')
ep = Transition(label='Expert Panel')
dw = Transition(label='Digital Watermark')
lc = Transition(label='Legal Clearance')
ha = Transition(label='Heritage Audit')
si = Transition(label='Seal Issuance')
tp = Transition(label='Tamper Proof')
ll = Transition(label='Ledger Logging')
sn = Transition(label='Stakeholder Notify')
fa = Transition(label='Final Approval')
ad = Transition(label='Artifact Dispatch')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    pr, ms, st, sc, hc, ep, dw, lc, ha, si, tp, ll, sn, fa, ad
])

# Define sequencing and concurrency relations
root.order.add_edge(pr, ms)
root.order.add_edge(ms, st)

# Stylistic and historical cross‐referencing in parallel after spectroscopy
root.order.add_edge(st, sc)
root.order.add_edge(st, hc)
root.order.add_edge(sc, ep)
root.order.add_edge(hc, ep)

# Watermarking after expert panel
root.order.add_edge(ep, dw)

# Legal clearance and heritage audit in parallel after watermarking
root.order.add_edge(dw, lc)
root.order.add_edge(dw, ha)
root.order.add_edge(lc, si)
root.order.add_edge(ha, si)

# Seal issuance, tamper‐proofing, ledger logging, notification, approval, dispatch
root.order.add_edge(si, tp)
root.order.add_edge(tp, ll)
root.order.add_edge(ll, sn)
root.order.add_edge(sn, fa)
root.order.add_edge(fa, ad)