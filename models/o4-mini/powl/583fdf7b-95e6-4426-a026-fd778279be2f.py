# Generated from: 583fdf7b-95e6-4426-a026-fd778279be2f.json
# Description: This process involves the systematic examination and validation of historical artifacts to determine authenticity and provenance. It includes detailed multi-disciplinary analyses such as material composition testing, stylistic comparison, and provenance verification through archival research. The workflow also requires coordination with external experts, legal compliance checks, and secure documentation. Final steps involve digital cataloging and controlled storage recommendations, ensuring artifacts are preserved and their history accurately recorded to support museum acquisitions or private collections. The entire process demands meticulous attention to detail and cross-functional collaboration to mitigate risks of forgery and ensure cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial = Transition(label='Initial Review')
ms = Transition(label='Material Scan')
xray = Transition(label='XRay Analysis')
rad = Transition(label='Radiocarbon Test')
style = Transition(label='Stylistic Match')
prov = Transition(label='Provenance Check')
expert = Transition(label='Expert Consult')
arch = Transition(label='Archival Search')
legal = Transition(label='Legal Verify')
cond = Transition(label='Condition Report')
store = Transition(label='Storage Plan')
doc = Transition(label='Documentation')
catalog = Transition(label='Digital Catalog')
final = Transition(label='Final Approval')
client = Transition(label='Client Brief')

# Parallel material analysis
po_tests = StrictPartialOrder(nodes=[ms, xray, rad])
# after Initial Review -> concurrent tests
# then stylistic match
# then provenance work: archival search runs in parallel with a loop of provenance-check & expert consult
loop_prov = OperatorPOWL(operator=Operator.LOOP, children=[prov, expert])
po_prov = StrictPartialOrder(nodes=[arch, loop_prov])

# Documentation sub-workflow: prepare condition report & storage plan in parallel, then documentation
po_doc_internal = StrictPartialOrder(nodes=[cond, store])

# Build root model
root = StrictPartialOrder(nodes=[
    initial,
    po_tests,
    style,
    po_prov,
    legal,
    po_doc_internal,
    doc,
    catalog,
    final,
    client
])

# Define ordering
root.order.add_edge(initial, po_tests)
root.order.add_edge(po_tests, style)
root.order.add_edge(style, po_prov)
root.order.add_edge(po_prov, legal)
root.order.add_edge(legal, po_doc_internal)
root.order.add_edge(po_doc_internal, doc)
root.order.add_edge(doc, catalog)
root.order.add_edge(catalog, final)
root.order.add_edge(final, client)