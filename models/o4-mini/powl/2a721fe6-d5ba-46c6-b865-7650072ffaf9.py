# Generated from: 2a721fe6-d5ba-46c6-b865-7650072ffaf9.json
# Description: This process outlines the establishment of an urban vertical farming system designed to optimize limited city space for sustainable agriculture. It involves selecting appropriate building infrastructure, integrating advanced hydroponic and aeroponic systems, implementing automated climate control and nutrient delivery, and establishing real-time monitoring via IoT sensors. The process further includes regulatory compliance checks, community engagement for local sourcing, workforce training on specialized equipment, and continuous yield optimization through data analytics. The complexity arises from merging construction, agriculture technology, environmental control, and urban planning within a compact footprint, ensuring efficient resource use and maximizing crop output year-round.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
siteSurvey = Transition(label='Site Survey')
structureDesign = Transition(label='Structure Design')
systemIntegration = Transition(label='System Integration')
sensorInstall = Transition(label='Sensor Install')
climateSetup = Transition(label='Climate Setup')
nutrientMix = Transition(label='Nutrient Mix')
waterCycle = Transition(label='Water Cycle')
lightingConfig = Transition(label='Lighting Config')
automationTest = Transition(label='Automation Test')
regulationCheck = Transition(label='Regulation Check')
communityMeet = Transition(label='Community Meet')
staffTraining = Transition(label='Staff Training')
cropSeeding = Transition(label='Crop Seeding')
growthMonitoring = Transition(label='Growth Monitoring')
dataAnalysis = Transition(label='Data Analysis')
harvestPlan = Transition(label='Harvest Plan')
wasteManage = Transition(label='Waste Manage')

# Define the monitoring & analysis loop: repeat Growth Monitoring, then optionally Data Analysis
monitoringLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growthMonitoring, dataAnalysis]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    siteSurvey,
    structureDesign,
    systemIntegration,
    sensorInstall,
    climateSetup,
    nutrientMix,
    waterCycle,
    lightingConfig,
    automationTest,
    regulationCheck,
    communityMeet,
    staffTraining,
    cropSeeding,
    harvestPlan,
    wasteManage,
    monitoringLoop
])

# Add control-flow dependencies
root.order.add_edge(siteSurvey, structureDesign)

root.order.add_edge(structureDesign, systemIntegration)

# After system integration, set up technology components in parallel
for setup in [sensorInstall, climateSetup, nutrientMix, waterCycle, lightingConfig]:
    root.order.add_edge(systemIntegration, setup)
    # they all must complete before testing
    root.order.add_edge(setup, automationTest)

# After automation test, do compliance and community engagement (in parallel)
root.order.add_edge(automationTest, regulationCheck)
root.order.add_edge(automationTest, communityMeet)

# Both these must finish before staff training
root.order.add_edge(regulationCheck, staffTraining)
root.order.add_edge(communityMeet, staffTraining)

# Then staff training before seeding
root.order.add_edge(staffTraining, cropSeeding)

# After seeding enter the monitoring loop
root.order.add_edge(cropSeeding, monitoringLoop)

# Exit loop into harvest planning
root.order.add_edge(monitoringLoop, harvestPlan)

# Finally manage waste after harvest
root.order.add_edge(harvestPlan, wasteManage)