# Generated from: 1a90e116-79ec-4290-9d02-a209a97aa87e.json
# Description: This process describes a complex cross-industry innovation cycle where a company integrates unconventional partnerships, iterative prototyping, and adaptive market testing to develop breakthrough products. Starting from ideation through biomimicry workshops, it moves into decentralized sourcing of unconventional materials, followed by rapid modular prototyping. The cycle includes parallel regulatory simulations, stakeholder co-creation sessions, and dynamic risk assessments. Post-launch, the process emphasizes continuous feedback loops via AI-driven sentiment analysis and adaptive supply chain recalibration to sustain competitive advantage in volatile markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
IdeaHarvest = Transition(label='Idea Harvest')
BiomimicryLab = Transition(label='Biomimicry Lab')
PartnerVetting = Transition(label='Partner Vetting')
MaterialScout = Transition(label='Material Scout')
PrototypeSprint = Transition(label='Prototype Sprint')
RegulatoryScan = Transition(label='Regulatory Scan')
RiskMapping = Transition(label='Risk Mapping')
CoCreation = Transition(label='Co-Creation')
MarketPilot = Transition(label='Market Pilot')
SentimentScan = Transition(label='Sentiment Scan')
SupplyRecalibrate = Transition(label='Supply Recalibrate')
DataFusion = Transition(label='Data Fusion')
TrendForecast = Transition(label='Trend Forecast')
FeedbackLoop = Transition(label='Feedback Loop')
ScaleAdjust = Transition(label='Scale Adjust')

# Construct the initial sequential phase:
# Idea Harvest --> Biomimicry Lab
initial_seq = StrictPartialOrder(nodes=[IdeaHarvest, BiomimicryLab])
initial_seq.order.add_edge(IdeaHarvest, BiomimicryLab)

# Decentralized sourcing & Partner Vetting concurrent
partner_material_PO = StrictPartialOrder(nodes=[PartnerVetting, MaterialScout])
# They can occur concurrently, no edges

# Rapid modular prototyping after sourcing and vetting
# So: (Partner Vetting || Material Scout) --> Prototype Sprint
proto_PO = StrictPartialOrder(nodes=[partner_material_PO, PrototypeSprint])
# we treat partner_material_PO and PrototypeSprint as nodes, 
# but here we build a PO of all:
all_initial_nodes = [PartnerVetting, MaterialScout, PrototypeSprint]
proto_PO = StrictPartialOrder(nodes=all_initial_nodes)
proto_PO.order.add_edge(PartnerVetting, PrototypeSprint)
proto_PO.order.add_edge(MaterialScout, PrototypeSprint)

# The cycle constructing regulatory simulations, stakeholder co-creation, and dynamic risk assessments happen in parallel:
# Regulatory Scan, Risk Mapping, Co-Creation can run in parallel:
simultaneous_assessments = StrictPartialOrder(
    nodes=[RegulatoryScan, RiskMapping, CoCreation]
)
# no edges -> fully concurrent

# Post launch continuous feedback loops:
# AI-driven sentiment analysis and adaptive supply chain recalibration to sustain advantage in volatile markets.
# Represent it by a loop:
# Loop body: Data Fusion (analysis), Trend Forecast (forecasting), then
# choice to exit or do Feedback Loop and Scale Adjust and then loop again (adaptive improvements)
# We'll model loop as (* (body, loopback))
# body: Data Fusion -> Trend Forecast
body_PO = StrictPartialOrder(nodes=[DataFusion, TrendForecast])
body_PO.order.add_edge(DataFusion, TrendForecast)

# loopback branch: Feedback Loop followed by Scale Adjust
loop_back_PO = StrictPartialOrder(nodes=[FeedbackLoop, ScaleAdjust])
loop_back_PO.order.add_edge(FeedbackLoop, ScaleAdjust)

# Compose the loop with body_PO and loop_back_PO
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_PO, loop_back_PO])

# Market Pilot comes after the parallel assessments
# MarketPilot after Regulatory Scan, Risk Mapping, and Co-Creation
post_assessment_PO = StrictPartialOrder(
    nodes=[simultaneous_assessments, MarketPilot]
)
# But we need to flatten and add edges from all nodes in simultaneous_assessments to MarketPilot
post_nodes = [RegulatoryScan, RiskMapping, CoCreation, MarketPilot]
post_assessment_PO = StrictPartialOrder(nodes=post_nodes)
post_assessment_PO.order.add_edge(RegulatoryScan, MarketPilot)
post_assessment_PO.order.add_edge(RiskMapping, MarketPilot)
post_assessment_PO.order.add_edge(CoCreation, MarketPilot)

# After Market Pilot, Sentiment Scan and Supply Recalibrate run in parallel
post_launch_concurrent = StrictPartialOrder(
    nodes=[SentimentScan, SupplyRecalibrate]
)
# No edges -> concurrent

# Connect Market Pilot to Sentiment Scan and Supply Recalibrate
post_launch_PO = StrictPartialOrder(
    nodes=[MarketPilot, SentimentScan, SupplyRecalibrate]
)
post_launch_PO.order.add_edge(MarketPilot, SentimentScan)
post_launch_PO.order.add_edge(MarketPilot, SupplyRecalibrate)

# Finally, connect all major phases in partial order:
# initial_seq --> proto_PO --> post_assessment_PO --> post_launch_PO --> feedback_loop

nodes_all = [
    initial_seq,
    proto_PO,
    post_assessment_PO,
    post_launch_PO,
    feedback_loop,
]

root = StrictPartialOrder(nodes=nodes_all)
root.order.add_edge(initial_seq, proto_PO)
root.order.add_edge(proto_PO, post_assessment_PO)
root.order.add_edge(post_assessment_PO, post_launch_PO)
root.order.add_edge(post_launch_PO, feedback_loop)