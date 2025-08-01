# Generated from: 683af796-cce1-4480-9133-6226ba95b043.json
# Description: This process outlines the establishment of a sustainable urban vertical farm within a repurposed industrial building. It involves site assessment, structural retrofitting, climate control system installation, hydroponic setup, nutrient solution calibration, crop selection based on urban demand, automation integration, pest monitoring via AI sensors, energy consumption optimization, staff training on novel farming techniques, regulatory compliance verification, market distribution planning, and continuous yield monitoring to ensure maximal efficiency and minimal environmental impact throughout the farm's operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
SiteAssessment = Transition(label='Site Assessment')
StructuralRetrofit = Transition(label='Structural Retrofit')
ClimateSetup = Transition(label='Climate Setup')
HydroponicInstall = Transition(label='Hydroponic Install')
NutrientCalibrate = Transition(label='Nutrient Calibrate')
CropSelection = Transition(label='Crop Selection')
AutomationIntegrate = Transition(label='Automation Integrate')
PestMonitoring = Transition(label='Pest Monitoring')
EnergyOptimize = Transition(label='Energy Optimize')
StaffTraining = Transition(label='Staff Training')
RegulatoryCheck = Transition(label='Regulatory Check')
MarketPlanning = Transition(label='Market Planning')
YieldMonitoring = Transition(label='Yield Monitoring')
WasteRecycling = Transition(label='Waste Recycling')
DataAnalysis = Transition(label='Data Analysis')

# Model partial order reflecting the process
# Logical flow according to description:
# Site Assessment → Structural Retrofit → Climate Setup → Hydroponic Install → Nutrient Calibrate
# → Crop Selection 
# → (Automation Integrate || Pest Monitoring || Energy Optimize) parallel
# → Staff Training
# → Regulatory Check
# → Market Planning
# → Loop for (Yield Monitoring → Waste Recycling → Data Analysis) repeated until exit

# Parallel block after Crop Selection
parallel_nodes = [AutomationIntegrate, PestMonitoring, EnergyOptimize]

# Loop: do Yield Monitoring, then choose to exit or Waste Recycling + Data Analysis then repeat 
inner_loop_body = StrictPartialOrder(nodes=[WasteRecycling, DataAnalysis])
inner_loop_body.order.add_edge(WasteRecycling, DataAnalysis)

loop = OperatorPOWL(operator=Operator.LOOP, children=[YieldMonitoring, inner_loop_body])

# Construct main partial order
nodes_main = [
    SiteAssessment,
    StructuralRetrofit,
    ClimateSetup,
    HydroponicInstall,
    NutrientCalibrate,
    CropSelection,
    *parallel_nodes,
    StaffTraining,
    RegulatoryCheck,
    MarketPlanning,
    loop
]

root = StrictPartialOrder(nodes=nodes_main)

# Add edges in the main partial order to represent precedence
root.order.add_edge(SiteAssessment, StructuralRetrofit)
root.order.add_edge(StructuralRetrofit, ClimateSetup)
root.order.add_edge(ClimateSetup, HydroponicInstall)
root.order.add_edge(HydroponicInstall, NutrientCalibrate)
root.order.add_edge(NutrientCalibrate, CropSelection)

# Crop Selection leads to all three parallel nodes concurrently; no order needed between them,
# but Crop Selection must precede each parallel node
for node in parallel_nodes:
    root.order.add_edge(CropSelection, node)

# All parallel nodes must finish before Staff Training
for node in parallel_nodes:
    root.order.add_edge(node, StaffTraining)

root.order.add_edge(StaffTraining, RegulatoryCheck)
root.order.add_edge(RegulatoryCheck, MarketPlanning)
root.order.add_edge(MarketPlanning, loop)