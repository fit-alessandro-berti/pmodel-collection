# Generated from: f2271a55-6bb3-4532-b010-2ece54f66c1c.json
# Description: This process involves the intricate steps required to authenticate rare cultural artifacts using a combination of advanced scientific testing, expert historical analysis, and blockchain verification. Initial provenance research is conducted to gather historical context, followed by material composition tests using spectroscopy and radiocarbon dating. Expert appraisers assess craftsmanship and stylistic elements, while digital imaging techniques detect restorations or alterations. Results are then cross-referenced with global artifact databases. Finally, a unique blockchain record is created to provide an immutable authentication certificate, preventing forgery and enhancing collector confidence. The process demands close coordination between scientists, historians, appraisers, and IT specialists to maintain integrity and traceability throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
ProvenanceCheck = Transition(label='Provenance Check')
SpectroscopyTest = Transition(label='Spectroscopy Test')
CarbonDating = Transition(label='Carbon Dating')
StyleAnalysis = Transition(label='Style Analysis')
ImageScanning = Transition(label='Image Scanning')
RestorationScan = Transition(label='Restoration Scan')
AppraiserReview = Transition(label='Appraiser Review')
DatabaseMatch = Transition(label='Database Match')
BlockchainEntry = Transition(label='Blockchain Entry')
CertificateIssue = Transition(label='Certificate Issue')
ForgeryDetect = Transition(label='Forgery Detect')
ReportCompilation = Transition(label='Report Compilation')
ClientBriefing = Transition(label='Client Briefing')
SecureStorage = Transition(label='Secure Storage')
FinalApproval = Transition(label='Final Approval')

# Step 1: Provenance Check (initial)
# Step 2: Material composition tests in parallel (Spectroscopy Test, Carbon Dating)
material_tests = StrictPartialOrder(nodes=[SpectroscopyTest, CarbonDating])

# Step 3: Expert appraisers (StyleAnalysis and AppraiserReview), and digital imaging (ImageScanning, RestorationScan)
# StyleAnalysis and ImageScanning branches are independent but AppraiserReview depends on StyleAnalysis and RestorationScan depends on ImageScanning
# We'll model StyleAnalysis then AppraiserReview sequentially
appraiser_branch = StrictPartialOrder(nodes=[StyleAnalysis, AppraiserReview])
appraiser_branch.order.add_edge(StyleAnalysis, AppraiserReview)

# Restoration branch: ImageScanning then RestorationScan
imaging_branch = StrictPartialOrder(nodes=[ImageScanning, RestorationScan])
imaging_branch.order.add_edge(ImageScanning, RestorationScan)

# These two branches (appraiser_branch and imaging_branch) proceed in parallel
expert_analysis = StrictPartialOrder(nodes=[appraiser_branch, imaging_branch])

# Step 4: Results cross-referenced with global database: DatabaseMatch
# DatabaseMatch depends on the completion of both expert_analysis branches
cross_reference = DatabaseMatch

# Step 5: BlockchainEntry (create blockchain record) depends on DatabaseMatch
blockchain = BlockchainEntry

# Step 6: Issue Certificate depends on BlockchainEntry
certificate = CertificateIssue

# Step 7: ForgeryDetect runs parallel with ReportCompilation
# Both happen after certificate issue
forgery_report = StrictPartialOrder(nodes=[ForgeryDetect, ReportCompilation])
# No order edges between ForgeryDetect and ReportCompilation (concurrent)

# Step 8: ClientBriefing depends on both ForgeryDetect and ReportCompilation completed
# This requires a PO with edges ForgeryDetect-->ClientBriefing and ReportCompilation-->ClientBriefing
client_briefing = StrictPartialOrder(nodes=[ForgeryDetect, ReportCompilation, ClientBriefing])
client_briefing.order.add_edge(ForgeryDetect, ClientBriefing)
client_briefing.order.add_edge(ReportCompilation, ClientBriefing)

# Step 9: SecureStorage and FinalApproval follow ClientBriefing sequentially
# Order: ClientBriefing --> SecureStorage --> FinalApproval
final_steps = StrictPartialOrder(nodes=[ClientBriefing, SecureStorage, FinalApproval])
final_steps.order.add_edge(ClientBriefing, SecureStorage)
final_steps.order.add_edge(SecureStorage, FinalApproval)

