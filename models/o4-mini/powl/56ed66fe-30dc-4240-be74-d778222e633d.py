# Generated from: 56ed66fe-30dc-4240-be74-d778222e633d.json
# Description: This process involves leveraging a global community to generate, refine, and implement innovative ideas for a company’s product line. It starts with launching a challenge, collecting submissions, and then curating entries through multiple review stages including peer voting and expert evaluation. Selected ideas undergo prototyping, iterative feedback loops with contributors, and final validation before integration into the product roadmap. The process requires coordination across multiple teams, continuous engagement with external contributors, and adaptive resource allocation based on idea potential and community response. It ensures a dynamic flow of creativity while maintaining quality and strategic alignment with business goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
LaunchChallenge    = Transition(label='Launch Challenge')
CollectIdeas       = Transition(label='Collect Ideas')
CommunityVoting    = Transition(label='Community Voting')
ExpertReview       = Transition(label='Expert Review')
SelectWinners      = Transition(label='Select Winners')
ResourceAlign      = Transition(label='Resource Align')
ContributorEngage  = Transition(label='Contributor Engage')
PrototypeBuild     = Transition(label='Prototype Build')
FeedbackLoop       = Transition(label='Feedback Loop')
RevisePrototype    = Transition(label='Revise Prototype')
FinalValidation    = Transition(label='Final Validation')
LegalCheck         = Transition(label='Legal Check')
IPFiling           = Transition(label='IP Filing')
ScaleProduction    = Transition(label='Scale Production')
MarketTest         = Transition(label='Market Test')
RoadmapUpdate      = Transition(label='Roadmap Update')

# Loop body for iterative feedback: (FeedbackLoop -> RevisePrototype)
redo_body = StrictPartialOrder(nodes=[FeedbackLoop, RevisePrototype])
redo_body.order.add_edge(FeedbackLoop, RevisePrototype)

# LOOP operator: do PrototypeBuild once, then optionally repeat redo_body + PrototypeBuild
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, redo_body])

# Compliance branch: LegalCheck -> IPFiling
compliance = StrictPartialOrder(nodes=[LegalCheck, IPFiling])
compliance.order.add_edge(LegalCheck, IPFiling)

# Production branch: ScaleProduction -> MarketTest
production = StrictPartialOrder(nodes=[ScaleProduction, MarketTest])
production.order.add_edge(ScaleProduction, MarketTest)

# Root partial order, assembling the entire process
root = StrictPartialOrder(nodes=[
    LaunchChallenge, CollectIdeas, CommunityVoting, ExpertReview, SelectWinners,
    ResourceAlign, ContributorEngage, feedback_loop, FinalValidation,
    compliance, production, RoadmapUpdate
])

# Control-flow dependencies
root.order.add_edge(LaunchChallenge,    CollectIdeas)
root.order.add_edge(CollectIdeas,       CommunityVoting)
root.order.add_edge(CommunityVoting,    ExpertReview)
root.order.add_edge(ExpertReview,       SelectWinners)
root.order.add_edge(SelectWinners,      ResourceAlign)
root.order.add_edge(SelectWinners,      ContributorEngage)
root.order.add_edge(ResourceAlign,      feedback_loop)
root.order.add_edge(ContributorEngage,  feedback_loop)
root.order.add_edge(feedback_loop,      FinalValidation)
root.order.add_edge(FinalValidation,    compliance)
root.order.add_edge(FinalValidation,    production)
root.order.add_edge(compliance,         RoadmapUpdate)
root.order.add_edge(production,         RoadmapUpdate)