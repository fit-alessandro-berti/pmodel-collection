# Generated from: 16764540-ae3c-496c-b082-2c38585872d6.json
# Description: This process governs the systematic exchange, validation, and monetization of intellectual assets between multiple stakeholders including creators, legal entities, and funding bodies. It involves ideation vetting, rights verification, cross-party negotiations, escrow management, and post-exchange auditing to ensure compliance, value integrity, and intellectual property protection. The process incorporates iterative feedback loops and conditional approvals to adapt dynamically to varying asset types and regulatory environments, fostering sustainable collaboration and innovation monetization within a controlled digital marketplace ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
idea_capture    = Transition(label='Idea Capture')
asset_vetting   = Transition(label='Asset Vetting')
rights_check    = Transition(label='Rights Check')
value_assess    = Transition(label='Value Assessment')
stakeholder_sync= Transition(label='Stakeholder Sync')
negotiation     = Transition(label='Negotiation Round')
contract_draft  = Transition(label='Contract Draft')
escrow_setup    = Transition(label='Escrow Setup')
funding_release = Transition(label='Funding Release')
ip_transfer     = Transition(label='IP Transfer')
compliance_audit= Transition(label='Compliance Audit')
dispute_review  = Transition(label='Dispute Review')
feedback_loop   = Transition(label='Feedback Loop')
performance_tr  = Transition(label='Performance Track')
renewal_review  = Transition(label='Renewal Review')
archival_store  = Transition(label='Archival Store')

# Loop for value assessment with dispute resolution
value_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[value_assess, dispute_review]
)

# Loop for negotiation rounds with feedback
negotiation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[negotiation, feedback_loop]
)

# After performance tracking, either renewal or archival
post_perf_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[renewal_review, archival_store]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    idea_capture,
    asset_vetting,
    rights_check,
    value_loop,
    stakeholder_sync,
    negotiation_loop,
    contract_draft,
    escrow_setup,
    funding_release,
    ip_transfer,
    compliance_audit,
    performance_tr,
    post_perf_choice
])

# Define the control‐flow edges
root.order.add_edge(idea_capture, asset_vetting)
root.order.add_edge(asset_vetting, rights_check)
root.order.add_edge(rights_check, value_loop)
root.order.add_edge(value_loop, stakeholder_sync)
root.order.add_edge(stakeholder_sync, negotiation_loop)
root.order.add_edge(negotiation_loop, contract_draft)
root.order.add_edge(contract_draft, escrow_setup)
root.order.add_edge(escrow_setup, funding_release)
root.order.add_edge(funding_release, ip_transfer)
root.order.add_edge(ip_transfer, compliance_audit)
root.order.add_edge(compliance_audit, performance_tr)
root.order.add_edge(performance_tr, post_perf_choice)