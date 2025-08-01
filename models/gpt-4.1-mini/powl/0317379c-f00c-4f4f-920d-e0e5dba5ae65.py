# Generated from: 0317379c-f00c-4f4f-920d-e0e5dba5ae65.json
# Description: This process involves a cyclical approach to integrating innovations across unrelated industries by leveraging interdisciplinary research, rapid prototyping, stakeholder feedback, and adaptive scaling. It begins with trend scouting in distant markets, followed by hypothesis generation through collaborative workshops. Concepts are then validated using virtual simulations and limited real-world pilot programs. Feedback loops from diverse user groups are incorporated to refine the product or service continuously. After successful validation, a phased rollout is executed with ongoing performance analytics to ensure adaptability to evolving market conditions. This atypical process emphasizes iterative learning and cross-sector synergy to drive breakthrough innovations that traditional industry-specific pipelines might overlook.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
TrendScout = Transition(label='Trend Scout')
IdeaWorkshop = Transition(label='Idea Workshop')
ConceptDraft = Transition(label='Concept Draft')
SimulateModel = Transition(label='Simulate Model')
PilotLaunch = Transition(label='Pilot Launch')
UserFeedback = Transition(label='User Feedback')
DataAnalyze = Transition(label='Data Analyze')
DesignRework = Transition(label='Design Rework')
StakeholderMeet = Transition(label='Stakeholder Meet')
ScalePlan = Transition(label='Scale Plan')
MarketTest = Transition(label='Market Test')
PerformanceTrack = Transition(label='Performance Track')
RiskAssess = Transition(label='Risk Assess')
AdaptStrategy = Transition(label='Adapt Strategy')
FinalDeploy = Transition(label='Final Deploy')
PostReview = Transition(label='Post Review')

# 1) Initial sequence: Trend Scout -> Idea Workshop -> Concept Draft
initial_po = StrictPartialOrder(nodes=[TrendScout, IdeaWorkshop, ConceptDraft])
initial_po.order.add_edge(TrendScout, IdeaWorkshop)
initial_po.order.add_edge(IdeaWorkshop, ConceptDraft)

# 2) Validation via Simulate Model and Pilot Launch (concurrent)
validation_po = StrictPartialOrder(nodes=[SimulateModel, PilotLaunch])
# They can be concurrent => no order edges

# 3) Feedback loop: User Feedback -> Data Analyze -> Design Rework -> Stakeholder Meet (order)
feedback_loop_po = StrictPartialOrder(
    nodes=[UserFeedback, DataAnalyze, DesignRework, StakeholderMeet]
)
feedback_loop_po.order.add_edge(UserFeedback, DataAnalyze)
feedback_loop_po.order.add_edge(DataAnalyze, DesignRework)
feedback_loop_po.order.add_edge(DesignRework, StakeholderMeet)

# 4) Loop on the product design refinement:
# loop = loop body: design rework and stakeholder meet
design_refinement_loop_body = feedback_loop_po
# loop operator: * (body = design refinement, redo A = Concept Draft)
design_refinement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ConceptDraft, design_refinement_loop_body]
)
# This models: execute Concept Draft, then choose to exit or execute feedback loop and Concept Draft again

# 5) Rollout and monitoring phases (sequential)
rollout_po = StrictPartialOrder(
    nodes=[
        ScalePlan,
        MarketTest,
        PerformanceTrack,
        RiskAssess,
        AdaptStrategy,
        FinalDeploy,
        PostReview,
    ]
)
rollout_po.order.add_edge(ScalePlan, MarketTest)
rollout_po.order.add_edge(MarketTest, PerformanceTrack)
rollout_po.order.add_edge(PerformanceTrack, RiskAssess)
rollout_po.order.add_edge(RiskAssess, AdaptStrategy)
rollout_po.order.add_edge(AdaptStrategy, FinalDeploy)
rollout_po.order.add_edge(FinalDeploy, PostReview)

# 6) Combine validation steps concurrent with design refinement loop:
validation_and_refinement = StrictPartialOrder(
    nodes=[validation_po, design_refinement_loop]
)
# Concept Draft is inside design_refinement_loop so ensure initial ConceptDraft done before
# We link Concept Draft in initial_po to validation_and_refinement combined node:
# But here validation and refinement are concurrent after Concept Draft

# Convention: after initial_po (ending with ConceptDraft) we proceed to validation and refinement concurrently
# To represent concurrency of validation and refinement, combine them as nodes in a StrictPartialOrder with no order edges

validation_and_refinement = StrictPartialOrder(
    nodes=[validation_po, design_refinement_loop]
)
# no edges: concurrent

# 7) In the initial Partial Order, ConceptDraft finishes before validation_and_refinement
# So combine initial_po and validation_and_refinement in a top-level StrictPartialOrder
# with initial_po nodes and the validation_and_refinement node (as a single node)
# but StrictPartialOrder nodes require POWL nodes, operatorPOWL or transitions or PO's

top_level_first = StrictPartialOrder(
    nodes=[initial_po, validation_and_refinement]
)
top_level_first.order.add_edge(initial_po, validation_and_refinement)

# 8) Combine the entire sequence: 
# top_level_first --> rollout_po

root = StrictPartialOrder(
    nodes=[top_level_first, rollout_po]
)
root.order.add_edge(top_level_first, rollout_po)