# Generated from: 66c40d11-42a7-447f-8650-0d3b1b14359a.json
# Description: This process involves the complex validation and authentication of rare cultural artifacts sourced globally. It encompasses provenance research, multi-layered material analysis, expert consensus, and legal compliance verification. Each artifact undergoes detailed historical cross-referencing, advanced chemical testing, and digital imaging before final certification. The process also includes stakeholder coordination spanning archaeologists, legal advisors, and auction houses, ensuring authenticity, ethical acquisition, and traceability. Post-authentication, artifacts are cataloged with secure blockchain entries to prevent forgery, and continuous monitoring for ownership disputes is maintained, integrating international regulatory updates and client feedback loops.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions with given labels
ArtifactIntake = Transition(label='Artifact Intake')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
HistoricalMatch = Transition(label='Historical Match')
ExpertReview = Transition(label='Expert Review')
LegalVerify = Transition(label='Legal Verify')
ImagingCapture = Transition(label='Imaging Capture')
ChemicalTest = Transition(label='Chemical Test')
ConsensusVote = Transition(label='Consensus Vote')
BlockchainLog = Transition(label='Blockchain Log')
OwnershipAudit = Transition(label='Ownership Audit')
EthicsReview = Transition(label='Ethics Review')
MarketAnalysis = Transition(label='Market Analysis')
ClientUpdate = Transition(label='Client Update')
DisputeMonitor = Transition(label='Dispute Monitor')
RegulationSync = Transition(label='Regulation Sync')

# Build provenance+material validation+authentication sub partial order:
# Provenance Research includes Provenance Check and Historical Match (likely sequential)
# Material Analysis includes Material Scan and Chemical Test (sequential)
# Authentication includes Expert Review, Consensus Vote, Legal Verify (partial order with some concurrency possible)
# Imaging Capture concurrent with Chemical Test or after? It's part of detailed testing, so we put it after MaterialScan, concurrent with ChemicalTest.

# HistoricalMatch is part of provenance research, so order: ProvenanceCheck --> HistoricalMatch
provenance_po = StrictPartialOrder(nodes=[ProvenanceCheck, HistoricalMatch])
provenance_po.order.add_edge(ProvenanceCheck, HistoricalMatch)

# MaterialScan --> ChemicalTest
material_po = StrictPartialOrder(nodes=[MaterialScan, ChemicalTest])
material_po.order.add_edge(MaterialScan, ChemicalTest)

# ImagingCapture can happen after MaterialScan and probably concurrently with ChemicalTest
imaging_po = StrictPartialOrder(nodes=[MaterialScan, ImagingCapture])
imaging_po.order.add_edge(MaterialScan, ImagingCapture)

# Combine material_po and imaging_po into combined material analysis:
mat_nodes = [MaterialScan, ChemicalTest, ImagingCapture]
mat_po = StrictPartialOrder(nodes=mat_nodes)
mat_po.order.add_edge(MaterialScan, ChemicalTest)
mat_po.order.add_edge(MaterialScan, ImagingCapture)
# ChemicalTest and ImagingCapture are concurrent (no edge between them)

# Authentication: ExpertReview --> ConsensusVote (vote after review)
# LegalVerify can happen after ExpertReview and ConsensusVote
auth_po = StrictPartialOrder(nodes=[ExpertReview, ConsensusVote, LegalVerify])
auth_po.order.add_edge(ExpertReview, ConsensusVote)
auth_po.order.add_edge(ConsensusVote, LegalVerify)

# The overall validation before certification:
# After Artifact Intake, provenance_po, mat_po and auth_po need to be done.
# ProvenanceCheck sequence and material analysis might start concurrently after Artifact Intake.
# Then Authentication after provenance+material testing

# So after ArtifactIntake:
# concurrently Provenance and Material analysis:
prov_mat_po = StrictPartialOrder(nodes=[provenance_po, mat_po])
# no edges between provenance_po and mat_po to indicate concurrency

# Then authentication after both provenance and material:
# So ordering: ArtifactIntake --> provenance_po and mat_po (concurrent), then --> auth_po

# Because provenance_po and mat_po are StrictPartialOrder objects, they are nodes in the dependency order

# We can model the concurrency of provenance_po and mat_po by having them as nodes in a PO with no order edge between them
# Then auth_po depends on both.

pre_auth_po = StrictPartialOrder(nodes=[ArtifactIntake, provenance_po, mat_po])
pre_auth_po.order.add_edge(ArtifactIntake, provenance_po)
pre_auth_po.order.add_edge(ArtifactIntake, mat_po)

valid_auth_po = StrictPartialOrder(nodes=[pre_auth_po, auth_po])
valid_auth_po.order.add_edge(pre_auth_po, auth_po)

# Stakeholder coordination includes EthicsReview, MarketAnalysis, LegalVerify (already in auth_po), Auction houses part not explicit, 
# LegalVerify is in auth_po, so EthicsReview and MarketAnalysis concurrent with LegalVerify?
# Let’s model EthicsReview and MarketAnalysis as concurrent activities after or during authentication.

stakeholders_po = StrictPartialOrder(nodes=[auth_po, EthicsReview, MarketAnalysis])
stakeholders_po.order.add_edge(auth_po, EthicsReview)
stakeholders_po.order.add_edge(auth_po, MarketAnalysis)
# No order between EthicsReview and MarketAnalysis

# After stakeholder review, final Certification including Blockchain log:
# Certification step: BlockchainLog after EthicsReview & MarketAnalysis

post_cert_po = StrictPartialOrder(nodes=[stakeholders_po, BlockchainLog])
post_cert_po.order.add_edge(stakeholders_po, BlockchainLog)

# After certification, continuous monitoring and updates:
# OwnershipAudit, DisputeMonitor, RegulationSync, ClientUpdate are ongoing activities,
# modeled as a loop:

# Loop body: Monitoring activities concurrent: OwnershipAudit, DisputeMonitor, RegulationSync, ClientUpdate
monitor_nodes = [OwnershipAudit, DisputeMonitor, RegulationSync, ClientUpdate]
monitor_po = StrictPartialOrder(nodes=monitor_nodes)
# No edges among these, fully concurrent monitoring

# Loop structure: loop body: monitor_po , loop guard: silent transition (exit)
skip = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_po, skip])

# Final root PO combining all:
root = StrictPartialOrder(nodes=[valid_auth_po, stakeholders_po, post_cert_po, monitor_loop])

# Add order edges:
root.order.add_edge(valid_auth_po, stakeholders_po)  # Authentication to stakeholder coordination
root.order.add_edge(stakeholders_po, post_cert_po)  # Stakeholders to blockchain log (certification)
root.order.add_edge(post_cert_po, monitor_loop)     # Certification to monitoring loop