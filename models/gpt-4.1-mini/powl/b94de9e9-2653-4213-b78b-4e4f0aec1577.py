# Generated from: b94de9e9-2653-4213-b78b-4e4f0aec1577.json
# Description: This process outlines the comprehensive lifecycle of an urban vertical farm operating within a densely populated city environment. It begins with site assessment and environmental analysis to ensure optimal location and conditions. Following that, the design of vertical growing modules integrates advanced hydroponic and aeroponic systems tailored for space efficiency. Seed selection focuses on high-yield, fast-growing crops suitable for indoor farming. Nutrient solution formulation is customized to maximize plant health and growth rates. Automated planting utilizes robotic arms for precision and speed. Continuous monitoring employs IoT sensors tracking humidity, light, and nutrient levels in real-time. Pollination is managed either manually or through controlled introduction of pollinator insects. Pest control combines biological agents and minimal chemical use aligned with sustainability goals. Harvesting schedules are optimized with AI-driven analytics predicting peak ripeness. Post-harvest processing includes cleaning, packaging, and cold storage within the facility to preserve freshness. Distribution logistics coordinate last-mile delivery via electric vehicles to minimize carbon footprint. Waste recycling converts plant residues into bio-compost or energy. Finally, data analytics assess overall yield, resource consumption, and environmental impact to inform iterative improvements and scalability strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
EnvAnalysis = Transition(label='Env Analysis')
ModuleDesign = Transition(label='Module Design')
SeedSelect = Transition(label='Seed Select')
NutrientMix = Transition(label='Nutrient Mix')
AutoPlant = Transition(label='Auto Plant')
SensorSetup = Transition(label='Sensor Setup')
PollinateManage = Transition(label='Pollinate Manage')
PestControl = Transition(label='Pest Control')
AIHarvest = Transition(label='AI Harvest')
CleanProcess = Transition(label='Clean Process')
PackGoods = Transition(label='Pack Goods')
ColdStorage = Transition(label='Cold Storage')
EcoDelivery = Transition(label='Eco Delivery')
WasteRecycle = Transition(label='Waste Recycle')
DataReview = Transition(label='Data Review')

# Model partial order for initial site assessment & environmental analysis (concurrent)
initialPO = StrictPartialOrder(nodes=[SiteAssess, EnvAnalysis])

# Design depends on completion of initial assessment and analysis
# SeedSelect depends on ModuleDesign
# NutrientMix depends on SeedSelect
designPO = StrictPartialOrder(nodes=[ModuleDesign, SeedSelect, NutrientMix])
designPO.order.add_edge(ModuleDesign, SeedSelect)
designPO.order.add_edge(SeedSelect, NutrientMix)

# Planting phase follows NutrientMix
# SensorSetup concurrent with AutoPlant (both after NutrientMix)
plantingPO = StrictPartialOrder(nodes=[AutoPlant, SensorSetup])
# NutrientMix precedes plantingPO
# We'll model combined so NutrientMix --> AutoPlant and NutrientMix --> SensorSetup
# We'll embed designPO and plantingPO into a larger PO below

# Pollination and Pest Control run in parallel after planting and sensor setup
pollinateAndPestPO = StrictPartialOrder(nodes=[PollinateManage, PestControl])

# Harvest phase after pollination and pest control
# AI Harvest
# Post harvest process: CleanProcess -> PackGoods -> ColdStorage (strict order)
postHarvestPO = StrictPartialOrder(nodes=[CleanProcess, PackGoods, ColdStorage])
postHarvestPO.order.add_edge(CleanProcess, PackGoods)
postHarvestPO.order.add_edge(PackGoods, ColdStorage)

# Distribution (Eco Delivery) and Waste Recycle run in parallel after post-harvest
distAndWastePO = StrictPartialOrder(nodes=[EcoDelivery, WasteRecycle])

# Final Data Review after distribution and waste recycle
finalPO = StrictPartialOrder(nodes=[DataReview])

# Assemble full model layer by layer with ordering

# Layer 1: initialPO (SiteAssess, EnvAnalysis)
# Layer 2: designPO (ModuleDesign, SeedSelect, NutrientMix) depends on initialPO
# Layer 3: plantingPO (AutoPlant, SensorSetup) depends on NutrientMix
# Layer 4: pollinateAndPestPO (PollinateManage, PestControl) depends on plantingPO (both)
# Layer 5: AIHarvest depends on pollinateAndPestPO
# Layer 6: postHarvestPO (CleanProcess, PackGoods, ColdStorage) depends on AIHarvest
# Layer 7: distAndWastePO (EcoDelivery, WasteRecycle) depends on postHarvestPO
# Layer 8: finalPO (DataReview) depends on distAndWastePO

# Compose composite StrictPartialOrders with all nodes and edges

nodes_all = [
    SiteAssess, EnvAnalysis,
    ModuleDesign, SeedSelect, NutrientMix,
    AutoPlant, SensorSetup,
    PollinateManage, PestControl,
    AIHarvest,
    CleanProcess, PackGoods, ColdStorage,
    EcoDelivery, WasteRecycle,
    DataReview
]

root = StrictPartialOrder(nodes=nodes_all)

# initialPO edges (no order between SiteAssess and EnvAnalysis)

# initialPO --> designPO
root.order.add_edge(SiteAssess, ModuleDesign)
root.order.add_edge(EnvAnalysis, ModuleDesign)

# designPO edges
root.order.add_edge(ModuleDesign, SeedSelect)
root.order.add_edge(SeedSelect, NutrientMix)

# designPO --> plantingPO
root.order.add_edge(NutrientMix, AutoPlant)
root.order.add_edge(NutrientMix, SensorSetup)

# plantingPO: AutoPlant and SensorSetup concurrent (no order)

# plantingPO --> pollinateAndPestPO
root.order.add_edge(AutoPlant, PollinateManage)
root.order.add_edge(AutoPlant, PestControl)
root.order.add_edge(SensorSetup, PollinateManage)
root.order.add_edge(SensorSetup, PestControl)

# pollinateAndPestPO: PollinateManage and PestControl concurrent (no order)

# pollinateAndPestPO --> AIHarvest
root.order.add_edge(PollinateManage, AIHarvest)
root.order.add_edge(PestControl, AIHarvest)

# AIHarvest --> postHarvestPO (CleanProcess)
root.order.add_edge(AIHarvest, CleanProcess)

# postHarvestPO edges
root.order.add_edge(CleanProcess, PackGoods)
root.order.add_edge(PackGoods, ColdStorage)

# postHarvestPO --> distAndWastePO (EcoDelivery, WasteRecycle)
root.order.add_edge(ColdStorage, EcoDelivery)
root.order.add_edge(ColdStorage, WasteRecycle)

# distAndWastePO: EcoDelivery and WasteRecycle concurrent (no order)

# distAndWastePO --> finalPO (DataReview)
root.order.add_edge(EcoDelivery, DataReview)
root.order.add_edge(WasteRecycle, DataReview)