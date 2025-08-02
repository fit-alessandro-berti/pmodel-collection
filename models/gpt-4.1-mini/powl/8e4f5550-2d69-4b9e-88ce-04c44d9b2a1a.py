# Generated from: 8e4f5550-2d69-4b9e-88ce-04c44d9b2a1a.json
# Description: This process involves synchronizing compliance standards and regulatory requirements across multiple independent business entities operating in different jurisdictions. It includes the collection and validation of legal documents, risk assessment alignment, multi-source data reconciliation, inter-entity audit coordination, and continuous monitoring for regulatory updates. The process ensures unified compliance reporting, conflict resolution between jurisdictional mandates, and the implementation of corrective actions while maintaining data privacy and security protocols. Stakeholders from legal, IT, and operational departments collaborate through automated and manual checkpoints to guarantee seamless compliance adherence and to mitigate potential liabilities arising from cross-border operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
Document_Review = Transition(label='Document Review')
Data_Collection = Transition(label='Data Collection')
Risk_Mapping = Transition(label='Risk Mapping')
Compliance_Audit = Transition(label='Compliance Audit')
Legal_Validation = Transition(label='Legal Validation')
Policy_Alignment = Transition(label='Policy Alignment')
Conflict_Check = Transition(label='Conflict Check')
Report_Generation = Transition(label='Report Generation')
Update_Monitoring = Transition(label='Update Monitoring')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Issue_Escalation = Transition(label='Issue Escalation')
Corrective_Action = Transition(label='Corrective Action')
Data_Encryption = Transition(label='Data Encryption')
Crosscheck_Entries = Transition(label='Crosscheck Entries')
Final_Approval = Transition(label='Final Approval')

# Partial order for initial document preparation and validation steps happening in partial order:
# Document Review and Data Collection can be concurrent
# Crosscheck Entries depends on Data Collection
# Legal Validation depends on Document Review
# Risk Mapping depends on Legal Validation
initial_preparation = StrictPartialOrder(nodes=[
    Document_Review, Data_Collection, Crosscheck_Entries, Legal_Validation, Risk_Mapping
])
initial_preparation.order.add_edge(Data_Collection, Crosscheck_Entries)
initial_preparation.order.add_edge(Document_Review, Legal_Validation)
initial_preparation.order.add_edge(Legal_Validation, Risk_Mapping)

# Compliance audit depends on Risk Mapping
# Policy Alignment depends on Risk Mapping
audit_alignment = StrictPartialOrder(nodes=[Compliance_Audit, Policy_Alignment])
# Both depend on Risk Mapping (add edges from Risk_Mapping nodes outside the PO, will connect later)

# Conflict Check follows Policy Alignment
conflict_check = Conflict_Check

# Report Generation depends on Compliance Audit and Conflict Check
report_generation = Report_Generation

# Update Monitoring runs concurrently to Stakeholder Sync,
# and is repeated as a loop that can trigger Issue Escalation and Corrective Action
# Loop: Update Monitoring then choose to exit or do Issue Escalation + Corrective Action then loop again
update_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Update_Monitoring,
        StrictPartialOrder(nodes=[Issue_Escalation, Corrective_Action])
    ]
)

# Stakeholder Sync can be concurrent with update_loop except Sync depends on Policy Alignment
stakeholder_sync = Stakeholder_Sync

# Data Encryption happens just before Final Approval (security protocols)
data_security = Data_Encryption

# Final Approval after Report Generation and Data Encryption
final_approval = Final_Approval

# Build partial order for final phases: Report Generation -> Data Encryption -> Final Approval
final_phase = StrictPartialOrder(nodes=[report_generation, data_security, final_approval])
final_phase.order.add_edge(report_generation, data_security)
final_phase.order.add_edge(data_security, final_approval)

# Compose partial orders and operators into one big partial order

# Collect nodes
nodes = [
    initial_preparation,
    audit_alignment,
    conflict_check,
    report_generation,
    update_loop,
    stakeholder_sync,
    data_security,
    final_approval,
    final_phase  # final_phase holds report_generation, data_security, final_approval (redundant, remove below)
]

# Actually we integrated report_generation, data_security, final_approval inside final_phase, no need to double add
# So let's reconstruct carefully:

# initial_preparation (with Document Review, Data Collection, Crosscheck Entries, Legal Validation, Risk Mapping)
# audit_alignment (Compliance Audit, Policy Alignment)
# conflict_check (single node)
# update_loop (loop node)
# stakeholder_sync (single node)
# final_phase (Report Generation, Data Encryption, Final Approval)

# Build root PO:
root = StrictPartialOrder(nodes=[
    initial_preparation,
    audit_alignment,
    conflict_check,
    update_loop,
    stakeholder_sync,
    final_phase
])

# Add the order dependencies between these nodes/POWLs:
# - Risk Mapping (in initial_preparation) -> audit_alignment nodes (Compliance Audit, Policy Alignment)
# Since these are inside nodes, add edges from initial_preparation to audit_alignment:
root.order.add_edge(initial_preparation, audit_alignment)

# Policy Alignment (inside audit_alignment) -> Conflict Check
root.order.add_edge(audit_alignment, conflict_check)

# Compliance Audit (audit_alignment) and Conflict Check -> Report Generation (final_phase contains it)
root.order.add_edge(audit_alignment, final_phase)
root.order.add_edge(conflict_check, final_phase)

# Policy Alignment -> Stakeholder Sync
root.order.add_edge(audit_alignment, stakeholder_sync)

# Stakeholder Sync and update_loop concurrent, no ordering

# Report Generation(inside final_phase) -> Data Encryption and Final Approval handled inside final_phase

# Data Encryption before Final Approval inside final_phase handled inside

# Stakeholder Sync and update_loop loosely synchronized, no order

# Add within update_loop the internal edge for loop structure:
# (loop children: Update Monitoring then choice of exit or Issue Escalation + Corrective Action then back)

# No extra edges needed at this level, LOOP operator semantics handle that.

# Lastly, Security protocols - Data Encryption happens just before Final Approval (inside final_phase),
# already modeled inside final_phase partial order.

# That completes the model.
