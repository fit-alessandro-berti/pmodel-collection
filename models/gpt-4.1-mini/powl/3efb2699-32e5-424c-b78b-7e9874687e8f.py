# Generated from: 3efb2699-32e5-424c-b78b-7e9874687e8f.json
# Description: This process involves the intricate steps required to authenticate and verify the provenance of rare historical artifacts. It includes multidisciplinary expert consultations, chemical composition analysis, provenance chain reconstruction, condition assessment, and advanced imaging techniques. The process aims to ensure the artifact's legitimacy, historical value, and legal ownership by integrating scientific, historical, and legal evaluations before final certification and cataloging for auction or museum acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
PreliminaryScan = Transition(label='Preliminary Scan')
ExpertConsult = Transition(label='Expert Consult')
MaterialTesting = Transition(label='Material Testing')
ProvenanceCheck = Transition(label='Provenance Check')
ConditionReport = Transition(label='Condition Report')
ImagingCapture = Transition(label='Imaging Capture')
RadiocarbonTest = Transition(label='Radiocarbon Test')
ForgeryAnalysis = Transition(label='Forgery Analysis')
LegalReview = Transition(label='Legal Review')
OwnershipTrace = Transition(label='Ownership Trace')
HistoricalContext = Transition(label='Historical Context')
DataIntegration = Transition(label='Data Integration')
CertificationPrep = Transition(label='Certification Prep')
FinalApproval = Transition(label='Final Approval')
CatalogEntry = Transition(label='Catalog Entry')
AuctionNotify = Transition(label='Auction Notify')

# Define Scientific Analysis partial order:
# (Material Testing, Radiocarbon Test, Forgery Analysis) concurrent,
# all must happen after Expert Consult (which happens after Preliminary Scan)
scientific_analysis = StrictPartialOrder(nodes=[MaterialTesting, RadiocarbonTest, ForgeryAnalysis])
# no edges inside scientific analysis, these three are concurrent

# Define Historical & Legal Checks partial order:
# Provenance Check --> Ownership Trace and Historical Context concurrent
# Ownership Trace and Historical Context after Provenance Check
historical_legal_checks = StrictPartialOrder(
    nodes=[ProvenanceCheck, OwnershipTrace, HistoricalContext]
)
historical_legal_checks.order.add_edge(ProvenanceCheck, OwnershipTrace)
historical_legal_checks.order.add_edge(ProvenanceCheck, HistoricalContext)

# Condition Assessment and Imaging Capture concurrent nodes depend on Preliminary Scan
condition_imaging = StrictPartialOrder(nodes=[ConditionReport, ImagingCapture])
# No order edges - concurrent

# Now assemble the order
# Start with Artifact Intake --> Preliminary Scan
# Preliminary Scan --> Expert Consult
# Expert Consult --> Scientific Analysis
# Preliminary Scan --> Condition & Imaging (these two concur after Preliminary Scan)
# After Scientific Analysis and Historical & Legal Checks and Condition/Imaging done,
# Data Integration proceeds.

# Historical & Legal Checks start after Provenance Check, which depends on Material Testing (material testing part of scientific)
# However, ProvenanceCheck is not explicitly dependent on MaterialTesting in description
# Will assume ProvenanceCheck concurrent after Expert Consult (same level as Scientific Analysis)
# or maybe better: ProvenanceCheck depends on Expert Consult too.

# Legal Review depends on Ownership Trace and Forgery Analysis (Forgery part of Scientific Analysis)
# Final Approval after Certification Prep, after Data Integration and Legal Review
# Certification Prep after Data Integration
# Catalog Entry after Final Approval
# Auction Notify concurrent with Catalog Entry

# Create higher-level partial orders for the branches after Expert Consult:

# Scientific + HistoricalLegal + ConditionImaging are concurrent after Expert Consult,
# so create PO with these three partial orders as nodes

# Wrap Scientific Analysis as a POWL node
# Same for HistoricalLegalChecks and ConditionImaging

