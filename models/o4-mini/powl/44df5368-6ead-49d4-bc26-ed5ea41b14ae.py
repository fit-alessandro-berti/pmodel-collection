# Generated from: 44df5368-6ead-49d4-bc26-ed5ea41b14ae.json
# Description: This process outlines the establishment of a fully automated urban vertical farming facility integrating IoT sensors, AI-driven climate control, and hydroponic systems. Activities include site selection based on solar exposure and urban zoning laws, modular rack installation, nutrient solution formulation, AI model training for crop yield prediction, pest control via biocontrol agents, continuous environmental monitoring, adaptive lighting scheduling, and integration with local distribution networks. The process also incorporates community engagement programs and sustainability reporting to ensure minimal environmental impact and maximum social benefit. This atypical yet realistic process blends agriculture, technology, and urban planning to create efficient food production in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
siteSurvey     = Transition(label='Site Survey')
zoningCheck    = Transition(label='Zoning Check')
rackSetup      = Transition(label='Rack Setup')
sensorInstall  = Transition(label='Sensor Install')
solutionMix    = Transition(label='Solution Mix')
aiTraining     = Transition(label='AI Training')
pestControl    = Transition(label='Pest Control')
envMonitor     = Transition(label='Env Monitor')
lightingPlan   = Transition(label='Lighting Plan')
waterRecirc    = Transition(label='Water Recirc')
yieldAssess    = Transition(label='Yield Assess')
dataSync       = Transition(label='Data Sync')
networkLink    = Transition(label='Network Link')
communityMeet  = Transition(label='Community Meet')
sustainReport  = Transition(label='Sustain Report')

# Loop for continuous environmental monitoring and adaptive lighting
body = StrictPartialOrder(nodes=[envMonitor, lightingPlan])
body.order.add_edge(envMonitor, lightingPlan)
loopMonitoring = OperatorPOWL(operator=Operator.LOOP, children=[body, waterRecirc])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    siteSurvey, zoningCheck, rackSetup, sensorInstall, solutionMix,
    aiTraining, pestControl, loopMonitoring, yieldAssess,
    dataSync, networkLink, communityMeet, sustainReport
])

# Define the control-flow dependencies
root.order.add_edge(siteSurvey,     zoningCheck)
root.order.add_edge(zoningCheck,    rackSetup)
root.order.add_edge(rackSetup,      sensorInstall)
root.order.add_edge(sensorInstall,  solutionMix)
root.order.add_edge(solutionMix,    aiTraining)
root.order.add_edge(aiTraining,     pestControl)
root.order.add_edge(pestControl,    loopMonitoring)
root.order.add_edge(loopMonitoring, yieldAssess)
root.order.add_edge(yieldAssess,    dataSync)
root.order.add_edge(dataSync,       networkLink)
# After integration with local distribution, start community engagement and reporting
root.order.add_edge(networkLink,    communityMeet)
root.order.add_edge(networkLink,    sustainReport)