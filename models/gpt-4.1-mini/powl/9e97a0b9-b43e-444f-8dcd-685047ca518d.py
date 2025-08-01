# Generated from: 9e97a0b9-b43e-444f-8dcd-685047ca518d.json
# Description: This process involves the detailed authentication of rare historical artifacts, integrating multidisciplinary expertise from provenance research to scientific analysis. Each artifact undergoes initial visual inspection, documentation review, and material composition testing using advanced spectroscopy. Provenance data is cross-checked with global registries and auction records. Anomaly detection algorithms flag inconsistencies for expert panel review. Conservation status assessment ensures proper handling protocols. Finally, a comprehensive certification report is generated, including high-resolution imaging and 3D scans, before secure archival and client delivery. The process demands coordination across historians, chemists, data scientists, and legal advisors to maintain authenticity standards and legal compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
VisualInspect = Transition(label='Visual Inspect')
DocumentReview = Transition(label='Document Review')
MaterialTest = Transition(label='Material Test')
SpectroscopyRun = Transition(label='Spectroscopy Run')
RegistryCheck = Transition(label='Registry Check')
AuctionVerify = Transition(label='Auction Verify')
AnomalyFlag = Transition(label='Anomaly Flag')
ExpertPanel = Transition(label='Expert Panel')
ConservationAssess = Transition(label='Conservation Assess')
HandleProtocol = Transition(label='Handle Protocol')
ReportCompile = Transition(label='Report Compile')
ImageCapture = Transition(label='Image Capture')
Scan3D = Transition(label='3D Scan')
ArchiveStore = Transition(label='Archive Store')
ClientDeliver = Transition(label='Client Deliver')
LegalReview = Transition(label='Legal Review')
DataSync = Transition(label='Data Sync')

# Partial orders for initial activities done concurrently:
# Visual Inspect, Document Review, Material Test (which includes Spectroscopy Run)
# The Material Test is composed by Material Test -> Spectroscopy Run
MaterialTest_PO = StrictPartialOrder(nodes=[MaterialTest, SpectroscopyRun])
MaterialTest_PO.order.add_edge(MaterialTest, SpectroscopyRun)

initial_PO = StrictPartialOrder(nodes=[VisualInspect, DocumentReview, MaterialTest_PO])
# No dependencies between VisualInspect, DocumentReview, MaterialTest_PO means they are concurrent.

# Provenance data cross-check: Registry Check and Auction Verify concurrently
provenance_PO = StrictPartialOrder(nodes=[RegistryCheck, AuctionVerify])

# Anomaly detection with a choice: if anomaly detected (AnomalyFlag) then Expert Panel review else skip
skip = SilentTransition()
anomaly_check = OperatorPOWL(operator=Operator.XOR, children=[ExpertPanel, skip])
# Expert Panel must follow Anomaly Flag
anomaly_PO = StrictPartialOrder(nodes=[AnomalyFlag, anomaly_check])
anomaly_PO.order.add_edge(AnomalyFlag, anomaly_check)

# Conservation assessment and handling protocol in sequence
conservation_PO = StrictPartialOrder(nodes=[ConservationAssess, HandleProtocol])
conservation_PO.order.add_edge(ConservationAssess, HandleProtocol)

# Report compilation consisting of Report Compile followed by Image Capture and 3D Scan concurrently
imaging_PO = StrictPartialOrder(nodes=[ImageCapture, Scan3D])
report_PO = StrictPartialOrder(nodes=[ReportCompile, imaging_PO])
report_PO.order.add_edge(ReportCompile, imaging_PO)

# Archive Store and Client Deliver concurrently, but both after report_PO
archive_client_PO = StrictPartialOrder(nodes=[ArchiveStore, ClientDeliver])  # concurrent

# Legal Review and Data Sync happen to ensure legal compliance and data coherence, after archive and delivery
legal_data_PO = StrictPartialOrder(nodes=[LegalReview, DataSync])  # concurrent

# Combine archive_client_PO and legal_data_PO in sequence: 
# archive_client_PO -> legal_data_PO
final_PO = StrictPartialOrder(nodes=[archive_client_PO, legal_data_PO])
final_PO.order.add_edge(archive_client_PO, legal_data_PO)

# Compose entire final sequence order:

# Step 1: initial_PO
# Step 2: provenance_PO
# Step 3: anomaly_PO
# Step 4: conservation_PO
# Step 5: report_PO
# Step 6: final_PO (archive_client_PO then legal_data_PO)

# Build a top-level PO combining all these in sequence
root = StrictPartialOrder(
    nodes=[
        initial_PO,
        provenance_PO,
        anomaly_PO,
        conservation_PO,
        report_PO,
        final_PO
    ]
)
root.order.add_edge(initial_PO, provenance_PO)
root.order.add_edge(provenance_PO, anomaly_PO)
root.order.add_edge(anomaly_PO, conservation_PO)
root.order.add_edge(conservation_PO, report_PO)
root.order.add_edge(report_PO, final_PO)