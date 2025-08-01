# Generated from: d91db867-8981-4706-a518-bfabaa30511e.json
# Description: This process involves the detailed verification and authentication of rare cultural artifacts for auction houses and private collectors. It begins with initial provenance research, followed by scientific material analysis, historical context validation, and expert consultations. Each artifact undergoes multi-stage imaging, condition assessment, and legal compliance checks. Additionally, the process includes risk evaluation for forgery, coordination with international registries, and ethical clearance. The final steps involve documentation creation, certification issuance, and secure digital archiving, ensuring the artifact's authenticity and legal transferability for sale or display purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
t_pc = Transition(label='Provenance Check')
t_ms = Transition(label='Material Scan')
t_cr = Transition(label='Context Review')
t_ec = Transition(label='Expert Consult')
t_ic = Transition(label='Image Capture')
t_ct = Transition(label='Condition Test')
t_lv = Transition(label='Legal Verify')
t_fr = Transition(label='Forgery Risk')
t_rc = Transition(label='Registry Crosscheck')
t_er = Transition(label='Ethics Review')
t_rd = Transition(label='Report Draft')
t_ci = Transition(label='Certificate Issue')
t_da = Transition(label='Digital Archive')
t_ts = Transition(label='Transfer Setup')
t_fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_pc, t_ms, t_cr, t_ec,
    t_ic, t_ct, t_lv, t_fr, t_rc, t_er,
    t_rd, t_ci, t_da, t_ts, t_fa
])

# Initial sequential provenance → material → context → expert consult
root.order.add_edge(t_pc, t_ms)
root.order.add_edge(t_ms, t_cr)
root.order.add_edge(t_cr, t_ec)

# After Expert Consult, all verification/imaging/legal/risk tasks can start in parallel
for check in [t_ic, t_ct, t_lv, t_fr, t_rc, t_er]:
    root.order.add_edge(t_ec, check)

# All those tasks must complete before drafting the report
for check in [t_ic, t_ct, t_lv, t_fr, t_rc, t_er]:
    root.order.add_edge(check, t_rd)

# Final steps in sequence: draft report → issue certificate → archive → transfer setup → final approval
root.order.add_edge(t_rd, t_ci)
root.order.add_edge(t_ci, t_da)
root.order.add_edge(t_da, t_ts)
root.order.add_edge(t_ts, t_fa)