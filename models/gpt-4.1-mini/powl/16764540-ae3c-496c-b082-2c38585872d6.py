# Generated from: 16764540-ae3c-496c-b082-2c38585872d6.json
# Description: This process governs the systematic exchange, validation, and monetization of intellectual assets between multiple stakeholders including creators, legal entities, and funding bodies. It involves ideation vetting, rights verification, cross-party negotiations, escrow management, and post-exchange auditing to ensure compliance, value integrity, and intellectual property protection. The process incorporates iterative feedback loops and conditional approvals to adapt dynamically to varying asset types and regulatory environments, fostering sustainable collaboration and innovation monetization within a controlled digital marketplace ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
IdeaCapture = Transition(label='Idea Capture')
AssetVetting = Transition(label='Asset Vetting')
RightsCheck = Transition(label='Rights Check')
ValueAssessment = Transition(label='Value Assessment')
StakeholderSync = Transition(label='Stakeholder Sync')
NegotiationRound = Transition(label='Negotiation Round')
ContractDraft = Transition(label='Contract Draft')
EscrowSetup = Transition(label='Escrow Setup')
FundingRelease = Transition(label='Funding Release')
IPTransfer = Transition(label='IP Transfer')
ComplianceAudit = Transition(label='Compliance Audit')
DisputeReview = Transition(label='Dispute Review')
FeedbackLoop = Transition(label='Feedback Loop')
PerformanceTrack = Transition(label='Performance Track')
RenewalReview = Transition(label='Renewal Review')
ArchivalStore = Transition(label='Archival Store')

# Silent step for internal exits/choices if needed
skip = SilentTransition()

# Loop for Feedback Loop and iterative approval cycle:
# After Dispute Review, there may be a Feedback Loop,
# so model (A=DisputeReview, B=FeedbackLoop) => Loop: Dispute Review, then choice: exit or Feedback Loop + Dispute Review again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[DisputeReview, FeedbackLoop])

# Renewal review and performance tracking loop to allow continuous monitoring and possible renewal
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[PerformanceTrack, RenewalReview])

# Negotiate and contract drafting choice, may repeat negotiations after Stakeholder Sync; 
# after StakeholderSync there is a choice: either proceed (ContractDraft) or do another NegotiationRound then ContractDraft again
negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[ContractDraft, NegotiationRound])

# After Asset Vetting and Rights Check, do Value Assessment, then Stakeholder Sync
# The loop on negotiation happens after Stakeholder Sync

# After Contract Drafting and Negotiations complete, Escrow Setup,
# Funding Release, IP Transfer occur in a sequence, then Compliance Audit

# After Compliance Audit, Dispute Review and feedback loop apply (already modeled)

# Finally, Archival Store at the end, after monitoring and renewal loop

# Define partial orders for sequences:

# 1. Early phase: Idea Capture -> Asset Vetting -> Rights Check -> Value Assessment -> Stakeholder Sync
early_phase = StrictPartialOrder(nodes=[
    IdeaCapture, AssetVetting, RightsCheck, ValueAssessment, StakeholderSync
])
early_phase.order.add_edge(IdeaCapture, AssetVetting)
early_phase.order.add_edge(AssetVetting, RightsCheck)
early_phase.order.add_edge(RightsCheck, ValueAssessment)
early_phase.order.add_edge(ValueAssessment, StakeholderSync)

# 2. Negotiation loop: Stakeholder Sync --> negotiation_loop
# negotiation_loop itself models looping contract draft + negotiation round
# negotiation_loop nodes are ContractDraft and NegotiationRound but wrapped
# The exit returns ContractDraft as last executed child, modeled internally

# 3. After negotiation_loop, Escrow Setup -> Funding Release -> IP Transfer
post_negotiation = StrictPartialOrder(nodes=[EscrowSetup, FundingRelease, IPTransfer])
post_negotiation.order.add_edge(EscrowSetup, FundingRelease)
post_negotiation.order.add_edge(FundingRelease, IPTransfer)

# 4. Compliance audit after IP Transfer
audit_phase = ComplianceAudit

# 5. Feedback loop after audit phase (feedback_loop defined above)

# 6. Monitoring loop for performance tracking and renewal review runs in parallel with Archival Store
# Model partial order with monitor_loop and Archival Store concurrent
archive_and_monitor = StrictPartialOrder(nodes=[monitor_loop, ArchivalStore])
# no order edges => concurrent

# Now compose the main sequence as:
# early_phase --> negotiation_loop --> post_negotiation --> audit_phase --> feedback_loop --> archive_and_monitor

# Combine early_phase and negotiation_loop
part1 = StrictPartialOrder(nodes=[early_phase, negotiation_loop])
part1.order.add_edge(early_phase, negotiation_loop)

# Combine part1 and post_negotiation
part2 = StrictPartialOrder(nodes=[part1, post_negotiation])
part2.order.add_edge(part1, post_negotiation)

# Combine part2 and audit_phase
part3 = StrictPartialOrder(nodes=[part2, audit_phase])
part3.order.add_edge(part2, audit_phase)

# Combine part3 and feedback_loop
part4 = StrictPartialOrder(nodes=[part3, feedback_loop])
part4.order.add_edge(part3, feedback_loop)

# Combine part4 and archive_and_monitor
root = StrictPartialOrder(nodes=[part4, archive_and_monitor])
root.order.add_edge(part4, archive_and_monitor)