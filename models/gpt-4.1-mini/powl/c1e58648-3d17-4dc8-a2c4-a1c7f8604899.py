# Generated from: c1e58648-3d17-4dc8-a2c4-a1c7f8604899.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a metropolitan environment. It covers site selection in dense urban areas, integration of advanced hydroponic systems, environmental control calibration, and multi-level crop scheduling. The process also includes securing permits, implementing renewable energy sources, establishing supply chain logistics for fresh produce, and coordinating with local community stakeholders to ensure sustainability and compliance with urban regulations. Each activity is designed to optimize yield while minimizing ecological footprint, ensuring year-round production with minimal human intervention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
DesignLayout = Transition(label='Design Layout')
HydroSetup = Transition(label='Hydro Setup')
LightingInstall = Transition(label='Lighting Install')
ClimateTune = Transition(label='Climate Tune')
SeedSourcing = Transition(label='Seed Sourcing')
PlantingCycle = Transition(label='Planting Cycle')
WaterTesting = Transition(label='Water Testing')
NutrientMix = Transition(label='Nutrient Mix')
EnergySetup = Transition(label='Energy Setup')
PestControl = Transition(label='Pest Control')
HarvestPlan = Transition(label='Harvest Plan')
LogisticsMap = Transition(label='Logistics Map')
CommunityMeet = Transition(label='Community Meet')
DataMonitor = Transition(label='Data Monitor')
WasteManage = Transition(label='Waste Manage')

# Step 1: Site Survey then Permit Filing
step1 = StrictPartialOrder(nodes=[SiteSurvey, PermitFiling])
step1.order.add_edge(SiteSurvey, PermitFiling)

# Step 2: Design Layout after Permit Filing
step2 = StrictPartialOrder(nodes=[PermitFiling, DesignLayout])
step2.order.add_edge(PermitFiling, DesignLayout)

# Step 3: Hydro Setup, Lighting Install, Climate Tune (environmental control calibration)
env_setup = StrictPartialOrder(nodes=[HydroSetup, LightingInstall, ClimateTune])
# These three can run concurrently after Design Layout, so partial order order edges from DesignLayout to each

# Step 4: Seed Sourcing after Design Layout (can overlap with env_setup)
step4 = StrictPartialOrder(nodes=[DesignLayout, SeedSourcing])
step4.order.add_edge(DesignLayout, SeedSourcing)

# Step 5: Planting Cycle depends on Seed Sourcing and env_setup done
# So Planting Cycle after SeedSourcing
planting_cycle = StrictPartialOrder(nodes=[SeedSourcing, PlantingCycle])
planting_cycle.order.add_edge(SeedSourcing, PlantingCycle)
# Planting Cycle also after all env_setup activities
# We'll model this by putting a PO with env_setup nodes plus DesignLayout, then edges

# Combine DesignLayout and env_setup nodes with order edges
env_and_design = StrictPartialOrder(nodes=[DesignLayout, HydroSetup, LightingInstall, ClimateTune])
env_and_design.order.add_edge(DesignLayout, HydroSetup)
env_and_design.order.add_edge(DesignLayout, LightingInstall)
env_and_design.order.add_edge(DesignLayout, ClimateTune)

# Planting Cycle after SeedSourcing and all env_setup done; 
# So from env_setup nodes and SeedSourcing to PlantingCycle
planting_phase = StrictPartialOrder(
    nodes=[HydroSetup, LightingInstall, ClimateTune, SeedSourcing, PlantingCycle]
)
planting_phase.order.add_edge(HydroSetup, PlantingCycle)
planting_phase.order.add_edge(LightingInstall, PlantingCycle)
planting_phase.order.add_edge(ClimateTune, PlantingCycle)
planting_phase.order.add_edge(SeedSourcing, PlantingCycle)

# Step 6: Water Testing and Nutrient Mix accompany Planting Cycle, can run concurrently but before Pest Control
testing_nutrient = StrictPartialOrder(nodes=[WaterTesting, NutrientMix])
# They happen after Planting Cycle started? We'll put them concurrent with Planting Cycle, but before Pest Control

