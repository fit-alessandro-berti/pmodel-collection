# Generated from: b1e714ed-4a75-492a-85bf-ad4a83495ab1.json
# Description: This process involves the comprehensive management of a multi-layer urban vertical farm integrating advanced hydroponics, IoT sensor networks, and AI-driven climate control. It includes seed selection and germination, nutrient solution calibration, pest detection via computer vision, robotic harvesting, and automated packaging. Continuous environmental monitoring adjusts light, humidity, and temperature to optimize crop yield and quality. The process further encompasses waste recycling, energy consumption analysis, real-time supply chain coordination, and dynamic market pricing updates to ensure sustainable and efficient production tailored to urban consumer demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
SeedSowing = Transition(label='Seed Sowing')
GerminationCheck = Transition(label='Germination Check')
NutrientMix = Transition(label='Nutrient Mix')
SensorCalibration = Transition(label='Sensor Calibration')
PestScan = Transition(label='Pest Scan')
ClimateAdjust = Transition(label='Climate Adjust')
WaterCirculate = Transition(label='Water Circulate')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestRobots = Transition(label='Harvest Robots')
QualityInspect = Transition(label='Quality Inspect')
WasteSort = Transition(label='Waste Sort')
EnergyAudit = Transition(label='Energy Audit')
PackProduce = Transition(label='Pack Produce')
OrderSync = Transition(label='Order Sync')
PriceUpdate = Transition(label='Price Update')
DeliveryPlan = Transition(label='Delivery Plan')

# Build partial orders for logical groupings

# 1) Seed & grow cycle before harvesting
seed_and_grow = StrictPartialOrder(nodes=[SeedSowing, GerminationCheck, NutrientMix])
seed_and_grow.order.add_edge(SeedSowing, GerminationCheck)
seed_and_grow.order.add_edge(GerminationCheck, NutrientMix)

# 2) Sensor setup and environment monitoring loop:
# SensorCalibration -> (loop over ClimateAdjust, WaterCirculate, GrowthMonitor)
env_monitor_body = StrictPartialOrder(nodes=[ClimateAdjust, WaterCirculate, GrowthMonitor])
# No order edges means these three are concurrent (can happen in parallel)
env_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[SensorCalibration, env_monitor_body])
# interpret as: do SensorCalibration, then repeatedly do the concurrency of ClimateAdjust, WaterCirculate, GrowthMonitor until exit

# 3) Pest detection and harvesting sequence
pest_and_harvest = StrictPartialOrder(nodes=[PestScan, HarvestRobots, QualityInspect])
pest_and_harvest.order.add_edge(PestScan, HarvestRobots)
pest_and_harvest.order.add_edge(HarvestRobots, QualityInspect)

# 4) Packaging and delivery sequence
pack_and_deliver = StrictPartialOrder(nodes=[PackProduce, OrderSync, PriceUpdate, DeliveryPlan])
pack_and_deliver.order.add_edge(PackProduce, OrderSync)
pack_and_deliver.order.add_edge(OrderSync, PriceUpdate)
pack_and_deliver.order.add_edge(PriceUpdate, DeliveryPlan)

# 5) Waste sorting and energy auditing are concurrent and can happen anytime after growth
waste_and_energy = StrictPartialOrder(nodes=[WasteSort, EnergyAudit])
# no order edges => concurrent

# Combine all major parts in a partial order reflecting typical dependencies:
# seed_and_grow -> env_monitor_loop (calibration & monitoring happens after initial nutrient mix)
# env_monitor_loop -> pest_and_harvest (harvesting depends on monitoring)
# pest_and_harvest -> pack_and_deliver (harvested goods go to packaging and delivery)
# seed_and_grow -> waste_and_energy (waste and energy can start after growing phase)
# env_monitor_loop -> waste_and_energy (monitoring might influence waste and energy assessment)
# Use partial order where waste_and_energy can run concurrently with pest_and_harvest and pack_and_deliver but after seed_and_grow and env_monitor_loop

nodes = [seed_and_grow, env_monitor_loop, pest_and_harvest, pack_and_deliver, waste_and_energy]
root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(seed_and_grow, env_monitor_loop)
root.order.add_edge(seed_and_grow, waste_and_energy)
root.order.add_edge(env_monitor_loop, pest_and_harvest)
root.order.add_edge(env_monitor_loop, waste_and_energy)
root.order.add_edge(pest_and_harvest, pack_and_deliver)