# Generated from: 3a218297-cb5d-44bb-b1c6-8b131795ef69.json
# Description: This process involves meticulously tracing the origin, ownership, and transformation history of unique cultural artifacts as they move through various custodians, restoration phases, and exhibition venues. It includes authentication, condition assessment, multi-party negotiations, legal verifications, and secure transportation planning to ensure the artifact's integrity and provenance remain uncompromised while satisfying collectors, museums, and regulatory bodies. The process requires collaboration between historians, legal experts, conservators, and logistics teams to maintain a transparent, documented chain of custody over extended periods, often spanning multiple countries and jurisdictions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')
Origin_Research = Transition(label='Origin Research')
Ownership_Verify = Transition(label='Ownership Verify')
Legal_Review = Transition(label='Legal Review')
Restoration_Plan = Transition(label='Restoration Plan')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Log = Transition(label='Provenance Log')
Custody_Transfer = Transition(label='Custody Transfer')
Transport_Arrange = Transition(label='Transport Arrange')
Security_Brief = Transition(label='Security Brief')
Exhibit_Setup = Transition(label='Exhibit Setup')
Insurance_Update = Transition(label='Insurance Update')
Documentation = Transition(label='Documentation')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Final_Audit = Transition(label='Final Audit')

# Construct partial orders reflecting the logical and partially parallel structure

# After Artifact Intake, Condition Check, Origin Research, and Ownership Verify run in parallel (independent)
# Then, Legal Review depends on Ownership Verify
# Restoration Plan and Expert Consult after Condition Check and Legal Review (concurrent)
# Provenance Log after Origin Research and Restoration Plan
# Custody Transfer after Expert Consult and Provenance Log
# Transport Arrange and Security Brief in parallel after Custody Transfer
# Exhibit Setup after Transport Arrange and Security Brief
# Insurance Update and Documentation in parallel after Exhibit Setup
# Stakeholder Notify after Insurance Update and Documentation
# Final Audit after Stakeholder Notify

# Create a strict partial order with all nodes
nodes = [
    Artifact_Intake,
    Condition_Check,
    Origin_Research,
    Ownership_Verify,
    Legal_Review,
    Restoration_Plan,
    Expert_Consult,
    Provenance_Log,
    Custody_Transfer,
    Transport_Arrange,
    Security_Brief,
    Exhibit_Setup,
    Insurance_Update,
    Documentation,
    Stakeholder_Notify,
    Final_Audit
]

root = StrictPartialOrder(nodes=nodes)

# Add edges describing partial order dependencies
root.order.add_edge(Artifact_Intake, Condition_Check)  # Intake before Condition Check
root.order.add_edge(Artifact_Intake, Origin_Research)  # Intake before Origin Research
root.order.add_edge(Artifact_Intake, Ownership_Verify) # Intake before Ownership Verify

# Legal Review depends on Ownership Verify
root.order.add_edge(Ownership_Verify, Legal_Review)

# Restoration Plan depends on Condition Check and Legal Review
root.order.add_edge(Condition_Check, Restoration_Plan)
root.order.add_edge(Legal_Review, Restoration_Plan)

# Expert Consult depends on Condition Check and Legal Review
root.order.add_edge(Condition_Check, Expert_Consult)
root.order.add_edge(Legal_Review, Expert_Consult)

# Provenance Log depends on Origin Research and Restoration Plan
root.order.add_edge(Origin_Research, Provenance_Log)
root.order.add_edge(Restoration_Plan, Provenance_Log)

# Custody Transfer depends on Expert Consult and Provenance Log
root.order.add_edge(Expert_Consult, Custody_Transfer)
root.order.add_edge(Provenance_Log, Custody_Transfer)

# Transport Arrange and Security Brief depend on Custody Transfer, concurrent
root.order.add_edge(Custody_Transfer, Transport_Arrange)
root.order.add_edge(Custody_Transfer, Security_Brief)

# Exhibit Setup depends on both Transport Arrange and Security Brief
root.order.add_edge(Transport_Arrange, Exhibit_Setup)
root.order.add_edge(Security_Brief, Exhibit_Setup)

# Insurance Update and Documentation depend on Exhibit Setup, concurrent
root.order.add_edge(Exhibit_Setup, Insurance_Update)
root.order.add_edge(Exhibit_Setup, Documentation)

# Stakeholder Notify depends on Insurance Update and Documentation
root.order.add_edge(Insurance_Update, Stakeholder_Notify)
root.order.add_edge(Documentation, Stakeholder_Notify)

# Final Audit depends on Stakeholder Notify
root.order.add_edge(Stakeholder_Notify, Final_Audit)