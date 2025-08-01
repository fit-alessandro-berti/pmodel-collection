# Generated from: 527fb39a-9849-4565-a440-c5ab2be20bef.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense city environment. It involves assessing structural integrity, securing permits, designing modular planting systems, selecting crop varieties suited for limited sunlight and space, integrating smart irrigation systems, recruiting local community volunteers, and setting up a supply chain for fresh produce distribution. The process also includes ongoing maintenance protocols, pest management strategies adapted to rooftop conditions, seasonal crop rotation planning, and data collection for yield optimization and environmental impact assessment. The goal is to create a self-sustaining, eco-friendly urban agricultural system that enhances city resilience and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
SiteAssess = Transition(label='Site Assess')
PermitSecure = Transition(label='Permit Secure')
DesignLayout = Transition(label='Design Layout')
SelectCrops = Transition(label='Select Crops')
BuildModules = Transition(label='Build Modules')
InstallIrrigation = Transition(label='Install Irrigation')
RecruitVolunteers = Transition(label='Recruit Volunteers')
SoilPrep = Transition(label='Soil Prep')
PlantSeeds = Transition(label='Plant Seeds')
SetupSensors = Transition(label='Setup Sensors')
ManagePests = Transition(label='Manage Pests')
HarvestProduce = Transition(label='Harvest Produce')
DistributeGoods = Transition(label='Distribute Goods')
RecordData = Transition(label='Record Data')
PlanRotation = Transition(label='Plan Rotation')
MaintainSystems = Transition(label='Maintain Systems')

# For ongoing maintenance, pest management, crop rotation and data collection, model a loop
# Loop body: MaintainSystems
# Loop condition body: choice (XOR) between ManagePests, PlanRotation, RecordData

# Choice of maintenance activities (concurrent or exclusive? description suggests strategies, planning and data collection - make exclusive choice)
maintenance_choices = OperatorPOWL(operator=Operator.XOR, children=[ManagePests, PlanRotation, RecordData])

# Loop: first execute MaintainSystems, then choose to exit or do maintenance choice and loop again
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[MaintainSystems, maintenance_choices])

# Model the main process partial order:
# sequence:
# Site Assess --> Permit Secure --> Design Layout
# Design Layout --> Select Crops 
# Select Crops --> Build Modules
# Build Modules --> Install Irrigation
# Install Irrigation --> Recruit Volunteers
# Recruit Volunteers --> Soil Prep --> Plant Seeds
# Plant Seeds --> Setup Sensors
# Setup Sensors --> maintenance loop
# maintenance loop --> Harvest Produce --> Distribute Goods

nodes = [
    SiteAssess,
    PermitSecure,
    DesignLayout,
    SelectCrops,
    BuildModules,
    InstallIrrigation,
    RecruitVolunteers,
    SoilPrep,
    PlantSeeds,
    SetupSensors,
    maintenance_loop,
    HarvestProduce,
    DistributeGoods,
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(SiteAssess, PermitSecure)
root.order.add_edge(PermitSecure, DesignLayout)
root.order.add_edge(DesignLayout, SelectCrops)
root.order.add_edge(SelectCrops, BuildModules)
root.order.add_edge(BuildModules, InstallIrrigation)
root.order.add_edge(InstallIrrigation, RecruitVolunteers)
root.order.add_edge(RecruitVolunteers, SoilPrep)
root.order.add_edge(SoilPrep, PlantSeeds)
root.order.add_edge(PlantSeeds, SetupSensors)
root.order.add_edge(SetupSensors, maintenance_loop)
root.order.add_edge(maintenance_loop, HarvestProduce)
root.order.add_edge(HarvestProduce, DistributeGoods)