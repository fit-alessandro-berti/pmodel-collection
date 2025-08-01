# Generated from: 95684354-a48a-4f99-b20c-00b9200f0171.json
# Description: This process involves the identification, authentication, and acquisition of rare cultural artifacts from remote or politically sensitive regions. It requires coordination with historians, local authorities, and international legal bodies to ensure compliance with heritage laws. Detailed provenance research, risk assessment, and secure transport logistics are crucial to prevent fraud, damage, or legal disputes. Post-acquisition, artifacts undergo conservation evaluation and are prepared for either museum display or private collection. Due diligence includes ethical sourcing verification and ongoing monitoring of geopolitical factors affecting ownership rights. The entire workflow demands meticulous documentation, multi-party approvals, and contingency planning for unexpected regulatory changes or transport complications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
ArtifactScan = Transition(label='Artifact Scan')
ProvenanceCheck = Transition(label='Provenance Check')
LegalReview = Transition(label='Legal Review')
RiskAssess = Transition(label='Risk Assess')
LocalLiaison = Transition(label='Local Liaison')
PermitRequest = Transition(label='Permit Request')
FundingApproval = Transition(label='Funding Approval')
SecurePacking = Transition(label='Secure Packing')
TransportArrange = Transition(label='Transport Arrange')
CustomsClear = Transition(label='Customs Clear')
ConditionReport = Transition(label='Condition Report')
ConservationPlan = Transition(label='Conservation Plan')
ExhibitPrep = Transition(label='Exhibit Prep')
OwnershipAudit = Transition(label='Ownership Audit')
ComplianceVerify = Transition(label='Compliance Verify')
FinalDocumentation = Transition(label='Final Documentation')

# Step 1: Identification & info gathering
initial_po = StrictPartialOrder(nodes=[
    SiteSurvey,
    ArtifactScan,
    ProvenanceCheck,
    LegalReview,
    RiskAssess,
    LocalLiaison
])
# Partial order:
# SiteSurvey and ArtifactScan must happen first, leading to ProvenanceCheck & LegalReview
initial_po.order.add_edge(SiteSurvey, ProvenanceCheck)
initial_po.order.add_edge(ArtifactScan, ProvenanceCheck)
initial_po.order.add_edge(ProvenanceCheck, LegalReview)
initial_po.order.add_edge(LegalReview, RiskAssess)
initial_po.order.add_edge(LegalReview, LocalLiaison)  # Legal and local liaison can proceed concurrently after legal review

# Step 2: Permits and funding approval (run in parallel but both needed)
permits_funding_po = StrictPartialOrder(nodes=[
    PermitRequest,
    FundingApproval
])
# No order between PermitRequest and FundingApproval; concurrent activities

# Step 3: Packing and transport logistics and customs clearance in sequence
logistics_po = StrictPartialOrder(nodes=[
    SecurePacking,
    TransportArrange,
    CustomsClear
])
logistics_po.order.add_edge(SecurePacking, TransportArrange)
logistics_po.order.add_edge(TransportArrange, CustomsClear)

# Step 4: Post-acquisition evaluations (concurrent)
post_acq_po = StrictPartialOrder(nodes=[
    ConditionReport,
    ConservationPlan
])
# No order between them

# Step 5: Prepare exhibit or private collection (exclusive choice)
exhibit_or_private = OperatorPOWL(operator=Operator.XOR, children=[ExhibitPrep, OwnershipAudit])

# Step 6: Compliance verify and final documentation (sequence)
final_steps_po = StrictPartialOrder(nodes=[
    ComplianceVerify,
    FinalDocumentation
])
final_steps_po.order.add_edge(ComplianceVerify, FinalDocumentation)

# Step 7: Loop for ongoing monitoring + contingency planning modeled as loop over ComplianceVerify + silent "continue" (skip)
skip = SilentTransition()
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceVerify, skip])

# Combine post acquisition with loop and exhibit/private choice
post_process_po = StrictPartialOrder(nodes=[
    post_acq_po,
    exhibit_or_private,
    loop_monitoring,
    final_steps_po
])
# Ordering: ConditionReport and ConservationPlan before exhibit_or_private and loop_monitoring, which before final steps
post_process_po.order.add_edge(post_acq_po, exhibit_or_private)
post_process_po.order.add_edge(post_acq_po, loop_monitoring)
post_process_po.order.add_edge(exhibit_or_private, final_steps_po)
post_process_po.order.add_edge(loop_monitoring, final_steps_po)

# Step 8: Combine initial, permits/funding, logistics, post-acquisition/process final in a full partial order
root = StrictPartialOrder(nodes=[
    initial_po,
    permits_funding_po,
    logistics_po,
    post_process_po
])

# Ordering among these big phases:
# initial_po before permits/funding and logistics
root.order.add_edge(initial_po, permits_funding_po)
root.order.add_edge(initial_po, logistics_po)
# permits/funding before logistics (funding approval may be needed to start packing)
root.order.add_edge(permits_funding_po, logistics_po)
# logistics before post_process_po
root.order.add_edge(logistics_po, post_process_po)