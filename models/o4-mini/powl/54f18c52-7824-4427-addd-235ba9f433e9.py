# Generated from: 54f18c52-7824-4427-addd-235ba9f433e9.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts for acquisition by a museum. It begins with initial artifact intake and cataloging, followed by provenance verification through archival research and expert consultations. Scientific analysis includes material composition testing and radiocarbon dating. Parallel activities involve digital imaging and 3D modeling for condition assessment. Subsequently, a multidisciplinary review committee evaluates all gathered evidence to confirm authenticity or flag discrepancies. Final approval triggers secure documentation creation and integration into the museum's digital registry. Each step demands meticulous record-keeping and cross-referencing to ensure the artifact's legitimacy before public exhibition or storage, thereby minimizing risks of fraud or misattribution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ti   = Transition(label='Artifact Intake')
ce   = Transition(label='Catalog Entry')
pc   = Transition(label='Provenance Check')
ar   = Transition(label='Archive Research')
ec   = Transition(label='Expert Consult')
mt   = Transition(label='Material Test')
rd   = Transition(label='Radiocarbon Date')
di   = Transition(label='Digital Imaging')
m3d  = Transition(label='3D Modeling')
cr   = Transition(label='Condition Review')
ev   = Transition(label='Evidence Collate')
rm   = Transition(label='Review Meeting')
av   = Transition(label='Authenticity Vote')
fa   = Transition(label='Final Approval')
doc  = Transition(label='Documentation')
ru   = Transition(label='Registry Update')
skip = SilentTransition()

# Build the positive branch after the vote: Final Approval -> Documentation -> Registry Update
positive_branch = StrictPartialOrder(nodes=[fa, doc, ru])
positive_branch.order.add_edge(fa, doc)
positive_branch.order.add_edge(doc, ru)

# XOR: either go through the positive branch or skip (i.e., flag discrepancy)
xor_decision = OperatorPOWL(operator=Operator.XOR, children=[positive_branch, skip])

# Assemble the full workflow as a partial order
root = StrictPartialOrder(nodes=[
    ti, ce, pc, ar, ec, mt, rd, di, m3d, cr, ev, rm, av, xor_decision
])

# Define control/dependency edges
# Initial intake and cataloging
root.order.add_edge(ti, ce)

# Provenance verification: after cataloging
root.order.add_edge(ce, pc)
# Parallel research tasks
root.order.add_edge(pc, ar)
root.order.add_edge(pc, ec)

# Scientific analysis after both research tasks
root.order.add_edge(ar, mt)
root.order.add_edge(ar, rd)
root.order.add_edge(ec, mt)
root.order.add_edge(ec, rd)

# Condition assessment after analysis
root.order.add_edge(mt, di)
root.order.add_edge(mt, m3d)
root.order.add_edge(rd, di)
root.order.add_edge(rd, m3d)

# Condition review, evidence collation, review meeting, authenticity vote
root.order.add_edge(di, cr)
root.order.add_edge(m3d, cr)
root.order.add_edge(cr, ev)
root.order.add_edge(ev, rm)
root.order.add_edge(rm, av)

# Decision point: authenticity vote leads into the XOR
root.order.add_edge(av, xor_decision)