# Generated from: 0155ce86-a786-454c-9042-13c629ba6da3.json
# Description: This process outlines the comprehensive workflow used by cultural heritage institutions to authenticate and verify the provenance of rare artifacts. The steps include initial artifact intake, condition assessment, historical data mining, scientific material analysis, expert panel review, digital imaging, and provenance chain verification. It integrates multidisciplinary expertise, advanced technology, and legal checks to ensure each artifact's authenticity and rightful ownership before cataloging for exhibition or sale. The process also incorporates risk assessment for potential forgeries and legal compliance with international cultural property laws, culminating in a final certification and archival documentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
dm = Transition(label='Data Mining')
ms = Transition(label='Material Scan')
di = Transition(label='Digital Imaging')
er = Transition(label='Expert Review')
st = Transition(label='Scientific Test')
pc = Transition(label='Provenance Check')
fr = Transition(label='Forgery Risk')
la = Transition(label='Legal Audit')
ov = Transition(label='Ownership Verify')
cert = Transition(label='Certification')
arch = Transition(label='Archival Store')
cat = Transition(label='Catalog Entry')
ex = Transition(label='Exhibit Prep')
sale = Transition(label='Sale Approval')

# Exclusive choice between exhibition and sale
xor = OperatorPOWL(operator=Operator.XOR, children=[ex, sale])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, cc,
    dm, ms, di,
    er, st,
    pc, fr, la,
    ov, cert, arch, cat,
    xor
])

# Define the control-flow dependencies
root.order.add_edge(ai, cc)

root.order.add_edge(cc, dm)
root.order.add_edge(cc, ms)
root.order.add_edge(cc, di)

root.order.add_edge(dm, er)
root.order.add_edge(ms, er)
root.order.add_edge(di, er)

root.order.add_edge(er, st)

root.order.add_edge(st, pc)
root.order.add_edge(st, fr)
root.order.add_edge(st, la)

root.order.add_edge(pc, ov)
root.order.add_edge(fr, ov)
root.order.add_edge(la, ov)

root.order.add_edge(ov, cert)
root.order.add_edge(cert, arch)
root.order.add_edge(arch, cat)
root.order.add_edge(cat, xor)