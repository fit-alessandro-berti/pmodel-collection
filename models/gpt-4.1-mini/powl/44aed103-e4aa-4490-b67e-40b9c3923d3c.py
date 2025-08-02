# Generated from: 44aed103-e4aa-4490-b67e-40b9c3923d3c.json
# Description: This process governs the authentication and provenance verification of rare historical artifacts submitted to a specialized auction house. It involves interdisciplinary collaboration among historians, scientists, and legal experts to validate the artifact's origin, material composition, and ownership history. The workflow includes initial intake, condition assessment, multi-level scientific testing (such as radiocarbon dating and spectroscopy), provenance research through archival databases, conflict artifact screening, expert panel review, legal clearance for export, and final certification issuance. The process ensures the integrity of the auction and prevents illicit trade, requiring meticulous documentation and secure data management throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
Artifact_Intake = Transition('Artifact Intake')
Condition_Check = Transition('Condition Check')
Initial_Screening = Transition('Initial Screening')
Scientific_Tests = Transition('Scientific Tests')
Radiocarbon_Date = Transition('Radiocarbon Date')
Spectroscopy_Test = Transition('Spectroscopy Test')
Provenance_Search = Transition('Provenance Search')
Archival_Review = Transition('Archival Review')
Conflict_Check = Transition('Conflict Check')
Expert_Panel = Transition('Expert Panel')
Legal_Clearance = Transition('Legal Clearance')
Export_Approval = Transition('Export Approval')
Certification = Transition('Certification')
Documentation = Transition('Documentation')
Data_Archiving = Transition('Data Archiving')
Client_Notification = Transition('Client Notification')

# Scientific Tests branch: Radiocarbon Date and Spectroscopy Test concurrent, then join as Scientific Tests
# Here, we model Radiocarbon Date and Spectroscopy Test as concurrent nodes preceding Scientific Tests
sci_tests_sub = StrictPartialOrder(nodes=[Radiocarbon_Date, Spectroscopy_Test, Scientific_Tests])
sci_tests_sub.order.add_edge(Radiocarbon_Date, Scientific_Tests)
sci_tests_sub.order.add_edge(Spectroscopy_Test, Scientific_Tests)

# Provenance Search branch: Archival Review after Provenance Search
prov_sub = StrictPartialOrder(nodes=[Provenance_Search, Archival_Review])
prov_sub.order.add_edge(Provenance_Search, Archival_Review)

# Combine Provenance Search, Conflict Check, Expert Panel in sequence:
# Provenance Review (the above), then Conflict Check, then Expert Panel
prov_review_seq = StrictPartialOrder(
    nodes=[prov_sub, Conflict_Check, Expert_Panel]
)
prov_review_seq.order.add_edge(prov_sub, Conflict_Check)
prov_review_seq.order.add_edge(Conflict_Check, Expert_Panel)

# After Scientific Tests and Provenance Review & Expert Panel both done,
# proceed to Legal Clearance
# Scientific Tests and Provenance Review sequence are concurrent to each other.
# Model concurrency at root level, with Legal Clearance starting after both.

# We create a PO for (Scientific Tests branch) and (Prov Review branch) concurrent, both precede Legal Clearance
# Note prov_review_seq and sci_tests_sub are StrictPartialOrder themselves.
# To model their concurrency, put them as nodes in a new PO, with edges to Legal Clearance

legal_and_after = StrictPartialOrder(
    nodes=[Legal_Clearance, Export_Approval, Certification, Documentation, Data_Archiving, Client_Notification]
)
legal_and_after.order.add_edge(Legal_Clearance, Export_Approval)
legal_and_after.order.add_edge(Export_Approval, Certification)
legal_and_after.order.add_edge(Certification, Documentation)
legal_and_after.order.add_edge(Documentation, Data_Archiving)
legal_and_after.order.add_edge(Data_Archiving, Client_Notification)

# Root PO:
# Artifact Intake --> Condition Check --> Initial Screening
# After Initial Screening, two concurrent activities:
# 1) Scientific Tests subtree
# 2) Provenance review subtree (prov_review_seq)
# Both must be done before Legal Clearance and after

