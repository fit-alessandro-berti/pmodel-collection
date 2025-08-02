# Generated from: 3029535b-f79d-4ff6-b3c2-7bd33561cb9c.json
# Description: This process outlines the comprehensive workflow for authenticating historical artifacts within a museum setting. It involves initial provenance research, physical examination, scientific testing such as radiocarbon dating and spectroscopy, expert consultations, legal clearance for acquisition, and final cataloging. The process ensures artifacts are genuine, ethically sourced, and properly documented before exhibition or storage. Additionally, it includes contingency steps for disputed items and integrates feedback loops with external historians and conservation specialists to maintain authenticity standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')
Initial_Survey = Transition(label='Initial Survey')
Material_Testing = Transition(label='Material Testing')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Microscopic_Scan = Transition(label='Microscopic Scan')
Expert_Review = Transition(label='Expert Review')
Legal_Review = Transition(label='Legal Review')
Acquisition_Approval = Transition(label='Acquisition Approval')
Restoration_Plan = Transition(label='Restoration Plan')
Documentation = Transition(label='Documentation')
Ethics_Clearance = Transition(label='Ethics Clearance')
Dispute_Handle = Transition(label='Dispute Handle')
Conservation = Transition(label='Conservation')
Catalog_Update = Transition(label='Catalog Update')
External_Feedback = Transition(label='External Feedback')

# Material Testing PO with radiocarbon dating and microscopic scan concurrent
material_test_po = StrictPartialOrder(nodes=[Radiocarbon_Date, Microscopic_Scan])
# no edges: Radiocarbon_Date and Microscopic_Scan concurrent

# Material Testing consists of Material Testing activity followed by the PO of two concurrent tests
material_testing_loop = StrictPartialOrder(nodes=[Material_Testing, material_test_po])
material_testing_loop.order.add_edge(Material_Testing, material_test_po)

# Expert Review and Legal Review concurrent after testing
review_po = StrictPartialOrder(nodes=[Expert_Review, Legal_Review])
# no edges: Expert_Review and Legal_Review concurrent

# Approval steps: Acquisition Approval after reviews
approval_po = StrictPartialOrder(nodes=[review_po, Acquisition_Approval])
approval_po.order.add_edge(review_po, Acquisition_Approval)

# After approval, ethics clearance and restoration plan concurrent
ethics_and_restoration = StrictPartialOrder(nodes=[Ethics_Clearance, Restoration_Plan])
# no edges: concurrent

# After ethics and restoration, Documentation
doc_after = StrictPartialOrder(nodes=[ethics_and_restoration, Documentation])
doc_after.order.add_edge(ethics_and_restoration, Documentation)

# Dispute Handle choice happens potentially after expert review (disputed items)
# We model a choice: either proceed normally or go to Dispute Handle then Conservation then External Feedback loop
dispute_loop_body = StrictPartialOrder(nodes=[Conservation, External_Feedback])
dispute_loop_body.order.add_edge(Conservation, External_Feedback)

dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[SilentTransition(), dispute_loop_body])

dispute_process = StrictPartialOrder(nodes=[Dispute_Handle, dispute_loop])
dispute_process.order.add_edge(Dispute_Handle, dispute_loop)

# Between Expert Review and Legal Review, add branching: either normal or dispute handle loop after Expert Review
# So we create a XOR choice after Expert Review: either continue Legal Review or dispute handle loop (then legal review waits after)
dispute_xor = OperatorPOWL(operator=Operator.XOR, children=[Legal_Review, dispute_process])

# Replace review_po with Expert_Review followed by dispute_xor
review_after_expert = StrictPartialOrder(nodes=[Expert_Review, dispute_xor])
review_after_expert.order.add_edge(Expert_Review, dispute_xor)

# Now approval after dispute_xor
approval_after_dispute = StrictPartialOrder(nodes=[review_after_expert, Acquisition_Approval])
approval_after_dispute.order.add_edge(review_after_expert, Acquisition_Approval)

# The main workflow:
# Provenance Check --> Initial Survey --> Material Testing Loop --> review and approval --> ethics/restoration --> documentation --> catalog update

# Main process order
main_po = StrictPartialOrder(nodes=[
    Provenance_Check,
    Initial_Survey,
    material_testing_loop,
    approval_after_dispute,
    ethics_and_restoration,
    Documentation,
    Catalog_Update
])

# Add edges accordingly
main_po.order.add_edge(Provenance_Check, Initial_Survey)
main_po.order.add_edge(Initial_Survey, material_testing_loop)
main_po.order.add_edge(material_testing_loop, approval_after_dispute)
main_po.order.add_edge(approval_after_dispute, ethics_and_restoration)
main_po.order.add_edge(ethics_and_restoration, Documentation)
main_po.order.add_edge(Documentation, Catalog_Update)

root = main_po