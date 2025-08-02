# Generated from: 0717f3f8-3290-4100-b3e0-5784d793d3fb.json
# Description: This process involves the remote authentication of historical artifacts using a combination of advanced imaging, chemical analysis, and blockchain verification. Experts initiate a virtual inspection, coordinate with on-site technicians for sample collection, and utilize AI-driven pattern recognition to compare findings with known databases. Simultaneously, provenance records are cross-checked against decentralized ledgers to ensure authenticity and prevent forgery. The process concludes with a certified digital report generation and secure archival for future reference, involving multiple stakeholders across different geographic locations, ensuring traceability and transparency throughout the entire workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
InitiateInspection = Transition(label='Initiate Inspection')
ScheduleSample = Transition(label='Schedule Sample')
CollectData = Transition(label='Collect Data')
ImageCapture = Transition(label='Image Capture')
ChemicalScan = Transition(label='Chemical Scan')
AIAnalysis = Transition(label='AI Analysis')
PatternMatch = Transition(label='Pattern Match')
RecordCheck = Transition(label='Record Check')
LedgerVerify = Transition(label='Ledger Verify')
ExpertReview = Transition(label='Expert Review')
ReportDraft = Transition(label='Report Draft')
DigitalSign = Transition(label='Digital Sign')
ArchiveStore = Transition(label='Archive Store')
NotifyStakeholders = Transition(label='Notify Stakeholders')
CloseCase = Transition(label='Close Case')

# Construct the parallel partial orders inside the workflow:

# Branch 1: Advanced Imaging and Chemical Analysis branch:
# Schedule Sample -> Collect Data -> (Image Capture & Chemical Scan in parallel) -> AI Analysis -> Pattern Match
imaging_chemical_po = StrictPartialOrder(nodes=[ImageCapture, ChemicalScan])
# no order between ImageCapture and ChemicalScan => concurrent
imaging_chemical_po.order  # empty

ai_pattern_po = StrictPartialOrder(nodes=[AIAnalysis, PatternMatch])
ai_pattern_po.order.add_edge(AIAnalysis, PatternMatch)

branch1_po = StrictPartialOrder(nodes=[ScheduleSample, CollectData, imaging_chemical_po, ai_pattern_po])
branch1_po.order.add_edge(ScheduleSample, CollectData)
branch1_po.order.add_edge(CollectData, imaging_chemical_po)
branch1_po.order.add_edge(imaging_chemical_po, ai_pattern_po)

# Branch 2: Provenance records check branch:
# Record Check -> Ledger Verify (sequential)
provenance_po = StrictPartialOrder(nodes=[RecordCheck, LedgerVerify])
provenance_po.order.add_edge(RecordCheck, LedgerVerify)

# Both branches (branch1_po and provenance_po) run simultaneously after Initiate Inspection:
# root PO nodes: InitiateInspection -> branch1_po and InitiateInspection -> provenance_po

# After both branches complete, Expert Review happens
# Then flow to reporting partial order: Report Draft -> Digital Sign -> Archive Store -> Notify Stakeholders -> Close Case

reporting_nodes = [ReportDraft, DigitalSign, ArchiveStore, NotifyStakeholders, CloseCase]
reporting_po = StrictPartialOrder(nodes=reporting_nodes)
reporting_po.order.add_edge(ReportDraft, DigitalSign)
reporting_po.order.add_edge(DigitalSign, ArchiveStore)
reporting_po.order.add_edge(ArchiveStore, NotifyStakeholders)
reporting_po.order.add_edge(NotifyStakeholders, CloseCase)

# Compose the main PO: nodes are InitiateInspection,
# branch1_po, provenance_po, ExpertReview, reporting_po
ExpertReview_node = ExpertReview

root_nodes = [
    InitiateInspection,
    branch1_po,
    provenance_po,
    ExpertReview_node,
    reporting_po
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges:
# InitiateInspection first:
root.order.add_edge(InitiateInspection, branch1_po)
root.order.add_edge(InitiateInspection, provenance_po)
# both branches must complete before Expert Review:
root.order.add_edge(branch1_po, ExpertReview_node)
root.order.add_edge(provenance_po, ExpertReview_node)
# Expert Review before reporting_po
root.order.add_edge(ExpertReview_node, reporting_po)