# Generated from: d06f813d-3ddc-4677-bbb0-504bf9218be7.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition. It begins with initial provenance research, followed by multi-disciplinary scientific testing including spectroscopy and radiocarbon dating. Expert consultations and forensic analysis are conducted to verify authenticity, while legal checks ensure clear ownership. Parallelly, risk assessment and insurance valuation take place. The process concludes with detailed documentation and final approval by the acquisition committee, ensuring the artifact's legitimacy and compliance with regulatory standards before procurement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
ProvenanceCheck = Transition(label='Provenance Check')
SpecimenSampling = Transition(label='Specimen Sampling')
SpectroscopyTest = Transition(label='Spectroscopy Test')
RadiocarbonDate = Transition(label='Radiocarbon Date')
MaterialAnalysis = Transition(label='Material Analysis')
ForensicReview = Transition(label='Forensic Review')
ExpertConsult = Transition(label='Expert Consult')
LegalVerify = Transition(label='Legal Verify')
OwnershipAudit = Transition(label='Ownership Audit')
RiskAssess = Transition(label='Risk Assess')
InsuranceQuote = Transition(label='Insurance Quote')
ConditionReport = Transition(label='Condition Report')
Documentation = Transition(label='Documentation')
CommitteeReview = Transition(label='Committee Review')
FinalApproval = Transition(label='Final Approval')

# Model scientific testing parallel activities:
# Specimen Sampling must be done before tests:
# Spectroscopy Test, Radiocarbon Date, Material Analysis run in parallel (partially ordered, no order between these three)
scientific_tests_PO = StrictPartialOrder(nodes=[SpectroscopyTest, RadiocarbonDate, MaterialAnalysis])
# no order edges between these 3: they run concurrently

# Forensic Review and Expert Consult are done in parallel (no stated order)
forensic_expert_PO = StrictPartialOrder(nodes=[ForensicReview, ExpertConsult])

# Legal checks: Legal Verify and Ownership Audit in parallel
legal_checks_PO = StrictPartialOrder(nodes=[LegalVerify, OwnershipAudit])

# Risk Assessment and Insurance Quote in parallel
risk_insurance_PO = StrictPartialOrder(nodes=[RiskAssess, InsuranceQuote])

# After provenance check:
# Specimen Sampling first, then scientific tests in parallel
sampling_and_tests_PO = StrictPartialOrder(
    nodes=[SpecimenSampling, scientific_tests_PO]
)
sampling_and_tests_PO.order.add_edge(SpecimenSampling, scientific_tests_PO)

# After scientific tests:
# Forensic and Expert in parallel (no order)
# Then legal checks and risk/insurance in parallel (these 4 activities cluster can be viewed as parallel groups)
# So after scientific_tests_PO finishes, forensic_expert_PO, legal_checks_PO, risk_insurance_PO run in parallel (no order among these three groups)
# We build a PO with nodes: forensic_expert_PO, legal_checks_PO, risk_insurance_PO, with no order edges among them
verif_checks_PO = StrictPartialOrder(
    nodes=[forensic_expert_PO, legal_checks_PO, risk_insurance_PO]
)
# no edges among them => parallel

# Create top level partial order:
# Provenance Check --> Specimen Sampling --> scientific_tests_PO --> verif_checks_PO --> Condition Report --> Documentation --> Committee Review --> Final Approval
root = StrictPartialOrder(nodes=[
    ProvenanceCheck,
    sampling_and_tests_PO,
    verif_checks_PO,
    ConditionReport,
    Documentation,
    CommitteeReview,
    FinalApproval
])

# Add sequential edges according to description
root.order.add_edge(ProvenanceCheck, sampling_and_tests_PO)
root.order.add_edge(sampling_and_tests_PO, verif_checks_PO)
root.order.add_edge(verif_checks_PO, ConditionReport)
root.order.add_edge(ConditionReport, Documentation)
root.order.add_edge(Documentation, CommitteeReview)
root.order.add_edge(CommitteeReview, FinalApproval)