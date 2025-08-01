# Generated from: 0d5885af-ffa2-40ad-a09c-10bf6b812536.json
# Description: This process involves the detailed verification and authentication of antique assets before acquisition or sale. It requires cross-referencing provenance records, conducting material analysis, consulting with historical experts, and validating ownership history. The process also includes condition assessment, restoration feasibility studies, legal compliance checks for cultural heritage, and coordinating with insurance providers to appraise value. Final approval must be documented in a secure ledger to ensure traceability and authenticity, integrating technological tools like blockchain for enhanced security and transparency in asset handling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
rr = Transition(label='Record Review')
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Test')
oc = Transition(label='Ownership Confirm')
ec = Transition(label='Expert Consult')
re = Transition(label='Risk Evaluate')
ca1 = Transition(label='Condition Assess')
rp = Transition(label='Restoration Plan')
ca2 = Transition(label='Condition Assess')
lv = Transition(label='Legal Verify')
iq = Transition(label='Insurance Quote')
va = Transition(label='Value Appraise')
rd = Transition(label='Report Draft')
fa = Transition(label='Final Approval')
le = Transition(label='Ledger Entry')
bc = Transition(label='Blockchain Log')
cn = Transition(label='Client Notify')

# Loop: consult expert then evaluate risk, repeat until exit
loop_consult = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ec, re]
)

# Loop: plan restoration then reassess condition, repeat until exit
loop_restore = OperatorPOWL(
    operator=Operator.LOOP,
    children=[rp, ca2]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    rr, pc, mt, oc,
    loop_consult,
    ca1,
    loop_restore,
    lv, iq,
    va, rd, fa,
    le, bc, cn
])

# Initial parallel checks after record review
root.order.add_edge(rr, pc)
root.order.add_edge(rr, mt)
root.order.add_edge(rr, oc)

# After all initial checks, enter the consult‐&‐evaluate loop
root.order.add_edge(pc, loop_consult)
root.order.add_edge(mt, loop_consult)
root.order.add_edge(oc, loop_consult)

# After the consult loop, do the first condition assessment
root.order.add_edge(loop_consult, ca1)

# After that, enter the restoration planning loop
root.order.add_edge(ca1, loop_restore)

# After restoration loop, run legal & insurance in parallel
root.order.add_edge(loop_restore, lv)
root.order.add_edge(loop_restore, iq)

# Both legal verify and insurance quote must finish before appraising value
root.order.add_edge(lv, va)
root.order.add_edge(iq, va)

# Then draft report, get final approval
root.order.add_edge(va, rd)
root.order.add_edge(rd, fa)

# Final approval triggers secure ledger entry and blockchain logging in parallel
root.order.add_edge(fa, le)
root.order.add_edge(fa, bc)

# Both entries complete before notifying the client
root.order.add_edge(le, cn)
root.order.add_edge(bc, cn)