# Generated from: 88119865-248d-494e-a95c-ca07105b8f89.json
# Description: This process governs the authentication of rare historical artifacts before acquisition by museums or private collectors. It involves multidisciplinary verification steps including provenance validation, scientific material analysis, expert consultation, and legal compliance checks. Initial artifact intake triggers documentation and condition assessment, followed by imaging and spectroscopy tests. Concurrently, provenance research is conducted through archival records and ownership history. Expert panels review findings to confirm authenticity, while legal teams ensure clear title and export permissions. Any conflicting data initiates re-examination or rejection. Final approval leads to cataloging and secure storage, completing the authentication cycle with comprehensive reporting for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic transitions
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')
Imaging_Scan = Transition(label='Imaging Scan')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Provenance_Research = Transition(label='Provenance Research')
Archival_Review = Transition(label='Archival Review')
Ownership_Verify = Transition(label='Ownership Verify')
Expert_Panel = Transition(label='Expert Panel')
Data_Reconcile = Transition(label='Data Reconcile')
Legal_Review = Transition(label='Legal Review')
Export_Check = Transition(label='Export Check')
Conflict_Resolve = Transition(label='Conflict Resolve')
Final_Approval = Transition(label='Final Approval')
Catalog_Entry = Transition(label='Catalog Entry')
Secure_Storage = Transition(label='Secure Storage')
skip = SilentTransition()

# Imaging and Spectroscopy tests concurrent
imaging_tests = StrictPartialOrder(nodes=[Imaging_Scan, Spectroscopy_Test])
# no order edge means they are concurrent

# Provenance research includes Archival Review and Ownership Verify in parallel
provenance_research = StrictPartialOrder(nodes=[Archival_Review, Ownership_Verify])
# no order edge means they are concurrent

# Provenance Research node models the research step that includes the two nodes above
# We'll model the "Provenance Research" Activity concurrently with its subtasks (Archival Review + Ownership Verify)
# But to keep model clear, we will consider Provenance_Research as a parent step (a separate Transition),
# and model Archival_Review and Ownership_Verify as part of it
# The problem states: Provenance Research is conducted through Archival Review and Ownership Verify concurrently.
# So Provenance_Research is an atomic step "Provenance Research". We'll model that step concurrently with its subtasks to indicate they're performed concurrently.

# Following that interpretation:
provenance_research_po = StrictPartialOrder(nodes=[Provenance_Research, Archival_Review, Ownership_Verify])
# no order edges => all concurrent

# Expert Panel waits for Imaging + Spectroscopy + Provenance Research done (all those three)
# So Expert Panel depends on:
# - (Imaging_Scan and Spectroscopy_Test concurrent)
# - (Provenance_Research, Archival_Review, Ownership_Verify concurrent)
# So all those must finish before Expert_Panel

# Legal Review includes Legal_Review and Export_Check in parallel
legal_review_po = StrictPartialOrder(nodes=[Legal_Review, Export_Check])

# Data Reconcile follows Expert Panel and Legal Review
# then Data Reconcile check conflicts => on conflict, go to Conflict Resolve or reject (reject not modeled as activity, so assume Conflict_Resolve activity models response to conflict)
# Re-examination is represented by looping back
# Loop structure: after Data Reconcile, either exit or go Conflict_Resolve then back to Expert Panel and Legal Review

# Build the loop:
# Loop semantics: 
#  * (A, B)
#  means: execute A, then choose exit or execute B then A again.

# Let's define:
# A = partial order of Expert Panel and Legal Review followed by Data Reconcile
# B = Conflict Resolve

# Step A1: join Expert Panel and Legal Review
# Expert Panel depends on Imaging/Spectroscopy + Provenance Research

# Build sub-po for Imaging + Spectroscopy + Provenance Research nodes:
imaging_prov = StrictPartialOrder(
    nodes=[imaging_tests, provenance_research_po]
)
# imaging_tests and provenance_research_po are PO nodes themselves, so use them as nodes
# They are concurrent, so no order edges here.

# Expert Panel depends on both imaging_tests and provenance_research_po
expert_legal = StrictPartialOrder(
    nodes=[Expert_Panel, legal_review_po]
)
# no order edges => concurrent

# But Expert Panel depends on imaging_prov
# So Imaging_Prov order edges to Expert Panel:
# Because imaging_prov is a PO node (with subnodes concurrent), we must make expert_legal dependent on imaging_prov.

# So define A as a PO with nodes: imaging_tests, provenance_research_po, Expert_Panel, legal_review_po, Data_Reconcile
# With order edges:
# imaging_tests --> Expert_Panel
# provenance_research_po --> Expert_Panel
# Expert_Panel --> Data_Reconcile
# legal_review_po --> Data_Reconcile

A_nodes = [imaging_tests, provenance_research_po, Expert_Panel, legal_review_po, Data_Reconcile]
A = StrictPartialOrder(nodes=A_nodes)
# Add edges:
# imaging_tests --> Expert_Panel
A.order.add_edge(imaging_tests, Expert_Panel)
# provenance_research_po --> Expert_Panel
A.order.add_edge(provenance_research_po, Expert_Panel)
# legal_review_po --> Data_Reconcile
A.order.add_edge(legal_review_po, Data_Reconcile)
# Expert_Panel --> Data_Reconcile
A.order.add_edge(Expert_Panel, Data_Reconcile)

# B is Conflict_Resolve
B = Conflict_Resolve

# Loop: * (A, B)
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# After loop exit, Final Approval then Catalog Entry then Secure Storage sequentially
final_seq = StrictPartialOrder(nodes=[Final_Approval, Catalog_Entry, Secure_Storage])
final_seq.order.add_edge(Final_Approval, Catalog_Entry)
final_seq.order.add_edge(Catalog_Entry, Secure_Storage)

# Build initial steps before imaging etc:
# Artifact Intake --> Condition Check --> (imaging + spectroscopy) & provenance research concur concurrently
initial_seq = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check])
initial_seq.order.add_edge(Artifact_Intake, Condition_Check)

# Define concurrent node of initial_seq --> imaging_tests and provenance_research_po
# Condition_Check precedes imaging_tests and provenance_research_po concurrently

# So, new PO with initial_seq, imaging_tests, provenance_research_po
initial_with_tests = StrictPartialOrder(
    nodes=[initial_seq, imaging_tests, provenance_research_po]
)
# Add order edges:
# initial_seq --> imaging_tests
initial_with_tests.order.add_edge(initial_seq, imaging_tests)
# initial_seq --> provenance_research_po
initial_with_tests.order.add_edge(initial_seq, provenance_research_po)

# Next, imaging_tests and provenance_research_po are part of A (loop child),
# but here just order above.

# The overall graph:
# initial_with_tests --> loop --> final_seq

root = StrictPartialOrder(nodes=[initial_with_tests, loop, final_seq])
root.order.add_edge(initial_with_tests, loop)
root.order.add_edge(loop, final_seq)