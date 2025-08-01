# Generated from: 0618ba6c-cd5e-4205-9b89-fd41ef27e339.json
# Description: This process outlines a dynamic and iterative approach to entering new international markets where traditional linear strategies are insufficient. It combines real-time market sensing, rapid prototyping of localized offerings, continuous stakeholder feedback loops, regulatory navigation, and adaptive resource allocation to optimize market fit and minimize entry risks. The process involves cross-functional collaboration between marketing, legal, product development, and local partners, ensuring responsiveness to emerging challenges and opportunities. It requires constant data-driven adjustments to the go-to-market plan based on evolving customer preferences, competitor moves, and regulatory changes, ultimately enabling faster and more sustainable market penetration in volatile environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
MarketScan = Transition(label='Market Scan')
RegulatoryMap = Transition(label='Regulatory Map')
StakeholderSync = Transition(label='Stakeholder Sync')
RiskAssess = Transition(label='Risk Assess')
LocalPartner = Transition(label='Local Partner')
PrototypeBuild = Transition(label='Prototype Build')
TestLaunch = Transition(label='Test Launch')
CustomerPoll = Transition(label='Customer Poll')
DataReview = Transition(label='Data Review')
PlanAdjust = Transition(label='Plan Adjust')
ResourceShift = Transition(label='Resource Shift')
ComplianceCheck = Transition(label='Compliance Check')
CompetitorWatch = Transition(label='Competitor Watch')
FeedbackLoop = Transition(label='Feedback Loop')
FinalRollout = Transition(label='Final Rollout')
PostLaunch = Transition(label='Post Launch')

skip = SilentTransition()

# Model the adaptive feedback loop as a LOOP:
# A = Data-driven adjustment steps: CustomerPoll -> DataReview -> PlanAdjust -> ResourceShift
# B = FeedbackStep: FeedbackLoop (which leads back to A)
# The loop is (* (A, B))
A_loop = StrictPartialOrder(
    nodes=[CustomerPoll, DataReview, PlanAdjust, ResourceShift],
)
A_loop.order.add_edge(CustomerPoll, DataReview)
A_loop.order.add_edge(DataReview, PlanAdjust)
A_loop.order.add_edge(PlanAdjust, ResourceShift)

# B child is FeedbackLoop activity
B_loop = FeedbackLoop

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Overall sequence partial order:
# Start: Market Scan
# Concurrent: Regulatory Map and Competitor Watch can be done in parallel after Market Scan
# Then Stakeholder Sync must happen after Market Scan, Regulatory Map, Competitor Watch
# Then Risk Assess after Stakeholder Sync
# Then Local Partner, Prototype Build, Compliance Check proceed concurrently after Risk Assess
# Then Test Launch after Prototype Build
# Then the feedback loop occurs after Test Launch and Compliance Check both have completed
# After the feedback loop finish, Final Rollout happens
# Finally Post Launch happens after Final Rollout

root = StrictPartialOrder(
    nodes=[
        MarketScan, RegulatoryMap, CompetitorWatch,
        StakeholderSync, RiskAssess,
        LocalPartner, PrototypeBuild, ComplianceCheck,
        TestLaunch,
        feedback_loop,
        FinalRollout,
        PostLaunch
    ]
)

# Add order edges based on above description

# Market Scan precedes Regulatory Map, Competitor Watch, Stakeholder Sync
root.order.add_edge(MarketScan, RegulatoryMap)
root.order.add_edge(MarketScan, CompetitorWatch)
root.order.add_edge(MarketScan, StakeholderSync)

# Regulatory Map and Competitor Watch precede Stakeholder Sync
root.order.add_edge(RegulatoryMap, StakeholderSync)
root.order.add_edge(CompetitorWatch, StakeholderSync)

# Stakeholder Sync precedes Risk Assess
root.order.add_edge(StakeholderSync, RiskAssess)

# Risk Assess precedes Local Partner, Prototype Build, Compliance Check in parallel
root.order.add_edge(RiskAssess, LocalPartner)
root.order.add_edge(RiskAssess, PrototypeBuild)
root.order.add_edge(RiskAssess, ComplianceCheck)

# Prototype Build precedes Test Launch
root.order.add_edge(PrototypeBuild, TestLaunch)

# Test Launch and Compliance Check both precede feedback loop
root.order.add_edge(TestLaunch, feedback_loop)
root.order.add_edge(ComplianceCheck, feedback_loop)

# Feedback loop precedes Final Rollout
root.order.add_edge(feedback_loop, FinalRollout)

# Final Rollout precedes Post Launch
root.order.add_edge(FinalRollout, PostLaunch)