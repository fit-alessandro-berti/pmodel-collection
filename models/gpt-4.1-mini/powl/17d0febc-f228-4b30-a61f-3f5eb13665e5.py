# Generated from: 17d0febc-f228-4b30-a61f-3f5eb13665e5.json
# Description: This process involves the intricate authentication of rare artifacts sourced from various undisclosed locations. It begins with preliminary provenance verification, followed by multi-spectral imaging and chemical analysis. Expert consultations and comparative historical research further validate authenticity. The process ensures secure transportation, condition reporting, and final certification before cataloging and archival storage. Each step requires meticulous documentation to prevent forgery and maintain chain of custody. The complexity is heightened by interdisciplinary collaboration, evolving technologies, and legal compliance with international cultural property laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Provenance_Check = Transition(label='Provenance Check')
Imaging_Scan = Transition(label='Imaging Scan')
Chemical_Test = Transition(label='Chemical Test')
Expert_Review = Transition(label='Expert Review')
Historical_Compare = Transition(label='Historical Compare')
Transport_Prep = Transition(label='Transport Prep')
Condition_Report = Transition(label='Condition Report')
Forgery_Analysis = Transition(label='Forgery Analysis')
Chain_Verify = Transition(label='Chain Verify')
Certification = Transition(label='Certification')
Catalog_Entry = Transition(label='Catalog Entry')
Archival_Store = Transition(label='Archival Store')
Legal_Audit = Transition(label='Legal Audit')
Tech_Update = Transition(label='Tech Update')
Final_Approval = Transition(label='Final Approval')

# Construct partial orders reflecting the described process

# Step 1: Preliminary provenance verification, followed by multi-spectral imaging and chemical analysis
# Provenance Check --> Imaging Scan --> Chemical Test
p1 = StrictPartialOrder(nodes=[Provenance_Check, Imaging_Scan, Chemical_Test])
p1.order.add_edge(Provenance_Check, Imaging_Scan)
p1.order.add_edge(Imaging_Scan, Chemical_Test)

# Step 2: Expert consultations and comparative historical research further validate authenticity
# Expert Review and Historical Compare are concurrent and both depend on Chemical Test
p2 = StrictPartialOrder(nodes=[Expert_Review, Historical_Compare])
# Combine p1 and p2 with dependencies: Chemical_Test --> Expert_Review and Chemical_Test --> Historical_Compare
p12_nodes = [Provenance_Check, Imaging_Scan, Chemical_Test, Expert_Review, Historical_Compare]
root12 = StrictPartialOrder(nodes=p12_nodes)
root12.order.add_edge(Provenance_Check, Imaging_Scan)
root12.order.add_edge(Imaging_Scan, Chemical_Test)
root12.order.add_edge(Chemical_Test, Expert_Review)
root12.order.add_edge(Chemical_Test, Historical_Compare)

# Step 3: Interdisciplinary collaboration and evolving technologies require Legal Audit and Tech Update in parallel with Expert Review/ Historical Compare activities (both must precede Transport Prep)
legal_and_tech = StrictPartialOrder(nodes=[Legal_Audit, Tech_Update])
# legal and tech are concurrent, no order between them

# Step 4: Transport Prep depends on completion of Expert Review, Historical Compare, Legal Audit, and Tech Update
# Transport Prep --> Condition Report --> Forgery Analysis --> Chain Verify
step4_nodes = [Transport_Prep, Condition_Report, Forgery_Analysis, Chain_Verify]
step4 = StrictPartialOrder(nodes=step4_nodes)
step4.order.add_edge(Transport_Prep, Condition_Report)
step4.order.add_edge(Condition_Report, Forgery_Analysis)
step4.order.add_edge(Forgery_Analysis, Chain_Verify)

# Step 5: Certification follows Chain Verify
# Certification --> Catalog Entry --> Archival Store
step5_nodes = [Certification, Catalog_Entry, Archival_Store]
step5 = StrictPartialOrder(nodes=step5_nodes)
step5.order.add_edge(Certification, Catalog_Entry)
step5.order.add_edge(Catalog_Entry, Archival_Store)

# Step 6: Final Approval depends on Certification and possibly after Catalog Entry (to enforce the final clearance)
# Let's say Final Approval depends on Certification and Catalog Entry - placing dependencies accordingly
final_approval_nodes = [Final_Approval]
final_approval = StrictPartialOrder(nodes=final_approval_nodes)

# Combine all partial orders into a big one:

# Collect all nodes
all_nodes = (
    [Provenance_Check, Imaging_Scan, Chemical_Test, Expert_Review, Historical_Compare] +
    [Legal_Audit, Tech_Update] +
    [Transport_Prep, Condition_Report, Forgery_Analysis, Chain_Verify] +
    [Certification, Catalog_Entry, Archival_Store] +
    [Final_Approval]
)

root = StrictPartialOrder(nodes=all_nodes)

# Add previous ordering edges
root.order.add_edge(Provenance_Check, Imaging_Scan)
root.order.add_edge(Imaging_Scan, Chemical_Test)

root.order.add_edge(Chemical_Test, Expert_Review)
root.order.add_edge(Chemical_Test, Historical_Compare)

# Legal Audit and Tech Update concurrent, no edges

# All of Expert Review, Historical Compare, Legal Audit, Tech Update must complete before Transport Prep:
root.order.add_edge(Expert_Review, Transport_Prep)
root.order.add_edge(Historical_Compare, Transport_Prep)
root.order.add_edge(Legal_Audit, Transport_Prep)
root.order.add_edge(Tech_Update, Transport_Prep)

# Transport Prep --> Condition Report --> Forgery Analysis --> Chain Verify
root.order.add_edge(Transport_Prep, Condition_Report)
root.order.add_edge(Condition_Report, Forgery_Analysis)
root.order.add_edge(Forgery_Analysis, Chain_Verify)

# Chain Verify --> Certification
root.order.add_edge(Chain_Verify, Certification)

# Certification --> Catalog Entry --> Archival Store
root.order.add_edge(Certification, Catalog_Entry)
root.order.add_edge(Catalog_Entry, Archival_Store)

# Certification and Catalog Entry --> Final Approval (final clearance after certification and cataloging)
root.order.add_edge(Certification, Final_Approval)
root.order.add_edge(Catalog_Entry, Final_Approval)