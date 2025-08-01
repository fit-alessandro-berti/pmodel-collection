# Generated from: 63daf7a6-6b9b-4fd8-b1ee-fcf366a6a6aa.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial warehouse. It involves site analysis, modular system design, environmental control integration, automated nutrient delivery, crop scheduling via AI, pest monitoring with drones, and real-time data analytics for yield optimization. The process also includes community engagement for local produce distribution, sustainability assessments, and iterative system upgrades to improve energy efficiency and crop variety diversification. Coordination between engineers, agronomists, and logistics managers is critical throughout to ensure seamless operation and scalability within dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
InstallModules = Transition(label='Install Modules')
SetupHVAC = Transition(label='Setup HVAC')
IntegrateSensors = Transition(label='Integrate Sensors')
DeployDrones = Transition(label='Deploy Drones')
ConfigureAI = Transition(label='Configure AI')
NutrientMix = Transition(label='Nutrient Mix')
PlantSeeding = Transition(label='Plant Seeding')
ScheduleCrops = Transition(label='Schedule Crops')
MonitorGrowth = Transition(label='Monitor Growth')
PestControl = Transition(label='Pest Control')
HarvestPlan = Transition(label='Harvest Plan')
DataAnalysis = Transition(label='Data Analysis')
CommunityOutreach = Transition(label='Community Outreach')
EnergyAudit = Transition(label='Energy Audit')
UpgradeSystems = Transition(label='Upgrade Systems')

# Loop for iterative energy audit and system upgrades
loop = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, UpgradeSystems])

# Build the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, DesignLayout, InstallModules,
    SetupHVAC, IntegrateSensors, DeployDrones,
    ConfigureAI, NutrientMix, PlantSeeding,
    ScheduleCrops, MonitorGrowth, PestControl,
    HarvestPlan, DataAnalysis, CommunityOutreach,
    loop
])

# Define the control-flow dependencies
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, InstallModules)

# After modules install, configure systems and deploy drones in parallel
root.order.add_edge(InstallModules, SetupHVAC)
root.order.add_edge(InstallModules, IntegrateSensors)
root.order.add_edge(InstallModules, DeployDrones)

# Prepare nutrient delivery and AI after systems are ready
root.order.add_edge(SetupHVAC, NutrientMix)
root.order.add_edge(IntegrateSensors, NutrientMix)
root.order.add_edge(IntegrateSensors, ConfigureAI)

# Crop cycle
root.order.add_edge(NutrientMix, PlantSeeding)
root.order.add_edge(ConfigureAI, ScheduleCrops)
root.order.add_edge(PlantSeeding, MonitorGrowth)

# Pest monitoring via drones
root.order.add_edge(DeployDrones, PestControl)

# Harvest planning requires growth monitoring, pest control, and crop schedule
root.order.add_edge(MonitorGrowth, HarvestPlan)
root.order.add_edge(PestControl, HarvestPlan)
root.order.add_edge(ScheduleCrops, HarvestPlan)

# After harvest plan, perform data analysis and do community outreach in parallel
root.order.add_edge(HarvestPlan, DataAnalysis)
root.order.add_edge(HarvestPlan, CommunityOutreach)

# After data analysis, enter the iterative energy audit & upgrade loop
root.order.add_edge(DataAnalysis, loop)