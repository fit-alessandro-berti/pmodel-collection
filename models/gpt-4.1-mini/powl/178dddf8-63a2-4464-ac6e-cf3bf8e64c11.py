# Generated from: 178dddf8-63a2-4464-ac6e-cf3bf8e64c11.json
# Description: This process involves the meticulous authentication and provenance verification of rare artifacts within a decentralized consortium of museums and private collectors. It begins with initial artifact intake and preliminary inspection, followed by multi-source historical data aggregation including archival documents, expert opinions, and scientific testing results. The process includes blockchain registration for immutable provenance records, advanced material composition analysis using spectrometry, and AI-driven stylistic comparison against established artifact databases. Discrepancies trigger a collaborative review session among curators and historians before final certification. Post-authentication, the artifact’s digital twin is created and integrated into a virtual exhibit platform, enabling real-time condition monitoring and public accessibility while ensuring ongoing provenance validation through periodic re-assessment cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
PrelimInspect = Transition(label='Prelim Inspect')

DataAggregation = Transition(label='Data Aggregation')
ArchiveReview = Transition(label='Archive Review')
ExpertConsult = Transition(label='Expert Consult')
MaterialTest = Transition(label='Material Test')

SpectrometryScan = Transition(label='Spectrometry Scan')
StyleCompare = Transition(label='Style Compare')

BlockchainEntry = Transition(label='Blockchain Entry')

DiscrepancyFlag = Transition(label='Discrepancy Flag')
ReviewSession = Transition(label='Review Session')

FinalCertify = Transition(label='Final Certify')

DigitalTwin = Transition(label='Digital Twin')
ExhibitUpload = Transition(label='Exhibit Upload')
ConditionMonitor = Transition(label='Condition Monitor')

PeriodicAudit = Transition(label='Periodic Audit')

# Data Aggregation partial order among the three parallel activities
data_agg_po = StrictPartialOrder(nodes=[ArchiveReview, ExpertConsult, MaterialTest])
# No order edges among these three, so fully concurrent inside aggregation

# After Data Aggregation is done, Spectrometry Scan and Style Compare can start in parallel
# But Spectrometry Scan depends on Material Test (scientific testing results -> spectrometry)
# Style Compare is after Expert Consult (AI stylistic comparison against database)
# We assume Spectrometry Scan depends on MaterialTest
# Style Compare depends on ExpertConsult
# ArchiveReview is another input to Data Aggregation with no dependency to spectrometry/style compare

# So we create a partial order for 'DataAggregation' expanded:
# DataAggregation first (this is a single transition), then parallel:

#   ArchiveReview, ExpertConsult, MaterialTest (concurrent)
# Then SpectrometryScan depends on MaterialTest
# StyleCompare depends on ExpertConsult

# To model this cleanly, we embed `DataAggregation --> PO(ArchiveReview, ExpertConsult, MaterialTest)`
# Then order edges from MaterialTest-->SpectrometryScan and ExpertConsult-->StyleCompare.

# Representing Data Aggregation and the 3 concurrent reviews/tests as a partial order:

data_agg_branch = StrictPartialOrder(
    nodes=[DataAggregation, ArchiveReview, ExpertConsult, MaterialTest, SpectrometryScan, StyleCompare]
)
data_agg_branch.order.add_edge(DataAggregation, ArchiveReview)
data_agg_branch.order.add_edge(DataAggregation, ExpertConsult)
data_agg_branch.order.add_edge(DataAggregation, MaterialTest)

data_agg_branch.order.add_edge(MaterialTest, SpectrometryScan)
data_agg_branch.order.add_edge(ExpertConsult, StyleCompare)
# ArchiveReview has no further dependencies

# After Data Aggregation branch, blockchain registration:

# Blockchain Entry after Data Aggregation branch:
blockchain_and_analysis = StrictPartialOrder(
    nodes=[data_agg_branch, BlockchainEntry]
)
blockchain_and_analysis.order.add_edge(data_agg_branch, BlockchainEntry)

# Next, check discrepancy: if discrepancy flagged then Review Session then Final Certify
# else direct Final Certify

discrepancy_choice = OperatorPOWL(operator=Operator.XOR, children=[StrictPartialOrder(nodes=[DiscrepancyFlag, ReviewSession]), StrictPartialOrder(nodes=[])])
# Empty strict partial order for no-discrepancy branch (skip)

# After discrepancy choice, Final Certify always

final_certify_branch = StrictPartialOrder(nodes=[discrepancy_choice, FinalCertify])
final_certify_branch.order.add_edge(discrepancy_choice, FinalCertify)

# So, after blockchain entry proceed to discrepancy check and final certify

blockchain_to_certify = StrictPartialOrder(
    nodes=[blockchain_and_analysis, final_certify_branch]
)
blockchain_to_certify.order.add_edge(blockchain_and_analysis, final_certify_branch)

# After Final Certify, create Digital Twin and Exhibit Upload concurrently
digital_exhibit = StrictPartialOrder(nodes=[DigitalTwin, ExhibitUpload])
# no order edge: concurrent

# Monitoring and periodic audit run as a loop after DigitalTwin and ExhibitUpload are done
# We represent the loop as:
# loop = *(post_auth, periodic_audit)
# post_auth = StrictPartialOrder(nodes=[DigitalTwin, ExhibitUpload])
# periodic_audit = StrictPartialOrder(nodes=[ConditionMonitor, PeriodicAudit])
# with loop children = [post_auth, periodic_audit]

post_auth = digital_exhibit
periodic_audit = StrictPartialOrder(nodes=[ConditionMonitor, PeriodicAudit])
periodic_audit.order.add_edge(ConditionMonitor, PeriodicAudit)

loop = OperatorPOWL(operator=Operator.LOOP, children=[post_auth, periodic_audit])

# Build the entire process partial order:

root = StrictPartialOrder(
    nodes=[ArtifactIntake, PrelimInspect, blockchain_to_certify, loop]
)
root.order.add_edge(ArtifactIntake, PrelimInspect)
root.order.add_edge(PrelimInspect, blockchain_to_certify)
root.order.add_edge(blockchain_to_certify, loop)