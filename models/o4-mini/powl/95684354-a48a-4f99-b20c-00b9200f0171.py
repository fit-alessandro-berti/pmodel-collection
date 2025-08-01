# Generated from: 95684354-a48a-4f99-b20c-00b9200f0171.json
# Description: This process involves the identification, authentication, and acquisition of rare cultural artifacts from remote or politically sensitive regions. It requires coordination with historians, local authorities, and international legal bodies to ensure compliance with heritage laws. Detailed provenance research, risk assessment, and secure transport logistics are crucial to prevent fraud, damage, or legal disputes. Post-acquisition, artifacts undergo conservation evaluation and are prepared for either museum display or private collection. Due diligence includes ethical sourcing verification and ongoing monitoring of geopolitical factors affecting ownership rights. The entire workflow demands meticulous documentation, multi-party approvals, and contingency planning for unexpected regulatory changes or transport complications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ts = Transition(label='Site Survey')
ta = Transition(label='Artifact Scan')
pc = Transition(label='Provenance Check')
rr = Transition(label='Risk Assess')
ll = Transition(label='Local Liaison')
pr = Transition(label='Permit Request')
lr = Transition(label='Legal Review')
fa = Transition(label='Funding Approval')
sp = Transition(label='Secure Packing')
ta2 = Transition(label='Transport Arrange')
cc = Transition(label='Customs Clear')
cr = Transition(label='Condition Report')
cp = Transition(label='Conservation Plan')
ep = Transition(label='Exhibit Prep')
oa = Transition(label='Ownership Audit')
cv = Transition(label='Compliance Verify')
fd = Transition(label='Final Documentation')

# Define the final choice: museum display or private collection
xor_final = OperatorPOWL(operator=Operator.XOR, children=[ep, oa])

# Define the monitoring loop: ongoing compliance checks and potential re-assessment of risk
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[cv, rr])

# Assemble the whole process as a partially ordered workflow
root = StrictPartialOrder(
    nodes=[
        ts, ta, pc, rr, ll, pr, lr, fa, sp,
        ta2, cc, cr, cp, xor_final, loop_monitor, fd
    ]
)

# Define the control-flow dependencies (partial order edges)
root.order.add_edge(ts, ta)
root.order.add_edge(ta, pc)
root.order.add_edge(ta, rr)
root.order.add_edge(ta, ll)

root.order.add_edge(pc, lr)
root.order.add_edge(pc, fa)

root.order.add_edge(rr, pr)
root.order.add_edge(rr, fa)

root.order.add_edge(ll, pr)

root.order.add_edge(lr, fa)

# All approvals must complete before packing
root.order.add_edge(lr, sp)
root.order.add_edge(pr, sp)
root.order.add_edge(fa, sp)

root.order.add_edge(sp, ta2)
root.order.add_edge(ta2, cc)
root.order.add_edge(cc, cr)
root.order.add_edge(cr, cp)

# After conservation plan, choose display vs. private
root.order.add_edge(cp, xor_final)

# After chosen branch, enter the monitoring loop, then finalize
root.order.add_edge(xor_final, loop_monitor)
root.order.add_edge(loop_monitor, fd)