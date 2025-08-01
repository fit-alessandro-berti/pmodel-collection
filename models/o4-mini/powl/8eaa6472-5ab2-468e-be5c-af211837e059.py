# Generated from: 8eaa6472-5ab2-468e-be5c-af211837e059.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museum acquisition. It includes initial provenance research, multispectral imaging analysis, material composition testing, expert panel review, and legal clearance. The workflow integrates interdisciplinary collaboration, ensuring both scientific validation and cultural significance are verified before final cataloging and insurance appraisal. Each stage involves iterative feedback loops to address discrepancies and confirm authenticity, culminating in secure digital archiving of all findings and certification issuance to guarantee artifact legitimacy and traceability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pr = Transition(label='Provenance Check')
im = Transition(label='Imaging Scan')
mt = Transition(label='Material Test')
cd = Transition(label='Carbon Dating')
er = Transition(label='Expert Review')
fb = Transition(label='Feedback Loop')
ca = Transition(label='Condition Assess')
cc = Transition(label='Cultural Context')
lv = Transition(label='Legal Verify')
sm = Transition(label='Stakeholder Meet')
rd = Transition(label='Report Draft')
fa = Transition(label='Final Approval')
da = Transition(label='Digital Archive')
ia = Transition(label='Insurance Appraise')
ci = Transition(label='Certification Issue')

# Silent skip for optional branches
skip = SilentTransition()

# Optional carbon dating
cd_choice = OperatorPOWL(operator=Operator.XOR, children=[cd, skip])

# Core sequence of scan, test and review
core_seq = StrictPartialOrder(nodes=[im, mt, er])
core_seq.order.add_edge(im, er)
core_seq.order.add_edge(mt, er)

# Feedback loop around the core sequence
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[core_seq, fb])

# Optional stakeholder meeting before reporting
sm_choice = OperatorPOWL(operator=Operator.XOR, children=[sm, skip])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    pr, cd_choice, feedback_loop, ca, cc, lv,
    sm_choice, rd, fa, da, ia, ci
])
root.order.add_edge(pr,    cd_choice)
root.order.add_edge(cd_choice, feedback_loop)
root.order.add_edge(feedback_loop, ca)
root.order.add_edge(ca,    cc)
root.order.add_edge(cc,    lv)
root.order.add_edge(lv,    sm_choice)
root.order.add_edge(sm_choice, rd)
root.order.add_edge(rd,    fa)
root.order.add_edge(fa,    da)
root.order.add_edge(da,    ia)
root.order.add_edge(ia,    ci)