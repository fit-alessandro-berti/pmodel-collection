# Generated from: 1bf2e8bd-7393-4438-a568-306d5ad51a03.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for a museum acquisition. It begins with preliminary research to establish provenance, followed by multi-disciplinary scientific testing including radiocarbon dating and material analysis. Concurrently, expert consultations are scheduled to verify stylistic consistency and historical accuracy. Documentation is meticulously gathered and cross-referenced against existing databases. Legal clearance is then obtained to ensure proper ownership transfer, while ethical considerations regarding cultural sensitivity are reviewed. The artifact undergoes condition assessment and conservation planning before final authentication approval is granted. The workflow concludes with digital archiving and preparation for public exhibition, ensuring transparency and traceability throughout the entire process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ir  = Transition(label='Initial Research')
pc  = Transition(label='Provenance Check')
rc  = Transition(label='Radiocarbon Test')
ma  = Transition(label='Material Analysis')
sv  = Transition(label='Style Verify')
er  = Transition(label='Expert Review')
dbc = Transition(label='Database Crosscheck')
lc  = Transition(label='Legal Clearance')
eth = Transition(label='Ethics Review')
ca  = Transition(label='Condition Assess')
cp  = Transition(label='Conservation Plan')
am  = Transition(label='Approval Meeting')
da  = Transition(label='Digital Archive')
ep  = Transition(label='Exhibit Prep')
fr  = Transition(label='Final Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ir, pc, rc, ma, sv, er, dbc, lc, eth,
    ca, cp, am, da, ep, fr
])

# Define the control-flow dependencies
root.order.add_edge(ir, pc)

# After provenance check, tests and reviews run in parallel
for nxt in (rc, ma, sv, er):
    root.order.add_edge(pc, nxt)

# All tests/reviews must finish before database crosscheck
for prev in (rc, ma, sv, er):
    root.order.add_edge(prev, dbc)

# Database crosscheck precedes legal and ethics clearance
root.order.add_edge(dbc, lc)
root.order.add_edge(dbc, eth)

# Both clearances must complete before condition assessment
root.order.add_edge(lc, ca)
root.order.add_edge(eth, ca)

# Condition assessment then conservation planning
root.order.add_edge(ca, cp)

# Conservation plan then approval meeting
root.order.add_edge(cp, am)

# After approval, finalize archiving, exhibition prep, and report
root.order.add_edge(am, da)
root.order.add_edge(am, ep)
root.order.add_edge(am, fr)