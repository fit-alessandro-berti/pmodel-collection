# Generated from: c497c902-6e69-4406-82f7-b0e63234cc68.json
# Description: This process involves the verification and authentication of rare artworks being shipped internationally for exhibition or sale. It combines expertise in provenance research, physical inspection, chemical analysis, and legal compliance across multiple jurisdictions. Activities include initial artist verification, historical documentation gathering, pigment and material testing, fraud detection through AI pattern recognition, customs clearance coordination, and final certification issuance. The process ensures the artwork's authenticity, legality, and safe transit while mitigating risks associated with art forgery, smuggling, and international trade disputes, requiring collaboration between art historians, forensic scientists, legal experts, and logistics providers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
artist_check      = Transition(label='Artist Check')
provenance_scan   = Transition(label='Provenance Scan')
document_review   = Transition(label='Document Review')
material_test     = Transition(label='Material Test')
pigment_analysis  = Transition(label='Pigment Analysis')
pattern_detect    = Transition(label='Pattern Detect')
fraud_screening   = Transition(label='Fraud Screening')
legal_compliance  = Transition(label='Legal Compliance')
customs_liaison   = Transition(label='Customs Liaison')
transport_plan    = Transition(label='Transport Plan')
insurance_setup   = Transition(label='Insurance Setup')
condition_report  = Transition(label='Condition Report')
exhibition_prep   = Transition(label='Exhibition Prep')
final_certify     = Transition(label='Final Certify')
stakeholder_notify= Transition(label='Stakeholder Notify')

# Loop for legal compliance with possible re-document-review
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[legal_compliance, document_review]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    artist_check,
    provenance_scan,
    document_review,
    material_test,
    pigment_analysis,
    pattern_detect,
    fraud_screening,
    loop,
    customs_liaison,
    transport_plan,
    insurance_setup,
    condition_report,
    exhibition_prep,
    final_certify,
    stakeholder_notify
])

# Define the control‐flow (partial order)
root.order.add_edge(artist_check,      provenance_scan)
root.order.add_edge(artist_check,      document_review)
root.order.add_edge(provenance_scan,   material_test)
root.order.add_edge(document_review,   material_test)
root.order.add_edge(material_test,     pigment_analysis)
root.order.add_edge(material_test,     pattern_detect)
root.order.add_edge(pigment_analysis,  fraud_screening)
root.order.add_edge(pattern_detect,    fraud_screening)
root.order.add_edge(fraud_screening,   loop)
root.order.add_edge(loop,              customs_liaison)
root.order.add_edge(customs_liaison,   transport_plan)
root.order.add_edge(customs_liaison,   insurance_setup)
root.order.add_edge(transport_plan,    condition_report)
root.order.add_edge(insurance_setup,   condition_report)
root.order.add_edge(condition_report,  exhibition_prep)
root.order.add_edge(exhibition_prep,   final_certify)
root.order.add_edge(final_certify,     stakeholder_notify)