# Generated from: c53b2c3c-4caa-4433-bb20-30a02ecb9c21.json
# Description: This process involves the multidisciplinary verification of rare artifacts combining historical research, material science, and expert consultation to establish provenance and authenticity. It includes initial discovery documentation, advanced imaging, chemical composition analysis, comparative stylistic evaluation, external expert validation, and legal ownership checks. Collaboration with museums and private collectors ensures accuracy, while risk assessment and conservation recommendations are made before final certification and secure transfer procedures. The process is iterative and may require revisiting prior steps based on new findings or disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Discover_Item = Transition(label='Discover Item')
Document_Find = Transition(label='Document Find')
Initial_Survey = Transition(label='Initial Survey')
Image_Capture = Transition(label='Image Capture')
Material_Testing = Transition(label='Material Testing')
Style_Compare = Transition(label='Style Compare')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')
Ownership_Verify = Transition(label='Ownership Verify')
Legal_Review = Transition(label='Legal Review')
Risk_Assess = Transition(label='Risk Assess')
Conservation_Plan = Transition(label='Conservation Plan')
Certification = Transition(label='Certification')
Secure_Transfer = Transition(label='Secure Transfer')
Dispute_Resolve = Transition(label='Dispute Resolve')
Final_Archive = Transition(label='Final Archive')

# Step 1: Initial discovery and documentation in sequence
initial_PO = StrictPartialOrder(
    nodes=[Discover_Item, Document_Find, Initial_Survey]
)
initial_PO.order.add_edge(Discover_Item, Document_Find)
initial_PO.order.add_edge(Document_Find, Initial_Survey)

# Step 2: Multidisciplinary evaluation: Image Capture, Material Testing, Style Compare
# These are concurrent after Initial_Survey
multidisciplinary_PO = StrictPartialOrder(
    nodes=[Image_Capture, Material_Testing, Style_Compare]
)
# No order edges: all concurrent

# Step 3: Expert consultation and provenance check in parallel
exp_prov_PO = StrictPartialOrder(
    nodes=[Expert_Consult, Provenance_Check]
)
# concurrent, no order edges

# Step 4: Ownership Verify and Legal Review sequential after provenance
ownership_PO = StrictPartialOrder(
    nodes=[Ownership_Verify, Legal_Review]
)
ownership_PO.order.add_edge(Ownership_Verify, Legal_Review)

# Step 5: Collaboration is implicit in previous steps, here represented by concurrent exp_prov_PO and ownership_PO
collab_PO = StrictPartialOrder(
    nodes=[exp_prov_PO, ownership_PO]
)
# Parallel between exp_prov_PO and ownership_PO - no order between them

# Step 6: Risk Assessment and Conservation Plan sequential
risk_conserv = StrictPartialOrder(
    nodes=[Risk_Assess, Conservation_Plan]
)
risk_conserv.order.add_edge(Risk_Assess, Conservation_Plan)

# Step 7: Certification and Secure Transfer sequential
cert_transfer = StrictPartialOrder(
    nodes=[Certification, Secure_Transfer]
)
cert_transfer.order.add_edge(Certification, Secure_Transfer)

# Step 8: Final Archive after Secure Transfer
# Step 9: Dispute Resolve is a loop choice: after Certification or Secure Transfer, disputes may arise requiring revisiting prior steps

# Build loop body: after initial_PO, multidisciplinary_PO, collab_PO, risk_conserv, cert_transfer
# The loop condition checks for Dispute_Resolve; if so, go back to Document_Find (revisit prior steps)
# Loop(A=main process, B=Dispute Resolve => Document Find ...)

# Compose main sequence before loop (excluding dispute resolve):
# initial_PO --> multidisciplinary_PO --> collab_PO --> risk_conserv --> cert_transfer --> Final_Archive

# Compose PO with these sequences via edges:

main_nodes = [initial_PO, multidisciplinary_PO, collab_PO, risk_conserv, cert_transfer, Final_Archive]

main_PO = StrictPartialOrder(nodes=main_nodes)

# Add ordering edges between these PO nodes (sequential)
main_PO.order.add_edge(initial_PO, multidisciplinary_PO)
main_PO.order.add_edge(multidisciplinary_PO, collab_PO)
main_PO.order.add_edge(collab_PO, risk_conserv)
main_PO.order.add_edge(risk_conserv, cert_transfer)
main_PO.order.add_edge(cert_transfer, Final_Archive)

# Now define the loop body B:
# B node: Dispute Resolve followed by Document Find and re-execute main process from there (loop back)
loop_back_PO = StrictPartialOrder(nodes=[Dispute_Resolve, Document_Find])
loop_back_PO.order.add_edge(Dispute_Resolve, Document_Find)

# The loop is LOOP(main_PO, loop_back_PO) means:
# execute main_PO, then either exit or execute loop_back_PO then main_PO again, iteratively

root = OperatorPOWL(operator=Operator.LOOP, children=[main_PO, loop_back_PO])