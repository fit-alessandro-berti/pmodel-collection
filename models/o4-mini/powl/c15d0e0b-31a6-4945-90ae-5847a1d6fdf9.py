# Generated from: c15d0e0b-31a6-4945-90ae-5847a1d6fdf9.json
# Description: This process involves the verification and authentication of rare cultural artifacts before acquisition by a museum. It includes provenance research, material analysis, expert consultations, and digital replication for archival purposes. The process ensures authenticity, legal compliance, and preservation standards while coordinating with international regulatory bodies and insurance providers. Multiple interdisciplinary teams collaborate to mitigate risks and document findings in a secure database, enabling informed decision-making and public transparency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
InitialReview     = Transition(label='Initial Review')
ProvenanceCheck   = Transition(label='Provenance Check')
MaterialTesting   = Transition(label='Material Testing')
ExpertPanel       = Transition(label='Expert Panel')
LegalAudit        = Transition(label='Legal Audit')
InsuranceSetup    = Transition(label='Insurance Setup')
RiskAssessment    = Transition(label='Risk Assessment')
StakeholderMeet   = Transition(label='Stakeholder Meet')
ComplianceReview  = Transition(label='Compliance Review')
DigitalScan       = Transition(label='Digital Scan')
ReplicationDraft  = Transition(label='Replication Draft')
ArchivalEntry     = Transition(label='Archival Entry')
ConditionReport   = Transition(label='Condition Report')
FinalDocumentation= Transition(label='Final Documentation')
AcquisitionApproval = Transition(label='Acquisition Approval')
TransportArrange  = Transition(label='Transport Arrange')

# A silent skip for optional branches
skip = SilentTransition()

# 1. Initial parallel research: Initial Review -> {Provenance Check, Material Testing} concurrently
start_parallel = StrictPartialOrder(
    nodes=[InitialReview, ProvenanceCheck, MaterialTesting]
)
start_parallel.order.add_edge(InitialReview, ProvenanceCheck)
start_parallel.order.add_edge(InitialReview, MaterialTesting)

# 2. Expert sequence: Expert Panel --> Legal Audit
expert_seq = StrictPartialOrder(
    nodes=[ExpertPanel, LegalAudit]
)
expert_seq.order.add_edge(ExpertPanel, LegalAudit)

# 3. Choice: either do expert_seq or skip both
xor_expert = OperatorPOWL(
    operator=Operator.XOR,
    children=[expert_seq, skip]
)

# 4. Loop for digital replication: Digital Scan; then optionally Replication Draft + repeat
loop_replication = OperatorPOWL(
    operator=Operator.LOOP,
    children=[DigitalScan, ReplicationDraft]
)

# 5. Build the root partial order
root = StrictPartialOrder(
    nodes=[
        start_parallel,
        xor_expert,
        InsuranceSetup,
        RiskAssessment,
        StakeholderMeet,
        ComplianceReview,
        loop_replication,
        ArchivalEntry,
        ConditionReport,
        FinalDocumentation,
        AcquisitionApproval,
        TransportArrange
    ]
)

# 5a. Ordering from research to expert choice
root.order.add_edge(start_parallel, xor_expert)

# 5b. From expert decision to insurance, risk, stakeholder (concurrent)
for child in [InsuranceSetup, RiskAssessment, StakeholderMeet]:
    root.order.add_edge(xor_expert, child)

# 5c. All three complete before compliance review
for child in [InsuranceSetup, RiskAssessment, StakeholderMeet]:
    root.order.add_edge(child, ComplianceReview)

# 5d. Compliance -> replication loop -> archival entry -> condition -> final doc -> approval -> transport
root.order.add_edge(ComplianceReview, loop_replication)
root.order.add_edge(loop_replication, ArchivalEntry)
root.order.add_edge(ArchivalEntry, ConditionReport)
root.order.add_edge(ConditionReport, FinalDocumentation)
root.order.add_edge(FinalDocumentation, AcquisitionApproval)
root.order.add_edge(AcquisitionApproval, TransportArrange)