# Generated from: ebe69634-86f5-4294-9a1c-020b1fb61df4.json
# Description: This process involves brokering custom artificial intelligence models between specialized developers and niche industry clients. It starts with client requirements gathering, followed by matching suitable AI developers with specific domain expertise. After initial vetting, prototype models are created and iteratively refined through collaborative feedback loops. Licensing agreements and intellectual property negotiations take place before final deployment. Post-deployment monitoring and optimization services ensure models remain effective. The process integrates legal, technical, and commercial teams to balance innovation with compliance, resulting in tailored AI solutions delivered through a secure and transparent platform.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ClientIntake    = Transition(label='Client Intake')
NeedsAnalysis  = Transition(label='Needs Analysis')
DeveloperMatch  = Transition(label='Developer Match')
ExpertVetting   = Transition(label='Expert Vetting')

PrototypeBuild  = Transition(label='Prototype Build')
FeedbackLoop    = Transition(label='Feedback Loop')
ModelRefinement = Transition(label='Model Refinement')

LicenseDraft    = Transition(label='License Draft')
IPNegotiation   = Transition(label='IP Negotiation')
ComplianceCheck = Transition(label='Compliance Check')
ContractSign    = Transition(label='Contract Sign')

FinalReview     = Transition(label='Final Review')
DeploymentPrep  = Transition(label='Deployment Prep')
GoLive          = Transition(label='Go Live')

MonitorModel    = Transition(label='Monitor Model')
OptimizeAI      = Transition(label='Optimize AI')
SupportHandoff  = Transition(label='Support Handoff')

# Build the iterative prototyping loop:
#   PrototypeBuild; then either exit or do (FeedbackLoop -> ModelRefinement) and repeat
loop_body = StrictPartialOrder(nodes=[FeedbackLoop, ModelRefinement])
loop_body.order.add_edge(FeedbackLoop, ModelRefinement)

prototype_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[PrototypeBuild, loop_body]
)

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    ClientIntake,
    NeedsAnalysis,
    DeveloperMatch,
    ExpertVetting,
    prototype_loop,
    LicenseDraft,
    IPNegotiation,
    ComplianceCheck,
    ContractSign,
    FinalReview,
    DeploymentPrep,
    GoLive,
    MonitorModel,
    OptimizeAI,
    SupportHandoff
])

# Define the control-flow (partial order) edges
root.order.add_edge(ClientIntake,   NeedsAnalysis)
root.order.add_edge(NeedsAnalysis,  DeveloperMatch)
root.order.add_edge(DeveloperMatch, ExpertVetting)

root.order.add_edge(ExpertVetting, prototype_loop)

# After the prototyping loop, legal/compliance activities run in parallel
root.order.add_edge(prototype_loop, LicenseDraft)
root.order.add_edge(prototype_loop, IPNegotiation)
root.order.add_edge(prototype_loop, ComplianceCheck)

# All three must complete before signing the contract
root.order.add_edge(LicenseDraft,    ContractSign)
root.order.add_edge(IPNegotiation,   ContractSign)
root.order.add_edge(ComplianceCheck, ContractSign)

# Final review and deployment
root.order.add_edge(ContractSign,   FinalReview)
root.order.add_edge(FinalReview,    DeploymentPrep)
root.order.add_edge(DeploymentPrep, GoLive)

# Post-deployment monitoring and support
root.order.add_edge(GoLive,        MonitorModel)
root.order.add_edge(MonitorModel,  OptimizeAI)
root.order.add_edge(OptimizeAI,    SupportHandoff)