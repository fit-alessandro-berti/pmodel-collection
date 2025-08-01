# Generated from: ed95eec0-2fa8-4404-91b3-a159ff27c87f.json
# Description: This process involves systematically integrating unconventional ideas from unrelated industries into a core business to foster groundbreaking innovation. It begins with identifying external trends, followed by cross-sector brainstorming sessions, prototype development using hybrid methodologies, and iterative feedback loops involving diverse stakeholder groups. The process emphasizes adaptive learning, risk mitigation through scenario testing, and strategic alignment with long-term corporate goals. Final steps include pilot launches in controlled markets, data-driven refinement, and scaling strategies that incorporate continuous market sensing and knowledge transfer across departments, ensuring sustainable competitive advantage through atypical innovation practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
TrendScan      = Transition(label='Trend Scan')
IdeaHarvest    = Transition(label='Idea Harvest')
SectorMatch    = Transition(label='Sector Match')
BrainstormHub  = Transition(label='Brainstorm Hub')
ConceptFilter  = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
HybridTesting  = Transition(label='Hybrid Testing')
StakeholderSync= Transition(label='Stakeholder Sync')
RiskAssess     = Transition(label='Risk Assess')
ScenarioMap    = Transition(label='Scenario Map')
StrategyAlign  = Transition(label='Strategy Align')
PilotLaunch    = Transition(label='Pilot Launch')
DataCapture    = Transition(label='Data Capture')
MarketSense    = Transition(label='Market Sense')
ScalePlan      = Transition(label='Scale Plan')

# Build the feedback sub‐process as a partial order
feedbackSeq = StrictPartialOrder(nodes=[HybridTesting, StakeholderSync, RiskAssess, ScenarioMap])
feedbackSeq.order.add_edge(HybridTesting, StakeholderSync)
feedbackSeq.order.add_edge(StakeholderSync, RiskAssess)
feedbackSeq.order.add_edge(RiskAssess, ScenarioMap)

# Define the prototype‐feedback loop: build → (feedback → build)*  
loopProto = OperatorPOWL(
    operator=Operator.LOOP,
    children=[PrototypeBuild, feedbackSeq]
)

# Assemble the top‐level workflow
root = StrictPartialOrder(nodes=[
    TrendScan, IdeaHarvest, SectorMatch, BrainstormHub,
    ConceptFilter, loopProto,
    StrategyAlign, PilotLaunch,
    DataCapture, MarketSense, ScalePlan
])

# Sequential ordering between major phases
root.order.add_edge(TrendScan,      IdeaHarvest)
root.order.add_edge(IdeaHarvest,    SectorMatch)
root.order.add_edge(SectorMatch,    BrainstormHub)
root.order.add_edge(BrainstormHub,  ConceptFilter)
root.order.add_edge(ConceptFilter,  loopProto)
root.order.add_edge(loopProto,      StrategyAlign)
root.order.add_edge(StrategyAlign,  PilotLaunch)
root.order.add_edge(PilotLaunch,    DataCapture)
root.order.add_edge(DataCapture,    MarketSense)
root.order.add_edge(MarketSense,    ScalePlan)