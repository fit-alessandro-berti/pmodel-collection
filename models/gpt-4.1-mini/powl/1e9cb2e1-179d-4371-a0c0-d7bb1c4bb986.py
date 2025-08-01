# Generated from: 1e9cb2e1-179d-4371-a0c0-d7bb1c4bb986.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a constrained city environment, integrating hydroponic and aeroponic systems. It involves site assessment, modular design, environmental calibration, seed selection, nutrient cycling, pest monitoring, and automated harvesting. The process also includes community engagement, energy optimization, waste recycling, and real-time data analytics to ensure sustainable production and market readiness of fresh produce. Each phase is interdependent, requiring cross-disciplinary coordination between agronomists, engineers, and city planners to maximize yield and minimize ecological footprint in an atypical urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SystemBuild = Transition(label='System Build')
EnvCalibration = Transition(label='Env Calibration')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
PlantingSetup = Transition(label='Planting Setup')
PestScan = Transition(label='Pest Scan')
GrowthMonitor = Transition(label='Growth Monitor')
WaterCycle = Transition(label='Water Cycle')
EnergyAudit = Transition(label='Energy Audit')
WasteProcess = Transition(label='Waste Process')
HarvestPlan = Transition(label='Harvest Plan')
DataSync = Transition(label='Data Sync')
MarketPrep = Transition(label='Market Prep')
CommunityMeet = Transition(label='Community Meet')

# Build partial order representing the process

# Phase 1: Site Survey -> Design Layout -> System Build -> Env Calibration
phase1 = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, SystemBuild, EnvCalibration])
phase1.order.add_edge(SiteSurvey, DesignLayout)
phase1.order.add_edge(DesignLayout, SystemBuild)
phase1.order.add_edge(SystemBuild, EnvCalibration)

# Phase 2: Seed Selection -> Nutrient Mix -> Planting Setup
phase2 = StrictPartialOrder(nodes=[SeedSelection, NutrientMix, PlantingSetup])
phase2.order.add_edge(SeedSelection, NutrientMix)
phase2.order.add_edge(NutrientMix, PlantingSetup)

# Phase 3: Pest Scan -> Growth Monitor -> Water Cycle
phase3 = StrictPartialOrder(nodes=[PestScan, GrowthMonitor, WaterCycle])
phase3.order.add_edge(PestScan, GrowthMonitor)
phase3.order.add_edge(GrowthMonitor, WaterCycle)

# Phase 4: Energy Audit -> Waste Process
phase4 = StrictPartialOrder(nodes=[EnergyAudit, WasteProcess])
phase4.order.add_edge(EnergyAudit, WasteProcess)

# Phase 5: Harvest Plan -> Data Sync -> Market Prep
phase5 = StrictPartialOrder(nodes=[HarvestPlan, DataSync, MarketPrep])
phase5.order.add_edge(HarvestPlan, DataSync)
phase5.order.add_edge(DataSync, MarketPrep)

# Community engagement happens in parallel with phases 4 and 5 (energy/waste and harvest/data/market)

# Compose phases 2 and 3 (biological operations) as partial order
bio_phase = StrictPartialOrder(nodes=[phase2, phase3])
bio_phase.order.add_edge(phase2, phase3)  # Seed/Nutrients/Planting before Pest/Growth/Water for clarity

# Compose phases 4,5 and Community Meet in parallel
post_harvest_phase = StrictPartialOrder(nodes=[phase4, phase5, CommunityMeet])

# Combine phases:
# Main flow: phase1 -> bio_phase -> post_harvest_phase
root = StrictPartialOrder(nodes=[phase1, bio_phase, post_harvest_phase])
root.order.add_edge(phase1, bio_phase)
root.order.add_edge(bio_phase, post_harvest_phase)