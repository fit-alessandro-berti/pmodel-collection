# Generated from: 4117b246-dc1c-47ca-aff8-a00990e524e0.json
# Description: This process details the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, environmental control calibration, hydroponic system installation, integrated pest management, and AI-driven crop monitoring. The process ensures sustainable energy use, water recycling, and optimized yield through data analytics and continuous improvement cycles. Stakeholders include agronomists, engineers, supply chain managers, and local regulators, coordinating to transform urban spaces into high-efficiency food production hubs while minimizing ecological impact and maximizing social benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
siteSurvey       = Transition(label='Site Survey')
designLayout     = Transition(label='Design Layout')
installFrames    = Transition(label='Install Frames')
setupHydroponics = Transition(label='Setup Hydroponics')
calibrateSensors = Transition(label='Calibrate Sensors')
energyAudit      = Transition(label='Energy Audit')
waterRecycling   = Transition(label='Water Recycling')
climateControl   = Transition(label='Climate Control')
seedPlanting     = Transition(label='Seed Planting')
nutrientMix      = Transition(label='Nutrient Mix')
pestInspection   = Transition(label='Pest Inspection')
dataIntegration  = Transition(label='Data Integration')
growthMonitoring = Transition(label='Growth Monitoring')
feedbackLoop     = Transition(label='Feedback Loop')
yieldForecast    = Transition(label='Yield Forecast')
harvestPrep      = Transition(label='Harvest Prep')
packaging        = Transition(label='Packaging')
regulatoryCheck  = Transition(label='Regulatory Check')
distribution     = Transition(label='Distribution')

# Define the continuous-improvement loop: monitor then optionally feedback and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[growthMonitoring, feedbackLoop])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    siteSurvey, designLayout, installFrames, setupHydroponics, calibrateSensors,
    energyAudit, waterRecycling, climateControl,
    seedPlanting, nutrientMix, pestInspection,
    dataIntegration, loop,
    yieldForecast, harvestPrep, packaging, regulatoryCheck, distribution
])

# Add the control‐flow edges
root.order.add_edge(siteSurvey, designLayout)
root.order.add_edge(designLayout, installFrames)
root.order.add_edge(installFrames, setupHydroponics)
root.order.add_edge(setupHydroponics, calibrateSensors)

# After calibration, perform energy audit, water recycling, and climate control concurrently
root.order.add_edge(calibrateSensors, energyAudit)
root.order.add_edge(calibrateSensors, waterRecycling)
root.order.add_edge(calibrateSensors, climateControl)

# Once all environmental controls are in place, proceed to planting
root.order.add_edge(energyAudit, seedPlanting)
root.order.add_edge(waterRecycling, seedPlanting)
root.order.add_edge(climateControl, seedPlanting)

# Planting sequence
root.order.add_edge(seedPlanting, nutrientMix)
root.order.add_edge(nutrientMix, pestInspection)

# Data integration follows inspection, then enter the monitoring-feedback loop
root.order.add_edge(pestInspection, dataIntegration)
root.order.add_edge(dataIntegration, loop)

# After exiting the loop, forecast yield and wrap up
root.order.add_edge(loop, yieldForecast)
root.order.add_edge(yieldForecast, harvestPrep)
root.order.add_edge(harvestPrep, packaging)
root.order.add_edge(packaging, regulatoryCheck)
root.order.add_edge(regulatoryCheck, distribution)