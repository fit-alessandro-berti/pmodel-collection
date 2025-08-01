# Generated from: 324cc83b-189c-4c7b-ace3-1b1c87acb789.json
# Description: This process outlines a cyclical approach to fostering innovation by integrating insights and technologies across unrelated industries. It begins with environmental scanning to identify emerging trends outside the core domain, followed by ideation sessions that leverage cross-sector expertise. Concept prototyping is done rapidly using agile methodologies, incorporating feedback from diverse stakeholders. The process includes periodic knowledge transfer workshops, external partnership development, and iterative refinement based on pilot results. Risk assessment and scalability evaluation ensure feasibility before full-scale implementation. Continuous learning loops from market response data feed back into future cycle iterations, promoting sustained innovation beyond traditional boundaries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
TrendScan = Transition(label='Trend Scan')
IdeaSprint = Transition(label='Idea Sprint')
StakeholderMap = Transition(label='Stakeholder Map')
ConceptBuild = Transition(label='Concept Build')
RapidPrototype = Transition(label='Rapid Prototype')
FeedbackLoop = Transition(label='Feedback Loop')
RiskReview = Transition(label='Risk Review')
PilotLaunch = Transition(label='Pilot Launch')
DataAnalyze = Transition(label='Data Analyze')
PartnerEngage = Transition(label='Partner Engage')
ScaleAssess = Transition(label='Scale Assess')
KnowledgeShare = Transition(label='Knowledge Share')
IterateDesign = Transition(label='Iterate Design')
MarketTest = Transition(label='Market Test')
CycleReview = Transition(label='Cycle Review')

# Build the core workflow PO with order:
# 
# TrendScan --> IdeaSprint --> StakeholderMap --> ConceptBuild --> RapidPrototype --> FeedbackLoop --> 
# [RiskReview --> PilotLaunch --> DataAnalyze --> PartnerEngage --> ScaleAssess --> KnowledgeShare --> IterateDesign --> MarketTest --> CycleReview]

main_po_nodes = [
    TrendScan, IdeaSprint, StakeholderMap, ConceptBuild, RapidPrototype, FeedbackLoop,
    RiskReview, PilotLaunch, DataAnalyze, PartnerEngage, ScaleAssess,
    KnowledgeShare, IterateDesign, MarketTest, CycleReview
]

main_po = StrictPartialOrder(nodes=main_po_nodes)

# Add edges for the linear sequence
main_po.order.add_edge(TrendScan, IdeaSprint)
main_po.order.add_edge(IdeaSprint, StakeholderMap)
main_po.order.add_edge(StakeholderMap, ConceptBuild)
main_po.order.add_edge(ConceptBuild, RapidPrototype)
main_po.order.add_edge(RapidPrototype, FeedbackLoop)

main_po.order.add_edge(FeedbackLoop, RiskReview)
main_po.order.add_edge(RiskReview, PilotLaunch)
main_po.order.add_edge(PilotLaunch, DataAnalyze)
main_po.order.add_edge(DataAnalyze, PartnerEngage)
main_po.order.add_edge(PartnerEngage, ScaleAssess)
main_po.order.add_edge(ScaleAssess, KnowledgeShare)
main_po.order.add_edge(KnowledgeShare, IterateDesign)
main_po.order.add_edge(IterateDesign, MarketTest)
main_po.order.add_edge(MarketTest, CycleReview)

# The process includes continuous learning loop feeding back into future cycle iterations.
# Represent this by a LOOP operator where:
# A = the full cycle (main_po)
# B = the earlier part of the cycle to repeat (starting from IdeaSprint along the chain back to FeedbackLoop).
#
# That is, after the full cycle, decide to exit or repeat the core innovation cycle from IdeaSprint.

# Build the loop body B = from IdeaSprint to FeedbackLoop sequential PO
loop_body_nodes = [
    IdeaSprint, StakeholderMap, ConceptBuild, RapidPrototype, FeedbackLoop
]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(IdeaSprint, StakeholderMap)
loop_body.order.add_edge(StakeholderMap, ConceptBuild)
loop_body.order.add_edge(ConceptBuild, RapidPrototype)
loop_body.order.add_edge(RapidPrototype, FeedbackLoop)

# Create the LOOP: execute A (full cycle), then either exit or execute B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[main_po, loop_body])