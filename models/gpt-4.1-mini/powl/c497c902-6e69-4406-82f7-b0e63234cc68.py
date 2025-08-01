# Generated from: c497c902-6e69-4406-82f7-b0e63234cc68.json
# Description: This process involves the verification and authentication of rare artworks being shipped internationally for exhibition or sale. It combines expertise in provenance research, physical inspection, chemical analysis, and legal compliance across multiple jurisdictions. Activities include initial artist verification, historical documentation gathering, pigment and material testing, fraud detection through AI pattern recognition, customs clearance coordination, and final certification issuance. The process ensures the artwork's authenticity, legality, and safe transit while mitigating risks associated with art forgery, smuggling, and international trade disputes, requiring collaboration between art historians, forensic scientists, legal experts, and logistics providers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions with the exact labels
Artist_Check = Transition(label='Artist Check')
Provenance_Scan = Transition(label='Provenance Scan')
Document_Review = Transition(label='Document Review')
Material_Test = Transition(label='Material Test')
Pigment_Analysis = Transition(label='Pigment Analysis')
Pattern_Detect = Transition(label='Pattern Detect')
Fraud_Screening = Transition(label='Fraud Screening')
Legal_Compliance = Transition(label='Legal Compliance')
Customs_Liaison = Transition(label='Customs Liaison')
Transport_Plan = Transition(label='Transport Plan')
Condition_Report = Transition(label='Condition Report')
Insurance_Setup = Transition(label='Insurance Setup')
Exhibition_Prep = Transition(label='Exhibition Prep')
Final_Certify = Transition(label='Final Certify')
Stakeholder_Notify = Transition(label='Stakeholder Notify')

# Model provenance research: Artist_Check then Provenance_Scan then Document_Review
provenance_research = StrictPartialOrder(nodes=[Artist_Check, Provenance_Scan, Document_Review])
provenance_research.order.add_edge(Artist_Check, Provenance_Scan)
provenance_research.order.add_edge(Provenance_Scan, Document_Review)

# Model physical inspection: Material_Test and Pigment_Analysis concurrent, both before Condition_Report
physical_inspection = StrictPartialOrder(nodes=[Material_Test, Pigment_Analysis, Condition_Report])
physical_inspection.order.add_edge(Material_Test, Condition_Report)
physical_inspection.order.add_edge(Pigment_Analysis, Condition_Report)

# Model fraud detection: Pattern_Detect then Fraud_Screening
fraud_detection = StrictPartialOrder(nodes=[Pattern_Detect, Fraud_Screening])
fraud_detection.order.add_edge(Pattern_Detect, Fraud_Screening)

# Legal and logistics partial order: Legal_Compliance then Customs_Liaison then Transport_Plan
legal_logistics = StrictPartialOrder(nodes=[Legal_Compliance, Customs_Liaison, Transport_Plan])
legal_logistics.order.add_edge(Legal_Compliance, Customs_Liaison)
legal_logistics.order.add_edge(Customs_Liaison, Transport_Plan)

# Insurance and exhibition preparation concurrent (both depend on Condition_Report and Transport_Plan)
insurance_and_exhibition = StrictPartialOrder(nodes=[Insurance_Setup, Exhibition_Prep, Stakeholder_Notify])
# Insurance_Setup and Exhibition_Prep can proceed concurrently, both before Stakeholder_Notify
insurance_and_exhibition.order.add_edge(Insurance_Setup, Stakeholder_Notify)
insurance_and_exhibition.order.add_edge(Exhibition_Prep, Stakeholder_Notify)

# Final certification depends on Condition_Report, Fraud_Screening, and Customs_Liaison
final_certify_partial = StrictPartialOrder(
    nodes=[Condition_Report, Fraud_Screening, Customs_Liaison, Final_Certify])
final_certify_partial.order.add_edge(Condition_Report, Final_Certify)
final_certify_partial.order.add_edge(Fraud_Screening, Final_Certify)
final_certify_partial.order.add_edge(Customs_Liaison, Final_Certify)

# Build the root partial order combining all major components
root_nodes = [provenance_research, physical_inspection, fraud_detection,
              legal_logistics, insurance_and_exhibition, final_certify_partial]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges to represent flow/dependencies between the subprocesses

# Provenance research completes before physical inspection and fraud detection start
root.order.add_edge(provenance_research, physical_inspection)
root.order.add_edge(provenance_research, fraud_detection)

# Physical inspection and fraud detection complete before final certification
root.order.add_edge(physical_inspection, final_certify_partial)
root.order.add_edge(fraud_detection, final_certify_partial)

# Legal and logistics complete before final certification
root.order.add_edge(legal_logistics, final_certify_partial)

# Final certification precedes insurance setup and exhibition prep
root.order.add_edge(final_certify_partial, insurance_and_exhibition)

# Transport plan (in legal_logistics) must complete before insurance and exhibition prep start
root.order.add_edge(legal_logistics, insurance_and_exhibition)

# Stakeholder notify is last, depends on insurance and exhibition prep (already ordered within that subprocess)
# No edge needed here; stakeholder_notify is inside insurance_and_exhibition and happens last there
