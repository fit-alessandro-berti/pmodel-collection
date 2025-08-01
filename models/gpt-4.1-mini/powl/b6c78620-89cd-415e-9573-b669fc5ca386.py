# Generated from: b6c78620-89cd-415e-9573-b669fc5ca386.json
# Description: This process outlines the comprehensive steps involved in authenticating rare cultural artifacts for a global auction house. It involves multidisciplinary expert evaluations, advanced scientific testing, provenance verification, legal compliance checks, and secure documentation handling. Each artifact undergoes intricate imaging, material analysis, historical cross-referencing, and ethical sourcing validation to ensure authenticity and legal ownership. The process culminates in certified approval and archival before public auction listing, ensuring transparency and trust for buyers and sellers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Artifact_Intake = Transition(label='Artifact Intake')
Preliminary_Scan = Transition(label='Preliminary Scan')
Material_Test = Transition(label='Material Test')
Historical_Check = Transition(label='Historical Check')
Provenance_Review = Transition(label='Provenance Review')
Ethics_Audit = Transition(label='Ethics Audit')
Expert_Panel = Transition(label='Expert Panel')
Legal_Verify = Transition(label='Legal Verify')
Imaging_Capture = Transition(label='Imaging Capture')
Data_Encryption = Transition(label='Data Encryption')
Report_Draft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
Archival_Store = Transition(label='Archival Store')
Auction_Setup = Transition(label='Auction Setup')
Client_Notify = Transition(label='Client Notify')
Final_Review = Transition(label='Final Review')

# Construct partial orders to capture concurrency and dependencies

# Multidisciplinary expert evaluations:
# Imaging Capture, Material Test, Historical Check, Ethics Audit are concurrent after Preliminary Scan
# Expert Panel depends on all four above

# Step 1: Artifact Intake --> Preliminary Scan
# Step 2: After Preliminary Scan, Imaging Capture || Material Test || Historical Check || Ethics Audit (concurrent)
# Step 3: Expert Panel after these four
# Step 4: Provenance Review and Legal Verify concurrent after Expert Panel
# Step 5: Data Encryption and Report Draft concurrent after Provenance Review and Legal Verify
# Step 6: Certification after Data Encryption and Report Draft
# Step 7: Archival Store after Certification
# Step 8: Final Review after Archival Store
# Step 9: Auction Setup after Final Review
# Step 10: Client Notify after Auction Setup

# To build these concurrency and dependencies:

# Step 2 concurrency nodes
step2_nodes = [Imaging_Capture, Material_Test, Historical_Check, Ethics_Audit]

# Step 4 concurrency nodes
step4_nodes = [Provenance_Review, Legal_Verify]

# Step 5 concurrency nodes
step5_nodes = [Data_Encryption, Report_Draft]

# Build partial order for steps 2-3:
po_step2_3 = StrictPartialOrder(nodes=step2_nodes + [Expert_Panel])
for node in step2_nodes:
    po_step2_3.order.add_edge(node, Expert_Panel)

# Build partial order for steps 4 (after Expert Panel)
po_step4 = StrictPartialOrder(nodes=step4_nodes + [Expert_Panel])
po_step4.order.add_edge(Expert_Panel, Provenance_Review)
po_step4.order.add_edge(Expert_Panel, Legal_Verify)

# Build partial order for steps 5 (after step4)
po_step5 = StrictPartialOrder(nodes=step5_nodes + step4_nodes)
po_step5.order.add_edge(Provenance_Review, Data_Encryption)
po_step5.order.add_edge(Provenance_Review, Report_Draft)
po_step5.order.add_edge(Legal_Verify, Data_Encryption)
po_step5.order.add_edge(Legal_Verify, Report_Draft)

# Combine step 2-5 into a single structure, managing edges among po_step2_3, po_step4, po_step5

# Instead of multiple partial orders, we will combine all nodes and edges in one StrictPartialOrder:
all_nodes = [
    Artifact_Intake,
    Preliminary_Scan,
    Imaging_Capture,
    Material_Test,
    Historical_Check,
    Ethics_Audit,
    Expert_Panel,
    Provenance_Review,
    Legal_Verify,
    Data_Encryption,
    Report_Draft,
    Certification,
    Archival_Store,
    Auction_Setup,
    Client_Notify,
    Final_Review
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges according to dependencies:

# Step 1
root.order.add_edge(Artifact_Intake, Preliminary_Scan)

# Step 2: Preliminary Scan --> Imaging Capture, Material Test, Historical Check, Ethics Audit (concurrent)
root.order.add_edge(Preliminary_Scan, Imaging_Capture)
root.order.add_edge(Preliminary_Scan, Material_Test)
root.order.add_edge(Preliminary_Scan, Historical_Check)
root.order.add_edge(Preliminary_Scan, Ethics_Audit)

# Step 3: All four step2 nodes --> Expert Panel
root.order.add_edge(Imaging_Capture, Expert_Panel)
root.order.add_edge(Material_Test, Expert_Panel)
root.order.add_edge(Historical_Check, Expert_Panel)
root.order.add_edge(Ethics_Audit, Expert_Panel)

# Step 4: Expert Panel --> Provenance Review and Legal Verify (concurrent)
root.order.add_edge(Expert_Panel, Provenance_Review)
root.order.add_edge(Expert_Panel, Legal_Verify)

# Step 5: Provenance Review and Legal Verify --> Data Encryption and Report Draft (both concurrent)
root.order.add_edge(Provenance_Review, Data_Encryption)
root.order.add_edge(Provenance_Review, Report_Draft)
root.order.add_edge(Legal_Verify, Data_Encryption)
root.order.add_edge(Legal_Verify, Report_Draft)

# Step 6: Data Encryption and Report Draft --> Certification
root.order.add_edge(Data_Encryption, Certification)
root.order.add_edge(Report_Draft, Certification)

# Step 7: Certification --> Archival Store
root.order.add_edge(Certification, Archival_Store)

# Step 8: Archival Store --> Final Review
root.order.add_edge(Archival_Store, Final_Review)

# Step 9: Final Review --> Auction Setup
root.order.add_edge(Final_Review, Auction_Setup)

# Step 10: Auction Setup --> Client Notify
root.order.add_edge(Auction_Setup, Client_Notify)