# Pest Control after these three: Planting Cycle, Water Testing, Nutrient Mix
pest_control_po = StrictPartialOrder(
    nodes=[PlantingCycle, WaterTesting, NutrientMix, PestControl]
)
pest_control_po.order.add_edge(PlantingCycle, PestControl)
pest_control_po.order.add_edge(WaterTesting, PestControl)
pest_control_po.order.add_edge(NutrientMix, PestControl)

# Step 7: Harvest Plan after Pest Control
harvest_plan_po = StrictPartialOrder(nodes=[PestControl, HarvestPlan])
harvest_plan_po.order.add_edge(PestControl, HarvestPlan)

# Step 8: Logistics Map after Harvest Plan
logistics_map_po = StrictPartialOrder(nodes=[HarvestPlan, LogisticsMap])
logistics_map_po.order.add_edge(HarvestPlan, LogisticsMap)

# Step 9: Community Meet can be concurrent with Logistics Map but after Harvest Plan
community_meet_po = StrictPartialOrder(nodes=[HarvestPlan, LogisticsMap, CommunityMeet])
community_meet_po.order.add_edge(HarvestPlan, LogisticsMap)
community_meet_po.order.add_edge(HarvestPlan, CommunityMeet)

# Step 10: Energy Setup can be done after Permit Filing (can be concurrent with env_setup)
energy_setup_po = StrictPartialOrder(nodes=[PermitFiling, EnergySetup])
energy_setup_po.order.add_edge(PermitFiling, EnergySetup)

# Step 11: Data Monitor and Waste Manage run continuously after Planting Cycle (modeled as concurrent and after Planting Cycle)

data_waste = StrictPartialOrder(nodes=[PlantingCycle, DataMonitor, WasteManage])
data_waste.order.add_edge(PlantingCycle, DataMonitor)
data_waste.order.add_edge(PlantingCycle, WasteManage)

# Now build the overall PO combining all nodes (all distinct) and orders by relationships:

# Collect unique nodes
all_nodes = {
    SiteSurvey,
    PermitFiling,
    DesignLayout,
    HydroSetup,
    LightingInstall,
    ClimateTune,
    SeedSourcing,
    PlantingCycle,
    WaterTesting,
    NutrientMix,
    PestControl,
    HarvestPlan,
    LogisticsMap,
    CommunityMeet,
    EnergySetup,
    DataMonitor,
    WasteManage,
}

root = StrictPartialOrder(nodes=list(all_nodes))

# Add order edges per above constraints:

# Site Survey -> Permit Filing
root.order.add_edge(SiteSurvey, PermitFiling)

# Permit Filing -> Design Layout & Energy Setup
root.order.add_edge(PermitFiling, DesignLayout)
root.order.add_edge(PermitFiling, EnergySetup)

# Design Layout -> Hydro Setup, Lighting Install, Climate Tune, Seed Sourcing
root.order.add_edge(DesignLayout, HydroSetup)
root.order.add_edge(DesignLayout, LightingInstall)
root.order.add_edge(DesignLayout, ClimateTune)
root.order.add_edge(DesignLayout, SeedSourcing)

# Hydro Setup, Lighting Install, Climate Tune, and Seed Sourcing -> Planting Cycle
root.order.add_edge(HydroSetup, PlantingCycle)
root.order.add_edge(LightingInstall, PlantingCycle)
root.order.add_edge(ClimateTune, PlantingCycle)
root.order.add_edge(SeedSourcing, PlantingCycle)

# Planting Cycle -> Water Testing, Nutrient Mix (concurrent start with planting is reasonable, but here order is Planting->WaterTesting/Nutrient)
root.order.add_edge(PlantingCycle, WaterTesting)
root.order.add_edge(PlantingCycle, NutrientMix)

# Water Testing, Nutrient Mix, and Planting Cycle -> Pest Control
root.order.add_edge(WaterTesting, PestControl)
root.order.add_edge(NutrientMix, PestControl)
root.order.add_edge(PlantingCycle, PestControl)

# Pest Control -> Harvest Plan
root.order.add_edge(PestControl, HarvestPlan)

# Harvest Plan -> Logistics Map, Community Meet
root.order.add_edge(HarvestPlan, LogisticsMap)
root.order.add_edge(HarvestPlan, CommunityMeet)

# Planting Cycle -> Data Monitor, Waste Manage (continuous monitoring)
root.order.add_edge(PlantingCycle, DataMonitor)
root.order.add_edge(PlantingCycle, WasteManage)