# For Legal Review dependency: depends on OwnershipTrace and ForgeryAnalysis
# OwnershipTrace in Historical legal, ForgeryAnalysis in Scientific analysis
# So we need to pick these nodes and direct edges accordingly.

# Start building from bottom up:

# Merge Scientific Analysis and Historical & Legal Checks and Condition + Imaging as one big PO with edges between relevant nodes

# First define all nodes to include inside main PO
nodes_main = [
    ArtifactIntake,
    PreliminaryScan,
    ExpertConsult,
    MaterialTesting,
    RadiocarbonTest,
    ForgeryAnalysis,
    ProvenanceCheck,
    OwnershipTrace,
    HistoricalContext,
    ConditionReport,
    ImagingCapture,
    LegalReview,
    DataIntegration,
    CertificationPrep,
    FinalApproval,
    CatalogEntry,
    AuctionNotify
]

root = StrictPartialOrder(nodes=nodes_main)

# Add base linear order: Artifact Intake --> Preliminary Scan --> Expert Consult
root.order.add_edge(ArtifactIntake, PreliminaryScan)
root.order.add_edge(PreliminaryScan, ExpertConsult)

# After Expert Consult, three concurrent branches start:

# Scientific Analysis branch: Material Testing, Radiocarbon Test, Forgery Analysis concurrent
# All after Expert Consult
root.order.add_edge(ExpertConsult, MaterialTesting)
root.order.add_edge(ExpertConsult, RadiocarbonTest)
root.order.add_edge(ExpertConsult, ForgeryAnalysis)

# Historical & Legal Checks branch: Provenance Check after Expert Consult
root.order.add_edge(ExpertConsult, ProvenanceCheck)

# Ownership Trace and Historical Context after Provenance Check
root.order.add_edge(ProvenanceCheck, OwnershipTrace)
root.order.add_edge(ProvenanceCheck, HistoricalContext)

# Condition Assessment and Imaging Capture concurrent after Preliminary Scan
root.order.add_edge(PreliminaryScan, ConditionReport)
root.order.add_edge(PreliminaryScan, ImagingCapture)

# Legal Review depends on Ownership Trace and Forgery Analysis
# thus edges from OwnershipTrace and ForgeryAnalysis to LegalReview
root.order.add_edge(OwnershipTrace, LegalReview)
root.order.add_edge(ForgeryAnalysis, LegalReview)

# Data Integration depends on completion of:
# - Scientific branch (Material Testing, Radiocarbon Test, Forgery Analysis)
# - Historical & Legal Checks branch (Provenance Check chain)
# - ConditionReport and ImagingCapture
# So add edges from all terminal nodes of these branches to DataIntegration:

# Material Testing, Radiocarbon Test are terminal in scientific analysis branch except ForgeryAnalysis (which leads to LegalReview)
# LegalReview is after ForgeryAnalysis and OwnershipTrace
root.order.add_edge(MaterialTesting, DataIntegration)
root.order.add_edge(RadiocarbonTest, DataIntegration)
root.order.add_edge(LegalReview, DataIntegration)

# HistoricalContext and OwnershipTrace lead to LegalReview or DataIntegration
# OwnershipTrace leads to LegalReview, add edge from HistoricalContext directly to DataIntegration
root.order.add_edge(HistoricalContext, DataIntegration)

# ConditionReport and ImagingCapture lead to DataIntegration
root.order.add_edge(ConditionReport, DataIntegration)
root.order.add_edge(ImagingCapture, DataIntegration)

# Certification Prep after Data Integration
root.order.add_edge(DataIntegration, CertificationPrep)

# Final Approval after Certification Prep
root.order.add_edge(CertificationPrep, FinalApproval)

# Catalog Entry after Final Approval
root.order.add_edge(FinalApproval, CatalogEntry)

# Auction Notify concurrent with Catalog Entry (no edge between them)

# No edge between Auction Notify and Catalog Entry means concurrent, but we need Auction Notify after Final Approval logically
root.order.add_edge(FinalApproval, AuctionNotify)

# Final model is root
