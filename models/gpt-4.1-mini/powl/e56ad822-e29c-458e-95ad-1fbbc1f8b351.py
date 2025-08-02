# Generated from: e56ad822-e29c-458e-95ad-1fbbc1f8b351.json
# Description: This process governs the authentication of rare cultural artifacts submitted by private collectors and museums for validation and certification. It involves multiple specialized steps such as provenance verification, material composition analysis, historical context assessment, expert panel reviews, and digital fingerprinting. The process integrates traditional scholarly methods with advanced AI-driven pattern recognition and blockchain registration to ensure authenticity, prevent fraud, and maintain an immutable record of artifact ownership and characteristics. Throughout the workflow, interdisciplinary collaboration, legal compliance checks, and secure data handling are prioritized to safeguard sensitive information and uphold ethical standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SubmitArtifact = Transition(label='Submit Artifact')
InitialReview = Transition(label='Initial Review')

# Parallel verification steps after Initial Review as partial order (concurrent):
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ContextAnalysis = Transition(label='Context Analysis')

# Expert panel review after provenance, material and context checks (order after these three)
ExpertPanel = Transition(label='Expert Panel')

# Digital fingerprinting and AI analysis after expert panel, partially ordered (concurrent):
DigitalFingerprint = Transition(label='Digital Fingerprint')
AIPattern = Transition(label='AI Pattern')

# Legal and ethics review after fingerprint and AI, partially ordered (concurrent):
LegalAudit = Transition(label='Legal Audit')
EthicsReview = Transition(label='Ethics Review')

# Fraud detection after legal and ethics reviews
FraudDetection = Transition(label='Fraud Detection')

# Blockchain logging after fraud detection
BlockchainLog = Transition(label='Blockchain Log')

# Certification follows blockchain log
Certification = Transition(label='Certification')

# Owner notification, data archiving and secure storage in parallel after certification
OwnerNotify = Transition(label='Owner Notify')
ArchiveData = Transition(label='Archive Data')
SecureStorage = Transition(label='Secure Storage')

#
# Build partial orders to represent concurrency and dependencies
#

# Step 1: Submit Artifact --> Initial Review
po1 = StrictPartialOrder(nodes=[SubmitArtifact, InitialReview])
po1.order.add_edge(SubmitArtifact, InitialReview)

# Step 2: Parallel provenance check, material scan, context analysis after Initial Review
po2_checks = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialScan, ContextAnalysis])
# No order edges among these checks since they are concurrent

# Combine Initial Review --> these checks
po2 = StrictPartialOrder(nodes=[InitialReview, po2_checks])
po2.order.add_edge(InitialReview, po2_checks)  # Note: po2_checks is a PO, but edges must be between nodes
# We cannot add edge to a POWL node in pm4py. Instead, represent as a PO containing all nodes

# So build a flat PO that includes InitialReview and the three checks,
# ordering InitialReview before each check

nodes_po2 = [InitialReview, ProvenanceCheck, MaterialScan, ContextAnalysis]
po2 = StrictPartialOrder(nodes=nodes_po2)
po2.order.add_edge(InitialReview, ProvenanceCheck)
po2.order.add_edge(InitialReview, MaterialScan)
po2.order.add_edge(InitialReview, ContextAnalysis)

# Step 3: Expert Panel after the three checks (all 3 must finish)
nodes_po3 = [ProvenanceCheck, MaterialScan, ContextAnalysis, ExpertPanel]
po3 = StrictPartialOrder(nodes=nodes_po3)
po3.order.add_edge(ProvenanceCheck, ExpertPanel)
po3.order.add_edge(MaterialScan, ExpertPanel)
po3.order.add_edge(ContextAnalysis, ExpertPanel)

# Step 4: Digital Fingerprint and AI Pattern concurrent after Expert Panel
nodes_po4 = [ExpertPanel, DigitalFingerprint, AIPattern]
po4 = StrictPartialOrder(nodes=nodes_po4)
po4.order.add_edge(ExpertPanel, DigitalFingerprint)
po4.order.add_edge(ExpertPanel, AIPattern)

# Step 5: Legal Audit and Ethics Review concurrent after fingerprinting and AI
nodes_po5 = [DigitalFingerprint, AIPattern, LegalAudit, EthicsReview]
po5 = StrictPartialOrder(nodes=nodes_po5)
po5.order.add_edge(DigitalFingerprint, LegalAudit)
po5.order.add_edge(DigitalFingerprint, EthicsReview)
po5.order.add_edge(AIPattern, LegalAudit)
po5.order.add_edge(AIPattern, EthicsReview)

# Step 6: Fraud Detection after Legal and Ethics review
nodes_po6 = [LegalAudit, EthicsReview, FraudDetection]
po6 = StrictPartialOrder(nodes=nodes_po6)
po6.order.add_edge(LegalAudit, FraudDetection)
po6.order.add_edge(EthicsReview, FraudDetection)

# Step 7: Blockchain Log after Fraud Detection
po7 = StrictPartialOrder(nodes=[FraudDetection, BlockchainLog])
po7.order.add_edge(FraudDetection, BlockchainLog)

# Step 8: Certification after Blockchain Log
po8 = StrictPartialOrder(nodes=[BlockchainLog, Certification])
po8.order.add_edge(BlockchainLog, Certification)

# Step 9: Owner Notify, Archive Data and Secure Storage in parallel after Certification

po9 = StrictPartialOrder(nodes=[Certification, OwnerNotify, ArchiveData, SecureStorage])
po9.order.add_edge(Certification, OwnerNotify)
po9.order.add_edge(Certification, ArchiveData)
po9.order.add_edge(Certification, SecureStorage)

# Now combine all partial orders as a single big PO
# We combine all unique nodes:
all_nodes = [
    SubmitArtifact,
    InitialReview,
    ProvenanceCheck,
    MaterialScan,
    ContextAnalysis,
    ExpertPanel,
    DigitalFingerprint,
    AIPattern,
    LegalAudit,
    EthicsReview,
    FraudDetection,
    BlockchainLog,
    Certification,
    OwnerNotify,
    ArchiveData,
    SecureStorage
]

root = StrictPartialOrder(nodes=all_nodes)

# Add all edges from above combined edges

# Step 1 edges
root.order.add_edge(SubmitArtifact, InitialReview)

# Step 2 edges
root.order.add_edge(InitialReview, ProvenanceCheck)
root.order.add_edge(InitialReview, MaterialScan)
root.order.add_edge(InitialReview, ContextAnalysis)

# Step 3 edges
root.order.add_edge(ProvenanceCheck, ExpertPanel)
root.order.add_edge(MaterialScan, ExpertPanel)
root.order.add_edge(ContextAnalysis, ExpertPanel)

# Step 4 edges
root.order.add_edge(ExpertPanel, DigitalFingerprint)
root.order.add_edge(ExpertPanel, AIPattern)

# Step 5 edges
root.order.add_edge(DigitalFingerprint, LegalAudit)
root.order.add_edge(DigitalFingerprint, EthicsReview)
root.order.add_edge(AIPattern, LegalAudit)
root.order.add_edge(AIPattern, EthicsReview)

# Step 6 edges
root.order.add_edge(LegalAudit, FraudDetection)
root.order.add_edge(EthicsReview, FraudDetection)

# Step 7 edges
root.order.add_edge(FraudDetection, BlockchainLog)

# Step 8 edges
root.order.add_edge(BlockchainLog, Certification)

# Step 9 edges
root.order.add_edge(Certification, OwnerNotify)
root.order.add_edge(Certification, ArchiveData)
root.order.add_edge(Certification, SecureStorage)