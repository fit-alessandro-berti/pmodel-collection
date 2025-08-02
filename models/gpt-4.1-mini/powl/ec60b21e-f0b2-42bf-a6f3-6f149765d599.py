# Generated from: ec60b21e-f0b2-42bf-a6f3-6f149765d599.json
# Description: This process outlines the comprehensive steps required to establish a vertical farming system within an urban environment. It involves site analysis, modular design, environmental control calibration, nutrient solution preparation, seed selection, crop scheduling, automated monitoring, pest management, data analytics integration, and supply chain coordination. The process ensures optimized plant growth through controlled lighting, humidity, and temperature, while incorporating sustainable resource management and waste recycling. Stakeholder engagement and regulatory compliance are integrated to meet urban agricultural standards and community expectations, aiming for high yield and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
ModularDesign = Transition(label='Modular Design')
SystemBuild = Transition(label='System Build')
EnvControl = Transition(label='Env Control')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
PlantingSetup = Transition(label='Planting Setup')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
WaterCycle = Transition(label='Water Cycle')
DataCapture = Transition(label='Data Capture')
YieldForecast = Transition(label='Yield Forecast')
WasteReuse = Transition(label='Waste Reuse')
StakeholderMeet = Transition(label='Stakeholder Meet')
ComplianceCheck = Transition(label='Compliance Check')
SupplySync = Transition(label='Supply Sync')

# Build partial orders and loop structure according to process description

# After Modular Design -> System Build -> Env Control (calibration)
# Two parallel branches start after Env Control:
# 1) Nutrient Mix -> Seed Selection -> Planting Setup -> Loop (GrowthMonitor then pest control alternatively until done)
# 2) Water Cycle -> Data Capture -> Yield Forecast -> Waste Reuse

# Stakeholder Meet and Compliance Check follow WasteReuse
# Final step Supply Sync after stakeholder/compliance

# Loop part: (* (GrowthMonitor, PestControl)) means do GrowthMonitor, then choice to exit or PestControl then GrowthMonitor again

loop_growth_pest = OperatorPOWL(operator=Operator.LOOP, children=[GrowthMonitor, PestControl])

# Branch 1 sequence:
# NutrientMix --> SeedSelection --> PlantingSetup --> loop_growth_pest

branch1 = StrictPartialOrder(nodes=[NutrientMix, SeedSelection, PlantingSetup, loop_growth_pest])
branch1.order.add_edge(NutrientMix, SeedSelection)
branch1.order.add_edge(SeedSelection, PlantingSetup)
branch1.order.add_edge(PlantingSetup, loop_growth_pest)

# Branch 2 sequence:
# WaterCycle --> DataCapture --> YieldForecast --> WasteReuse

branch2 = StrictPartialOrder(nodes=[WaterCycle, DataCapture, YieldForecast, WasteReuse])
branch2.order.add_edge(WaterCycle, DataCapture)
branch2.order.add_edge(DataCapture, YieldForecast)
branch2.order.add_edge(YieldForecast, WasteReuse)

# Parallel branches after EnvControl

# Compose parallel branches in a partial order with EnvControl before both
after_env = StrictPartialOrder(nodes=[branch1, branch2])
after_env.order.add_edge(branch1, branch2)  # no direct order between branch1 and branch2 means concurrency, so remove edge

# Actually to model concurrency we do not add edges between branch1 and branch2

# Upstream sequence:
# SiteSurvey --> ModularDesign --> SystemBuild --> EnvControl --> (branch1 || branch2)

upstream = StrictPartialOrder(nodes=[SiteSurvey, ModularDesign, SystemBuild, EnvControl])
upstream.order.add_edge(SiteSurvey, ModularDesign)
upstream.order.add_edge(ModularDesign, SystemBuild)
upstream.order.add_edge(SystemBuild, EnvControl)

# Combine upstream with after_env concurrency branches

top = StrictPartialOrder(nodes=[upstream, branch1, branch2])
top.order.add_edge(upstream, branch1)
top.order.add_edge(upstream, branch2)

# After both branches complete WasteReuse -> StakeholderMeet -> ComplianceCheck -> SupplySync

final_seq = StrictPartialOrder(nodes=[WasteReuse, StakeholderMeet, ComplianceCheck, SupplySync])
final_seq.order.add_edge(WasteReuse, StakeholderMeet)
final_seq.order.add_edge(StakeholderMeet, ComplianceCheck)
final_seq.order.add_edge(ComplianceCheck, SupplySync)

# WasteReuse is part of branch2, we must ensure WasteReuse from branch2 connects to StakeholderMeet in final_seq

# So the right approach is to incorporate StakeholderMeet, ComplianceCheck, SupplySync into the main partial order

# To do so create a big PO with all nodes:

root_nodes = [
    SiteSurvey,
    ModularDesign,
    SystemBuild,
    EnvControl,
    NutrientMix,
    SeedSelection,
    PlantingSetup,
    loop_growth_pest,
    WaterCycle,
    DataCapture,
    YieldForecast,
    WasteReuse,
    StakeholderMeet,
    ComplianceCheck,
    SupplySync,
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges to represent the logic:

# Upstream chain
root.order.add_edge(SiteSurvey, ModularDesign)
root.order.add_edge(ModularDesign, SystemBuild)
root.order.add_edge(SystemBuild, EnvControl)

# EnvControl splits to NutrientMix and WaterCycle concurrently:
root.order.add_edge(EnvControl, NutrientMix)
root.order.add_edge(EnvControl, WaterCycle)

# Branch 1
root.order.add_edge(NutrientMix, SeedSelection)
root.order.add_edge(SeedSelection, PlantingSetup)
root.order.add_edge(PlantingSetup, loop_growth_pest)

# Branch 2
root.order.add_edge(WaterCycle, DataCapture)
root.order.add_edge(DataCapture, YieldForecast)
root.order.add_edge(YieldForecast, WasteReuse)

# After WasteReuse
root.order.add_edge(WasteReuse, StakeholderMeet)
root.order.add_edge(StakeholderMeet, ComplianceCheck)
root.order.add_edge(ComplianceCheck, SupplySync)