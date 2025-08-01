# Generated from: b6f50622-e1bf-496e-bdbe-9490d85cc24c.json
# Description: This process involves the intricate verification and authentication of rare cultural artifacts sourced from multiple continents. It begins with initial provenance research, followed by scientific material analysis and expert consultation. The process requires coordinating with international regulatory bodies, performing forensic age dating, and executing advanced imaging techniques. After validation, artifact digitization and certification are carried out before final cataloging into a secure database. Throughout, legal compliance checks and ownership transfer protocols ensure legitimacy while mitigating risks of illicit trade. The process concludes with archival storage recommendations and stakeholder reporting to maintain transparency and integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ProvenanceCheck = Transition(label='Provenance Check')
MaterialAnalysis = Transition(label='Material Analysis')
ExpertReview = Transition(label='Expert Review')
RegulatoryLiaison = Transition(label='Regulatory Liaison')
AgeDating = Transition(label='Age Dating')
ImagingScan = Transition(label='Imaging Scan')
DigitalCapture = Transition(label='Digital Capture')
Certification = Transition(label='Certification')
DatabaseEntry = Transition(label='Database Entry')
ComplianceAudit = Transition(label='Compliance Audit')
OwnershipTransfer = Transition(label='Ownership Transfer')
RiskAssessment = Transition(label='Risk Assessment')
ArchivalPrep = Transition(label='Archival Prep')
StakeholderReport = Transition(label='Stakeholder Report')
FinalApproval = Transition(label='Final Approval')

# Step 1: Initial provenance research
# Step 2: scientific material analysis and expert consultation (MaterialAnalysis and ExpertReview can be partially concurrent after ProvenanceCheck)
# Step 3: coordinating with international regulatory bodies (RegulatoryLiaison),
# forensic age dating (AgeDating), and imaging techniques (ImagingScan)
# These three can be concurrent but after MaterialAnalysis and ExpertReview

# Step 4: After validation (which is the three above), then digitization and certification sequentially
# Step 5: final cataloging (DatabaseEntry)

# Throughout legal compliance checks and ownership transfer protocols ensure legitimacy:
# ComplianceAudit, OwnershipTransfer and RiskAssessment are concurrent and must happen before final approval

# Step 6: conclude with archival storage recommendations (ArchivalPrep) and stakeholder reporting (StakeholderReport)
# These two are concurrent and after final approval

# Step 7: final approval (FinalApproval) after compliance/ownership/risk and before archival + reporting

# Build partial orders accordingly

# Partial order1: ProvenanceCheck --> MaterialAnalysis and ExpertReview (both concurrent)
po1 = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialAnalysis, ExpertReview])
po1.order.add_edge(ProvenanceCheck, MaterialAnalysis)
po1.order.add_edge(ProvenanceCheck, ExpertReview)

# Partial order2: MaterialAnalysis and ExpertReview --> RegulatoryLiaison, AgeDating, ImagingScan (concurrent)
po2_nodes = [RegulatoryLiaison, AgeDating, ImagingScan]
po2 = StrictPartialOrder(nodes=po2_nodes)
# Add edges from both MaterialAnalysis and ExpertReview to these three activities
for src in [MaterialAnalysis, ExpertReview]:
    for tgt in po2_nodes:
        # We'll add the edges outside po2 as the strict PO only includes these nodes.

        # But po2 only includes these three nodes; edges from outside will be set in a higher PO

        # So for now po2 has no edges (all three concurrent)
        pass

# Partial Order representing the three tasks concurrently:
# We'll later link po1 to po2 with proper edges

# Partial order3: Digitization and Certification sequential after validation
po3 = StrictPartialOrder(nodes=[DigitalCapture, Certification])
po3.order.add_edge(DigitalCapture, Certification)

# Partial order4: DatabaseEntry after Certification
po4 = StrictPartialOrder(nodes=[Certification, DatabaseEntry])
po4.order.add_edge(Certification, DatabaseEntry)

# Partial order5: ComplianceAudit, OwnershipTransfer, RiskAssessment concurrent before final approval
po5 = StrictPartialOrder(nodes=[ComplianceAudit, OwnershipTransfer, RiskAssessment])

# FinalApproval after po5
# Partial order6: ArchivalPrep and StakeholderReport concurrent after FinalApproval
po6 = StrictPartialOrder(nodes=[ArchivalPrep, StakeholderReport])

# Assemble the large PO by combining and adding the correct edges to model all dependencies.

# The biggest partial order with all nodes
all_nodes = [
    po1,      # ProvenanceCheck, MaterialAnalysis, ExpertReview
    po2,      # RegulatoryLiaison, AgeDating, ImagingScan
    po3,      # DigitalCapture, Certification
    po4,      # Certification, DatabaseEntry
    po5,      # ComplianceAudit, OwnershipTransfer, RiskAssessment
    po6,      # ArchivalPrep, StakeholderReport
    FinalApproval
]

# We cannot directly nest partial orders, so we flatten nodes and create edges carefully.

# Collect all atomic transitions
all_transitions = [
    ProvenanceCheck,
    MaterialAnalysis,
    ExpertReview,
    RegulatoryLiaison,
    AgeDating,
    ImagingScan,
    DigitalCapture,
    Certification,
    DatabaseEntry,
    ComplianceAudit,
    OwnershipTransfer,
    RiskAssessment,
    ArchivalPrep,
    StakeholderReport,
    FinalApproval
]

root = StrictPartialOrder(nodes=all_transitions)

# Add edges according to described process:

# ProvenanceCheck --> MaterialAnalysis & ExpertReview
root.order.add_edge(ProvenanceCheck, MaterialAnalysis)
root.order.add_edge(ProvenanceCheck, ExpertReview)

# MaterialAnalysis & ExpertReview --> RegulatoryLiaison, AgeDating, ImagingScan (all three concurrent)
root.order.add_edge(MaterialAnalysis, RegulatoryLiaison)
root.order.add_edge(MaterialAnalysis, AgeDating)
root.order.add_edge(MaterialAnalysis, ImagingScan)
root.order.add_edge(ExpertReview, RegulatoryLiaison)
root.order.add_edge(ExpertReview, AgeDating)
root.order.add_edge(ExpertReview, ImagingScan)

# RegulatoryLiaison, AgeDating, ImagingScan --> DigitalCapture
root.order.add_edge(RegulatoryLiaison, DigitalCapture)
root.order.add_edge(AgeDating, DigitalCapture)
root.order.add_edge(ImagingScan, DigitalCapture)

# DigitalCapture --> Certification --> DatabaseEntry
root.order.add_edge(DigitalCapture, Certification)
root.order.add_edge(Certification, DatabaseEntry)

# ComplianceAudit, OwnershipTransfer, RiskAssessment all concurrent but all before FinalApproval
root.order.add_edge(ComplianceAudit, FinalApproval)
root.order.add_edge(OwnershipTransfer, FinalApproval)
root.order.add_edge(RiskAssessment, FinalApproval)

# DatabaseEntry --> ComplianceAudit (process states compliance & ownership proceed after cataloging)
root.order.add_edge(DatabaseEntry, ComplianceAudit)
root.order.add_edge(DatabaseEntry, OwnershipTransfer)
root.order.add_edge(DatabaseEntry, RiskAssessment)

# FinalApproval --> ArchivalPrep & StakeholderReport (concurrent)
root.order.add_edge(FinalApproval, ArchivalPrep)
root.order.add_edge(FinalApproval, StakeholderReport)