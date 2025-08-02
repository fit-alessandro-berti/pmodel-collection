# Generated from: 53d1a04f-2d5b-4757-aabd-e0435ed0d0cd.json
# Description: This process outlines a structured, iterative approach to generating breakthrough innovations by combining insights and technologies from disparate industries. It begins with Opportunity Scouting to identify unconventional problem spaces, followed by Cross-Pollination Workshops where multidisciplinary teams brainstorm and exchange domain knowledge. Prototyping leverages rapid, low-fidelity models to test core concepts, while Feedback Loops gather both internal and external stakeholder inputs to refine ideas. Parallel Pathways run simultaneous experiments in different sectors, increasing the chance of success. The Validation Gate assesses feasibility and potential impact before scaling. Finally, Knowledge Capture ensures lessons learned are documented for future cycles, promoting continuous improvement and fostering a culture of sustainable innovation beyond typical R&D pipelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
OpportunityScout = Transition(label='Opportunity Scout')
IdeaHarvest = Transition(label='Idea Harvest')
CrossPollinate = Transition(label='Cross-Pollinate')
ConceptSketch = Transition(label='Concept Sketch')
RapidPrototype = Transition(label='Rapid Prototype')
StakeholderSync = Transition(label='Stakeholder Sync')
FeedbackLoop = Transition(label='Feedback Loop')
ParallelExperiment = Transition(label='Parallel Experiment')
RiskAssess = Transition(label='Risk Assess')
ValidationGate = Transition(label='Validation Gate')
ScalePlan = Transition(label='Scale Plan')
KnowledgeCapture = Transition(label='Knowledge Capture')
ResourceAlign = Transition(label='Resource Align')
PilotLaunch = Transition(label='Pilot Launch')
ImpactReview = Transition(label='Impact Review')
ContinuousIterate = Transition(label='Continuous Iterate')

# Loop body: iterative refinement
# Loop semantics: * (body, condition)
# Here body = (ResourceAlign -> PilotLaunch -> ImpactReview -> ContinuousIterate)
#   then choice to either exit or feedback loop again for refinement.

loop_body = StrictPartialOrder(nodes=[ResourceAlign, PilotLaunch, ImpactReview, ContinuousIterate])
loop_body.order.add_edge(ResourceAlign, PilotLaunch)
loop_body.order.add_edge(PilotLaunch, ImpactReview)
loop_body.order.add_edge(ImpactReview, ContinuousIterate)

# Condition branch for loop: feedback/refine
loop_condition = StrictPartialOrder(nodes=[FeedbackLoop])

# Define the loop: execute body, then either exit or do FeedbackLoop then body again
loop_iterate = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_condition])

# Parallel pathways: run experiments and risk assess simultaneously
parallel_paths = StrictPartialOrder(nodes=[ParallelExperiment, RiskAssess])
# No order edges, so they are concurrent

# Feedback loops activity includes Stakeholder Sync and Feedback Loop (sequential)
feedback_activities = StrictPartialOrder(nodes=[StakeholderSync, FeedbackLoop])
feedback_activities.order.add_edge(StakeholderSync, FeedbackLoop)

# Prototyping is: Concept Sketch -> Rapid Prototype (sequential)
prototyping = StrictPartialOrder(nodes=[ConceptSketch, RapidPrototype])
prototyping.order.add_edge(ConceptSketch, RapidPrototype)

# Cross-Pollination Workshops includes Idea Harvest and Cross-Pollinate concurrently
cross_pollination = StrictPartialOrder(nodes=[IdeaHarvest, CrossPollinate])
# No order edges, concurrent

# Initial phase: Opportunity Scout -> cross_pollination
initial_phase = StrictPartialOrder(nodes=[OpportunityScout, cross_pollination])
initial_phase.order.add_edge(OpportunityScout, cross_pollination)

# After Cross-Pollination come prototyping and feedback activities in sequence
proto_and_feedback = StrictPartialOrder(nodes=[prototyping, feedback_activities])
proto_and_feedback.order.add_edge(prototyping, feedback_activities)

# After feedback, parallel pathways run
proto_feedback_parallel = StrictPartialOrder(nodes=[proto_and_feedback, parallel_paths])
proto_feedback_parallel.order.add_edge(proto_and_feedback, parallel_paths)

# Validation and scaling after parallel paths
validation_and_scale = StrictPartialOrder(nodes=[ValidationGate, ScalePlan])
validation_and_scale.order.add_edge(ValidationGate, ScalePlan)

# Knowledge capture after scaling
knowledge_phase = KnowledgeCapture  # single activity

# Assemble the whole process in order:

# Phase 1: initial_phase
# Phase 2: proto_feedback_parallel
# Phase 3: validation_and_scale
# Phase 4: knowledge_capture
# Phase 5: loop_iterate (continuous improvement)

root = StrictPartialOrder(
    nodes=[
        initial_phase,
        proto_feedback_parallel,
        validation_and_scale,
        knowledge_phase,
        loop_iterate
    ]
)
root.order.add_edge(initial_phase, proto_feedback_parallel)
root.order.add_edge(proto_feedback_parallel, validation_and_scale)
root.order.add_edge(validation_and_scale, knowledge_phase)
root.order.add_edge(knowledge_phase, loop_iterate)