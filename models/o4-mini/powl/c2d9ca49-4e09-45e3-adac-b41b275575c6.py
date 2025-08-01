# Generated from: c2d9ca49-4e09-45e3-adac-b41b275575c6.json
# Description: This process outlines the establishment of an urban vertical farming facility integrating advanced hydroponics and AI-driven climate control systems. The workflow begins with site analysis and structural adaptation, followed by nutrient solution formulation and seed selection tailored for urban microclimates. It involves iterative sensor calibration, data-driven growth optimization, automated pest detection, and energy consumption balancing. The process also includes continuous staff training on biosecurity protocols and sustainability metrics evaluation, culminating in the integration of a consumer subscription model for fresh produce delivery, ensuring a closed-loop urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
siteSurvey = Transition(label='Site Survey')
structureAdapt = Transition(label='Structure Adapt')
seedChoose = Transition(label='Seed Choose')
nutrientMix = Transition(label='Nutrient Mix')
climateSetup = Transition(label='Climate Setup')

plantingCycle = Transition(label='Planting Cycle')
sensorCalibrate = Transition(label='Sensor Calibrate')
growthMonitor = Transition(label='Growth Monitor')
pestDetect = Transition(label='Pest Detect')
dataAnalyze = Transition(label='Data Analyze')
energyBalance = Transition(label='Energy Balance')

staffTrain = Transition(label='Staff Train')
biosecurityCheck = Transition(label='Biosecurity Check')
sustainabilityAudit = Transition(label='Sustainability Audit')

yieldForecast = Transition(label='Yield Forecast')
subscriptionSetup = Transition(label='Subscription Setup')
deliveryPlan = Transition(label='Delivery Plan')

# Main planting loop body: sensor calibration -> growth monitoring -> pest detection -> data analysis -> energy balancing
main_body = StrictPartialOrder(nodes=[
    sensorCalibrate, growthMonitor, pestDetect, dataAnalyze, energyBalance
])
main_body.order.add_edge(sensorCalibrate, growthMonitor)
main_body.order.add_edge(growthMonitor, pestDetect)
main_body.order.add_edge(pestDetect, dataAnalyze)
main_body.order.add_edge(dataAnalyze, energyBalance)

# Loop: execute a planting cycle, then the main_body repeatedly
mainLoop = OperatorPOWL(operator=Operator.LOOP, children=[plantingCycle, main_body])

# Training loop body: biosecurity check -> sustainability audit
training_body = StrictPartialOrder(nodes=[biosecurityCheck, sustainabilityAudit])
training_body.order.add_edge(biosecurityCheck, sustainabilityAudit)

# Loop: staff training followed by the training body, repeated
trainingLoop = OperatorPOWL(operator=Operator.LOOP, children=[staffTrain, training_body])

# Root partial order
root = StrictPartialOrder(nodes=[
    siteSurvey,
    structureAdapt,
    seedChoose,
    nutrientMix,
    climateSetup,
    mainLoop,
    trainingLoop,
    yieldForecast,
    subscriptionSetup,
    deliveryPlan
])

# Control-flow edges
root.order.add_edge(siteSurvey, structureAdapt)
root.order.add_edge(structureAdapt, seedChoose)
root.order.add_edge(structureAdapt, nutrientMix)

root.order.add_edge(seedChoose, climateSetup)
root.order.add_edge(nutrientMix, climateSetup)

root.order.add_edge(climateSetup, mainLoop)
root.order.add_edge(climateSetup, trainingLoop)

root.order.add_edge(mainLoop, yieldForecast)
root.order.add_edge(yieldForecast, subscriptionSetup)
root.order.add_edge(subscriptionSetup, deliveryPlan)