# Generated from: 728d126e-02cc-4d82-a4f8-9bbdecb935ca.json
# Description: This process involves the detailed authentication and provenance verification of historical artifacts before acquisition or exhibition. It begins with initial artifact intake and visual inspection, followed by material composition analysis using advanced spectroscopy techniques. Next, provenance research is conducted through archival records and expert interviews. Radiocarbon dating and microscopic wear pattern analysis are performed to ascertain age and usage. Concurrently, digital 3D scanning captures precise artifact morphology for virtual reconstruction. A multidisciplinary panel reviews the compiled data to confirm authenticity. Finally, secure cataloging and condition reporting conclude the workflow, ensuring that only verified artifacts proceed to display or sale, minimizing fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define atomic activities
ai = Transition(label='Artifact Intake')
vi = Transition(label='Visual Inspect')
ms = Transition(label='Material Scan')
pr = Transition(label='Provenance Check')
ar = Transition(label='Archive Research')
ec = Transition(label='Expert Consult')
rc = Transition(label='Radiocarbon Test')
wa = Transition(label='Wear Analysis')
sc = Transition(label='3D Scanning')
dc = Transition(label='Data Compilation')
prv = Transition(label='Panel Review')
ac = Transition(label='Authenticity Confirm')
sec = Transition(label='Secure Catalog')
cr = Transition(label='Condition Report')
fa = Transition(label='Final Approval')

# Sub‐process: provenance research (archive + expert → provenance check)
prov_sub = StrictPartialOrder(nodes=[ar, ec, pr])
prov_sub.order.add_edge(ar, pr)
prov_sub.order.add_edge(ec, pr)

# Sub‐process: age & morphology analyses → data compilation
age_sub = StrictPartialOrder(nodes=[rc, wa, sc, dc])
age_sub.order.add_edge(rc, dc)
age_sub.order.add_edge(wa, dc)
age_sub.order.add_edge(sc, dc)

# Sub‐process: final catalog & condition reporting
final_sub = StrictPartialOrder(nodes=[sec, cr])
# no edges => sec and cr concurrent

# Main workflow
root = StrictPartialOrder(nodes=[ai, vi, ms, prov_sub, age_sub, prv, ac, final_sub, fa])
root.order.add_edge(ai, vi)
root.order.add_edge(vi, ms)
root.order.add_edge(ms, prov_sub)
root.order.add_edge(prov_sub, age_sub)
root.order.add_edge(age_sub, prv)
root.order.add_edge(prv, ac)
root.order.add_edge(ac, final_sub)
root.order.add_edge(final_sub, fa)