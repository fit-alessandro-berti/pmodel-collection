# Generated from: 55a6c373-40fd-4a04-83fa-53ca3a2d38bb.json
# Description: This process involves coordinating a multi-phase campaign where influencers across different social media platforms collaborate to promote a product launch. It includes identifying niche influencers, negotiating collaborations, scheduling synchronized content releases, monitoring real-time engagement metrics, managing cross-platform content adaptations, and handling regulatory compliance checks for advertising standards. The process also requires crisis management protocols for negative feedback, iterative optimization based on analytics, and final reporting to stakeholders. Each step demands close communication between marketing, legal, and creative teams to ensure unified brand messaging and maximize campaign impact across diverse digital audiences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
influencer_search   = Transition(label='Influencer Search')
profile_vetting     = Transition(label='Profile Vetting')
collab_invite       = Transition(label='Collab Invite')
contract_draft      = Transition(label='Contract Draft')
content_plan        = Transition(label='Content Plan')
schedule_sync       = Transition(label='Schedule Sync')
content_review      = Transition(label='Content Review')
platform_adapt      = Transition(label='Platform Adapt')
compliance_check    = Transition(label='Compliance Check')
launch_monitor      = Transition(label='Launch Monitor')
engagement_track    = Transition(label='Engagement Track')
feedback_log        = Transition(label='Feedback Log')
crisis_alert        = Transition(label='Crisis Alert')
optimize_campaign   = Transition(label='Optimize Campaign')
final_reporting     = Transition(label='Final Reporting')
stakeholder_meet    = Transition(label='Stakeholder Meet')

# Build the loop for feedback -> (crisis alert & optimize) -> feedback ...
# Loop children = [A, B] where
#   A = feedback_log
#   B = sequence(crisis_alert -> optimize_campaign)
body = StrictPartialOrder(nodes=[crisis_alert, optimize_campaign])
body.order.add_edge(crisis_alert, optimize_campaign)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_log, body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    influencer_search,
    profile_vetting,
    collab_invite,
    contract_draft,
    content_plan,
    schedule_sync,
    content_review,
    platform_adapt,
    compliance_check,
    launch_monitor,
    engagement_track,
    feedback_loop,
    final_reporting,
    stakeholder_meet
])

# Add control‐flow edges
root.order.add_edge(influencer_search,  profile_vetting)
root.order.add_edge(profile_vetting,    collab_invite)
root.order.add_edge(collab_invite,      contract_draft)
root.order.add_edge(contract_draft,     content_plan)
root.order.add_edge(content_plan,       schedule_sync)
root.order.add_edge(schedule_sync,      content_review)
root.order.add_edge(content_review,     platform_adapt)
root.order.add_edge(platform_adapt,     compliance_check)
root.order.add_edge(compliance_check,   launch_monitor)
root.order.add_edge(launch_monitor,     engagement_track)
root.order.add_edge(engagement_track,   feedback_loop)
root.order.add_edge(feedback_loop,      final_reporting)
root.order.add_edge(final_reporting,    stakeholder_meet)