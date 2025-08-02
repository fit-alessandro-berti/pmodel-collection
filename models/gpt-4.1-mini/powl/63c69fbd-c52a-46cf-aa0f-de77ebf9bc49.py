# Generated from: 63c69fbd-c52a-46cf-aa0f-de77ebf9bc49.json
# Description: This process outlines the complex adaptive cycle of urban farming within a dynamic city environment, integrating environmental monitoring, community engagement, and resource optimization. It involves iterative soil testing, microclimate analysis, and crop selection based on real-time data. Community workshops promote sustainable practices, while automated irrigation systems adjust to weather variability. Waste from local markets is repurposed as compost, closing the nutrient loop. The process also includes periodic economic assessments to ensure profitability and social impact, as well as regulatory compliance checks. Data from IoT sensors feed into AI models that predict pest outbreaks and growth rates, enabling proactive interventions. This atypical urban agricultural approach balances ecological, social, and economic objectives to create resilient food production systems within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SoilTesting = Transition(label='Soil Testing')
ClimateScan = Transition(label='Climate Scan')
CropSelection = Transition(label='Crop Selection')
CommunityMeet = Transition(label='Community Meet')
IrrigationAdjust = Transition(label='Irrigation Adjust')
WasteCollect = Transition(label='Waste Collect')
CompostCreation = Transition(label='Compost Creation')
MarketSync = Transition(label='Market Sync')
PestForecast = Transition(label='Pest Forecast')
GrowthMonitor = Transition(label='Growth Monitor')
DataAnalysis = Transition(label='Data Analysis')
AIPrediction = Transition(label='AI Prediction')
RegulationCheck = Transition(label='Regulation Check')
EconomicReview = Transition(label='Economic Review')
ResourceShift = Transition(label='Resource Shift')
WorkshopHost = Transition(label='Workshop Host')
YieldReport = Transition(label='Yield Report')

# Soil Testing, Climate Scan, Crop Selection form an iterative loop with Crop Selection dependent on latest data from prior activities
# Loop: Execute SoilTesting and ClimateScan (partial order parallel), then CropSelection, then choose either exit or waste/resource cycle and loop again.

# Inner partial order for Soil Testing and Climate Scan concurrent
soil_climate_po = StrictPartialOrder(nodes=[SoilTesting, ClimateScan])
# They are concurrent so no edges

# Partial order: SoilTesting, ClimateScan --> CropSelection
pre_crop_po = StrictPartialOrder(nodes=[soil_climate_po, CropSelection])
pre_crop_po.order.add_edge(soil_climate_po, CropSelection)  # This means CropSelection depends on both finishing

# Waste nutrient loop:
# WasteCollect --> CompostCreation --> MarketSync --> ResourceShift
waste_loop_po = StrictPartialOrder(nodes=[WasteCollect, CompostCreation, MarketSync, ResourceShift])
waste_loop_po.order.add_edge(WasteCollect, CompostCreation)
waste_loop_po.order.add_edge(CompostCreation, MarketSync)
waste_loop_po.order.add_edge(MarketSync, ResourceShift)

# Loop operator body: After CropSelection
# Choose to either exit the loop or do waste/resource shift then loop back

# Loop cycle body: B = waste_loop_po, A = pre_crop_po
# LOOP executes pre_crop_po, then chooses to exit or execute waste_loop_po then again pre_crop_po
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_crop_po, waste_loop_po])

# Community workshops with WorkshopHost and CommunityMeet concurrent within partial order
community_po = StrictPartialOrder(nodes=[WorkshopHost, CommunityMeet])
# Concurrent so no edges

# IrrigationAdjust adjusts automatically after Climate Scan
# So ClimateScan --> IrrigationAdjust
irrigation_po = StrictPartialOrder(nodes=[ClimateScan, IrrigationAdjust])
irrigation_po.order.add_edge(ClimateScan, IrrigationAdjust)

# PestForecast and GrowthMonitor after AI Prediction and Data Analysis (DataAnalysis --> AIPrediction --> (PestForecast, GrowthMonitor concurrent))
data_ai_po = StrictPartialOrder(nodes=[DataAnalysis, AIPrediction])
data_ai_po.order.add_edge(DataAnalysis, AIPrediction)
pest_growth_po = StrictPartialOrder(nodes=[PestForecast, GrowthMonitor])
# Concurrent nodes PestForecast and GrowthMonitor

# AI related part partial order: data_ai_po --> pest_growth_po
ai_part_po = StrictPartialOrder(nodes=[data_ai_po, pest_growth_po])
ai_part_po.order.add_edge(data_ai_po, pest_growth_po)

# Periodic Economic Review and Regulation Check (EconomicReview --> RegulationCheck)
econ_reg_po = StrictPartialOrder(nodes=[EconomicReview, RegulationCheck])
econ_reg_po.order.add_edge(EconomicReview, RegulationCheck)

# YieldReport depends on CropSelection and ResourceShift (final output after loop and resource cycle)
yield_po = StrictPartialOrder(nodes=[CropSelection, ResourceShift, YieldReport])
yield_po.order.add_edge(CropSelection, YieldReport)
yield_po.order.add_edge(ResourceShift, YieldReport)

# Combine community, irrigation, ai, econ/reg and yield in a main partial order concurrent structure after main loop
# main_loop --> community_po
# main_loop --> irrigation_po
# main_loop --> ai_part_po
# main_loop --> econ_reg_po
# Also YieldReport depends on CropSelection and ResourceShift (included in yield_po)
full_po = StrictPartialOrder(
    nodes=[main_loop, community_po, irrigation_po, ai_part_po, econ_reg_po, yield_po]
)

full_po.order.add_edge(main_loop, community_po)
full_po.order.add_edge(main_loop, irrigation_po)
full_po.order.add_edge(main_loop, ai_part_po)
full_po.order.add_edge(main_loop, econ_reg_po)

# YieldReport already depends on CropSelection and ResourceShift in yield_po partial order

root = full_po