# Generated from: 5f7ac9d8-6717-44ab-9675-5941eee25789.json
# Description: This complex process involves verifying the authenticity of rare historical artifacts through a multi-disciplinary approach. It includes initial provenance research, material composition analysis using spectroscopy, expert visual examination, cross-referencing with global databases, and legal ownership validation. The process also incorporates risk assessment for potential forgeries, condition reporting, digital archiving of findings, and final certification issuance. Communication with stakeholders is maintained throughout to ensure transparency and compliance with international trade regulations, culminating in secure storage or exhibition preparation depending on the artifact's status.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
va = Transition(label='Visual Audit')
dm = Transition(label='Database Match')
ov = Transition(label='Ownership Verify')
fr = Transition(label='Forgery Risk')
cr = Transition(label='Condition Report')
lr = Transition(label='Legal Review')
ca = Transition(label='Compliance Audit')
ec = Transition(label='Expert Consultation')
da = Transition(label='Digital Archive')
ci = Transition(label='Certification Issue')
sp = Transition(label='Storage Prep')
ep = Transition(label='Exhibit Plan')
ss = Transition(label='Stakeholder Sync')

# Choice at the end: storage or exhibit
end_choice = OperatorPOWL(operator=Operator.XOR, children=[sp, ep])

# Build the partial order
root = StrictPartialOrder(nodes=[pc, ms, va, dm, ov, fr, cr, lr, ca, ec, da, ci, end_choice, ss])

# Sequential ordering of the core workflow
root.order.add_edge(pc, ms)
root.order.add_edge(ms, va)
root.order.add_edge(va, dm)
root.order.add_edge(dm, ov)
root.order.add_edge(ov, fr)
root.order.add_edge(fr, cr)
root.order.add_edge(cr, lr)
root.order.add_edge(lr, ca)
root.order.add_edge(ca, ec)
root.order.add_edge(ec, da)
root.order.add_edge(da, ci)
root.order.add_edge(ci, end_choice)

# 'Stakeholder Sync' is concurrent (no ordering constraints) to model ongoing communication
# so we do not add any edges to/from ss.