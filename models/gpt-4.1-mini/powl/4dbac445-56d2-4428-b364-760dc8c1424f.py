# Generated from: 4dbac445-56d2-4428-b364-760dc8c1424f.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farming operation within a metropolitan environment. It includes site evaluation, modular system design, environmental controls integration, and supply chain coordination for organic seed sourcing. The process requires precise synchronization of technological installation, nutrient solution calibration, and real-time monitoring setup to optimize crop yield. Additionally, it incorporates community engagement for local market feedback and regulatory compliance checks to ensure sustainable practices. The workflow culminates with staff training, pilot harvests, and iterative system refinement based on data analytics, fostering a resilient and scalable urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitAcquire = Transition(label='Permit Acquire')
SeedSourcing = Transition(label='Seed Sourcing')
ModuleInstall = Transition(label='Module Install')
IrrigationSetup = Transition(label='Irrigation Setup')
LightingConfigure = Transition(label='Lighting Configure')
NutrientMix = Transition(label='Nutrient Mix')
SensorCalibrate = Transition(label='Sensor Calibrate')
ClimateControl = Transition(label='Climate Control')
DataIntegration = Transition(label='Data Integration')
StaffTraining = Transition(label='Staff Training')
TrialHarvest = Transition(label='Trial Harvest')
MarketEngage = Transition(label='Market Engage')
ComplianceAudit = Transition(label='Compliance Audit')
SystemReview = Transition(label='System Review')
YieldAnalyze = Transition(label='Yield Analyze')

# 1. Initial part: Site Survey --> Design Layout --> Permit Acquire
init_po = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermitAcquire])
init_po.order.add_edge(SiteSurvey, DesignLayout)
init_po.order.add_edge(DesignLayout, PermitAcquire)

# 2. Supply chain & modular system and environmental controls branch with some parallelism
# Seed Sourcing independent of Module Install & environmental controls setup
# Module Install --> Irrigation Setup, Lighting Configure, Nutrient Mix, Sensor Calibrate, Climate Control can run in partial order with some concurrency.
# We'll define env controls as a partial order with some parallelism among Irrigation, Lighting, Nutrient, Sensor, Climate.

env_controls_nodes = [IrrigationSetup, LightingConfigure, NutrientMix, SensorCalibrate, ClimateControl]

env_controls_po = StrictPartialOrder(nodes=env_controls_nodes)
# Nutrient Mix requires water (Irrigation), so IrrigationSetup --> NutrientMix
env_controls_po.order.add_edge(IrrigationSetup, NutrientMix)
# Sensor Calibrate requires at least some setup, we place as parallel to NutrientMix, no strict order
# Climate Control can start after Sensor Calibrate and Lighting Configure both done, 
# so SensorCalibrate --> ClimateControl and LightingConfigure --> ClimateControl
env_controls_po.order.add_edge(SensorCalibrate, ClimateControl)
env_controls_po.order.add_edge(LightingConfigure, ClimateControl)

modular_env_po = StrictPartialOrder(nodes=[ModuleInstall, env_controls_po])
modular_env_po.order.add_edge(ModuleInstall, env_controls_po)

# Combine Seed Sourcing and modular_env_po concurrently (no order edges)
supply_modular_nodes = [SeedSourcing, modular_env_po]

# 3. Data Integration depends on completion of Seed Sourcing and env controls (modular_env_po)
data_integration_po = StrictPartialOrder(nodes=supply_modular_nodes + [DataIntegration])
data_integration_po.order.add_edge(SeedSourcing, DataIntegration)
data_integration_po.order.add_edge(modular_env_po, DataIntegration)

# 4. Market Engage and Compliance Audit can be executed in parallel after Permit Acquire
market_compliance_po = StrictPartialOrder(nodes=[MarketEngage, ComplianceAudit])
# No order edges between MarketEngage and ComplianceAudit (parallel)

permit_branch_po = StrictPartialOrder(nodes=[PermitAcquire, market_compliance_po])
permit_branch_po.order.add_edge(PermitAcquire, market_compliance_po)

# 5. Trial Harvest after Data Integration and Market/Compliance activities have finished
post_trial_po = StrictPartialOrder(nodes=[data_integration_po, permit_branch_po, TrialHarvest])
post_trial_po.order.add_edge(data_integration_po, TrialHarvest)
post_trial_po.order.add_edge(permit_branch_po, TrialHarvest)

# 6. After Trial Harvest, Staff Training then System Review, then Yield Analyze
final_seq = StrictPartialOrder(nodes=[TrialHarvest, StaffTraining, SystemReview, YieldAnalyze])
final_seq.order.add_edge(TrialHarvest, StaffTraining)
final_seq.order.add_edge(StaffTraining, SystemReview)
final_seq.order.add_edge(SystemReview, YieldAnalyze)

# 7. Combine all: initial parts --> supply/modular/env/data integration + permit branch --> trial + final sequence
overall_po = StrictPartialOrder(nodes=[init_po, data_integration_po, permit_branch_po, TrialHarvest, StaffTraining, SystemReview, YieldAnalyze])

overall_po.order.add_edge(init_po, data_integration_po)
overall_po.order.add_edge(init_po, permit_branch_po)
overall_po.order.add_edge(data_integration_po, TrialHarvest)
overall_po.order.add_edge(permit_branch_po, TrialHarvest)
overall_po.order.add_edge(TrialHarvest, StaffTraining)
overall_po.order.add_edge(StaffTraining, SystemReview)
overall_po.order.add_edge(SystemReview, YieldAnalyze)

root = overall_po