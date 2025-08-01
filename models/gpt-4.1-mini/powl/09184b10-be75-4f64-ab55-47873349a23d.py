# Generated from: 09184b10-be75-4f64-ab55-47873349a23d.json
# Description: This process involves the authentication and provenance verification of rare artifacts, combining scientific analysis, historical research, and legal validation. The workflow includes initial artifact inspection, material composition testing, provenance tracing through archival databases, expert consultations, and legal ownership verification. Additional steps cover condition reporting, restoration assessment, forgery detection, and final certification issuance. This atypical process requires coordination between archaeologists, chemists, historians, legal experts, and conservators to ensure an artifact's authenticity and legality before it can be acquired or exhibited. The complex interplay of scientific, historical, and legal evaluations makes this process unique in the business context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
ArtifactIntake = Transition(label='Artifact Intake')
VisualScan = Transition(label='Visual Scan')
MaterialTest = Transition(label='Material Test')
DataLogging = Transition(label='Data Logging')
ArchiveSearch = Transition(label='Archive Search')
ExpertConsult = Transition(label='Expert Consult')
ConditionCheck = Transition(label='Condition Check')
ForgeryScan = Transition(label='Forgery Scan')
OwnershipCheck = Transition(label='Ownership Check')
LegalReview = Transition(label='Legal Review')
RestorationPlan = Transition(label='Restoration Plan')
ReportDraft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
ClientBrief = Transition(label='Client Brief')
FinalApproval = Transition(label='Final Approval')
ArtifactReturn = Transition(label='Artifact Return')

# Build partial orders for different subprocesses

# 1) Initial Inspection & Testing: Artifact Intake -> Visual Scan & Material Test in parallel -> Data Logging
initial_PO = StrictPartialOrder(nodes=[ArtifactIntake, VisualScan, MaterialTest, DataLogging])
initial_PO.order.add_edge(ArtifactIntake, VisualScan)
initial_PO.order.add_edge(ArtifactIntake, MaterialTest)
initial_PO.order.add_edge(VisualScan, DataLogging)
initial_PO.order.add_edge(MaterialTest, DataLogging)
# VisualScan and MaterialTest concurrent, both precede DataLogging

# 2) Provenance verification: Archive Search -> Expert Consult
provenance_PO = StrictPartialOrder(nodes=[ArchiveSearch, ExpertConsult])
provenance_PO.order.add_edge(ArchiveSearch, ExpertConsult)

# 3) Legal validation: Ownership Check -> Legal Review
legal_PO = StrictPartialOrder(nodes=[OwnershipCheck, LegalReview])
legal_PO.order.add_edge(OwnershipCheck, LegalReview)

# 4) Condition & Forgery checks: Condition Check -> Forgery Scan
condition_PO = StrictPartialOrder(nodes=[ConditionCheck, ForgeryScan])
condition_PO.order.add_edge(ConditionCheck, ForgeryScan)

# 5) Restoration & Reporting: Restoration Plan -> Report Draft
restoration_PO = StrictPartialOrder(nodes=[RestorationPlan, ReportDraft])
restoration_PO.order.add_edge(RestorationPlan, ReportDraft)

# 6) Final steps: Certification -> Client Brief -> Final Approval -> Artifact Return
final_PO = StrictPartialOrder(nodes=[Certification, ClientBrief, FinalApproval, ArtifactReturn])
final_PO.order.add_edge(Certification, ClientBrief)
final_PO.order.add_edge(ClientBrief, FinalApproval)
final_PO.order.add_edge(FinalApproval, ArtifactReturn)

# Combine provenance_PO, legal_PO, condition_PO to run in parallel after DataLogging
# They can be executed concurrently after DataLogging

# Create a partial order that runs these three parallel nodes (each a PO)
# To represent concurrency of these subprocesses after DataLogging, we embed them as nodes in a higher-level PO model.
# Because each is a partial order, they are nodes themselves.

# We create a partial order with nodes = [provenance_PO, legal_PO, condition_PO]
# No ordering edges, so they run concurrently
concurrent_checks_PO = StrictPartialOrder(nodes=[provenance_PO, legal_PO, condition_PO])

# Now, after concurrent_checks_PO finishes, Restoration & Reporting (restoration_PO) happens
# So connect concurrent_checks_PO -> restoration_PO

# Combine concurrent_checks_PO and restoration_PO sequentially
post_checks_PO = StrictPartialOrder(nodes=[concurrent_checks_PO, restoration_PO])
post_checks_PO.order.add_edge(concurrent_checks_PO, restoration_PO)

# After restoration_PO, final steps (final_PO) happen
post_restoration_PO = StrictPartialOrder(nodes=[post_checks_PO, final_PO])
post_restoration_PO.order.add_edge(post_checks_PO, final_PO)

# Overall process order:
# initial_PO -> post_restoration_PO
root = StrictPartialOrder(nodes=[initial_PO, post_restoration_PO])
root.order.add_edge(initial_PO, post_restoration_PO)