# Generated from: 57bb9868-07f5-4dbb-95a2-bddafc2cbe3e.json
# Description: This process outlines the complex logistics and operational steps involved in managing an urban vertical farming supply chain. It begins with seed procurement and genetic selection, followed by environmental calibration and hydroponic setup. Continuous monitoring of nutrient levels and pest control ensures optimal plant growth. Harvesting is scheduled based on data analytics predicting peak freshness. Post-harvest processing includes automated packaging and quality inspection. The produce is then routed through cold-chain logistics and distributed via micro-fulfillment centers to local retailers and direct-to-consumer platforms. Feedback loops from sales data influence future crop planning and resource allocation, creating a dynamic, sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
SeedSourcing = Transition(label='Seed Sourcing')
GeneticSelect = Transition(label='Genetic Select')
EnvCalibration = Transition(label='Env Calibration')
HydroSetup = Transition(label='Hydro Setup')
NutrientMonitor = Transition(label='Nutrient Monitor')
PestControl = Transition(label='Pest Control')
GrowthAnalytics = Transition(label='Growth Analytics')
HarvestPlan = Transition(label='Harvest Plan')
AutomatedPack = Transition(label='Automated Pack')
QualityCheck = Transition(label='Quality Check')
ColdStorage = Transition(label='Cold Storage')
LogisticsRoute = Transition(label='Logistics Route')
MicroFulfill = Transition(label='Micro Fulfill')
RetailSupply = Transition(label='Retail Supply')
ConsumerShip = Transition(label='Consumer Ship')
SalesFeedback = Transition(label='Sales Feedback')
CropAdjust = Transition(label='Crop Adjust')

# Model environmental calibration and hydroponic setup in partial order (concurrent)
env_hydro = StrictPartialOrder(nodes=[EnvCalibration, HydroSetup])
# No order edges: concurrent

# Continuous monitoring: Nutrient Monitor and Pest Control concurrent
monitoring = StrictPartialOrder(nodes=[NutrientMonitor, PestControl])

# Distribution choice: Micro Fulfill and Retail Supply can run concurrently and both precede Consumer Ship
micro_retail = StrictPartialOrder(nodes=[MicroFulfill, RetailSupply])
# Consumer Ship depends on both Micro Fulfill and Retail Supply
dist = StrictPartialOrder(nodes=[micro_retail, ConsumerShip])
dist.order.add_edge(micro_retail, ConsumerShip)

# But above is not correct because micro_retail is a StrictPartialOrder node, we need to flatten:
# Instead, create a PO with nodes MicroFulfill, RetailSupply, ConsumerShip
dist = StrictPartialOrder(nodes=[MicroFulfill, RetailSupply, ConsumerShip])
dist.order.add_edge(MicroFulfill, ConsumerShip)
dist.order.add_edge(RetailSupply, ConsumerShip)

# Post-harvest packaging and quality check partial order
pack_quality = StrictPartialOrder(nodes=[AutomatedPack, QualityCheck])
# No order edges: concurrent

# Cold chain logistics before distribution
cold_and_logistics = StrictPartialOrder(nodes=[ColdStorage, LogisticsRoute])
cold_and_logistics.order.add_edge(ColdStorage, LogisticsRoute)

# Harvest plan after growth analytics
harvest_plan = StrictPartialOrder(nodes=[GrowthAnalytics, HarvestPlan])
harvest_plan.order.add_edge(GrowthAnalytics, HarvestPlan)

# Loop: SalesFeedback and CropAdjust form feedback loop to adjust crop planning
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[SalesFeedback, CropAdjust])

# Now construct the overall model:

# 1. Seed Sourcing -> Genetic Select
seed_genetic = StrictPartialOrder(nodes=[SeedSourcing, GeneticSelect])
seed_genetic.order.add_edge(SeedSourcing, GeneticSelect)

# 2. After GeneticSelect, env calibration and hydro setup concurrently
genetic_envhydro = StrictPartialOrder(nodes=[GeneticSelect, env_hydro])
genetic_envhydro.order.add_edge(GeneticSelect, env_hydro)

# 3. After env_hydro, monitoring concurrent activities
envhydro_monitor = StrictPartialOrder(nodes=[env_hydro, monitoring])
envhydro_monitor.order.add_edge(env_hydro, monitoring)

# 4. After monitoring, growth analytics
monitor_growth = StrictPartialOrder(nodes=[monitoring, GrowthAnalytics])
monitor_growth.order.add_edge(monitoring, GrowthAnalytics)

# 5. After growth analytics, harvest plan
growth_harvest = StrictPartialOrder(nodes=[GrowthAnalytics, HarvestPlan])
growth_harvest.order.add_edge(GrowthAnalytics, HarvestPlan)

