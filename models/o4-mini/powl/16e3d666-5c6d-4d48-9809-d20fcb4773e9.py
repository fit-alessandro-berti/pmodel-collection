# Generated from: 16e3d666-5c6d-4d48-9809-d20fcb4773e9.json
# Description: This process involves verifying the authenticity and provenance of rare artifacts through multidisciplinary examination methods. It includes initial discovery reporting, detailed physical and chemical analysis, historical provenance research, expert consultations, and final certification. The process integrates advanced imaging, isotopic testing, and digital archiving to ensure comprehensive validation. Each step requires collaboration among archaeologists, chemists, historians, and legal experts to mitigate forgery risks and establish legitimate ownership. The final output is a verified artifact dossier for collectors or museums, including risk assessment and insurance recommendations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
dr = Transition(label='Discovery Report')
ps = Transition(label='Preliminary Scan')
ms = Transition(label='Material Sampling')
ic = Transition(label='Imaging Capture')
it = Transition(label='Isotope Test')
pc = Transition(label='Provenance Check')
ot = Transition(label='Ownership Trace')
er = Transition(label='Expert Review')
fa = Transition(label='Forgery Analysis')
lv = Transition(label='Legal Verify')
ra = Transition(label='Risk Assess')
ia = Transition(label='Insurance Advise')
da = Transition(label='Digital Archive')
ci = Transition(label='Certification Issue')
fd = Transition(label='Final Dossier')

# Physical & chemical analysis branch (strict order)
scan = StrictPartialOrder(nodes=[ps, ms, ic, it])
scan.order.add_edge(ps, ms)
scan.order.add_edge(ms, ic)
scan.order.add_edge(ic, it)

# Historical provenance branch (strict order)
prov = StrictPartialOrder(nodes=[pc, ot])
prov.order.add_edge(pc, ot)

# Expert review with possible forgery-analysis loop
# LOOP(children=[A, B]) means: do A, then either exit or do B then A again, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[er, fa])

# Parallel finalization of digital archive and certification issue
final_conc = StrictPartialOrder(nodes=[da, ci])
# no edges => da and ci are concurrent

# Assemble the overall process
root = StrictPartialOrder(
    nodes=[dr, scan, prov, loop, lv, ra, ia, final_conc, fd]
)

# Define the partial order
root.order.add_edge(dr, scan)
root.order.add_edge(dr, prov)
root.order.add_edge(scan, loop)
root.order.add_edge(prov, loop)
root.order.add_edge(loop, lv)
root.order.add_edge(lv, ra)
root.order.add_edge(ra, ia)
root.order.add_edge(ia, final_conc)
root.order.add_edge(final_conc, fd)