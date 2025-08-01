# Generated from: 68a51af6-4c69-4481-8605-89282a7d27f3.json
# Description: This process outlines the complex and atypical procedure of establishing an urban vertical farm within a repurposed high-rise building. It involves multiple stages including site evaluation, environmental control design, modular system integration, crop selection, nutrient delivery setup, and waste recycling methods. The process requires coordination between architects, agricultural scientists, engineers, and logistics teams to ensure optimal crop yield and sustainability. Additionally, it addresses regulatory compliance, energy efficiency optimization, and community engagement to incorporate local needs and reduce environmental impact. Continuous monitoring and iterative adjustments are essential to adapt to urban constraints and maximize productivity in a non-traditional farming environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
siteSurvey      = Transition(label='Site Survey')
regulationCheck = Transition(label='Regulation Check')
layoutPlan      = Transition(label='Layout Plan')
climateSetup    = Transition(label='Climate Setup')
modularInstall  = Transition(label='Modular Install')
communityMeet   = Transition(label='Community Meet')
cropSelect      = Transition(label='Crop Select')
nutrientMix     = Transition(label='Nutrient Mix')
lightingConfig  = Transition(label='Lighting Config')
wasteSystem     = Transition(label='Waste System')
energyAudit     = Transition(label='Energy Audit')
irrigationSetup = Transition(label='Irrigation Setup')
staffTrain      = Transition(label='Staff Train')

# The monitoring & adjustment activities (to be put inside a loop)
yieldMonitor    = Transition(label='Yield Monitor')
pestControl     = Transition(label='Pest Control')
maintenancePlan = Transition(label='Maintenance Plan')
dataAnalysis    = Transition(label='Data Analysis')

# Build the "adjustment" partial order (the B branch of the loop)
adjust = StrictPartialOrder(nodes=[yieldMonitor, pestControl, maintenancePlan])
adjust.order.add_edge(yieldMonitor, maintenancePlan)
adjust.order.add_edge(pestControl, maintenancePlan)

# Build the LOOP node: first Data Analysis, then choose to exit or do adjust+analysis again
monitorLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[dataAnalysis, adjust]
)

# Build the root partial order with all main setup activities and the loop
root = StrictPartialOrder(nodes=[
    siteSurvey, regulationCheck, layoutPlan,
    climateSetup, modularInstall, communityMeet,
    cropSelect, nutrientMix, lightingConfig,
    wasteSystem, energyAudit, irrigationSetup,
    staffTrain, monitorLoop
])

# Define control‐flow edges
root.order.add_edge(siteSurvey,      regulationCheck)
root.order.add_edge(siteSurvey,      layoutPlan)

root.order.add_edge(regulationCheck, communityMeet)

root.order.add_edge(layoutPlan,      climateSetup)
root.order.add_edge(layoutPlan,      modularInstall)
root.order.add_edge(layoutPlan,      wasteSystem)
root.order.add_edge(layoutPlan,      energyAudit)
root.order.add_edge(layoutPlan,      cropSelect)
root.order.add_edge(communityMeet,   cropSelect)

root.order.add_edge(cropSelect,      nutrientMix)
root.order.add_edge(nutrientMix,     irrigationSetup)
root.order.add_edge(modularInstall,  irrigationSetup)
root.order.add_edge(climateSetup,    lightingConfig)

root.order.add_edge(wasteSystem,     staffTrain)
root.order.add_edge(energyAudit,     staffTrain)
root.order.add_edge(lightingConfig,  staffTrain)
root.order.add_edge(irrigationSetup, staffTrain)

root.order.add_edge(staffTrain,      monitorLoop)