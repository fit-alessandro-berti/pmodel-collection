# Generated from: e5f30513-2f2d-4e30-a95f-d16edc56a39e.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts for a high-profile auction house. It begins with initial artifact intake and preliminary inspection, followed by provenance verification through archival research. Scientific analysis, including material composition and radiocarbon dating, is conducted to confirm authenticity. Parallelly, expert consultations are arranged to assess stylistic and cultural relevance. Findings are compiled into a comprehensive report, reviewed internally, and then presented to the client. Final approval triggers secure packaging and logistics coordination for transport to the auction venue. Throughout, strict chain-of-custody protocols ensure artifact integrity and legal compliance, minimizing risks of forgery or damage during handling and transit.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Intake_Review = Transition(label='Intake Review')
Preliminary_Inspect = Transition(label='Preliminary Inspect')
Provenance_Check = Transition(label='Provenance Check')
Archival_Research = Transition(label='Archival Research')
Material_Testing = Transition(label='Material Testing')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Stylistic_Assess = Transition(label='Stylistic Assess')
Expert_Consult = Transition(label='Expert Consult')
Findings_Compile = Transition(label='Findings Compile')
Internal_Review = Transition(label='Internal Review')
Client_Present = Transition(label='Client Present')
Approval_Confirm = Transition(label='Approval Confirm')
Secure_Package = Transition(label='Secure Package')
Transport_Arrange = Transition(label='Transport Arrange')
Chain_Custody = Transition(label='Chain Custody')

# Provenance verification: Provenance Check -> Archival Research (sequential)
provenance = StrictPartialOrder(nodes=[Provenance_Check, Archival_Research])
provenance.order.add_edge(Provenance_Check, Archival_Research)

# Scientific analysis parallel activities: Material Testing and Radiocarbon Date (concurrent)
scientific_analysis = StrictPartialOrder(nodes=[Material_Testing, Radiocarbon_Date])
# no edges (concurrent)

# Expert consultations parallel activities: Stylistic Assess and Expert Consult (concurrent)
expert_consult = StrictPartialOrder(nodes=[Stylistic_Assess, Expert_Consult])
# no edges (concurrent)

# Parallel block for scientific analysis and expert consultations (both concurrent)
parallel_analyses = StrictPartialOrder(nodes=[scientific_analysis, expert_consult])
# no edges (concurrent)

# Compile findings and review sequence
findings_review = StrictPartialOrder(nodes=[Findings_Compile, Internal_Review])
findings_review.order.add_edge(Findings_Compile, Internal_Review)

# Present and approval sequence
present_approval = StrictPartialOrder(nodes=[Client_Present, Approval_Confirm])
present_approval.order.add_edge(Client_Present, Approval_Confirm)

# Packaging and transport sequence
pack_transport = StrictPartialOrder(nodes=[Secure_Package, Transport_Arrange])
pack_transport.order.add_edge(Secure_Package, Transport_Arrange)

# Chain Custody is a strict protocol running throughout; model as first and then concurrent with
# other nodes to simplify we put Chain Custody first and link to Intake Review so it precedes all
# or model it as concurrent after Intake Review for simplicity:
# Chain Custody starts with Intake Review, likely continuous, so place Chain Custody parallel with
# the rest after Intake Review; but since chain custody spans entire flow,
# best to place it concurrent to the rest but after Intake Review

# Initial sequential Intake Review -> Preliminary Inspect
initial_review = StrictPartialOrder(nodes=[Intake_Review, Preliminary_Inspect])
initial_review.order.add_edge(Intake_Review, Preliminary_Inspect)

# Provenance verification after prelim inspect
provenance_block = provenance

# After provenance we do scientific and expert consult analyses in parallel
# Then findings compile and internal review
# Then client present and approval confirm
# Then packaging and transport

# Create the main strict partial order with all top-level elements
# We'll have nodes:
#  - initial_review (which is a StrictPartialOrder)
#  - provenance_block
#  - parallel_analyses
#  - findings_review
#  - present_approval
#  - pack_transport
#  - Chain_Custody

# But StrictPartialOrder expects nodes to be POWL elements (activities or operators or SPOs)

# Let's organize the big flow:

# Step 1: initial_review
# Step 2: provenance_block
# Step 3: parallel_analyses
# Step 4: findings_review
# Step 5: present_approval
# Step 6: pack_transport

# Chain Custody (continuous) - model as concurrent with steps 2..6,
# but must start after Intake Review (so after initial_review starts) - 
# for simplicity, place Chain Custody concurrent with provenance_block and onwards
# by making it a node linked from Intake Review (or prelim) to chain custody and chain custody concurrently with other steps

# Because we cannot express full continuous concurrency, we simplify placing Chain_Custody as concurrent with everything after Preliminary Inspect

# Compose a PO with:

# Nodes: initial_review, Chain_Custody, provenance_block, parallel_analyses, findings_review, present_approval, pack_transport

# Edges:

# initial_review --> Chain_Custody
# initial_review --> provenance_block
# Chain_Custody concurrent with provenance_block and rest (no edges)

# provenance_block --> parallel_analyses
# parallel_analyses --> findings_review
# findings_review --> present_approval
# present_approval --> pack_transport

root = StrictPartialOrder(
    nodes=[
        initial_review,
        Chain_Custody,
        provenance_block,
        parallel_analyses,
        findings_review,
        present_approval,
        pack_transport,
    ]
)

root.order.add_edge(initial_review, Chain_Custody)
root.order.add_edge(initial_review, provenance_block)
root.order.add_edge(provenance_block, parallel_analyses)
root.order.add_edge(parallel_analyses, findings_review)
root.order.add_edge(findings_review, present_approval)
root.order.add_edge(present_approval, pack_transport)