# We must connect client_briefing (that includes ClientBriefing) with final_steps
# But the final_steps also includes ClientBriefing node, to avoid node duplication we will merge 
# Instead, define final_steps with SecureStorage and FinalApproval only, and add ClientBriefing edge from client_briefing to final_steps nodes

# Adjust final_steps nodes - exclude ClientBriefing here
final_steps = StrictPartialOrder(nodes=[SecureStorage, FinalApproval])
final_steps.order.add_edge(SecureStorage, FinalApproval)

# Build a combined PO for ForgeryDetect, ReportCompilation, ClientBriefing, SecureStorage, FinalApproval
# We'll keep client_briefing for first three with ClientBriefing as node
# Then add edges from ClientBriefing to SecureStorage and so on

final_phase = StrictPartialOrder(nodes=[ForgeryDetect, ReportCompilation, ClientBriefing, SecureStorage, FinalApproval])
final_phase.order.add_edge(ForgeryDetect, ClientBriefing)
final_phase.order.add_edge(ReportCompilation, ClientBriefing)
final_phase.order.add_edge(ClientBriefing, SecureStorage)
final_phase.order.add_edge(SecureStorage, FinalApproval)

# Connect all steps together in a final PO:
# ProvenanceCheck --> material_tests (SpectroscopyTest and CarbonDating are nodes but appear in material_tests)
# Both material tests must complete before expert_analysis starts

# We need to create a combined PO for all major steps:
# Nodes: ProvenanceCheck, SpectroscopyTest, CarbonDating, appraiser_branch (StyleAnalysis->AppraiserReview),
# imaging_branch (ImageScanning->RestorationScan), DatabaseMatch, BlockchainEntry, CertificateIssue,
# ForgeryDetect, ReportCompilation, ClientBriefing, SecureStorage, FinalApproval

# However, appraiser_branch and imaging_branch are StrictPartialOrders, their nodes are inner transitions.
# Instead of nested POs, better to represent all these transitions flat and add edges accordingly.

# We'll flatten appraiser_branch and imaging_branch nodes, and add edges for internal dependencies

# Collect all nodes
nodes = [
    ProvenanceCheck,
    SpectroscopyTest, CarbonDating,
    StyleAnalysis, AppraiserReview,
    ImageScanning, RestorationScan,
    DatabaseMatch,
    BlockchainEntry,
    CertificateIssue,
    ForgeryDetect, ReportCompilation, ClientBriefing, SecureStorage, FinalApproval,
]

root = StrictPartialOrder(nodes=nodes)

# Define dependencies:

# ProvenanceCheck --> SpectroscopyTest, CarbonDating (both start after provenance check)
root.order.add_edge(ProvenanceCheck, SpectroscopyTest)
root.order.add_edge(ProvenanceCheck, CarbonDating)

# SpectroscopyTest and CarbonDating run in parallel,
# after both complete, expert analysis branches start (StyleAnalysis and ImageScanning)
root.order.add_edge(SpectroscopyTest, StyleAnalysis)
root.order.add_edge(SpectroscopyTest, ImageScanning)
root.order.add_edge(CarbonDating, StyleAnalysis)
root.order.add_edge(CarbonDating, ImageScanning)

# Internal appraiser branch dependency: StyleAnalysis --> AppraiserReview
root.order.add_edge(StyleAnalysis, AppraiserReview)

# Internal imaging branch dependency: ImageScanning --> RestorationScan
root.order.add_edge(ImageScanning, RestorationScan)

# Both appraiser branch and imaging branch must complete before DatabaseMatch
root.order.add_edge(AppraiserReview, DatabaseMatch)
root.order.add_edge(RestorationScan, DatabaseMatch)

# DatabaseMatch --> BlockchainEntry --> CertificateIssue
root.order.add_edge(DatabaseMatch, BlockchainEntry)
root.order.add_edge(BlockchainEntry, CertificateIssue)

# CertificateIssue precedes both ForgeryDetect and ReportCompilation which run concurrently
root.order.add_edge(CertificateIssue, ForgeryDetect)
root.order.add_edge(CertificateIssue, ReportCompilation)

# Both ForgeryDetect and ReportCompilation must complete before ClientBriefing
root.order.add_edge(ForgeryDetect, ClientBriefing)
root.order.add_edge(ReportCompilation, ClientBriefing)

# ClientBriefing --> SecureStorage --> FinalApproval
root.order.add_edge(ClientBriefing, SecureStorage)
root.order.add_edge(SecureStorage, FinalApproval)