# 6. After harvest plan, packaging and quality check concurrent
harvest_pack = StrictPartialOrder(nodes=[HarvestPlan, pack_quality])
harvest_pack.order.add_edge(HarvestPlan, pack_quality)

# 7. After packaging and quality check, cold storage and logistics route
pack_coldlogistics = StrictPartialOrder(nodes=[pack_quality, cold_and_logistics])
pack_coldlogistics.order.add_edge(pack_quality, cold_and_logistics)

# 8. After logistics route, distribution (micro fulfill, retail supply) and consumer ship
logistics_distribution = StrictPartialOrder(nodes=[cold_and_logistics, dist])
logistics_distribution.order.add_edge(cold_and_logistics, dist)

# 9. After distribution, sales feedback (start of loop)
dist_feedback = StrictPartialOrder(nodes=[dist, feedback_loop])
dist_feedback.order.add_edge(dist, feedback_loop)

# Finally, seed_genetic -> envhydro_monitor...
# Compose the entire chain by nesting:
# seed_genetic -> genetic_envhydro (has geneticselect again, but we reuse same)
# To avoid duplication of GeneticSelect, flatten and create a full order tree.

# Construct steps incrementally to include all unique nodes with proper ordering.
# Because nodes must be unique, create one global PO that combines all steps:

nodes = [
    SeedSourcing,
    GeneticSelect,
    EnvCalibration,
    HydroSetup,
    NutrientMonitor,
    PestControl,
    GrowthAnalytics,
    HarvestPlan,
    AutomatedPack,
    QualityCheck,
    ColdStorage,
    LogisticsRoute,
    MicroFulfill,
    RetailSupply,
    ConsumerShip,
    SalesFeedback,
    CropAdjust,
    feedback_loop,
]

# feedback_loop is already included, no extra here; actually feedback_loop children are SalesFeedback and CropAdjust

# Actually, feedback_loop is OperatorPOWL node, children SalesFeedback and CropAdjust are also included as nodes above
# So we should not add feedback_loop as separate node along with SalesFeedback and CropAdjust.
# Instead, add only feedback_loop node, and exclude SalesFeedback and CropAdjust as separate nodes from the PO nodes set.

# Re-define nodes accordingly:

nodes = [
    SeedSourcing,
    GeneticSelect,
    EnvCalibration,
    HydroSetup,
    NutrientMonitor,
    PestControl,
    GrowthAnalytics,
    HarvestPlan,
    AutomatedPack,
    QualityCheck,
    ColdStorage,
    LogisticsRoute,
    MicroFulfill,
    RetailSupply,
    ConsumerShip,
    feedback_loop,
]

# define the PO
root = StrictPartialOrder(nodes=nodes)

# Add order edges representing all dependencies:

# Seed Sourcing --> Genetic Select
root.order.add_edge(SeedSourcing, GeneticSelect)

# Genetic Select --> Env Calibration and Hydro Setup (both concurrent)
root.order.add_edge(GeneticSelect, EnvCalibration)
root.order.add_edge(GeneticSelect, HydroSetup)

# Env Calibration --> Nutrient Monitor and Pest Control (both concurrent)
root.order.add_edge(EnvCalibration, NutrientMonitor)
root.order.add_edge(EnvCalibration, PestControl)

# Hydro Setup --> Nutrient Monitor and Pest Control (both concurrent)
root.order.add_edge(HydroSetup, NutrientMonitor)
root.order.add_edge(HydroSetup, PestControl)

# Nutrient Monitor and Pest Control --> Growth Analytics
root.order.add_edge(NutrientMonitor, GrowthAnalytics)
root.order.add_edge(PestControl, GrowthAnalytics)

# Growth Analytics --> Harvest Plan
root.order.add_edge(GrowthAnalytics, HarvestPlan)

# Harvest Plan --> Automated Pack and Quality Check (concurrent)
root.order.add_edge(HarvestPlan, AutomatedPack)
root.order.add_edge(HarvestPlan, QualityCheck)

# Automated Pack and Quality Check --> Cold Storage and then Logistics Route (sequential)
root.order.add_edge(AutomatedPack, ColdStorage)
root.order.add_edge(QualityCheck, ColdStorage)

root.order.add_edge(ColdStorage, LogisticsRoute)

# Logistics Route --> Micro Fulfill and Retail Supply (concurrent)
root.order.add_edge(LogisticsRoute, MicroFulfill)
root.order.add_edge(LogisticsRoute, RetailSupply)

# Micro Fulfill and Retail Supply --> Consumer Ship
root.order.add_edge(MicroFulfill, ConsumerShip)
root.order.add_edge(RetailSupply, ConsumerShip)

# Consumer Ship --> feedback loop node
root.order.add_edge(ConsumerShip, feedback_loop)

# feedback_loop children are SalesFeedback and CropAdjust in a loop:
# loop semantics are embedded in feedback_loop node itself
