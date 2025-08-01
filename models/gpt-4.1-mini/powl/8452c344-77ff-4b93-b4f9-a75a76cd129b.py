# Generated from: 8452c344-77ff-4b93-b4f9-a75a76cd129b.json
# Description: This process describes the complex operational cycle of an urban vertical farming facility that integrates automated hydroponics, AI-driven environmental control, and community engagement. It begins with nutrient formulation and seed selection, followed by automated planting and continuous environmental monitoring. The system adjusts lighting, humidity, and nutrient delivery dynamically, responding to real-time sensor data. Periodic pest detection and organic treatment application ensure crop health without chemicals. Harvesting is automated using robotic arms, then produce undergoes quality inspection and packaging. The process also includes data logging for yield optimization and community distribution planning. Finally, waste recycling and equipment maintenance close the loop, ensuring sustainability and operational efficiency in an atypical yet realistic urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
AutomatedPlant = Transition(label='Automated Plant')
EnviroMonitor = Transition(label='Enviro Monitor')
LightAdjust = Transition(label='Light Adjust')
HumidityControl = Transition(label='Humidity Control')
NutrientFeed = Transition(label='Nutrient Feed')
PestDetect = Transition(label='Pest Detect')
OrganicTreat = Transition(label='Organic Treat')
RoboticHarvest = Transition(label='Robotic Harvest')
QualityCheck = Transition(label='Quality Check')
ProducePack = Transition(label='Produce Pack')
DataLog = Transition(label='Data Log')
YieldReview = Transition(label='Yield Review')
CommunityPlan = Transition(label='Community Plan')
WasteRecycle = Transition(label='Waste Recycle')
EquipMaintain = Transition(label='Equip Maintain')

# Loop body for continuous environmental adjustment:
# Periodic pest detection and treatment is optional and repeated during the loop.
# The loop components:
#   A: Environmental adjustment and monitoring part (EnviroMonitor -> [LightAdjust, HumidityControl, NutrientFeed] in parallel)
#   B: Pest Detect + Organic Treat (optional, must repeat with A)

# Model parallel environmental controls as partially concurrent:
env_controls_nodes = [LightAdjust, HumidityControl, NutrientFeed]
env_controls_po = StrictPartialOrder(nodes=env_controls_nodes)
# No order edges -> fully concurrent

# EnviroMonitor before environmental controls:
env_monitor_body_nodes = [EnviroMonitor, env_controls_po]
env_monitor_body = StrictPartialOrder(nodes=env_monitor_body_nodes)
env_monitor_body.order.add_edge(EnviroMonitor, env_controls_po)

# Pest treatment PO:
pest_treatment_po = StrictPartialOrder(nodes=[PestDetect, OrganicTreat])
pest_treatment_po.order.add_edge(PestDetect, OrganicTreat)

# Loop: 
# Execute environmental monitoring and adjustment (env_monitor_body),
# then choose to exit or do pest treatment + restart loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[env_monitor_body, pest_treatment_po])

# Partial order for initial steps:
# Seed Selection -> Nutrient Mix -> Automated Plant -> loop
initial_steps = StrictPartialOrder(nodes=[SeedSelection, NutrientMix, AutomatedPlant, loop])
initial_steps.order.add_edge(SeedSelection, NutrientMix)
initial_steps.order.add_edge(NutrientMix, AutomatedPlant)
initial_steps.order.add_edge(AutomatedPlant, loop)

# After loop:
# RoboticHarvest -> QualityCheck -> ProducePack
harvest_pack_po = StrictPartialOrder(nodes=[RoboticHarvest, QualityCheck, ProducePack])
harvest_pack_po.order.add_edge(RoboticHarvest, QualityCheck)
harvest_pack_po.order.add_edge(QualityCheck, ProducePack)

# After packaging:
# DataLog -> YieldReview -> CommunityPlan  (strict order)
data_yield_community = StrictPartialOrder(nodes=[DataLog, YieldReview, CommunityPlan])
data_yield_community.order.add_edge(DataLog, YieldReview)
data_yield_community.order.add_edge(YieldReview, CommunityPlan)

# Final closing loop: WasteRecycle and EquipMaintain can be concurrent
final_nodes = [WasteRecycle, EquipMaintain]
final_po = StrictPartialOrder(nodes=final_nodes)
# No order edges -> concurrent

# Compose the final partial order for the whole process:
root_nodes = [initial_steps, harvest_pack_po, data_yield_community, final_po]
root = StrictPartialOrder(nodes=root_nodes)

# Add order edges connecting the phases strictly
root.order.add_edge(initial_steps, harvest_pack_po)
root.order.add_edge(harvest_pack_po, data_yield_community)
root.order.add_edge(data_yield_community, final_po)