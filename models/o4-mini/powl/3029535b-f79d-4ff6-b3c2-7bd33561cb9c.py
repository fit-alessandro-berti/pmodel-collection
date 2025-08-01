# Generated from: 3029535b-f79d-4ff6-b3c2-7bd33561cb9c.json
# Description: This process outlines the comprehensive workflow for authenticating historical artifacts within a museum setting. It involves initial provenance research, physical examination, scientific testing such as radiocarbon dating and spectroscopy, expert consultations, legal clearance for acquisition, and final cataloging. The process ensures artifacts are genuine, ethically sourced, and properly documented before exhibition or storage. Additionally, it includes contingency steps for disputed items and integrates feedback loops with external historians and conservation specialists to maintain authenticity standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pr_check = Transition(label='Provenance Check')
init_survey = Transition(label='Initial Survey')
mat_test = Transition(label='Material Testing')
rad_date = Transition(label='Radiocarbon Date')
micro_scan = Transition(label='Microscopic Scan')
expert_review = Transition(label='Expert Review')
external_fb = Transition(label='External Feedback')
dispute_handle = Transition(label='Dispute Handle')
legal_review = Transition(label='Legal Review')
ethics_clearance = Transition(label='Ethics Clearance')
acquisition_approval = Transition(label='Acquisition Approval')
restoration_plan = Transition(label='Restoration Plan')
conservation = Transition(label='Conservation')
documentation = Transition(label='Documentation')
catalog_update = Transition(label='Catalog Update')
skip = SilentTransition()

# Material Testing sub‐process: perform Radiocarbon Date and Microscopic Scan in parallel after Material Testing
tests_po = StrictPartialOrder(nodes=[mat_test, rad_date, micro_scan])
tests_po.order.add_edge(mat_test, rad_date)
tests_po.order.add_edge(mat_test, micro_scan)

# Feedback/dispute loop: always do Expert Review, then either exit or do (External Feedback or Dispute Handle) and repeat
xor_feedback_or_dispute = OperatorPOWL(
    operator=Operator.XOR,
    children=[external_fb, dispute_handle]
)
review_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_review, xor_feedback_or_dispute]
)

# Restoration branch: either perform Restoration Plan -> Conservation, or skip
restoration_branch = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        StrictPartialOrder(
            nodes=[restoration_plan, conservation]
        ),
        skip
    ]
)
# ensure Restoration Plan precedes Conservation
restoration_branch.children[0].order.add_edge(restoration_plan, conservation)

# Legal & Ethics in parallel, then Acquisition Approval
leg_eth_acq = StrictPartialOrder(nodes=[legal_review, ethics_clearance, acquisition_approval])
leg_eth_acq.order.add_edge(legal_review, acquisition_approval)
leg_eth_acq.order.add_edge(ethics_clearance, acquisition_approval)

# Assemble the full workflow
root = StrictPartialOrder(nodes=[
    pr_check,
    init_survey,
    tests_po,
    review_loop,
    leg_eth_acq,
    restoration_branch,
    documentation,
    catalog_update
])
# Define the sequence flow
root.order.add_edge(pr_check, init_survey)
root.order.add_edge(init_survey, tests_po)
root.order.add_edge(tests_po, review_loop)
root.order.add_edge(review_loop, leg_eth_acq)
root.order.add_edge(leg_eth_acq, restoration_branch)
root.order.add_edge(restoration_branch, documentation)
root.order.add_edge(documentation, catalog_update)