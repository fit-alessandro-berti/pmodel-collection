# Generated from: 9d6447e0-57ed-4746-8753-d2fe485f1108.json
# Description: This process outlines the establishment of a sustainable urban rooftop farming system designed to maximize limited space in metropolitan areas. It involves site assessment, structural analysis, soil preparation, hydroponic installation, seed selection, and environment control setup. The workflow integrates community engagement and digital monitoring to optimize crop yield while minimizing environmental impact. The process also includes regulatory compliance verification, pest management protocols, and periodic harvest scheduling, ensuring continuous production and quality assurance within an urban agricultural framework.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
LoadTesting = Transition(label='Load Testing')
DesignLayout = Transition(label='Design Layout')
SoilPrep = Transition(label='Soil Prep')
HydroSetup = Transition(label='Hydro Setup')
SeedSelection = Transition(label='Seed Selection')
PlantingSeeds = Transition(label='Planting Seeds')
IrrigationConfig = Transition(label='Irrigation Config')
SensorInstall = Transition(label='Sensor Install')
ClimateControl = Transition(label='Climate Control')
PestInspection = Transition(label='Pest Inspection')
CommunityMeet = Transition(label='Community Meet')
RegulationCheck = Transition(label='Regulation Check')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestPlan = Transition(label='Harvest Plan')
YieldAnalysis = Transition(label='Yield Analysis')

# Phase 1: Site assessment and structural analysis
phase1 = StrictPartialOrder(nodes=[SiteSurvey, LoadTesting, DesignLayout])
phase1.order.add_edge(SiteSurvey, LoadTesting)
phase1.order.add_edge(LoadTesting, DesignLayout)

# Phase 2: Soil and hydroponic setup
phase2 = StrictPartialOrder(nodes=[SoilPrep, HydroSetup])
phase2.order.add_edge(SoilPrep, HydroSetup)

# Phase 3: Planting preparation (Seed selection and planting seeds)
phase3 = StrictPartialOrder(nodes=[SeedSelection, PlantingSeeds])
phase3.order.add_edge(SeedSelection, PlantingSeeds)

# Phase 4: Environment control configuration
phase4 = StrictPartialOrder(nodes=[IrrigationConfig, SensorInstall, ClimateControl])
phase4.order.add_edge(IrrigationConfig, SensorInstall)
phase4.order.add_edge(SensorInstall, ClimateControl)

# Phase 5: Regulatory and pest protocols
phase5 = StrictPartialOrder(nodes=[PestInspection, RegulationCheck])
# They can happen in any order (concurrent)

# Phase 6: Monitoring and community engagement
phase6 = StrictPartialOrder(nodes=[CommunityMeet, GrowthMonitor])
# concurrent

# Phase 7: Harvest planning and yield analysis
phase7 = StrictPartialOrder(nodes=[HarvestPlan, YieldAnalysis])
phase7.order.add_edge(HarvestPlan, YieldAnalysis)

# Compose main workflow partial order
# The order follows the phases sequentially:
# phase1 --> phase2 --> phase3 --> phase4 --> phase5 --> phase6 --> phase7
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5, phase6, phase7]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, phase7)