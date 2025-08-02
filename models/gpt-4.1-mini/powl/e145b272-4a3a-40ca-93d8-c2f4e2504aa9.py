# Generated from: e145b272-4a3a-40ca-93d8-c2f4e2504aa9.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, climate control integration, nutrient cycling optimization, and IoT sensor deployment. The operation includes real-time monitoring, AI-driven crop scheduling, waste recycling, and energy efficiency audits. Coordination with local regulators ensures compliance with zoning and environmental standards. The process culminates in continuous yield analysis and adaptive system upgrades to maximize sustainable food production in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
ComplianceCheck = Transition(label='Compliance Check')

SystemDesign = Transition(label='System Design')
ModularBuild = Transition(label='Modular Build')

ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
WasteSetup = Transition(label='Waste Setup')

SensorInstall = Transition(label='Sensor Install')
IoTDeploy = Transition(label='IoT Deploy')

AI_Scheduling = Transition(label='AI Scheduling')
EnergyAudit = Transition(label='Energy Audit')

CropPlanting = Transition(label='Crop Planting')
YieldMonitor = Transition(label='Yield Monitor')
DataAnalysis = Transition(label='Data Analysis')
SystemUpgrade = Transition(label='System Upgrade')

# Compliance branch: PermitFiling -> ComplianceCheck
perm_branch = StrictPartialOrder(nodes=[PermitFiling, ComplianceCheck])
perm_branch.order.add_edge(PermitFiling, ComplianceCheck)

# Initial site and permit phase (Site Survey -> PermitFiling -> ComplianceCheck)
initial_phase = StrictPartialOrder(nodes=[SiteSurvey, perm_branch])
initial_phase.order.add_edge(SiteSurvey, perm_branch)

# Modular system design branch: SystemDesign -> ModularBuild
modular_design = StrictPartialOrder(nodes=[SystemDesign, ModularBuild])
modular_design.order.add_edge(SystemDesign, ModularBuild)

# Nutrient, waste, climate setup partial order (can be parallel)
env_setups = StrictPartialOrder(nodes=[ClimateSetup, NutrientMix, WasteSetup])
# No edges: all concurrent

# Sensor and IoT deployment sequence: SensorInstall -> IoTDeploy
sensor_iot = StrictPartialOrder(nodes=[SensorInstall, IoTDeploy])
sensor_iot.order.add_edge(SensorInstall, IoTDeploy)

# Monitoring and scheduling partial order: AI Scheduling and Energy Audit in parallel
monitoring = StrictPartialOrder(nodes=[AI_Scheduling, EnergyAudit])
# no edges - concurrent

# Final continuous loop: CropPlanting -> (YieldMonitor -> DataAnalysis -> SystemUpgrade)* loop
monitor_analysis_upgrade = StrictPartialOrder(nodes=[YieldMonitor, DataAnalysis, SystemUpgrade])
monitor_analysis_upgrade.order.add_edge(YieldMonitor, DataAnalysis)
monitor_analysis_upgrade.order.add_edge(DataAnalysis, SystemUpgrade)

loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[CropPlanting, monitor_analysis_upgrade])

# Combine all: from initial phase to modular design, to env setups, to sensor_iot, to monitoring, to loop
root = StrictPartialOrder(
    nodes=[initial_phase, modular_design, env_setups, sensor_iot, monitoring, loop_monitor]
)

root.order.add_edge(initial_phase, modular_design)
root.order.add_edge(modular_design, env_setups)
root.order.add_edge(env_setups, sensor_iot)
root.order.add_edge(sensor_iot, monitoring)
root.order.add_edge(monitoring, loop_monitor)