# Generated from: 129b15ef-2c87-4ea5-aa94-70cfa1e11b4d.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts brought in by collectors or museums. It involves initial inspection, provenance research, scientific testing, expert consultation, and final certification. The workflow ensures that each item undergoes rigorous validation combining physical examination and digital verification methods, including spectral analysis and blockchain tracking, to prevent forgery and establish authenticity before public or private acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
ItemIntake = Transition(label='Item Intake')
VisualScan = Transition(label='Visual Scan')
ProvenanceCheck = Transition(label='Provenance Check')
HistoricalReview = Transition(label='Historical Review')
MaterialSampling = Transition(label='Material Sampling')
SpectralTest = Transition(label='Spectral Test')
DatabaseMatch = Transition(label='Database Match')
ExpertReview = Transition(label='Expert Review')
ForgeryAnalysis = Transition(label='Forgery Analysis')
DigitalScan = Transition(label='Digital Scan')
BlockchainLog = Transition(label='Blockchain Log')
ConditionReport = Transition(label='Condition Report')
CertificationPrep = Transition(label='Certification Prep')
FinalApproval = Transition(label='Final Approval')
ClientNotification = Transition(label='Client Notification')
ArchiveUpdate = Transition(label='Archive Update')

# Construct the partial orders based on the description:

# Initial inspection phase:
# Item Intake --> Visual Scan
initial_inspection = StrictPartialOrder(nodes=[ItemIntake, VisualScan])
initial_inspection.order.add_edge(ItemIntake, VisualScan)

# Provenance research branch: Provenance Check --> Historical Review
provenance_research = StrictPartialOrder(nodes=[ProvenanceCheck, HistoricalReview])
provenance_research.order.add_edge(ProvenanceCheck, HistoricalReview)

# Scientific testing branch:
# Material Sampling --> Spectral Test (physical testing order)
physical_testing = StrictPartialOrder(nodes=[MaterialSampling, SpectralTest])
physical_testing.order.add_edge(MaterialSampling, SpectralTest)

# Digital verification branch:
# Digital Scan --> Blockchain Log
digital_verification = StrictPartialOrder(nodes=[DigitalScan, BlockchainLog])
digital_verification.order.add_edge(DigitalScan, BlockchainLog)

# Database matching can happen after blockchain log
db_and_analysis = StrictPartialOrder(nodes=[digital_verification, DatabaseMatch, ForgeryAnalysis])
db_and_analysis.order.add_edge(digital_verification, DatabaseMatch)
db_and_analysis.order.add_edge(DatabaseMatch, ForgeryAnalysis)

# Expert review after provenance and scientific testing and digital verification + forgery analysis
# Combine provenance research + physical testing + db_and_analysis all must precede Expert Review
# Since StrictPartialOrder nodes must be a flat list and edges connect nodes, we merge nodes but keep edges
expert_review_prelude_nodes = [
    provenance_research, physical_testing, db_and_analysis, ExpertReview
]

# In partial order, to enforce provenance_research, physical_testing, and db_and_analysis to happen before expert review,
# we add edges from each root node in those to ExpertReview.

expert_review_partial = StrictPartialOrder(nodes=expert_review_prelude_nodes)
expert_review_partial.order.add_edge(provenance_research, ExpertReview)
expert_review_partial.order.add_edge(physical_testing, ExpertReview)
expert_review_partial.order.add_edge(db_and_analysis, ExpertReview)

# Condition report and certification prep after expert review
cond_cert_nodes = [ConditionReport, CertificationPrep]
cond_cert = StrictPartialOrder(nodes=cond_cert_nodes)
cond_cert.order.add_edge(ConditionReport, CertificationPrep)

# Final approval after certification prep
final_approval_nodes = [CertificationPrep, FinalApproval]
final_approval = StrictPartialOrder(nodes=final_approval_nodes)
final_approval.order.add_edge(CertificationPrep, FinalApproval)

# Client notification and archive update in parallel after final approval
client_archive_nodes = [ClientNotification, ArchiveUpdate]

client_archive = StrictPartialOrder(nodes=client_archive_nodes)
# no order edges => concurrent

# Compose last steps: final_approval --> (client notification and archive update parallel)
last_steps = StrictPartialOrder(nodes=[final_approval, client_archive])
last_steps.order.add_edge(final_approval, client_archive)

# Now combine all main phases:
# initial inspection --> expert review partial --> cond_cert --> final approval steps
main_nodes = [
    initial_inspection,
    VisualScan, # Visual Scan is node inside initial_inspection, but we used initial_inspection as a node
    expert_review_partial,
    cond_cert,
    last_steps
]

# initial_inspection already contains VisualScan, so no need to include VisualScan separately
# So nodes are initial_inspection, expert_review_partial, cond_cert, last_steps

root = StrictPartialOrder(nodes=[initial_inspection, expert_review_partial, cond_cert, last_steps])
# Add order edges describing the sequence:

root.order.add_edge(initial_inspection, expert_review_partial)
root.order.add_edge(expert_review_partial, cond_cert)
root.order.add_edge(cond_cert, last_steps)