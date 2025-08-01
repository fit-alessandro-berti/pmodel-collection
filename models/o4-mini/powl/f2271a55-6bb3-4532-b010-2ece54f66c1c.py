# Generated from: f2271a55-6bb3-4532-b010-2ece54f66c1c.json
# Description: This process involves the intricate steps required to authenticate rare cultural artifacts using a combination of advanced scientific testing, expert historical analysis, and blockchain verification. Initial provenance research is conducted to gather historical context, followed by material composition tests using spectroscopy and radiocarbon dating. Expert appraisers assess craftsmanship and stylistic elements, while digital imaging techniques detect restorations or alterations. Results are then cross-referenced with global artifact databases. Finally, a unique blockchain record is created to provide an immutable authentication certificate, preventing forgery and enhancing collector confidence. The process demands close coordination between scientists, historians, appraisers, and IT specialists to maintain integrity and traceability throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
prov = Transition(label="Provenance Check")
spectro = Transition(label="Spectroscopy Test")
carbon = Transition(label="Carbon Dating")
style = Transition(label="Style Analysis")
app_rev = Transition(label="Appraiser Review")
image = Transition(label="Image Scanning")
rest = Transition(label="Restoration Scan")

db = Transition(label="Database Match")
block = Transition(label="Blockchain Entry")
cert = Transition(label="Certificate Issue")

forg = Transition(label="Forgery Detect")

rc1 = Transition(label="Report Compilation")
cb1 = Transition(label="Client Briefing")
fa1 = Transition(label="Final Approval")
ss1 = Transition(label="Secure Storage")

rc2 = Transition(label="Report Compilation")
cb2 = Transition(label="Client Briefing")
fa2 = Transition(label="Final Approval")
ss2 = Transition(label="Secure Storage")

# Normal (no-forgery) branch sequence
normal_seq = StrictPartialOrder(nodes=[db, block, cert, rc1, cb1, fa1, ss1])
normal_seq.order.add_edge(db, block)
normal_seq.order.add_edge(block, cert)
normal_seq.order.add_edge(cert, rc1)
normal_seq.order.add_edge(rc1, cb1)
normal_seq.order.add_edge(cb1, fa1)
normal_seq.order.add_edge(fa1, ss1)

# Forgery-detected branch sequence
forgery_seq = StrictPartialOrder(nodes=[forg, rc2, cb2, fa2, ss2])
forgery_seq.order.add_edge(forg, rc2)
forgery_seq.order.add_edge(rc2, cb2)
forgery_seq.order.add_edge(cb2, fa2)
forgery_seq.order.add_edge(fa2, ss2)

# Exclusive choice between normal and forgery branches
xor_choice = OperatorPOWL(operator=Operator.XOR, children=[normal_seq, forgery_seq])

# Root partial order
root = StrictPartialOrder(
    nodes=[prov, spectro, carbon, style, app_rev, image, rest, xor_choice]
)

# 1) Provenance → material tests
root.order.add_edge(prov, spectro)
root.order.add_edge(prov, carbon)

# 2) Material tests → expert & imaging analyses (parallel)
for m in [spectro, carbon]:
    root.order.add_edge(m, style)
    root.order.add_edge(m, app_rev)
    root.order.add_edge(m, image)

# 3) Imaging sequence
root.order.add_edge(image, rest)

# 4) After expert & imaging → make the XOR decision
for src in [style, app_rev, rest]:
    root.order.add_edge(src, xor_choice)