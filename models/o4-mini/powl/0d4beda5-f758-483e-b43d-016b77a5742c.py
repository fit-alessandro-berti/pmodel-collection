# Generated from: 0d4beda5-f758-483e-b43d-016b77a5742c.json
# Description: This process involves the comprehensive authentication of rare historical artifacts prior to their acquisition by museums or private collectors. It begins with preliminary provenance research, followed by multispectral imaging and chemical composition analysis. Next, expert consultations and cross-referencing with databases are conducted to ensure authenticity and legality. Ethical considerations and cultural heritage laws are reviewed before final valuation and acquisition decisions. Throughout the process, documentation and chain-of-custody records are meticulously maintained to prevent fraud and ensure transparency in the artifact's history and ownership.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities as POWL Transitions
pc     = Transition(label='Provenance Check')
img    = Transition(label='Image Capture')
spec   = Transition(label='Spectral Scan')
chem   = Transition(label='Chemical Test')
dbq    = Transition(label='Database Query')
rev    = Transition(label='Expert Review')
leg    = Transition(label='Legal Audit')
eth    = Transition(label='Ethics Review')
cond   = Transition(label='Condition Report')
chrec  = Transition(label='Chain Record')
ownv   = Transition(label='Ownership Verify')
fraud  = Transition(label='Fraud Analysis')
vs     = Transition(label='Valuation Setup')
vote   = Transition(label='Acquisition Vote')
fin    = Transition(label='Final Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    pc, img, spec, chem,
    dbq, rev,
    eth, leg,
    cond, chrec, ownv, fraud,
    vs, vote, fin
])

# 1. Start → Imaging & Chemical Analyses
root.order.add_edge(pc, img)
root.order.add_edge(pc, spec)
root.order.add_edge(pc, chem)

# 2. Imaging & Chemical Analyses → Database Query & Expert Review
for src in (img, spec, chem):
    root.order.add_edge(src, dbq)
    root.order.add_edge(src, rev)

# 3. Query & Review → Ethics & Legal
for tgt in (eth, leg):
    root.order.add_edge(dbq, tgt)
    root.order.add_edge(rev, tgt)

# 4. Ethics & Legal → Valuation & Vote
for src in (eth, leg):
    root.order.add_edge(src, vs)
    root.order.add_edge(src, vote)

# 5. Valuation & Vote → Final Approval
root.order.add_edge(vs, fin)
root.order.add_edge(vote, fin)

# 6. Documentation & Chain‐of‐Custody run in parallel from Provenance Check and finish before Final Approval
for doc in (cond, chrec, ownv, fraud):
    root.order.add_edge(pc, doc)
    root.order.add_edge(doc, fin)