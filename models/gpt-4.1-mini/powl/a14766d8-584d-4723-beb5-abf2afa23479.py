# Generated from: a14766d8-584d-4723-beb5-abf2afa23479.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield and resource efficiency within constrained city environments. It integrates dynamic environmental sensing, soil nutrient recalibration, automated planting, and waste recycling while incorporating community feedback and local market trends. The cycle continuously adjusts irrigation, lighting, and nutrient delivery based on real-time data, ensuring sustainability and responsiveness to urban microclimates. Additionally, it includes predictive pest control measures and periodic crop rotation planning to maintain soil health and biodiversity. Post-harvest, the system manages distribution logistics and engages in regenerative practices by leveraging organic waste for composting, creating a closed-loop ecosystem that maximizes productivity and minimizes environmental impact in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SensorSetup = Transition(label='Sensor Setup')
DataCapture = Transition(label='Data Capture')
NutrientTest = Transition(label='Nutrient Test')
SoilRecalibrate = Transition(label='Soil Recalibrate')
SeedSelection = Transition(label='Seed Selection')
AutomatedPlanting = Transition(label='Automated Planting')
IrrigationAdjust = Transition(label='Irrigation Adjust')
LightingControl = Transition(label='Lighting Control')
PestPrediction = Transition(label='Pest Prediction')
CropRotation = Transition(label='Crop Rotation')
WasteCollection = Transition(label='Waste Collection')
CompostProcess = Transition(label='Compost Process')
YieldForecast = Transition(label='Yield Forecast')
MarketSurvey = Transition(label='Market Survey')
DistributionPlan = Transition(label='Distribution Plan')
CommunityFeedback = Transition(label='Community Feedback')

# Define partial orders and operators according to process logic:

# 1. Initial environmental sensing and soil preparation sequence:
# Sensor Setup --> Data Capture --> (Nutrient Test --> Soil Recalibrate)

nutrient_PO = StrictPartialOrder(nodes=[NutrientTest, SoilRecalibrate])
nutrient_PO.order.add_edge(NutrientTest, SoilRecalibrate)

sensor_PO = StrictPartialOrder(nodes=[SensorSetup, DataCapture, nutrient_PO])
sensor_PO.order.add_edge(SensorSetup, DataCapture)
sensor_PO.order.add_edge(DataCapture, nutrient_PO)

# 2. Seed Selection and Automated Planting are sequential after soil prep
planting_PO = StrictPartialOrder(nodes=[SeedSelection, AutomatedPlanting])
planting_PO.order.add_edge(SeedSelection, AutomatedPlanting)

# 3. Adjustments loop: Irrigation Adjust, Lighting Control, Nutrient delivery adjustment modeled within a loop with Pest Prediction as part of the loop body
# Loop body: B = PO(Irrigation Adjust, Lighting Control, Pest Prediction), then A = Automated Planting (the execute A then choose to exit or execute B then A again loop)
adjust_loop_body = StrictPartialOrder(nodes=[IrrigationAdjust, LightingControl, PestPrediction])
# no order edges between these - they can be concurrent

# Loop: execute Automated Planting, then either exit or execute B and then Automated Planting again (repeated)
loop_adjustments = OperatorPOWL(operator=Operator.LOOP, children=[AutomatedPlanting, adjust_loop_body])

# 4. Crop rotation planning and yield forecasting incorporates sustainability with ongoing adjustments
# Model this as a partial order with Crop Rotation and Yield Forecast concurrent (can happen in parallel)
crop_yield_PO = StrictPartialOrder(nodes=[CropRotation, YieldForecast])

# 5. Market Survey and Community Feedback (choice/fork affecting Distribution Plan)
# Model Market Survey and Community Feedback concurrent
market_feedback_PO = StrictPartialOrder(nodes=[MarketSurvey, CommunityFeedback])

# 6. Waste Collection and Compost Process form a sequence (regenerative practices)
waste_PO = StrictPartialOrder(nodes=[WasteCollection, CompostProcess])
waste_PO.order.add_edge(WasteCollection, CompostProcess)

# 7. Distribution Plan follows Market and Community input
distribution_PO = StrictPartialOrder(nodes=[market_feedback_PO, DistributionPlan])
distribution_PO.order.add_edge(market_feedback_PO, DistributionPlan)

# 8. Combine all:  
# After soil prep (sensor_PO),
# seed selection and planting preparations (planting_PO),
# followed by loop_adjustments,
# then crop_yield_PO,
# then distribution_PO,
# and waste management (waste_PO) can be concurrent with distribution_PO (both post-harvest management),
# but distribution_PO should start only after crop_yield_PO

post_harvest_PO = StrictPartialOrder(nodes=[distribution_PO, waste_PO])
# no ordering between distribution_PO and waste_PO => concurrent

# Build full process order with edges:

full_PO = StrictPartialOrder(nodes=[sensor_PO, planting_PO, loop_adjustments, crop_yield_PO, post_harvest_PO])

# sensor_PO --> planting_PO --> loop_adjustments --> crop_yield_PO --> post_harvest_PO
full_PO.order.add_edge(sensor_PO, planting_PO)
full_PO.order.add_edge(planting_PO, loop_adjustments)
full_PO.order.add_edge(loop_adjustments, crop_yield_PO)
full_PO.order.add_edge(crop_yield_PO, post_harvest_PO)

root = full_PO