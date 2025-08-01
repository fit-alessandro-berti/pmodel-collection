# Generated from: 01a7abb8-2f63-47e4-bc6b-b3706fe048df.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment for structural integrity and sunlight access, modular system design for hydroponics and aeroponics integration, procurement of specialized equipment, installation of climate control and nutrient delivery systems, staff training on innovative cultivation techniques, implementation of IoT sensors for real-time monitoring, compliance with local agricultural regulations, iterative crop testing to optimize yield, marketing strategies for urban produce distribution, and continuous sustainability assessments to reduce energy and water consumption. The process demands coordination between architects, agronomists, engineers, and business strategists to ensure a profitable and eco-friendly farming solution in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
siteSurvey      = Transition(label='Site Survey')
structuralCheck = Transition(label='Structural Check')
lightMapping    = Transition(label='Light Mapping')
systemDesign    = Transition(label='System Design')
equipmentOrder  = Transition(label='Equipment Order')
climateSetup    = Transition(label='Climate Setup')
nutrientMix     = Transition(label='Nutrient Mix')
sensorInstall   = Transition(label='Sensor Install')
staffTraining   = Transition(label='Staff Training')
regulationReview= Transition(label='Regulation Review')
cropTesting     = Transition(label='Crop Testing')
yieldAnalysis   = Transition(label='Yield Analysis')
marketOutreach  = Transition(label='Market Outreach')
energyAudit     = Transition(label='Energy Audit')
waterRecycling  = Transition(label='Water Recycling')
dataMonitoring  = Transition(label='Data Monitoring')
feedbackLoop    = Transition(label='Feedback Loop')

# 1. Site assessment: Site Survey -> {Structural Check, Light Mapping} in parallel
po_site = StrictPartialOrder(nodes=[siteSurvey, structuralCheck, lightMapping])
po_site.order.add_edge(siteSurvey, structuralCheck)
po_site.order.add_edge(siteSurvey, lightMapping)

# 2. Installation of systems in parallel: Climate Setup and Nutrient Mix
po_install = StrictPartialOrder(nodes=[climateSetup, nutrientMix])
# (no edges = concurrent execution)

# 3. Iterative crop testing loop: Crop Testing, Yield Analysis
cropLoop = OperatorPOWL(operator=Operator.LOOP, children=[cropTesting, yieldAnalysis])

# 4. Continuous sustainability assessments (modeled as a concurrent block)
sustainability = StrictPartialOrder(
    nodes=[energyAudit, waterRecycling, dataMonitoring, feedbackLoop]
)
# (no internal edges = all can run concurrently)

# 5. Assemble the overall process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        po_site,
        systemDesign,
        equipmentOrder,
        po_install,
        sensorInstall,
        staffTraining,
        regulationReview,
        cropLoop,
        marketOutreach,
        sustainability
    ]
)

# Define the control-flow (partial order) between the major steps
root.order.add_edge(po_site,           systemDesign)
root.order.add_edge(systemDesign,      equipmentOrder)
root.order.add_edge(equipmentOrder,    po_install)
root.order.add_edge(po_install,        sensorInstall)
root.order.add_edge(sensorInstall,     staffTraining)
root.order.add_edge(staffTraining,     regulationReview)
root.order.add_edge(regulationReview,  cropLoop)
root.order.add_edge(cropLoop,          marketOutreach)
root.order.add_edge(marketOutreach,    sustainability)