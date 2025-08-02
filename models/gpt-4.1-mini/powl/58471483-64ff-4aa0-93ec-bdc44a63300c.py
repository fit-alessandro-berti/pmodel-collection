# Generated from: 58471483-64ff-4aa0-93ec-bdc44a63300c.json
# Description: This process manages an adaptive art auction where artworks are dynamically evaluated and re-categorized based on real-time bidder interest and external market trends. It involves continuous data collection from bidders, automated artwork reclassification, targeted marketing campaigns, and iterative reserve price adjustments. The process also integrates expert appraisals triggered by unusual bidding patterns and coordinates logistics for art delivery only after final payment confirmation, ensuring security and compliance with international art trade regulations. Throughout, a feedback loop engages artists and collectors to refine future auction strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

CollectBids = Transition(label='Collect Bids')
AnalyzeTrends = Transition(label='Analyze Trends')
ReclassifyArt = Transition(label='Reclassify Art')
AdjustReserves = Transition(label='Adjust Reserves')
TriggerAppraisal = Transition(label='Trigger Appraisal')
NotifyBidders = Transition(label='Notify Bidders')
LaunchCampaign = Transition(label='Launch Campaign')
MonitorEngagement = Transition(label='Monitor Engagement')
ValidatePayments = Transition(label='Validate Payments')
ScheduleDelivery = Transition(label='Schedule Delivery')
ConfirmCompliance = Transition(label='Confirm Compliance')
UpdateCatalog = Transition(label='Update Catalog')
GatherFeedback = Transition(label='Gather Feedback')
RefineStrategy = Transition(label='Refine Strategy')
ArchiveRecords = Transition(label='Archive Records')

# Expert appraisal triggered by unusual bidding pattern is a choice (trigger or not)
AppraisalChoice = OperatorPOWL(operator=Operator.XOR, children=[TriggerAppraisal, SilentTransition()])

# Marketing campaign with notification and monitoring in sequence
# Use strict partial order for campaign flow: LaunchCampaign --> NotifyBidders --> MonitorEngagement
MarketingPO = StrictPartialOrder(nodes=[LaunchCampaign, NotifyBidders, MonitorEngagement])
MarketingPO.order.add_edge(LaunchCampaign, NotifyBidders)
MarketingPO.order.add_edge(NotifyBidders, MonitorEngagement)

# Logistics after final payment validation and compliance confirmation:
# Sequential order: ValidatePayments --> ScheduleDelivery --> ConfirmCompliance
LogisticsPO = StrictPartialOrder(nodes=[ValidatePayments, ScheduleDelivery, ConfirmCompliance])
LogisticsPO.order.add_edge(ValidatePayments, ScheduleDelivery)
LogisticsPO.order.add_edge(ScheduleDelivery, ConfirmCompliance)

# Feedback loop engaging artists and collectors for refining strategies:
# Loop (GatherFeedback, RefineStrategy)
FeedbackLoop = OperatorPOWL(operator=Operator.LOOP, children=[GatherFeedback, RefineStrategy])

# The core adaptive auction flow:
# Collect bids --> Analyze trends --> Reclassify art --> Adjust reserves
CoreFlow = StrictPartialOrder(nodes=[CollectBids, AnalyzeTrends, ReclassifyArt, AdjustReserves])
CoreFlow.order.add_edge(CollectBids, AnalyzeTrends)
CoreFlow.order.add_edge(AnalyzeTrends, ReclassifyArt)
CoreFlow.order.add_edge(ReclassifyArt, AdjustReserves)

# After adjusting reserves, optionally trigger appraisal (choice)
AdjustAndAppraise = StrictPartialOrder(nodes=[CoreFlow, AppraisalChoice])
AdjustAndAppraise.order.add_edge(CoreFlow, AppraisalChoice)

# Bring together the marketing campaign and logistics -- can be concurrent after appraisal step
# So marketing and logistics can run concurrently
# Use a PO with nodes = MarketingPO, LogisticsPO, UpdateCatalog, ArchiveRecords and feedback loop
# Before marketing and logistics start, appraisal step must be finished

# Update catalog and archive records happen after appraisals and logistics complete
PostLogisticsPO = StrictPartialOrder(nodes=[UpdateCatalog, ArchiveRecords])
# ArchiveRecords depends on UpdateCatalog (serial)
PostLogisticsPO.order.add_edge(UpdateCatalog, ArchiveRecords)

# Combine Marketing, Logistics, PostLogistics, and FeedbackLoop concurrently (no order among them)
ConcurrentAfterAppraisal = StrictPartialOrder(
    nodes=[MarketingPO, LogisticsPO, PostLogisticsPO, FeedbackLoop]
)

# The root partial order:
# CoreFlow and appraisal step
# Then ConcurrentAfterAppraisal
root = StrictPartialOrder(
    nodes=[AdjustAndAppraise, ConcurrentAfterAppraisal]
)
root.order.add_edge(AdjustAndAppraise, ConcurrentAfterAppraisal)