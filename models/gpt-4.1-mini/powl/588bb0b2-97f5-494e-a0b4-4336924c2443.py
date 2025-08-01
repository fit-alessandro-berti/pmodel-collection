# Generated from: 588bb0b2-97f5-494e-a0b4-4336924c2443.json
# Description: This process involves the complex validation and authentication of ancient artifacts within a museum's acquisition department. It includes steps such as provenance verification, material analysis, historical context research, and expert consultations. The workflow ensures that every artifact undergoes rigorous scrutiny before being approved for display or storage, considering both scientific and historical perspectives. The process integrates cross-disciplinary collaboration, digital record updates, and compliance with international cultural heritage laws, culminating in a final authentication report and database entry.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
InitialInspection = Transition(label='Initial Inspection')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialSampling = Transition(label='Material Sampling')
LabAnalysis = Transition(label='Lab Analysis')
HistoricalResearch = Transition(label='Historical Research')
ExpertReview = Transition(label='Expert Review')
ConditionAssessment = Transition(label='Condition Assessment')
DigitalImaging = Transition(label='Digital Imaging')
CrossReference = Transition(label='Cross-Reference')
LegalCompliance = Transition(label='Legal Compliance')
ReportDrafting = Transition(label='Report Drafting')
StakeholderMeeting = Transition(label='Stakeholder Meeting')
FinalApproval = Transition(label='Final Approval')
DatabaseEntry = Transition(label='Database Entry')
StorageAllocation = Transition(label='Storage Allocation')
ExhibitPlanning = Transition(label='Exhibit Planning')

# Provenance, Material, Historical branch (concurrent)
# MaterialSampling -> LabAnalysis
material_PO = StrictPartialOrder(nodes=[MaterialSampling, LabAnalysis])
material_PO.order.add_edge(MaterialSampling, LabAnalysis)

# HistoricalResearch (independent)

# Build the validation partial order (provenance + material + historical)
validation_PO = StrictPartialOrder(nodes=[ProvenanceCheck, material_PO, HistoricalResearch])
validation_PO.order.add_edge(ProvenanceCheck, material_PO)
validation_PO.order.add_edge(ProvenanceCheck, HistoricalResearch)

# ExpertReview depends on all validation activities
expert_review_PO = StrictPartialOrder(nodes=[validation_PO, ExpertReview])
expert_review_PO.order.add_edge(validation_PO, ExpertReview)

# ConditionAssessment and DigitalImaging concurrently, after InitialInspection
inspection_PO = StrictPartialOrder(nodes=[InitialInspection, ConditionAssessment, DigitalImaging])
inspection_PO.order.add_edge(InitialInspection, ConditionAssessment)
inspection_PO.order.add_edge(InitialInspection, DigitalImaging)

# CrossReference depends on DigitalImaging and ExpertReview
crossref_PO = StrictPartialOrder(nodes=[DigitalImaging, ExpertReview, CrossReference])
crossref_PO.order.add_edge(DigitalImaging, CrossReference)
crossref_PO.order.add_edge(ExpertReview, CrossReference)

# LegalCompliance after CrossReference
legal_PO = StrictPartialOrder(nodes=[CrossReference, LegalCompliance])
legal_PO.order.add_edge(CrossReference, LegalCompliance)

# ReportDrafting after LegalCompliance and ConditionAssessment
report_PO = StrictPartialOrder(nodes=[LegalCompliance, ConditionAssessment, ReportDrafting])
report_PO.order.add_edge(LegalCompliance, ReportDrafting)
report_PO.order.add_edge(ConditionAssessment, ReportDrafting)

# StakeholderMeeting after ReportDrafting
stakeholder_PO = StrictPartialOrder(nodes=[ReportDrafting, StakeholderMeeting])
stakeholder_PO.order.add_edge(ReportDrafting, StakeholderMeeting)

# FinalApproval after StakeholderMeeting
approval_PO = StrictPartialOrder(nodes=[StakeholderMeeting, FinalApproval])
approval_PO.order.add_edge(StakeholderMeeting, FinalApproval)

# DatabaseEntry after FinalApproval
database_PO = StrictPartialOrder(nodes=[FinalApproval, DatabaseEntry])
database_PO.order.add_edge(FinalApproval, DatabaseEntry)

