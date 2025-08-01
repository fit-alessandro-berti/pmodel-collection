# Generated from: dc8d320c-660d-4071-ac0c-2bb1701c5a96.json
# Description: This process involves the detailed verification and authentication of antique artifacts before acquisition or sale. It includes provenance research, material analysis, historical context validation, expert consultation, and legal compliance checks. Each artifact undergoes multi-stage verification to ensure authenticity, prevent fraud, and assess value accurately. The process also incorporates digital cataloging, condition reporting, and restoration recommendations, culminating in final approval or rejection for market entry.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
hr = Transition(label='Historical Review')
ei = Transition(label='Expert Interview')
ca = Transition(label='Condition Audit')
dc = Transition(label='Digital Catalog')
fd = Transition(label='Forgery Detection')
lc = Transition(label='Legal Compliance')
rp = Transition(label='Restoration Plan')
vr = Transition(label='Valuation Report')
ma = Transition(label='Market Analysis')
fa = Transition(label='Final Approval')
sp = Transition(label='Sale Preparation')
cn = Transition(label='Client Notification')
skip = SilentTransition()

# Build the XOR for approval vs. no-sale
branch_approval = StrictPartialOrder(nodes=[fa, sp])
branch_approval.order.add_edge(fa, sp)
xor = OperatorPOWL(operator=Operator.XOR, children=[branch_approval, skip])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[ai, pc, mt, hr, ei, ca, dc, fd, lc, rp, vr, ma, xor, cn]
)

# Artifact Intake precedes all verification activities
for t in [pc, mt, hr, ei, ca, dc, fd, lc]:
    root.order.add_edge(ai, t)

# Material Testing and Condition Audit → Restoration Plan
root.order.add_edge(mt, rp)
root.order.add_edge(ca, rp)

# All verification & restoration → Valuation Report
for t in [pc, mt, hr, ei, ca, dc, fd, lc, rp]:
    root.order.add_edge(t, vr)

# Valuation → Market Analysis → Decision XOR → Client Notification
root.order.add_edge(vr, ma)
root.order.add_edge(ma, xor)
root.order.add_edge(xor, cn)