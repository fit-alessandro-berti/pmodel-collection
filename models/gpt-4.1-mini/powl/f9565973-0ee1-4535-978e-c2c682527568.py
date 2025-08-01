# Generated from: f9565973-0ee1-4535-978e-c2c682527568.json
# Description: This process involves the detailed validation and documentation of an artifact's origin, ownership, and authenticity through multiple verification stages including material analysis, historical registry checks, provenance interviews, and secure digital ledger entries. Each step ensures comprehensive traceability and legal compliance, often requiring interdisciplinary collaboration between historians, scientists, legal experts, and technology specialists to certify rare or culturally significant objects before sale or exhibition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Artifact_Intake = Transition(label='Artifact Intake')
Initial_Survey = Transition(label='Initial Survey')

Material_Test = Transition(label='Material Test')

Historical_Check = Transition(label='Historical Check')
Registry_Search = Transition(label='Registry Search')

Owner_Interview = Transition(label='Owner Interview')

Condition_Report = Transition(label='Condition Report')
Forgery_Scan = Transition(label='Forgery Scan')

Digital_Tagging = Transition(label='Digital Tagging')
Ledger_Entry = Transition(label='Ledger Entry')

Expert_Review = Transition(label='Expert Review')
Legal_Verify = Transition(label='Legal Verify')

Provenance_Draft = Transition(label='Provenance Draft')
Client_Approval = Transition(label='Client Approval')

Final_Certificate = Transition(label='Final Certificate')
Archive_Storage = Transition(label='Archive Storage')

# Construct partial orders for sub-processes.

# Material analysis branch (could happen concurrently with Historical branch)
material_po = StrictPartialOrder(
    nodes=[Material_Test, Condition_Report, Forgery_Scan]
)
material_po.order.add_edge(Material_Test, Condition_Report)
material_po.order.add_edge(Condition_Report, Forgery_Scan)

# Historical registry checks branch (historical_check and registry_search parallel)
historical_po = StrictPartialOrder(
    nodes=[Historical_Check, Registry_Search]
)
# These can be concurrent, no order edge

# Owner interview alone branch (just Owner Interview)
owner_interview_po = StrictPartialOrder(
    nodes=[Owner_Interview]
)

# Digital ledger entries branch (Digital_Tagging then Ledger_Entry)
ledger_po = StrictPartialOrder(
    nodes=[Digital_Tagging, Ledger_Entry]
)
ledger_po.order.add_edge(Digital_Tagging, Ledger_Entry)

# Expert review then legal verify
expert_legal_po = StrictPartialOrder(
    nodes=[Expert_Review, Legal_Verify]
)
expert_legal_po.order.add_edge(Expert_Review, Legal_Verify)

# Provenance draft then client approval
prov_client_po = StrictPartialOrder(
    nodes=[Provenance_Draft, Client_Approval]
)
prov_client_po.order.add_edge(Provenance_Draft, Client_Approval)

# Final cert then archiving
final_archive_po = StrictPartialOrder(
    nodes=[Final_Certificate, Archive_Storage]
)
final_archive_po.order.add_edge(Final_Certificate, Archive_Storage)

# Historical branch: combine Historical_Check, Registry_Search concurrent, then join Owner Interview after (owner interview requires both done)
# Build a PO that contains Historical_Check, Registry_Search concurrent => then Owner Interview after both (so edges from both to Owner_Interview)
hist_registry_owner_po = StrictPartialOrder(
    nodes=[Historical_Check, Registry_Search, Owner_Interview]
)
hist_registry_owner_po.order.add_edge(Historical_Check, Owner_Interview)
hist_registry_owner_po.order.add_edge(Registry_Search, Owner_Interview)

# Now, combine the 3 verification branches in parallel:
# 1) material_po
# 2) hist_registry_owner_po
# 3) ledger_po

verification_nodes = [material_po, hist_registry_owner_po, ledger_po]

verification_po = StrictPartialOrder(
    nodes=verification_nodes
)
# No ordering between these three - they are concurrent

# After verification, expert review + legal verify
# Put expert_legal_po after verification_po

# Provenance review after expert/legal
# prov_client_po after expert_legal_po

# Then Final Certificate and Archive after client approval

# Compose partial orders in a chain:

# Step 1: Artifact Intake --> Initial Survey --> verification_po --> expert_legal_po --> prov_client_po --> final_archive_po

root = StrictPartialOrder(
    nodes=[Artifact_Intake, Initial_Survey, verification_po,
           expert_legal_po, prov_client_po, final_archive_po]
)

# Add edges for sequential ordering
root.order.add_edge(Artifact_Intake, Initial_Survey)
root.order.add_edge(Initial_Survey, verification_po)
root.order.add_edge(verification_po, expert_legal_po)
root.order.add_edge(expert_legal_po, prov_client_po)
root.order.add_edge(prov_client_po, final_archive_po)