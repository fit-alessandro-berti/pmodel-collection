# Generated from: b6268122-3b44-4d07-a756-afd1c4b4e835.json
# Description: This process involves verifying the authenticity and provenance of rare artifacts through multidisciplinary methods. It begins with initial visual inspection, followed by advanced material analysis and historical context research. The artifact undergoes comparative studies with known pieces, expert consultations, and digital imaging. Next, scientific dating techniques are applied, and provenance documentation is cross-verified. Once all data is consolidated, a risk assessment is conducted to identify potential forgery indicators. The final step involves generating a detailed authentication report, which is then reviewed by a certification board before the artifact is officially authenticated and cataloged in a secure database for future reference and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
vc = Transition(label='Visual Check')
ms = Transition(label='Material Scan')
cs = Transition(label='Context Study')
cr = Transition(label='Comparative Review')
ec = Transition(label='Expert Consult')
di = Transition(label='Digital Imaging')
cd = Transition(label='Carbon Dating')
pc = Transition(label='Provenance Check')
dc = Transition(label='Data Consolidate')
fa = Transition(label='Forgery Assess')
rd = Transition(label='Report Draft')
br = Transition(label='Board Review')
ce = Transition(label='Certification')
cat = Transition(label='Catalog Entry')
ss = Transition(label='Secure Storage')

# Build the partial order
root = StrictPartialOrder(nodes=[vc, ms, cs, cr, ec, di, cd, pc, dc, fa, rd, br, ce, cat, ss])

# Initial inspection leads to material and context analyses
root.order.add_edge(vc, ms)
root.order.add_edge(vc, cs)

# Material scan and context study complete before comparative review, expert consult, and imaging
for pre in [ms, cs]:
    for nxt in [cr, ec, di]:
        root.order.add_edge(pre, nxt)

# Comparative, expert consult, and imaging complete before dating and provenance check
for pre in [cr, ec, di]:
    for nxt in [cd, pc]:
        root.order.add_edge(pre, nxt)

# Dating and provenance check complete before data consolidation
root.order.add_edge(cd, dc)
root.order.add_edge(pc, dc)

# Sequential final steps
root.order.add_edge(dc, fa)
root.order.add_edge(fa, rd)
root.order.add_edge(rd, br)
root.order.add_edge(br, ce)
root.order.add_edge(ce, cat)
root.order.add_edge(cat, ss)