# StorageAllocation and ExhibitPlanning concurrently after DatabaseEntry
storage_exhibit_PO = StrictPartialOrder(nodes=[DatabaseEntry, StorageAllocation, ExhibitPlanning])
storage_exhibit_PO.order.add_edge(DatabaseEntry, StorageAllocation)
storage_exhibit_PO.order.add_edge(DatabaseEntry, ExhibitPlanning)

# Combine all parts in order:
# ArtifactIntake -> InitialInspection -> (inspection_PO's ConditionAssessment and DigitalImaging included) and 
# validation_PO: ProvenanceCheck etc. all before ExpertReview and so on.

# Because InitialInspection feeds into inspection_PO, but inspection_PO includes InitialInspection itself,
# we build order accordingly.

# First, Initial part: Artifact Intake -> Initial Inspection
start_PO = StrictPartialOrder(nodes=[ArtifactIntake, InitialInspection])
start_PO.order.add_edge(ArtifactIntake, InitialInspection)

# Combine start_PO and validation_PO and expert_review_PO and inspection_PO and crossref_PO and legal_PO and further

# Let's integrate inspection_PO after InitialInspection:
# inspection_PO nodes: InitialInspection, ConditionAssessment, DigitalImaging
# start_PO already has InitialInspection. So merge ConditionAssessment and DigitalImaging after InitialInspection.

# We'll create one big PO with all nodes and edges.

nodes_all = [
    ArtifactIntake,
    InitialInspection,
    ProvenanceCheck,
    MaterialSampling,
    LabAnalysis,
    HistoricalResearch,
    ExpertReview,
    ConditionAssessment,
    DigitalImaging,
    CrossReference,
    LegalCompliance,
    ReportDrafting,
    StakeholderMeeting,
    FinalApproval,
    DatabaseEntry,
    StorageAllocation,
    ExhibitPlanning,
]

root = StrictPartialOrder(nodes=nodes_all)

# Add order edges

# Artifact Intake --> Initial Inspection
root.order.add_edge(ArtifactIntake, InitialInspection)

# Initial Inspection --> Condition Assessment and Digital Imaging
root.order.add_edge(InitialInspection, ConditionAssessment)
root.order.add_edge(InitialInspection, DigitalImaging)

# Artifact Intake --> Provenance Check (we assume provenance can start after intake concurrently with inspection)
root.order.add_edge(ArtifactIntake, ProvenanceCheck)

# Provenance Check --> Material Sampling and Historical Research
root.order.add_edge(ProvenanceCheck, MaterialSampling)
root.order.add_edge(ProvenanceCheck, HistoricalResearch)

# Material Sampling --> Lab Analysis
root.order.add_edge(MaterialSampling, LabAnalysis)

# After all validation steps (ProvenanceCheck, LabAnalysis, HistoricalResearch) --> Expert Review
# So ExpertReview depends on:
root.order.add_edge(ProvenanceCheck, ExpertReview)
root.order.add_edge(LabAnalysis, ExpertReview)
root.order.add_edge(HistoricalResearch, ExpertReview)

# Expert Review and Digital Imaging must finish before Cross Reference
root.order.add_edge(ExpertReview, CrossReference)
root.order.add_edge(DigitalImaging, CrossReference)

# Cross Reference --> Legal Compliance
root.order.add_edge(CrossReference, LegalCompliance)

# Legal Compliance and Condition Assessment --> Report Drafting
root.order.add_edge(LegalCompliance, ReportDrafting)
root.order.add_edge(ConditionAssessment, ReportDrafting)

# Report Drafting --> Stakeholder Meeting
root.order.add_edge(ReportDrafting, StakeholderMeeting)

# Stakeholder Meeting --> Final Approval
root.order.add_edge(StakeholderMeeting, FinalApproval)

# Final Approval --> Database Entry
root.order.add_edge(FinalApproval, DatabaseEntry)

# Database Entry --> Storage Allocation and Exhibit Planning (concurrent)
root.order.add_edge(DatabaseEntry, StorageAllocation)
root.order.add_edge(DatabaseEntry, ExhibitPlanning)