# Generated from: 55a6c373-40fd-4a04-83fa-53ca3a2d38bb.json
# Description: This process involves coordinating a multi-phase campaign where influencers across different social media platforms collaborate to promote a product launch. It includes identifying niche influencers, negotiating collaborations, scheduling synchronized content releases, monitoring real-time engagement metrics, managing cross-platform content adaptations, and handling regulatory compliance checks for advertising standards. The process also requires crisis management protocols for negative feedback, iterative optimization based on analytics, and final reporting to stakeholders. Each step demands close communication between marketing, legal, and creative teams to ensure unified brand messaging and maximize campaign impact across diverse digital audiences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Influencer_Search = Transition(label='Influencer Search')
Profile_Vetting = Transition(label='Profile Vetting')
Collab_Invite = Transition(label='Collab Invite')
Contract_Draft = Transition(label='Contract Draft')
Content_Plan = Transition(label='Content Plan')
Schedule_Sync = Transition(label='Schedule Sync')
Content_Review = Transition(label='Content Review')
Platform_Adapt = Transition(label='Platform Adapt')
Launch_Monitor = Transition(label='Launch Monitor')
Engagement_Track = Transition(label='Engagement Track')
Feedback_Log = Transition(label='Feedback Log')
Crisis_Alert = Transition(label='Crisis Alert')
Optimize_Campaign = Transition(label='Optimize Campaign')
Compliance_Check = Transition(label='Compliance Check')
Final_Reporting = Transition(label='Final Reporting')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# Model the initial influencer coordination phase (search => vetting => invite => contract)
initial_PO = StrictPartialOrder(nodes=[Influencer_Search, Profile_Vetting, Collab_Invite, Contract_Draft])
initial_PO.order.add_edge(Influencer_Search, Profile_Vetting)
initial_PO.order.add_edge(Profile_Vetting, Collab_Invite)
initial_PO.order.add_edge(Collab_Invite, Contract_Draft)

# Content planning and scheduling phase (plan => schedule sync)
planning_PO = StrictPartialOrder(nodes=[Content_Plan, Schedule_Sync])
planning_PO.order.add_edge(Content_Plan, Schedule_Sync)

# Content review and platform adaptation are concurrent but ordered after scheduling sync
content_review = Content_Review
platform_adapt = Platform_Adapt
content_phase_PO = StrictPartialOrder(nodes=[Schedule_Sync, content_review, platform_adapt])
content_phase_PO.order.add_edge(Schedule_Sync, content_review)
content_phase_PO.order.add_edge(Schedule_Sync, platform_adapt)

# Launch monitoring and engagement tracking concurrent after adaptation/review
monitor_engage_PO = StrictPartialOrder(nodes=[Launch_Monitor, Engagement_Track])
# No direct order: concurrent

# Feedback log and crisis alert: crisis depends on feedback
feedback_PO = StrictPartialOrder(nodes=[Feedback_Log, Crisis_Alert])
feedback_PO.order.add_edge(Feedback_Log, Crisis_Alert)

# After crisis alert, iterative optimization can occur multiple times with monitoring and tracking
# Model iterative optimization loop:
# Loop body: Optimize Campaign (B)
# Loop entry: Launch Monitor + Engagement Track + Feedback Log + Crisis Alert + Compliance Check (A)
# The process after initial phases continues with a loop:
# Execute A = monitoring, engagement tracking, feedback, crisis, compliance check
# Then optional Optimize Campaign (B) then back to A, repeated until exit

# Group A nodes:
monitor_engage_feedback_PO = StrictPartialOrder(
    nodes=[Launch_Monitor, Engagement_Track, Feedback_Log, Crisis_Alert, Compliance_Check]
)
monitor_engage_feedback_PO.order.add_edge(Feedback_Log, Crisis_Alert)

# LOOP(A, B): A followed by optional B + A repeat

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_engage_feedback_PO, Optimize_Campaign]
)

# Final reporting and stakeholder meeting after loop
final_PO = StrictPartialOrder(nodes=[Final_Reporting, Stakeholder_Meet])
final_PO.order.add_edge(Final_Reporting, Stakeholder_Meet)

# Assemble overall partial order:
# initial_PO -> planning_PO -> content_phase_PO -> loop -> final_PO

root = StrictPartialOrder(
    nodes=[initial_PO, planning_PO, content_phase_PO, loop, final_PO]
)
root.order.add_edge(initial_PO, planning_PO)
root.order.add_edge(planning_PO, content_phase_PO)
root.order.add_edge(content_phase_PO, loop)
root.order.add_edge(loop, final_PO)