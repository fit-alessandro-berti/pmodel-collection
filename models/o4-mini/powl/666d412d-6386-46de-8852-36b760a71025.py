# Generated from: 666d412d-6386-46de-8852-36b760a71025.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming facility within a repurposed industrial building. It includes site analysis, environmental impact assessments, modular system design, selection of crop varieties optimized for vertical growth, installation of automated irrigation and lighting systems, integration of IoT sensors for real-time monitoring, staff recruitment and training focused on hydroponic techniques, implementation of pest control measures using biological agents, establishment of nutrient delivery schedules, continuous data analysis for yield optimization, compliance with local agricultural regulations, marketing strategy development targeting urban consumers, logistics planning for distribution within city limits, and periodic facility maintenance to ensure sustainability and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
siteSurvey       = Transition(label='Site Survey')
impactStudy      = Transition(label='Impact Study')
systemDesign     = Transition(label='System Design')
cropSelection    = Transition(label='Crop Selection')
irrigationSetup  = Transition(label='Irrigation Setup')
lightingInstall  = Transition(label='Lighting Install')
sensorIntegration= Transition(label='Sensor Integration')
staffHiring      = Transition(label='Staff Hiring')
trainingSessions = Transition(label='Training Sessions')
pestControl      = Transition(label='Pest Control')
nutrientPlan     = Transition(label='Nutrient Plan')
dataAnalysis     = Transition(label='Data Analysis')
regulationCheck  = Transition(label='Regulation Check')
marketingPlan    = Transition(label='Marketing Plan')
logisticsSetup   = Transition(label='Logistics Setup')
facilityAudit    = Transition(label='Facility Audit')

# Loop body: Pest Control -> Nutrient Plan -> Data Analysis
body = StrictPartialOrder(nodes=[pestControl, nutrientPlan, dataAnalysis])
body.order.add_edge(pestControl, nutrientPlan)
body.order.add_edge(nutrientPlan, dataAnalysis)

# Silent transition for loop continuation
skip = SilentTransition()

# LOOP operator: repeat the body until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])

# Root partial order including all phases
root = StrictPartialOrder(nodes=[
    siteSurvey, impactStudy, systemDesign, cropSelection, regulationCheck,
    irrigationSetup, lightingInstall, sensorIntegration,
    staffHiring, trainingSessions,
    loop,
    marketingPlan, logisticsSetup,
    facilityAudit
])

# Define the ordering relations
root.order.add_edge(siteSurvey,       impactStudy)
root.order.add_edge(impactStudy,      systemDesign)
root.order.add_edge(systemDesign,     cropSelection)
root.order.add_edge(cropSelection,    regulationCheck)

root.order.add_edge(regulationCheck,  irrigationSetup)
root.order.add_edge(regulationCheck,  lightingInstall)
root.order.add_edge(regulationCheck,  sensorIntegration)

root.order.add_edge(irrigationSetup,  staffHiring)
root.order.add_edge(lightingInstall,  staffHiring)
root.order.add_edge(sensorIntegration, staffHiring)

root.order.add_edge(staffHiring,      trainingSessions)
root.order.add_edge(trainingSessions, loop)

root.order.add_edge(loop,             marketingPlan)
root.order.add_edge(loop,             logisticsSetup)

root.order.add_edge(marketingPlan,    facilityAudit)
root.order.add_edge(logisticsSetup,   facilityAudit)