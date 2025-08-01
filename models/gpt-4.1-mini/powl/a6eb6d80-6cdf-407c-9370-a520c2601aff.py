# Generated from: a6eb6d80-6cdf-407c-9370-a520c2601aff.json
# Description: This process outlines the end-to-end setup of an urban vertical farm, integrating advanced hydroponics, renewable energy sourcing, and automated climate control. It includes site analysis, modular construction, nutrient solution formulation, sensor calibration, crop seeding, growth monitoring, pest management with bioagents, yield forecasting using AI models, and finally, supply chain coordination for fresh produce delivery to local markets. The process emphasizes sustainability, tech integration, and urban space optimization to maximize output in limited areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
StructureBuild = Transition(label='Structure Build')
InstallHydroponics = Transition(label='Install Hydroponics')
EnergySetup = Transition(label='Energy Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorCalibrate = Transition(label='Sensor Calibrate')
SeedCrops = Transition(label='Seed Crops')
ClimateTune = Transition(label='Climate Tune')
MonitorGrowth = Transition(label='Monitor Growth')
PestControl = Transition(label='Pest Control')
DataAnalyze = Transition(label='Data Analyze')
YieldForecast = Transition(label='Yield Forecast')
HarvestPlan = Transition(label='Harvest Plan')
LogisticsSync = Transition(label='Logistics Sync')
MarketOutreach = Transition(label='Market Outreach')

# Model partial orders representing logical causal flow

# Phase 1: Initial site and design, then construction and installation (some concurrency allowed)
phase1 = StrictPartialOrder(
    nodes=[SiteSurvey, DesignLayout, StructureBuild, InstallHydroponics, EnergySetup]
)
phase1.order.add_edge(SiteSurvey, DesignLayout)
phase1.order.add_edge(DesignLayout, StructureBuild)
phase1.order.add_edge(StructureBuild, InstallHydroponics)
phase1.order.add_edge(StructureBuild, EnergySetup)
# InstallHydroponics and EnergySetup can run concurrently after StructureBuild

# Phase 2: Nutrient prep, sensor calibration, seed, climate tuning
phase2 = StrictPartialOrder(
    nodes=[NutrientMix, SensorCalibrate, SeedCrops, ClimateTune]
)
# NutrientMix and SensorCalibrate concurrent, both needed before seeding and climate tuning
phase2.order.add_edge(NutrientMix, SeedCrops)
phase2.order.add_edge(SensorCalibrate, SeedCrops)
phase2.order.add_edge(SensorCalibrate, ClimateTune)
phase2.order.add_edge(SeedCrops, ClimateTune)

# Phase 3: Monitoring growth, pest control and data analysis - pest control and data analysis can be concurrency branches inside a loop until growth done

# PestControl and DataAnalyze can be concurrent; YieldForecast depends on DataAnalyze; HarvestPlan after YieldForecast

inner_loop_body = StrictPartialOrder(
    nodes=[PestControl, DataAnalyze]
)
# no order between PestControl and DataAnalyze (concurrent)

# Loop: continuously monitor growth, then decide to continue pest/data monitoring or exit loop

# Construct the loop:
# LOOP(children=[MonitorGrowth, inner_loop_body])
# meaning: do MonitorGrowth, then choose exit or do (inner_loop_body then MonitorGrowth) again

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[MonitorGrowth, inner_loop_body]
)

# After loop ends: YieldForecast, HarvestPlan
phase3after = StrictPartialOrder(
    nodes=[YieldForecast, HarvestPlan]
)
phase3after.order.add_edge(YieldForecast, HarvestPlan)

# Final phase: LogisticsSync, MarketOutreach (serial)
final_phase = StrictPartialOrder(
    nodes=[LogisticsSync, MarketOutreach]
)
final_phase.order.add_edge(LogisticsSync, MarketOutreach)

# Connect phase2 to loop (growth monitoring phase), loop output to yield/harvest, then final phase

# Compose up everything in one big PO:

root = StrictPartialOrder(
    nodes=[phase1, phase2, loop, phase3after, final_phase]
)
# Add edges to represent dependencies:

root.order.add_edge(phase1, phase2)       # after installation/nutrient prep start sensor calibration etc.
root.order.add_edge(phase2, loop)         # monitor growth after seeding and climate tune
root.order.add_edge(loop, phase3after)    # after growth monitoring loop, forecast and plan harvest
root.order.add_edge(phase3after, final_phase)  # after planning harvest, sync logistics and market outreach