# Generated from: 0008eec6-68d3-46ff-a77c-2544742ba9f8.json
# Description: This process outlines the complex and atypical series of activities involved in launching an urban vertical farming operation within a densely populated city. It starts with site analysis, followed by modular system design tailored to space constraints, integration of IoT sensors for environmental control, and optimization of nutrient delivery systems. The process also involves securing permits from multiple municipal authorities, coordinating logistics for equipment transport through narrow urban corridors, and training staff on sustainable farming practices. Continuous monitoring of crop health using AI-driven analytics and adaptive lighting schedules ensures maximum yield. Additionally, the operation includes establishing partnerships with local restaurants and markets to create a direct-to-consumer supply chain, reducing food miles and enhancing freshness. The final stages focus on environmental impact assessments and scalability planning for future urban sites, making this process a unique blend of agriculture, technology, and urban planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Create transitions for each activity
SiteSurvey = Transition(label='Site Survey')
ModularDesign = Transition(label='Modular Design')
PermitCheck = Transition(label='Permit Check')
SensorSetup = Transition(label='Sensor Setup')
NutrientMix = Transition(label='Nutrient Mix')
LogisticsPlan = Transition(label='Logistics Plan')
StaffTraining = Transition(label='Staff Training')
CropSeeding = Transition(label='Crop Seeding')
LightAdjust = Transition(label='Light Adjust')
DataMonitor = Transition(label='Data Monitor')
AIAnalytics = Transition(label='AI Analytics')
YieldReview = Transition(label='Yield Review')
MarketLink = Transition(label='Market Link')
ImpactStudy = Transition(label='Impact Study')
ScalePlan = Transition(label='Scale Plan')

# Construct parts according to description logic:

# Initial sequence:
# Site Survey --> Modular Design --> Sensor Setup --> Nutrient Mix
# Permit Check runs concurrently but must finish before Logistics Plan
# Logistics Plan --> Staff Training --> Crop Seeding

# After Crop Seeding: loop of adaptive lighting and monitoring phases:
# Loop: execute Light Adjust, then choice to exit or
#       execute Data Monitor, AI Analytics, Yield Review, then Light Adjust again

light_cycle = LightAdjust
monitoring_sequence = StrictPartialOrder(nodes=[DataMonitor, AIAnalytics, YieldReview])
monitoring_sequence.order.add_edge(DataMonitor, AIAnalytics)
monitoring_sequence.order.add_edge(AIAnalytics, YieldReview)
monitoring_with_light = StrictPartialOrder(nodes=[monitoring_sequence, LightAdjust])
monitoring_with_light.order.add_edge(monitoring_sequence, LightAdjust)

loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[light_cycle, monitoring_with_light])

# After loop, Market Link --> Impact Study --> Scale Plan

final_sequence = StrictPartialOrder(nodes=[MarketLink, ImpactStudy, ScalePlan])
final_sequence.order.add_edge(MarketLink, ImpactStudy)
final_sequence.order.add_edge(ImpactStudy, ScalePlan)

# PermitCheck must finish before LogisticsPlan
# Permit Check possibly concurrent with initial phases (likely after Modular Design)

# Assemble beginning partial order with PermitCheck concurrently but needed before LogisticsPlan
first_part = StrictPartialOrder(
    nodes=[SiteSurvey, ModularDesign, PermitCheck, SensorSetup, NutrientMix]
)
first_part.order.add_edge(SiteSurvey, ModularDesign)
first_part.order.add_edge(ModularDesign, SensorSetup)
first_part.order.add_edge(SensorSetup, NutrientMix)
# PermitCheck can run after ModularDesign (logical) or in parallel after SiteSurvey completion,
# For safe ordering, let's add SiteSurvey->PermitCheck (both start after site survey)
first_part.order.add_edge(SiteSurvey, PermitCheck)

# LogisticsPlan after NutrientMix and PermitCheck
second_part = StrictPartialOrder(
    nodes=[NutrientMix, PermitCheck, LogisticsPlan, StaffTraining, CropSeeding]
)
second_part.order.add_edge(NutrientMix, LogisticsPlan)
second_part.order.add_edge(PermitCheck, LogisticsPlan)
second_part.order.add_edge(LogisticsPlan, StaffTraining)
second_part.order.add_edge(StaffTraining, CropSeeding)

# Combine first_part and second_part into beginning PO with partial order edges

beginning = StrictPartialOrder(
    nodes=[SiteSurvey, ModularDesign, PermitCheck,
           SensorSetup, NutrientMix, LogisticsPlan, StaffTraining, CropSeeding])
# from first_part
beginning.order.add_edge(SiteSurvey, ModularDesign)
beginning.order.add_edge(ModularDesign, SensorSetup)
beginning.order.add_edge(SensorSetup, NutrientMix)
beginning.order.add_edge(SiteSurvey, PermitCheck)
# from second_part
beginning.order.add_edge(NutrientMix, LogisticsPlan)
beginning.order.add_edge(PermitCheck, LogisticsPlan)
beginning.order.add_edge(LogisticsPlan, StaffTraining)
beginning.order.add_edge(StaffTraining, CropSeeding)

# After CropSeeding, loop of light/monitoring, then final sequence
after_crops = StrictPartialOrder(nodes=[CropSeeding, loop_monitoring, final_sequence])
after_crops.order.add_edge(CropSeeding, loop_monitoring)
after_crops.order.add_edge(loop_monitoring, final_sequence)

# Root PO combining beginning and after_crops
root = StrictPartialOrder(nodes=[beginning, after_crops])
root.order.add_edge(beginning, after_crops)