# Create PO for initial intake branch
initial_seq = StrictPartialOrder(
    nodes=[Artifact_Intake, Condition_Check, Initial_Screening]
)
initial_seq.order.add_edge(Artifact_Intake, Condition_Check)
initial_seq.order.add_edge(Condition_Check, Initial_Screening)

# Now, concurrency between scientific and provenance branches after Initial Screening
branches_after_init = StrictPartialOrder(
    nodes=[sci_tests_sub, prov_review_seq]
)
# no order edges between sci_tests_sub and prov_review_seq -> concurrency

# Now combine Initial Screening -> branches_after_init (both branches)
# This means Initial Screening precedes both branches
# We create a bigger PO:

middle_and_after = StrictPartialOrder(
    nodes=[Initial_Screening, sci_tests_sub, prov_review_seq]
)
middle_and_after.order.add_edge(Initial_Screening, sci_tests_sub)
middle_and_after.order.add_edge(Initial_Screening, prov_review_seq)

# Now, Legal Clearance can be done only after both sci_tests_sub and prov_review_seq complete
# So we create another PO combining those branches with legal_and_after
# edges from sci_tests_sub and prov_review_seq to Legal_Clearance in legal_and_after

# So extend legal_and_after nodes by adding sci_tests_sub and prov_review_seq as predecessors
legal_and_after_extended = StrictPartialOrder(
    nodes=[sci_tests_sub, prov_review_seq, Legal_Clearance, Export_Approval, Certification, Documentation, Data_Archiving, Client_Notification]
)
legal_and_after_extended.order.add_edge(sci_tests_sub, Legal_Clearance)
legal_and_after_extended.order.add_edge(prov_review_seq, Legal_Clearance)
legal_and_after_extended.order.add_edge(Legal_Clearance, Export_Approval)
legal_and_after_extended.order.add_edge(Export_Approval, Certification)
legal_and_after_extended.order.add_edge(Certification, Documentation)
legal_and_after_extended.order.add_edge(Documentation, Data_Archiving)
legal_and_after_extended.order.add_edge(Data_Archiving, Client_Notification)

# Finally, the full model combines:
# initial_seq --> middle_and_after (which starts from Initial Screening)
# We have initial_seq ending with Initial Screening, middle_and_after starting from Initial Screening again (duplicate node)
# To avoid duplication, we will merge the sequences:
# initial_seq till Condition Check,
# then put Initial Screening, after it two concurrent branches sci_tests_sub and prov_review_seq,
# and from those to legal_and_after nodes

# Create a new PO for initial part:
initial_part = StrictPartialOrder(
    nodes=[Artifact_Intake, Condition_Check, Initial_Screening]
)
initial_part.order.add_edge(Artifact_Intake, Condition_Check)
initial_part.order.add_edge(Condition_Check, Initial_Screening)

# The core concurrency is after Initial Screening:
# concurrent sci_tests_sub and prov_review_seq, which both precede Legal Clearance
# Then chain legal clearance and subsequent activities

# now root is:
nodes = [Artifact_Intake, Condition_Check, Initial_Screening,
         sci_tests_sub, prov_review_seq,
         Legal_Clearance, Export_Approval, Certification, Documentation, Data_Archiving, Client_Notification]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Artifact_Intake, Condition_Check)
root.order.add_edge(Condition_Check, Initial_Screening)

root.order.add_edge(Initial_Screening, sci_tests_sub)
root.order.add_edge(Initial_Screening, prov_review_seq)

root.order.add_edge(sci_tests_sub, Legal_Clearance)
root.order.add_edge(prov_review_seq, Legal_Clearance)

root.order.add_edge(Legal_Clearance, Export_Approval)
root.order.add_edge(Export_Approval, Certification)
root.order.add_edge(Certification, Documentation)
root.order.add_edge(Documentation, Data_Archiving)
root.order.add_edge(Data_Archiving, Client_Notification)