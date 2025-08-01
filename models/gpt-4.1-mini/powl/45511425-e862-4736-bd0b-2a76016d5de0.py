# Generated from: 45511425-e862-4736-bd0b-2a76016d5de0.json
# Description: This process involves verifying the authenticity of rare cultural artifacts sourced globally through a multi-layered approach combining scientific analysis, provenance research, and expert consultations. It begins with initial artifact intake and condition assessment, followed by advanced material composition testing and historical document cross-referencing. The process integrates blockchain registration for immutable provenance tracking and concludes with a final certification report issued to clients. Throughout, coordination with international regulatory bodies and ethical compliance reviews ensures that every artifact is legally and ethically validated before entering the market or museum collections, minimizing fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
MaterialTesting = Transition(label='Material Testing')
ProvenanceReview = Transition(label='Provenance Review')
ExpertConsult = Transition(label='Expert Consult')
DocumentAnalysis = Transition(label='Document Analysis')
BlockchainEntry = Transition(label='Blockchain Entry')
EthicsAudit = Transition(label='Ethics Audit')
LegalVerification = Transition(label='Legal Verification')
MarketScan = Transition(label='Market Scan')
RegulatorLiaison = Transition(label='Regulator Liaison')
ReportDraft = Transition(label='Report Draft')
ClientReview = Transition(label='Client Review')
FinalCertification = Transition(label='Final Certification')
ArchivalStorage = Transition(label='Archival Storage')

# Partial order for scientific analysis branch:
# Material Testing --> Document Analysis (implied by "advanced composition testing and historical document cross-referencing")
# plus Expert Consult is parallel with Document Analysis after Material Testing

scientific_PO = StrictPartialOrder(nodes=[MaterialTesting, DocumentAnalysis, ExpertConsult])
scientific_PO.order.add_edge(MaterialTesting, DocumentAnalysis)
scientific_PO.order.add_edge(MaterialTesting, ExpertConsult)

# Provenance branch: Provenance Review --> Blockchain Entry
provenance_PO = StrictPartialOrder(nodes=[ProvenanceReview, BlockchainEntry])
provenance_PO.order.add_edge(ProvenanceReview, BlockchainEntry)

# Regulatory and ethical compliance parallel activities:
# Ethics Audit and Legal Verification and Regulator Liaison and Market Scan are concurrent (all parallel)
compliance_PO = StrictPartialOrder(nodes=[EthicsAudit, LegalVerification, RegulatorLiaison, MarketScan])

# Initial phase: Artifact Intake --> Condition Check
initial_PO = StrictPartialOrder(nodes=[ArtifactIntake, ConditionCheck])
initial_PO.order.add_edge(ArtifactIntake, ConditionCheck)

# After Condition Check: run scientific_PO and provenance_PO and compliance_PO concurrently
# So we create a PO of the three nodes: scientific_PO, provenance_PO, compliance_PO concurrently without ordering edges
middle_PO = StrictPartialOrder(nodes=[scientific_PO, provenance_PO, compliance_PO])

# The process flow:
# initial_PO --> middle_PO --> reporting_PO

# Reporting sub-process:
# Report Draft --> Client Review --> Final Certification --> Archival Storage
reporting_PO = StrictPartialOrder(nodes=[ReportDraft, ClientReview, FinalCertification, ArchivalStorage])
reporting_PO.order.add_edge(ReportDraft, ClientReview)
reporting_PO.order.add_edge(ClientReview, FinalCertification)
reporting_PO.order.add_edge(FinalCertification, ArchivalStorage)

# Compose root PO with initial_PO --> middle_PO --> reporting_PO
root = StrictPartialOrder(nodes=[initial_PO, middle_PO, reporting_PO])
root.order.add_edge(initial_PO, middle_PO)
root.order.add_edge(middle_PO, reporting_PO)