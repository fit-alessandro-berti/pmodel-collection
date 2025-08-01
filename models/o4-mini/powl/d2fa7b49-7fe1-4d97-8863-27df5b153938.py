# Generated from: d2fa7b49-7fe1-4d97-8863-27df5b153938.json
# Description: This process involves the intricate verification and certification of rare cultural artifacts before international auction. It begins with artifact intake and preliminary assessment, followed by multi-disciplinary expert validation including historical, chemical, and provenance analyses. After validation, a blockchain-based authenticity token is minted to ensure traceability. Next, legal compliance checks across jurisdictions are conducted, alongside insurance valuation and risk assessment. Finally, the artifact undergoes packaging with climate control measures before secure transport arrangements are finalized for auction delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Preliminary Check')
hr = Transition(label='Historical Review')
ct = Transition(label='Chemical Test')
pa = Transition(label='Provenance Audit')
ep = Transition(label='Expert Panel')
tm = Transition(label='Token Minting')
lr = Transition(label='Legal Review')
cc = Transition(label='Compliance Check')
iv = Transition(label='Insurance Valuation')
ra = Transition(label='Risk Assessment')
pp = Transition(label='Packaging Prep')
cl = Transition(label='Climate Control')
ts = Transition(label='Transport Setup')
fa = Transition(label='Final Approval')

# Create the partial order model
root = StrictPartialOrder(nodes=[ai, pc, hr, ct, pa, ep, tm,
                                 lr, cc, iv, ra, pp, cl, ts, fa])

# Sequential intake and preliminary check
root.order.add_edge(ai, pc)

# Parallel expert analyses after preliminary check
root.order.add_edge(pc, hr)
root.order.add_edge(pc, ct)
root.order.add_edge(pc, pa)

# Expert panel after all analyses
root.order.add_edge(hr, ep)
root.order.add_edge(ct, ep)
root.order.add_edge(pa, ep)

# Minting token after panel
root.order.add_edge(ep, tm)

# Parallel legal/compliance and insurance/risk after minting
root.order.add_edge(tm, lr)
root.order.add_edge(tm, cc)
root.order.add_edge(tm, iv)
root.order.add_edge(tm, ra)

# Packaging and climate control after all checks
for prev in (lr, cc, iv, ra):
    root.order.add_edge(prev, pp)
    root.order.add_edge(prev, cl)

# Transport setup after packaging and climate control
root.order.add_edge(pp, ts)
root.order.add_edge(cl, ts)

# Final approval after transport setup
root.order.add_edge(ts, fa)