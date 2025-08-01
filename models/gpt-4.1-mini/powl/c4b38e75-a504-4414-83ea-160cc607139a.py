# Generated from: c4b38e75-a504-4414-83ea-160cc607139a.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed high-rise building. It involves site evaluation, modular system design, climate control calibration, seed selection, hydroponic nutrient optimization, robotic planting, continuous environmental monitoring, pest detection through AI, data-driven growth analysis, automated harvesting, packaging customization, waste recycling integration, energy consumption auditing, and real-time market demand alignment. The goal is to create a sustainable, high-yield farm capable of responding dynamically to urban food supply needs while minimizing ecological footprint and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
select_seeds = Transition(label='Select Seeds')
optimize_nutrients = Transition(label='Optimize Nutrients')
deploy_robots = Transition(label='Deploy Robots')
monitor_growth = Transition(label='Monitor Growth')
detect_pests = Transition(label='Detect Pests')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
customize_pack = Transition(label='Customize Pack')
recycle_waste = Transition(label='Recycle Waste')
audit_energy = Transition(label='Audit Energy')
align_demand = Transition(label='Align Demand')

# Construct the partial order reflecting typical dependencies:
# SiteSurvey -> DesignModules -> (InstallSensors -> CalibrateClimate)
# SelectSeeds -> OptimizeNutrients
# DeployRobots runs after InstallSensors and CalibrateClimate
# MonitorGrowth follows DeployRobots
# DetectPests and AnalyzeData depend on MonitorGrowth (concurrent)
# HarvestCrops after AnalyzeData
# CustomizePack after HarvestCrops
# RecycleWaste and AuditEnergy after CustomizePack (concurrent)
# AlignDemand after RecycleWaste and AuditEnergy

nodes = [
    site_survey,
    design_modules,
    install_sensors,
    calibrate_climate,
    select_seeds,
    optimize_nutrients,
    deploy_robots,
    monitor_growth,
    detect_pests,
    analyze_data,
    harvest_crops,
    customize_pack,
    recycle_waste,
    audit_energy,
    align_demand,
]

root = StrictPartialOrder(nodes=nodes)

# Define order constraints according to process description

# Site Survey → Design Modules
root.order.add_edge(site_survey, design_modules)

# Design Modules → Install Sensors, Calibrate Climate
root.order.add_edge(design_modules, install_sensors)
root.order.add_edge(design_modules, calibrate_climate)

# Deploy Robots depends on both Install Sensors and Calibrate Climate
root.order.add_edge(install_sensors, deploy_robots)
root.order.add_edge(calibrate_climate, deploy_robots)

# Select Seeds → Optimize Nutrients
root.order.add_edge(select_seeds, optimize_nutrients)

# Monitor Growth depends on Deploy Robots
root.order.add_edge(deploy_robots, monitor_growth)

# Detect Pests and Analyze Data depend on Monitor Growth (these two concurrent)
root.order.add_edge(monitor_growth, detect_pests)
root.order.add_edge(monitor_growth, analyze_data)

# Harvest Crops after Analyze Data
root.order.add_edge(analyze_data, harvest_crops)

# Customize Pack after Harvest Crops
root.order.add_edge(harvest_crops, customize_pack)

# Recycle Waste and Audit Energy depend on Customize Pack (concurrent)
root.order.add_edge(customize_pack, recycle_waste)
root.order.add_edge(customize_pack, audit_energy)

# Align Demand after both Recycle Waste and Audit Energy
root.order.add_edge(recycle_waste, align_demand)
root.order.add_edge(audit_energy, align_demand)