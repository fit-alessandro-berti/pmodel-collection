# Generated from: 0424f32e-6025-4787-b49f-41b89af6cc01.json
# Description: This process involves the intricate steps required to authenticate rare and ancient artifacts before acquisition or exhibition. It includes multidisciplinary activities such as provenance research, material analysis, expert consultation, digital imaging, and legal clearance. The workflow ensures the artifact's legitimacy through scientific testing, historical verification, and ethical sourcing checks. Complex coordination between historians, scientists, legal advisors, and curators is essential. The process culminates in certification, secure cataloging, and preparation for transport or display, minimizing risks of fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
prelim = Transition(label='Preliminary Review')
prov = Transition(label='Provenance Check')
hist = Transition(label='Historical Analysis')
mat = Transition(label='Material Testing')
expert = Transition(label='Expert Panel')
carb = Transition(label='Carbon Dating')
cond = Transition(label='Condition Report')
risk = Transition(label='Risk Assessment')
xray = Transition(label='XRay Imaging')
dscan = Transition(label='Digital Scan')
legal = Transition(label='Legal Clearance')
ethics = Transition(label='Ethics Approval')
auth = Transition(label='Authentication Cert')
sec = Transition(label='Secure Cataloging')
transp = Transition(label='Transport Prep')
exhib = Transition(label='Exhibit Setup')

# Provenance research: Provenance Check -> Historical Analysis
PO_prov = StrictPartialOrder(nodes=[prov, hist])
PO_prov.order.add_edge(prov, hist)

# Material analysis loop: Material Testing <loop> Expert Panel
loop_mat = OperatorPOWL(operator=Operator.LOOP, children=[mat, expert])
# After loop: Carbon Dating -> Condition Report -> Risk Assessment
PO_mat = StrictPartialOrder(nodes=[loop_mat, carb, cond, risk])
PO_mat.order.add_edge(loop_mat, carb)
PO_mat.order.add_edge(carb, cond)
PO_mat.order.add_edge(cond, risk)

# Imaging (concurrent): XRay Imaging || Digital Scan
PO_imaging = StrictPartialOrder(nodes=[xray, dscan])
# no edges => concurrent

# Legal & ethics: Legal Clearance -> Ethics Approval
PO_legal = StrictPartialOrder(nodes=[legal, ethics])
PO_legal.order.add_edge(legal, ethics)

# Final choice: Transport Prep xor Exhibit Setup
final_xor = OperatorPOWL(operator=Operator.XOR, children=[transp, exhib])

# Root model assembling all flows
root = StrictPartialOrder(
    nodes=[prelim, PO_prov, PO_mat, PO_imaging, PO_legal, auth, sec, final_xor]
)

# Control-flow edges
# After Preliminary Review start all four parallel flows
root.order.add_edge(prelim, PO_prov)
root.order.add_edge(prelim, PO_mat)
root.order.add_edge(prelim, PO_imaging)
root.order.add_edge(prelim, PO_legal)

# After all flows complete -> Authentication Certificate
root.order.add_edge(PO_prov, auth)
root.order.add_edge(PO_mat, auth)
root.order.add_edge(PO_imaging, auth)
root.order.add_edge(PO_legal, auth)

# Certification -> Secure Cataloging -> final choice
root.order.add_edge(auth, sec)
root.order.add_edge(sec, final_xor)