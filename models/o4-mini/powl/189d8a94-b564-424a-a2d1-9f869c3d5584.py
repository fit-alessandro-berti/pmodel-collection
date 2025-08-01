# Generated from: 189d8a94-b564-424a-a2d1-9f869c3d5584.json
# Description: This process involves establishing a fully operational vertical farm within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and renewable energy sources. It begins with site selection and proceeds through modular infrastructure assembly, nutrient solution formulation, seedling cultivation, continuous environmental monitoring, and automated harvesting. The process also includes waste recycling, data analytics for yield optimization, and final product packaging for local distribution. Unique challenges involve balancing technological integration with urban regulations, minimizing water usage, and ensuring crop diversity while maintaining sustainability goals throughout the farm lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
siteSelection     = Transition(label='Site Selection')
designLayout      = Transition(label='Design Layout')
permitApproval    = Transition(label='Permit Approval')
infrastructureBuild = Transition(label='Infrastructure Build')
systemInstall     = Transition(label='System Install')
nutrientMix       = Transition(label='Nutrient Mix')
seedlingPlant     = Transition(label='Seedling Plant')
climateSetup      = Transition(label='Climate Setup')
sensorCalibrate   = Transition(label='Sensor Calibrate')
harvestCrop       = Transition(label='Harvest Crop')
wasteProcess      = Transition(label='Waste Process')
dataAnalyze       = Transition(label='Data Analyze')
packageGoods      = Transition(label='Package Goods')
localDeliver      = Transition(label='Local Deliver')

# Define the monitoring cycle (water, growth, pest) as concurrent tasks
waterCycle    = Transition(label='Water Cycle')
growthMonitor = Transition(label='Growth Monitor')
pestControl   = Transition(label='Pest Control')
monitor_cycle = StrictPartialOrder(nodes=[waterCycle, growthMonitor, pestControl])
# No order edges inside: they run concurrently

# Build a loop for continuous monitoring
pivot = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pivot, monitor_cycle])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    siteSelection,
    designLayout,
    permitApproval,
    infrastructureBuild,
    systemInstall,
    nutrientMix,
    seedlingPlant,
    climateSetup,
    sensorCalibrate,
    monitor_loop,
    harvestCrop,
    wasteProcess,
    dataAnalyze,
    packageGoods,
    localDeliver
])

# Sequential dependencies before monitoring
root.order.add_edge(siteSelection, designLayout)
root.order.add_edge(designLayout, permitApproval)
root.order.add_edge(permitApproval, infrastructureBuild)
root.order.add_edge(infrastructureBuild, systemInstall)
root.order.add_edge(systemInstall, nutrientMix)
root.order.add_edge(nutrientMix, seedlingPlant)
root.order.add_edge(seedlingPlant, climateSetup)
root.order.add_edge(climateSetup, sensorCalibrate)
root.order.add_edge(sensorCalibrate, monitor_loop)

# After monitoring loop, proceed to harvest
root.order.add_edge(monitor_loop, harvestCrop)

# After harvest, waste processing and data analysis can start in parallel
root.order.add_edge(harvestCrop, wasteProcess)
root.order.add_edge(harvestCrop, dataAnalyze)

# Packaging and delivery
root.order.add_edge(harvestCrop, packageGoods)
root.order.add_edge(packageGoods, localDeliver)