# Generated from: c53b2c3c-4caa-4433-bb20-30a02ecb9c21.json
# Description: This process involves the multidisciplinary verification of rare artifacts combining historical research, material science, and expert consultation to establish provenance and authenticity. It includes initial discovery documentation, advanced imaging, chemical composition analysis, comparative stylistic evaluation, external expert validation, and legal ownership checks. Collaboration with museums and private collectors ensures accuracy, while risk assessment and conservation recommendations are made before final certification and secure transfer procedures. The process is iterative and may require revisiting prior steps based on new findings or disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
t_discover        = Transition(label='Discover Item')
t_document        = Transition(label='Document Find')
t_survey          = Transition(label='Initial Survey')
t_image           = Transition(label='Image Capture')
t_material        = Transition(label='Material Testing')
t_style           = Transition(label='Style Compare')
t_expert          = Transition(label='Expert Consult')
t_provenance      = Transition(label='Provenance Check')
t_ownership       = Transition(label='Ownership Verify')
t_legal           = Transition(label='Legal Review')
t_risk            = Transition(label='Risk Assess')
t_conserve        = Transition(label='Conservation Plan')
t_cert            = Transition(label='Certification')
t_transfer        = Transition(label='Secure Transfer')
t_dispute         = Transition(label='Dispute Resolve')
t_archive         = Transition(label='Final Archive')

# Define the core analysis partial order (A-block of the loop)
Ablock = StrictPartialOrder(nodes=[
    t_image, t_material, t_style,
    t_expert, t_provenance, t_ownership,
    t_legal, t_risk, t_conserve
])
# Parallel first three -> Expert Consult
Ablock.order.add_edge(t_image,      t_expert)
Ablock.order.add_edge(t_material,   t_expert)
Ablock.order.add_edge(t_style,      t_expert)
# Expert Consult -> Provenance & Ownership
Ablock.order.add_edge(t_expert,     t_provenance)
Ablock.order.add_edge(t_expert,     t_ownership)
# Provenance & Ownership -> Legal Review
Ablock.order.add_edge(t_provenance, t_legal)
Ablock.order.add_edge(t_ownership,  t_legal)
# Legal Review -> Risk Assess -> Conservation Plan
Ablock.order.add_edge(t_legal,      t_risk)
Ablock.order.add_edge(t_risk,       t_conserve)

# Define the loop: do Ablock, then either exit or do dispute + Ablock again
loop = OperatorPOWL(operator=Operator.LOOP, children=[Ablock, t_dispute])

# Compose the full workflow
root = StrictPartialOrder(nodes=[
    t_discover, t_document, t_survey,
    loop,
    t_cert, t_transfer, t_archive
])
# Define the main sequence / partial order
root.order.add_edge(t_discover, t_document)
root.order.add_edge(t_document, t_survey)
root.order.add_edge(t_survey,   loop)
root.order.add_edge(loop,       t_cert)
root.order.add_edge(t_cert,     t_transfer)
root.order.add_edge(t_transfer, t_archive)