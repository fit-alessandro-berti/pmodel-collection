# Generated from: caf2784b-5fe2-4a65-b0f5-6d36f16fcc7a.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farm inside a repurposed industrial building. It includes initial site assessment, environmental impact evaluation, modular system design, and the integration of IoT sensors for real-time monitoring. The process continues with hydroponic system installation, nutrient calibration, and automated lighting setup tailored for optimal plant growth. It further encompasses staff training on sustainable farming techniques, ongoing data analytics for yield optimization, pest management protocols, and finally, the distribution logistics for delivering fresh produce directly to local markets. This atypical yet realistic business process requires cross-disciplinary coordination between architects, engineers, agronomists, and supply chain experts to ensure profitability and sustainability in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
siteAudit         = Transition(label='Site Audit')
impactStudy       = Transition(label='Impact Study')
designModules     = Transition(label='Design Modules')
sensorSetup       = Transition(label='Sensor Setup')
hydroponicsInstall= Transition(label='Hydroponics Install')
nutrientTest      = Transition(label='Nutrient Test')
lightingConfig    = Transition(label='Lighting Config')
staffTraining     = Transition(label='Staff Training')
dataCollection    = Transition(label='Data Collection')
yieldAnalysis     = Transition(label='Yield Analysis')
pestControl       = Transition(label='Pest Control')
harvestPlan       = Transition(label='Harvest Plan')
packagingPrep     = Transition(label='Packaging Prep')
marketDelivery    = Transition(label='Market Delivery')
feedbackLoop      = Transition(label='Feedback Loop')

# Phase A: data collection and analysis
phaseA = StrictPartialOrder(nodes=[dataCollection, yieldAnalysis])
phaseA.order.add_edge(dataCollection, yieldAnalysis)

# Phase B: pest management through feedback
phaseB = StrictPartialOrder(nodes=[
    pestControl, harvestPlan, packagingPrep, marketDelivery, feedbackLoop
])
phaseB.order.add_edge(pestControl,   harvestPlan)
phaseB.order.add_edge(harvestPlan,   packagingPrep)
phaseB.order.add_edge(packagingPrep, marketDelivery)
phaseB.order.add_edge(marketDelivery, feedbackLoop)

# Loop: execute A, then optionally B then A again, repeated
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[phaseA, phaseB])

# Root partial order of the overall process
root = StrictPartialOrder(nodes=[
    siteAudit,
    impactStudy,
    designModules,
    sensorSetup,
    hydroponicsInstall,
    nutrientTest,
    lightingConfig,
    staffTraining,
    feedback_loop
])
root.order.add_edge(siteAudit,          impactStudy)
root.order.add_edge(impactStudy,        designModules)
root.order.add_edge(designModules,      sensorSetup)
root.order.add_edge(sensorSetup,        hydroponicsInstall)
root.order.add_edge(hydroponicsInstall, nutrientTest)
root.order.add_edge(nutrientTest,       lightingConfig)
root.order.add_edge(lightingConfig,     staffTraining)
root.order.add_edge(staffTraining,      feedback_loop)