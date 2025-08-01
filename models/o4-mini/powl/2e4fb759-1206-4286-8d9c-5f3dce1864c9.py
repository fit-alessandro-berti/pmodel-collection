# Generated from: 2e4fb759-1206-4286-8d9c-5f3dce1864c9.json
# Description: This process describes the iterative cycle of cross-industry innovation where insights from disparate sectors are systematically gathered, synthesized, and applied to develop breakthrough products or services. It begins with environmental scanning and trend spotting across unrelated markets, followed by ideation sessions leveraging diverse expert panels. Concepts are rapidly prototyped using agile methodologies and tested through pilot programs in controlled environments. Feedback loops incorporate user data and expert reviews to refine solutions before scaling. The process also includes strategic partnerships formation, IP management, and continuous knowledge dissemination to ensure competitive advantage and sustainable innovation across industries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
TrendScan       = Transition(label='Trend Scan')
MarketMapping   = Transition(label='Market Mapping')
ExpertPanel     = Transition(label='Expert Panel')
IdeaGeneration  = Transition(label='Idea Generation')
ConceptSketch   = Transition(label='Concept Sketch')
RapidPrototype  = Transition(label='Rapid Prototype')
PilotLaunch     = Transition(label='Pilot Launch')
UserFeedback    = Transition(label='User Feedback')
DataAnalysis    = Transition(label='Data Analysis')
SolutionRefinement = Transition(label='Solution Refinement')
PartnershipSetup   = Transition(label='Partnership Setup')
IPReview           = Transition(label='IP Review')
KnowledgeShare     = Transition(label='Knowledge Share')
ScalePlanning      = Transition(label='Scale Planning')
ImpactAudit        = Transition(label='Impact Audit')
ContinuousLoop     = Transition(label='Continuous Loop')

# Build the one‐cycle partial order
cycle = StrictPartialOrder(nodes=[
    TrendScan, MarketMapping,
    ExpertPanel, IdeaGeneration,
    ConceptSketch, RapidPrototype,
    PilotLaunch, UserFeedback,
    DataAnalysis, SolutionRefinement,
    PartnershipSetup, IPReview,
    KnowledgeShare, ScalePlanning,
    ImpactAudit
])
sequence = [
    TrendScan, MarketMapping,
    ExpertPanel, IdeaGeneration,
    ConceptSketch, RapidPrototype,
    PilotLaunch, UserFeedback,
    DataAnalysis, SolutionRefinement,
    PartnershipSetup, IPReview,
    KnowledgeShare, ScalePlanning,
    ImpactAudit
]
for src, tgt in zip(sequence, sequence[1:]):
    cycle.order.add_edge(src, tgt)

# Wrap the cycle in a LOOP to model continuous iteration
root = OperatorPOWL(operator=Operator.LOOP, children=[cycle, ContinuousLoop])