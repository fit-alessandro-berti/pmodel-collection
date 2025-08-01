# Generated from: 4d455b38-5afc-4224-b3b0-75932dc7543a.json
# Description: This process involves the detailed verification and certification of rare cultural artifacts before acquisition or sale. It integrates multidisciplinary expert analysis, provenance research, non-invasive material testing, and legal clearance. Activities include coordinating with historians, forensic labs, and legal advisors to ensure authenticity and compliance with international trade laws. The workflow also manages digital archiving of findings, stakeholder communications, and final certification issuance, ensuring transparency and traceability throughout the artifact's lifecycle from discovery to market placement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial_review       = Transition(label='Initial Review')
provenance_check     = Transition(label='Provenance Check')
expert_consultation  = Transition(label='Expert Consultation')
material_sampling    = Transition(label='Material Sampling')
lab_analysis         = Transition(label='Lab Analysis')
data_synthesis       = Transition(label='Data Synthesis')
legal_clearance      = Transition(label='Legal Clearance')
digital_archiving    = Transition(label='Digital Archiving')
market_evaluation    = Transition(label='Market Evaluation')
certification_draft  = Transition(label='Certification Draft')
quality_assurance    = Transition(label='Quality Assurance')
final_approval       = Transition(label='Final Approval')
document_issuance    = Transition(label='Document Issuance')
post_sale_audit      = Transition(label='Post-Sale Audit')

# Loop children for iterative risk assessment
risk_assessment      = Transition(label='Risk Assessment')
stakeholder_update   = Transition(label='Stakeholder Update')
risk_loop            = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment, stakeholder_update])

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial_review, provenance_check, expert_consultation,
    material_sampling, lab_analysis, data_synthesis,
    legal_clearance, digital_archiving, market_evaluation,
    certification_draft, quality_assurance, final_approval,
    document_issuance, post_sale_audit, risk_loop
])

# Define the order relations
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(initial_review, expert_consultation)
root.order.add_edge(provenance_check, material_sampling)
root.order.add_edge(expert_consultation, material_sampling)
root.order.add_edge(material_sampling, lab_analysis)
root.order.add_edge(lab_analysis, data_synthesis)
root.order.add_edge(data_synthesis, legal_clearance)
root.order.add_edge(data_synthesis, risk_loop)
root.order.add_edge(data_synthesis, digital_archiving)
root.order.add_edge(legal_clearance, market_evaluation)
root.order.add_edge(risk_loop, market_evaluation)
root.order.add_edge(market_evaluation, certification_draft)
root.order.add_edge(certification_draft, quality_assurance)
root.order.add_edge(quality_assurance, final_approval)
root.order.add_edge(final_approval, document_issuance)
root.order.add_edge(document_issuance, post_sale_audit)