# Generated from: 93be9179-8755-4f4d-a117-2aaf6a0a8c92.json
# Description: This process outlines the complex and atypical steps involved in establishing a vertical farm within an urban environment. It begins with site evaluation focusing on structural integrity and sunlight availability, followed by modular design planning tailored to limited urban space. The process integrates hydroponic system installation, climate control calibration, and IoT sensor deployment for real-time monitoring. It includes nutrient solution preparation, seed selection based on urban crop suitability, and automated planting schedules. Additionally, energy optimization through renewable sources is implemented alongside waste recycling protocols. The final stages involve staff training on specialized equipment, compliance checks with urban agricultural regulations, and community engagement for local food distribution, ensuring a sustainable and efficient vertical farming operation within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteEval = Transition(label='Site Eval')
DesignPlan = Transition(label='Design Plan')
HydroponicInstall = Transition(label='Hydroponic Install')
ClimateSetup = Transition(label='Climate Setup')
SensorDeploy = Transition(label='Sensor Deploy')
NutrientPrep = Transition(label='Nutrient Prep')
SeedSelect = Transition(label='Seed Select')
AutomatePlant = Transition(label='Automate Plant')
EnergyOptimize = Transition(label='Energy Optimize')
WasteRecycle = Transition(label='Waste Recycle')
StaffTrain = Transition(label='Staff Train')
ComplianceCheck = Transition(label='Compliance Check')
CommunityMeet = Transition(label='Community Meet')
HarvestPlan = Transition(label='Harvest Plan')
DataAnalyze = Transition(label='Data Analyze')

# Partial order from description:

# 1. Start: Site Eval --> Design Plan
# 2. After Design Plan, three parallel modules: 
#    a) Hydroponic Install --> Climate Setup --> Sensor Deploy
#    b) Nutrient Prep --> Seed Select --> Automate Plant
#    c) Energy Optimize and Waste Recycle (concurrent)
# 3. After all three modules complete, Staff Train
# 4. Then Compliance Check --> Community Meet
# 5. Finally, Harvest Plan and Data Analyze (concurrent)

# Define partial orders for each module chain:

moduleA_nodes = [HydroponicInstall, ClimateSetup, SensorDeploy]
moduleA_order = {(HydroponicInstall, ClimateSetup), (ClimateSetup, SensorDeploy)}
moduleA = StrictPartialOrder(nodes=moduleA_nodes)
for src, tgt in moduleA_order:
    moduleA.order.add_edge(src, tgt)

moduleB_nodes = [NutrientPrep, SeedSelect, AutomatePlant]
moduleB_order = {(NutrientPrep, SeedSelect), (SeedSelect, AutomatePlant)}
moduleB = StrictPartialOrder(nodes=moduleB_nodes)
for src, tgt in moduleB_order:
    moduleB.order.add_edge(src, tgt)

moduleC_nodes = [EnergyOptimize, WasteRecycle]  # concurrent
moduleC = StrictPartialOrder(nodes=moduleC_nodes)

# Combine the three modules into one partial order running concurrently:
modulesABC_nodes = moduleA_nodes + moduleB_nodes + moduleC_nodes
modulesABC = StrictPartialOrder(nodes=modulesABC_nodes)
for src, tgt in moduleA_order:
    modulesABC.order.add_edge(src, tgt)
for src, tgt in moduleB_order:
    modulesABC.order.add_edge(src, tgt)
# No edges between modulesA, B, C => they run concurrently

# Partial order for the entire process:
# Site Eval --> Design Plan --> modulesABC --> Staff Train --> Compliance Check --> Community Meet --> (Harvest Plan || Data Analyze)

nodes_all = [SiteEval, DesignPlan, modulesABC, StaffTrain, ComplianceCheck, CommunityMeet, HarvestPlan, DataAnalyze]

root = StrictPartialOrder(nodes=nodes_all)

# Add edges:
root.order.add_edge(SiteEval, DesignPlan)
root.order.add_edge(DesignPlan, modulesABC)
root.order.add_edge(modulesABC, StaffTrain)
root.order.add_edge(StaffTrain, ComplianceCheck)
root.order.add_edge(ComplianceCheck, CommunityMeet)
root.order.add_edge(CommunityMeet, HarvestPlan)
root.order.add_edge(CommunityMeet, DataAnalyze)

# HarvestPlan and DataAnalyze are concurrent (no order between them)