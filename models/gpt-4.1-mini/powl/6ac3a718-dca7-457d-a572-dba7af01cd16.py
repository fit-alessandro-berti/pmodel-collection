# Generated from: 6ac3a718-dca7-457d-a572-dba7af01cd16.json
# Description: This process involves the verification and authentication of historical artifacts using a combination of physical examination, chemical analysis, provenance validation, and blockchain recording. Initially, artifacts undergo visual inspection to detect anomalies, followed by microscopic and spectroscopic tests to determine material composition. Concurrently, provenance documents are digitized and cross-referenced with global registries. Verified data is then encrypted and logged into a blockchain ledger to ensure immutable record keeping. Finally, an expert panel reviews consolidated findings for final certification, and a digital twin is created for virtual display and further analysis. The process ensures authenticity while integrating modern technology with traditional expertise, reducing fraud in the antiquities market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Visual_Scan = Transition(label='Visual Scan')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Document_Digitize = Transition(label='Document Digitize')
Registry_Crossref = Transition(label='Registry Crossref')
Chemical_Analysis = Transition(label='Chemical Analysis')
Microscopic_Review = Transition(label='Microscopic Review')
Data_Encryption = Transition(label='Data Encryption')
Blockchain_Log = Transition(label='Blockchain Log')
Expert_Panel = Transition(label='Expert Panel')
Final_Certification = Transition(label='Final Certification')
Digital_Twin = Transition(label='Digital Twin')
Virtual_Display = Transition(label='Virtual Display')
Fraud_Detect = Transition(label='Fraud Detect')
Report_Generate = Transition(label='Report Generate')
Archive_Storage = Transition(label='Archive Storage')

# Step 1: Visual Scan
# Step 2: two concurrent branches:
#    a) Material Test and Chemical Analysis and Microscopic Review - all three in partial order Material_Test-->Chemical_Analysis-->Microscopic_Review
#    b) Provenance Check after Document Digitize and Registry Crossref
# Step 3: After both branches complete, Data Encryption then Blockchain Log
# Step 4: Expert Panel then Final Certification
# Step 5: Digital Twin then Virtual Display
# Step 6: Fraud Detect, Report Generate, Archive Storage concurrent at the end

# Define partial order for branch a
branch_a = StrictPartialOrder(nodes=[Material_Test, Chemical_Analysis, Microscopic_Review])
branch_a.order.add_edge(Material_Test, Chemical_Analysis)
branch_a.order.add_edge(Chemical_Analysis, Microscopic_Review)

# Define partial order for branch b
branch_b = StrictPartialOrder(nodes=[Document_Digitize, Registry_Crossref, Provenance_Check])
branch_b.order.add_edge(Document_Digitize, Registry_Crossref)
branch_b.order.add_edge(Registry_Crossref, Provenance_Check)

# Now the concurrent branches (branch_a and branch_b) run concurrently after Visual Scan
concurrent_branches = StrictPartialOrder(nodes=[branch_a, branch_b])

# After both branches: Data Encryption --> Blockchain Log
encryption_log = StrictPartialOrder(nodes=[Data_Encryption, Blockchain_Log])
encryption_log.order.add_edge(Data_Encryption, Blockchain_Log)

# Expert panel and Final Certification in order
expert_cert = StrictPartialOrder(nodes=[Expert_Panel, Final_Certification])
expert_cert.order.add_edge(Expert_Panel, Final_Certification)

# Digital Twin then Virtual Display
digital_virtual = StrictPartialOrder(nodes=[Digital_Twin, Virtual_Display])
digital_virtual.order.add_edge(Digital_Twin, Virtual_Display)

# Fraud Detect, Report Generate, Archive Storage concurrent at the end
final_concurrent = StrictPartialOrder(nodes=[Fraud_Detect, Report_Generate, Archive_Storage])

# Compose the full model partial order structure stepwise
po_part1 = StrictPartialOrder(nodes=[Visual_Scan, concurrent_branches])
po_part1.order.add_edge(Visual_Scan, concurrent_branches)

po_part2 = StrictPartialOrder(nodes=[po_part1, encryption_log])
po_part2.order.add_edge(po_part1, encryption_log)

po_part3 = StrictPartialOrder(nodes=[po_part2, expert_cert])
po_part3.order.add_edge(po_part2, expert_cert)

po_part4 = StrictPartialOrder(nodes=[po_part3, digital_virtual])
po_part4.order.add_edge(po_part3, digital_virtual)

root = StrictPartialOrder(nodes=[po_part4, final_concurrent])
root.order.add_edge(po_part4, final_concurrent)