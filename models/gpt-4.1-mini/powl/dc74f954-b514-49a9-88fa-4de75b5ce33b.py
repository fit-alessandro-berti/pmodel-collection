# Generated from: dc74f954-b514-49a9-88fa-4de75b5ce33b.json
# Description: This process outlines the complex establishment of an urban vertical farming facility designed to optimize limited city space for high-yield crop production. It involves site analysis, modular infrastructure assembly, environmental system calibration, automated nutrient delivery, integrated pest management, and data-driven crop monitoring. The process demands coordination between agronomists, engineers, and IT specialists to ensure sustainable operations while maximizing output and minimizing resource consumption within a controlled urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
PermitFiling = Transition(label='Permit Filing')
ModuleBuild = Transition(label='Module Build')
SystemInstall = Transition(label='System Install')
ClimateSetup = Transition(label='Climate Setup')
LightingConfigure = Transition(label='Lighting Configure')
IrrigationSetup = Transition(label='Irrigation Setup')
NutrientMix = Transition(label='Nutrient Mix')
PestCheck = Transition(label='Pest Check')
SensorCalibrate = Transition(label='Sensor Calibrate')
DataIntegration = Transition(label='Data Integration')
CropPlanting = Transition(label='Crop Planting')
GrowthMonitor = Transition(label='Growth Monitor')
YieldAnalyze = Transition(label='Yield Analyze')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')

# Build Phase: ModuleBuild and SystemInstall can be concurrent
build_phase = StrictPartialOrder(nodes=[ModuleBuild, SystemInstall])

# Environmental and system setup (ordered: ClimateSetup --> LightingConfigure --> IrrigationSetup)
env_setup = StrictPartialOrder(nodes=[ClimateSetup, LightingConfigure, IrrigationSetup])
env_setup.order.add_edge(ClimateSetup, LightingConfigure)
env_setup.order.add_edge(LightingConfigure, IrrigationSetup)

# Nutrient and pest management (ordered: NutrientMix --> PestCheck)
nutrient_pest = StrictPartialOrder(nodes=[NutrientMix, PestCheck])
nutrient_pest.order.add_edge(NutrientMix, PestCheck)

# Sensor calibration and data integration (SensorCalibrate --> DataIntegration)
sensor_data = StrictPartialOrder(nodes=[SensorCalibrate, DataIntegration])
sensor_data.order.add_edge(SensorCalibrate, DataIntegration)

# Crop cycle: CropPlanting --> GrowthMonitor --> YieldAnalyze
crop_cycle = StrictPartialOrder(nodes=[CropPlanting, GrowthMonitor, YieldAnalyze])
crop_cycle.order.add_edge(CropPlanting, GrowthMonitor)
crop_cycle.order.add_edge(GrowthMonitor, YieldAnalyze)

# Final cleanup and audit (WasteManage and EnergyAudit can be concurrent)
final_steps = StrictPartialOrder(nodes=[WasteManage, EnergyAudit])
# No edges → concurrent

# Initial phase: SiteSurvey --> DesignLayout --> PermitFiling
initial_phase = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, PermitFiling])
initial_phase.order.add_edge(SiteSurvey, DesignLayout)
initial_phase.order.add_edge(DesignLayout, PermitFiling)

# Compose full process partial order with ordering between phases:
# initial_phase --> build_phase --> env_setup --> nutrient_pest and sensor_data concurrent --> crop_cycle --> final_steps

# Combine nutrient_pest and sensor_data concurrently
nutrient_and_sensor = StrictPartialOrder(
    nodes=[nutrient_pest, sensor_data]
)
# no ordering edges between nutrient_pest and sensor_data (concurrent)

# Combine nutrient_and_sensor before crop_cycle
pre_crop = StrictPartialOrder(
    nodes=[nutrient_and_sensor, crop_cycle]
)
pre_crop.order.add_edge(nutrient_and_sensor, crop_cycle)

# Combine phases in correct order
middle_phases = StrictPartialOrder(
    nodes=[build_phase, env_setup, pre_crop]
)
middle_phases.order.add_edge(build_phase, env_setup)
middle_phases.order.add_edge(env_setup, pre_crop)

# Compose initial, middle, and final steps
upper = StrictPartialOrder(
    nodes=[initial_phase, middle_phases]
)
upper.order.add_edge(initial_phase, middle_phases)

root = StrictPartialOrder(
    nodes=[upper, final_steps]
)
root.order.add_edge(upper, final_steps)