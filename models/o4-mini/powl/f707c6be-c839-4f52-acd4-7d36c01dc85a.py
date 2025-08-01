# Generated from: f707c6be-c839-4f52-acd4-7d36c01dc85a.json
# Description: This process involves the verification and authentication of ancient artifacts using a combination of forensic analysis, historical research, and advanced imaging technologies. The process starts with initial artifact intake and condition assessment, followed by multi-spectral scanning and material composition testing. Experts cross-reference findings with historical databases and provenance records to identify inconsistencies or confirm authenticity. Additionally, the process includes collaboration with external historians and laboratories, legal documentation preparation, and final certification. The authentication process ensures the artifact's legitimacy for museums, collectors, and auction houses, reducing the risk of forgeries entering the market while preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
intake = Transition(label='Artifact Intake')
cond = Transition(label='Condition Check')
scan = Transition(label='Multi-spectral Scan')
test = Transition(label='Material Test')
imaging = Transition(label='Imaging Analysis')
db = Transition(label='Database Match')
prov = Transition(label='Provenance Check')
expert = Transition(label='Expert Review')
hist = Transition(label='Historical Query')
lab = Transition(label='Lab Collaboration')
forg = Transition(label='Forgery Detection')
legal = Transition(label='Legal Drafting')
cert = Transition(label='Certification Issue')
brief = Transition(label='Client Briefing')
arch = Transition(label='Archival Update')
skip = SilentTransition()

# Sub-workflow for legal/certification/briefing
drafting = StrictPartialOrder(nodes=[legal, cert, brief])
drafting.order.add_edge(legal, cert)
drafting.order.add_edge(cert, brief)

# Choice: either do drafting subprocess or skip (if forgery)
xor_branch = OperatorPOWL(operator=Operator.XOR, children=[drafting, skip])

# Loop for expert review with optional historical query or lab collaboration
query_choice = OperatorPOWL(operator=Operator.XOR, children=[hist, lab])
loop = OperatorPOWL(operator=Operator.LOOP, children=[expert, query_choice])

# Root partial order
root = StrictPartialOrder(nodes=[
    intake, cond,
    scan, test, imaging,
    db, prov,
    loop,
    forg,
    xor_branch,
    arch
])

# Control-flow ordering
root.order.add_edge(intake, cond)
root.order.add_edge(cond, scan)
root.order.add_edge(cond, test)
root.order.add_edge(cond, imaging)
for prev in [scan, test, imaging]:
    root.order.add_edge(prev, db)
    root.order.add_edge(prev, prov)
root.order.add_edge(db, loop)
root.order.add_edge(prov, loop)
root.order.add_edge(loop, forg)
root.order.add_edge(forg, xor_branch)
root.order.add_edge(xor_branch, arch)