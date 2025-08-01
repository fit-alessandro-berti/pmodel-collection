# Generated from: 03f336f4-5282-4512-b83c-1b1b0f1ace8b.json
# Description: This complex business process involves the systematic authentication of historical artifacts acquired through various channels. It begins with initial artifact intake and proceeds through multi-disciplinary expert evaluations including material analysis, provenance verification, and stylistic assessment. The process integrates scientific testing such as radiocarbon dating and spectroscopic examination alongside archival research and expert interviews. Discrepancies trigger secondary review loops and risk assessment protocols. Once authenticated, the artifact undergoes documentation, cataloging, and secure storage preparations. The workflow concludes with compliance reporting and preparation for either exhibition or controlled sale, ensuring legal and ethical standards are maintained throughout. This atypical process demands coordination across curatorial, scientific, legal, and logistical teams to guarantee authenticity and integrity in artifact handling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
intake = Transition(label='Intake Check')
material_test = Transition(label='Material Test')
provenance_scan = Transition(label='Provenance Scan')
stylistic_review = Transition(label='Stylistic Review')
radiocarbon_date = Transition(label='Radiocarbon Date')
spectro_analysis = Transition(label='Spectro Analysis')
archive_research = Transition(label='Archive Research')
expert_interview = Transition(label='Expert Interview')
discrepancy_flag = Transition(label='Discrepancy Flag')
secondary_review = Transition(label='Secondary Review')
risk_assess = Transition(label='Risk Assess')
documentation = Transition(label='Documentation')
catalog_update = Transition(label='Catalog Update')
storage_prep = Transition(label='Storage Prep')
compliance_report = Transition(label='Compliance Report')
exhibit_prep = Transition(label='Exhibit Prep')
sale_approval = Transition(label='Sale Approval')

# Phase 1: concurrent expert evaluations
eval_PO = StrictPartialOrder(nodes=[material_test,
                                    provenance_scan,
                                    stylistic_review])
# Phase 2: concurrent scientific & archival tasks
science_PO = StrictPartialOrder(nodes=[radiocarbon_date,
                                       spectro_analysis,
                                       archive_research,
                                       expert_interview])

# A = eval_PO -> science_PO -> discrepancy_flag
A = StrictPartialOrder(nodes=[eval_PO, science_PO, discrepancy_flag])
A.order.add_edge(eval_PO, science_PO)
A.order.add_edge(science_PO, discrepancy_flag)

# B = secondary_review -> risk_assess
B = StrictPartialOrder(nodes=[secondary_review, risk_assess])
B.order.add_edge(secondary_review, risk_assess)

# Loop: run A, then either exit or do B and A again
auth_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Final choice: exhibit or sale
final_choice = OperatorPOWL(operator=Operator.XOR,
                           children=[exhibit_prep, sale_approval])

# Root partial order
root = StrictPartialOrder(nodes=[
    intake,
    auth_loop,
    documentation,
    catalog_update,
    storage_prep,
    compliance_report,
    final_choice
])
root.order.add_edge(intake, auth_loop)
root.order.add_edge(auth_loop, documentation)
root.order.add_edge(documentation, catalog_update)
root.order.add_edge(catalog_update, storage_prep)
root.order.add_edge(storage_prep, compliance_report)
root.order.add_edge(compliance_report, final_choice)