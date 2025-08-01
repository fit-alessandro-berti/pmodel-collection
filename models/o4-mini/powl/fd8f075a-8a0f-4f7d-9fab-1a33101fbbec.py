# Generated from: fd8f075a-8a0f-4f7d-9fab-1a33101fbbec.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and automated climate control to optimize crop yield year-round. It involves site analysis, structural adaptation for vertical stacking, nutrient solution formulation, sensor calibration for environmental monitoring, and integration of AI-driven growth prediction models. The workflow includes securing permits, community engagement for sustainability awareness, supplier coordination for seeds and equipment, staff training on novel cultivation techniques, and continuous data-driven optimization for resource efficiency and minimal waste. This atypical agricultural process combines technology, urban planning, and environmental stewardship to create a resilient food production system tailored to dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
siteSurvey     = Transition(label='Site Survey')
permitFiling   = Transition(label='Permit Filing')
structurePrep  = Transition(label='Structure Prep')
systemInstall  = Transition(label='System Install')
energyConnect  = Transition(label='Energy Connect')
waterCycle     = Transition(label='Water Cycle')
nutrientMix    = Transition(label='Nutrient Mix')
sensorSetup    = Transition(label='Sensor Setup')
aiCalibration  = Transition(label='AI Calibration')
seedSourcing   = Transition(label='Seed Sourcing')
staffTraining  = Transition(label='Staff Training')
communityMeet  = Transition(label='Community Meet')
growthMonitor  = Transition(label='Growth Monitor')
wasteAudit     = Transition(label='Waste Audit')
dataReview     = Transition(label='Data Review')
yieldForecast  = Transition(label='Yield Forecast')
skip           = SilentTransition()

# Sub-workflow: system installation with energy & water
sysInstallPO = StrictPartialOrder(nodes=[systemInstall, energyConnect, waterCycle])
sysInstallPO.order.add_edge(systemInstall, energyConnect)
sysInstallPO.order.add_edge(systemInstall, waterCycle)

# Sub-workflow: one iteration of continuous optimization
iteration = StrictPartialOrder(nodes=[growthMonitor, wasteAudit, dataReview, yieldForecast])
iteration.order.add_edge(growthMonitor, wasteAudit)
iteration.order.add_edge(wasteAudit, dataReview)
iteration.order.add_edge(dataReview, yieldForecast)

# Loop for continuous data‐driven optimization
optLoop = OperatorPOWL(operator=Operator.LOOP, children=[skip, iteration])

# Root partial order
root = StrictPartialOrder(nodes=[
    siteSurvey, permitFiling, structurePrep,
    sysInstallPO, seedSourcing, communityMeet, staffTraining,
    nutrientMix, sensorSetup, aiCalibration,
    optLoop
])

# Control‐flow dependencies
root.order.add_edge(siteSurvey,   permitFiling)
root.order.add_edge(permitFiling, structurePrep)
root.order.add_edge(structurePrep, sysInstallPO)
root.order.add_edge(structurePrep, seedSourcing)
root.order.add_edge(structurePrep, communityMeet)
root.order.add_edge(structurePrep, staffTraining)
root.order.add_edge(sysInstallPO,  nutrientMix)
root.order.add_edge(nutrientMix,   sensorSetup)
root.order.add_edge(sensorSetup,   aiCalibration)
root.order.add_edge(aiCalibration, optLoop)