# Generated from: 123751a7-ed99-4282-a93c-a954326eb58c.json
# Description: This process involves the detailed examination and verification of antique artifacts to establish provenance and authenticity before acquisition or sale. It integrates multidisciplinary expertise including historical research, scientific analysis, and expert appraisal. Initial steps include preliminary inspection and documentation, followed by provenance tracing through archives and previous ownership records. Scientific testing such as radiocarbon dating, spectroscopy, and material composition analysis are conducted to verify age and origin. Parallel to technical evaluation, stylistic comparison is performed against known authentic pieces. The process requires collaboration with legal teams to confirm ownership legitimacy and compliance with cultural heritage laws. Finally, a comprehensive authentication report is compiled, including visual documentation and certification, before the artifact is approved for market entry or museum acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
pi      = Transition(label='Prelim Inspect')
doc     = Transition(label='Document Item')
trace   = Transition(label='Trace Provenance')
arch    = Transition(label='Archive Search')
own     = Transition(label='Ownership Check')
rc      = Transition(label='Radiocarbon Test')
spec    = Transition(label='Spectroscopy Scan')
mat     = Transition(label='Material Analysis')
style   = Transition(label='Style Compare')
app     = Transition(label='Expert Appraise')
legal   = Transition(label='Legal Review')
herit   = Transition(label='Heritage Compliance')
comp    = Transition(label='Compile Report')
vis     = Transition(label='Visual Document')
cert    = Transition(label='Certification Issue')
flt     = Transition(label='Market Approval')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    pi, doc, trace,
    arch, own,
    rc, spec, mat, style,
    app,
    legal, herit,
    comp, vis, cert,
    flt
])

# Preliminary inspection and documentation
root.order.add_edge(pi, doc)

# Provenance tracing
root.order.add_edge(doc, trace)
root.order.add_edge(trace, arch)
root.order.add_edge(trace, own)

# Technical evaluation (parallel tests) and style comparison
root.order.add_edge(trace, rc)
root.order.add_edge(trace, spec)
root.order.add_edge(trace, mat)
root.order.add_edge(trace, style)

# Expert appraisal after all checks/tests
for predecessor in [arch, own, rc, spec, mat, style]:
    root.order.add_edge(predecessor, app)

# Legal and heritage compliance in parallel
root.order.add_edge(app, legal)
root.order.add_edge(app, herit)

# Compile report after legal checks
root.order.add_edge(legal, comp)
root.order.add_edge(herit, comp)

# Include visual documentation and certification
root.order.add_edge(comp, vis)
root.order.add_edge(comp, cert)

# Final market approval
root.order.add_edge(vis, flt)
root.order.add_edge(cert, flt)