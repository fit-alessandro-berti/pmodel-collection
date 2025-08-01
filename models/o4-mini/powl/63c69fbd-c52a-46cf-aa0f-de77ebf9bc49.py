# Generated from: 63c69fbd-c52a-46cf-aa0f-de77ebf9bc49.json
# Description: This process outlines the complex adaptive cycle of urban farming within a dynamic city environment, integrating environmental monitoring, community engagement, and resource optimization. It involves iterative soil testing, microclimate analysis, and crop selection based on real-time data. Community workshops promote sustainable practices, while automated irrigation systems adjust to weather variability. Waste from local markets is repurposed as compost, closing the nutrient loop. The process also includes periodic economic assessments to ensure profitability and social impact, as well as regulatory compliance checks. Data from IoT sensors feed into AI models that predict pest outbreaks and growth rates, enabling proactive interventions. This atypical urban agricultural approach balances ecological, social, and economic objectives to create resilient food production systems within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SoilTesting      = Transition(label='Soil Testing')
ClimateScan      = Transition(label='Climate Scan')
CropSelection    = Transition(label='Crop Selection')
IrrigationAdjust = Transition(label='Irrigation Adjust')

PestForecast   = Transition(label='Pest Forecast')
GrowthMonitor  = Transition(label='Growth Monitor')
DataAnalysis   = Transition(label='Data Analysis')
AIPrediction   = Transition(label='AI Prediction')

WasteCollect     = Transition(label='Waste Collect')
CompostCreation  = Transition(label='Compost Creation')
MarketSync       = Transition(label='Market Sync')
ResourceShift    = Transition(label='Resource Shift')

CommunityMeet = Transition(label='Community Meet')
WorkshopHost  = Transition(label='Workshop Host')

RegulationCheck  = Transition(label='Regulation Check')
EconomicReview   = Transition(label='Economic Review')

YieldReport = Transition(label='Yield Report')

# Silent transition (if needed for optional branches)
skip = SilentTransition()

# 1) Core agronomic cycle: Soil→Climate→Crop→Irrigation
body_cycle = StrictPartialOrder(nodes=[SoilTesting, ClimateScan, CropSelection, IrrigationAdjust])
body_cycle.order.add_edge(SoilTesting, ClimateScan)
body_cycle.order.add_edge(ClimateScan, CropSelection)
body_cycle.order.add_edge(CropSelection, IrrigationAdjust)

#    Redo part of the loop: Pest forecast→Growth monitor→Data analysis→AI prediction
redo_cycle = StrictPartialOrder(nodes=[PestForecast, GrowthMonitor, DataAnalysis, AIPrediction])
redo_cycle.order.add_edge(PestForecast, GrowthMonitor)
redo_cycle.order.add_edge(GrowthMonitor, DataAnalysis)
redo_cycle.order.add_edge(DataAnalysis, AIPrediction)

#    Combine into a LOOP: execute body_cycle, then either exit or do redo_cycle and repeat
core_cycle = OperatorPOWL(operator=Operator.LOOP, children=[body_cycle, redo_cycle])

# 2) Community engagement sequence
community_engagement = StrictPartialOrder(nodes=[CommunityMeet, WorkshopHost])
community_engagement.order.add_edge(CommunityMeet, WorkshopHost)

# 3) Waste-to-compost flow: Collect→Compost→Market sync→Resource shift
waste_flow = StrictPartialOrder(nodes=[WasteCollect, CompostCreation, MarketSync, ResourceShift])
waste_flow.order.add_edge(WasteCollect, CompostCreation)
waste_flow.order.add_edge(CompostCreation, MarketSync)
waste_flow.order.add_edge(MarketSync, ResourceShift)

# 4) Compliance & economic assessment: Regulation→Economic review
compliance_seq = StrictPartialOrder(nodes=[RegulationCheck, EconomicReview])
compliance_seq.order.add_edge(RegulationCheck, EconomicReview)

# 5) Final yield report
#    (can be seen as a standalone activity)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[core_cycle,
           community_engagement,
           waste_flow,
           compliance_seq,
           YieldReport]
)

# Define the inter‐group ordering
root.order.add_edge(core_cycle, community_engagement)
root.order.add_edge(community_engagement, waste_flow)
root.order.add_edge(waste_flow, compliance_seq)
root.order.add_edge(compliance_seq, YieldReport)