# Generated from: 05bc3c3e-1fa9-4008-8c38-a3afd15ba456.json
# Description: This process governs the complex lifecycle of negotiating, drafting, and executing patent licenses across multiple jurisdictions with varying legal frameworks. It involves initial patent portfolio analysis, competitive landscape mapping, jurisdiction-specific compliance checks, risk assessments, drafting multi-region agreements, coordinating with local counsel, managing translation and localization of documents, handling royalty tracking and audit processes, and ensuring timely renewals and dispute resolutions. The process demands continuous collaboration between legal, technical, and financial teams to ensure alignment with global IP strategies while mitigating infringement risks and maximizing licensing revenue streams. It concludes with post-license performance reviews and adaptation to evolving regulatory environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pr  = Transition(label='Portfolio Review')
ms  = Transition(label='Market Scan')
comp = Transition(label='Compliance Check')
risk = Transition(label='Risk Assess')
dt  = Transition(label='Draft Terms')
lc  = Transition(label='Local Counsel')
doc = Transition(label='Document Translate')
ar  = Transition(label='Agreement Review')
nm  = Transition(label='Negotiation Meet')
rsu = Transition(label='Royalty Setup')
aud = Transition(label='Audit Plan')
pt  = Transition(label='Payment Track')
ren = Transition(label='Renewal Alert')
dis = Transition(label='Dispute Manage')
perf= Transition(label='Performance Review')
reg = Transition(label='Regulation Update')

# Build the compliance‐risk subprocess (parallel) and wrap it in a LOOP with regulation updates
complianceRisk = StrictPartialOrder(nodes=[comp, risk])
loopComp = OperatorPOWL(operator=Operator.LOOP, children=[complianceRisk, reg])

# Build drafting subprocess (parallel)
drafting = StrictPartialOrder(nodes=[dt, lc, doc])

# Build royalty & audit subprocess (parallel)
royalty = StrictPartialOrder(nodes=[rsu, aud, pt])

# Assemble the root partial order
root = StrictPartialOrder(
    nodes=[pr, ms, loopComp, drafting, ar, nm, royalty, ren, dis, perf]
)

# Specify the control‐flow (partial order) between those major blocks
root.order.add_edge(pr,    ms)         # Portfolio Review → Market Scan
root.order.add_edge(ms,    loopComp)   # Market Scan → {Compliance ∥ Risk} (with loop)
root.order.add_edge(loopComp, drafting) # After compliance/risk loop → drafting
root.order.add_edge(drafting, ar)      # Drafting → Agreement Review
root.order.add_edge(ar,    nm)         # Agreement Review → Negotiation
root.order.add_edge(nm,    royalty)    # Negotiation → royalty & audit
root.order.add_edge(royalty, ren)      # Royalty/audit → Renewal Alert
root.order.add_edge(ren,   dis)        # Renewal Alert → Dispute Manage
root.order.add_edge(dis,   perf)       # Dispute Manage → Performance Review