# Generated from: 588bb0b2-97f5-494e-a0b4-4336924c2443.json
# Description: This process involves the complex validation and authentication of ancient artifacts within a museum's acquisition department. It includes steps such as provenance verification, material analysis, historical context research, and expert consultations. The workflow ensures that every artifact undergoes rigorous scrutiny before being approved for display or storage, considering both scientific and historical perspectives. The process integrates cross-disciplinary collaboration, digital record updates, and compliance with international cultural heritage laws, culminating in a final authentication report and database entry.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artifact_intake     = Transition(label='Artifact Intake')
initial_inspection  = Transition(label='Initial Inspection')
provenance_check    = Transition(label='Provenance Check')
material_sampling   = Transition(label='Material Sampling')
lab_analysis        = Transition(label='Lab Analysis')
historical_research = Transition(label='Historical Research')
expert_review       = Transition(label='Expert Review')
condition_assess    = Transition(label='Condition Assessment')
digital_imaging     = Transition(label='Digital Imaging')
cross_reference     = Transition(label='Cross-Reference')
legal_compliance    = Transition(label='Legal Compliance')
report_drafting     = Transition(label='Report Drafting')
stakeholder_meeting = Transition(label='Stakeholder Meeting')
final_approval      = Transition(label='Final Approval')
database_entry      = Transition(label='Database Entry')
storage_alloc       = Transition(label='Storage Allocation')
exhibit_planning    = Transition(label='Exhibit Planning')

# Silent skip transition for optional stakeholder meeting
skip = SilentTransition()

# XOR for optional stakeholder meeting
xor_meeting = OperatorPOWL(
    operator=Operator.XOR,
    children=[stakeholder_meeting, skip]
)

# XOR for final disposition: storage or exhibit
xor_disposition = OperatorPOWL(
    operator=Operator.XOR,
    children=[storage_alloc, exhibit_planning]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    initial_inspection,
    provenance_check,
    material_sampling,
    lab_analysis,
    historical_research,
    digital_imaging,
    condition_assess,
    cross_reference,
    expert_review,
    xor_meeting,
    legal_compliance,
    report_drafting,
    final_approval,
    database_entry,
    xor_disposition
])

# Define the ordering (arrows) among nodes
# Intake → Inspection
root.order.add_edge(artifact_intake, initial_inspection)

# Inspection → parallel validations
for nxt in [provenance_check, material_sampling, historical_research, digital_imaging, condition_assess]:
    root.order.add_edge(initial_inspection, nxt)

# Material Sampling → Lab Analysis
root.order.add_edge(material_sampling, lab_analysis)

# Historical Research & Provenance Check → Cross-Reference
root.order.add_edge(historical_research, cross_reference)
root.order.add_edge(provenance_check, cross_reference)

# Cross-Reference & Lab Analysis & Condition Assessment → Expert Review
root.order.add_edge(cross_reference, expert_review)
root.order.add_edge(lab_analysis, expert_review)
root.order.add_edge(condition_assess, expert_review)

# Expert Review → optional stakeholder meeting
root.order.add_edge(expert_review, xor_meeting)

# After meeting/skip → Legal Compliance
root.order.add_edge(xor_meeting, legal_compliance)

# Legal Compliance → Report Drafting → Final Approval
root.order.add_edge(legal_compliance, report_drafting)
root.order.add_edge(report_drafting, final_approval)

# Final Approval → Database Entry & final disposition (storage/exhibit)
root.order.add_edge(final_approval, database_entry)
root.order.add_edge(final_approval, xor_disposition)