# Generated from: 43aac3a1-da0b-41c0-9429-9add62701c56.json
# Description: This process outlines a strategic approach for managing unforeseen crises affecting multiple business units and external stakeholders simultaneously. It involves rapid assessment, cross-functional coordination, resource reallocation, real-time communication through diverse channels, and iterative feedback loops. The goal is to minimize operational disruption, safeguard brand reputation, and ensure compliance with regulatory requirements by leveraging data analytics and stakeholder engagement strategies. This atypical yet realistic process integrates emergency protocols with business continuity planning in a dynamic environment requiring agility and precision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
AlertTrigger = Transition(label='Alert Trigger')
InitialAssess = Transition(label='Initial Assess')
StakeholderMap = Transition(label='Stakeholder Map')
ResourceCheck = Transition(label='Resource Check')
ImpactForecast = Transition(label='Impact Forecast')
TeamMobilize = Transition(label='Team Mobilize')
ChannelSetup = Transition(label='Channel Setup')
MessageDraft = Transition(label='Message Draft')
LegalReview = Transition(label='Legal Review')
SendAlerts = Transition(label='Send Alerts')
MonitorFeedback = Transition(label='Monitor Feedback')
DataAnalytics = Transition(label='Data Analytics')
AdjustStrategy = Transition(label='Adjust Strategy')
ExternalLiaise = Transition(label='External Liaise')
ReportCompile = Transition(label='Report Compile')
DebriefSession = Transition(label='Debrief Session')

# Build partial order for initial sequence up to mobilization:
# Alert Trigger -> Initial Assess -> Stakeholder Map -> Resource Check -> Impact Forecast -> Team Mobilize

init_seq = StrictPartialOrder(nodes=[AlertTrigger, InitialAssess, StakeholderMap, ResourceCheck, ImpactForecast, TeamMobilize])
init_seq.order.add_edge(AlertTrigger, InitialAssess)
init_seq.order.add_edge(InitialAssess, StakeholderMap)
init_seq.order.add_edge(StakeholderMap, ResourceCheck)
init_seq.order.add_edge(ResourceCheck, ImpactForecast)
init_seq.order.add_edge(ImpactForecast, TeamMobilize)

# Parallel after Team Mobilize:
# Two major branches run concurrently:
# 1) Communications branch: Channel Setup -> Message Draft -> Legal Review -> Send Alerts
# 2) Coordination branch: External Liaise and Data Analytics concurrent; then join for Report Compile
# Also, Monitor Feedback and Adjust Strategy form a loop for iterative feedback

# Construct communications partial order
communications = StrictPartialOrder(nodes=[ChannelSetup, MessageDraft, LegalReview, SendAlerts])
communications.order.add_edge(ChannelSetup, MessageDraft)
communications.order.add_edge(MessageDraft, LegalReview)
communications.order.add_edge(LegalReview, SendAlerts)

# Coordination partial order with concurrency: External Liaise and Data Analytics concurrent, then Report Compile
coordination = StrictPartialOrder(nodes=[ExternalLiaise, DataAnalytics, ReportCompile])
coordination.order.add_edge(ExternalLiaise, ReportCompile)
coordination.order.add_edge(DataAnalytics, ReportCompile)

# Feedback loop partial order:
# Loop body: Monitor Feedback then Adjust Strategy
# Initial part to enter the loop is Team Mobilize done (which we already sequence)
feedback_loop_body = StrictPartialOrder(nodes=[MonitorFeedback, AdjustStrategy])
feedback_loop_body.order.add_edge(MonitorFeedback, AdjustStrategy)

# The loop node: * (Monitor Feedback -> Adjust Strategy, silent exit)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop_body, SilentTransition()])

# After coordination and communications run in parallel, they converge into a join before Report Compile or separately?
# Report Compile is already after External Liaise and Data Analytics, included in coordination.
# We can compose overall parallel with coordination, communications, and feedback_loop.

# We form a PO of these three nodes concurrently:
parallel_nodes = [communications, coordination, feedback_loop]

# After they complete, the final step is Debrief Session
# So, Debrief Session depends on completion of communications, coordination, and feedback loop

final_PO = StrictPartialOrder(nodes=[init_seq, *parallel_nodes, ReportCompile, DebriefSession])

# Add order edges for the overall process:

# From init_seq (Team Mobilize) to start each parallel branch
final_PO.order.add_edge(init_seq, communications)
final_PO.order.add_edge(init_seq, coordination)
final_PO.order.add_edge(init_seq, feedback_loop)

# ReportCompile is in coordination already, but also present explicitly as node in final_PO,
# so link coordination to ReportCompile
final_PO.order.add_edge(coordination, ReportCompile)

# DebriefSession depends on ReportCompile and all parallel branches finishing:
# Link ReportCompile -> DebriefSession (already done)
final_PO.order.add_edge(ReportCompile, DebriefSession)

# Since feedback_loop can keep running asynchronously, but to finish the process,
# we require feedback loop to finish before DebriefSession:
final_PO.order.add_edge(feedback_loop, DebriefSession)

# Also communications completion before debriefing:
final_PO.order.add_edge(communications, DebriefSession)

root = final_PO