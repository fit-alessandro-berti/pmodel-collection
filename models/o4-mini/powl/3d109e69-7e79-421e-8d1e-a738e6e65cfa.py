# Generated from: 3d109e69-7e79-421e-8d1e-a738e6e65cfa.json
# Description: This process oversees the end-to-end supply chain management of artisan cheese production, starting from raw milk sourcing from local farms, followed by quality testing and fermentation control. It includes specialized aging environment setup, periodic sensory evaluations, packaging customization, cold chain logistics, seasonal demand forecasting, compliance with regional food safety regulations, and collaboration with boutique retailers for exclusive product launches. The process ensures traceability, sustainability practices, and customer feedback integration to refine cheese varieties and distribution strategies, maintaining a balance between tradition and innovation throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milkSourcing    = Transition(label='Milk Sourcing')
qualityTesting  = Transition(label='Quality Testing')
starterCulture  = Transition(label='Starter Culture')
coagulation     = Transition(label='Coagulation')
curdCutting     = Transition(label='Curd Cutting')
wheyDraining    = Transition(label='Whey Draining')
moldingPress    = Transition(label='Molding Press')
saltingStage    = Transition(label='Salting Stage')
agingSetup      = Transition(label='Aging Setup')
tempCheck       = Transition(label='Temperature Check')
sensoryEval     = Transition(label='Sensory Eval')
packagingPrep   = Transition(label='Packaging Prep')
labelPrinting   = Transition(label='Label Printing')
coldStorage     = Transition(label='Cold Storage')
orderForecast   = Transition(label='Order Forecast')
regCompliance   = Transition(label='Reg Compliance')
logisticsPlan   = Transition(label='Logistics Plan')
retailSync      = Transition(label='Retail Sync')
feedbackReview  = Transition(label='Feedback Review')

# Loop for periodic sensory evaluation and temperature checks
evaluationLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[tempCheck, sensoryEval]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    milkSourcing, qualityTesting, starterCulture, coagulation,
    curdCutting, wheyDraining, moldingPress, saltingStage,
    agingSetup, evaluationLoop, packagingPrep, labelPrinting,
    coldStorage, orderForecast, regCompliance, logisticsPlan,
    retailSync, feedbackReview
])

# Sequential ordering for the cheese‐making stages
root.order.add_edge(milkSourcing,   qualityTesting)
root.order.add_edge(qualityTesting,  starterCulture)
root.order.add_edge(starterCulture,  coagulation)
root.order.add_edge(coagulation,     curdCutting)
root.order.add_edge(curdCutting,     wheyDraining)
root.order.add_edge(wheyDraining,    moldingPress)
root.order.add_edge(moldingPress,    saltingStage)
root.order.add_edge(saltingStage,    agingSetup)

# After aging setup, enter the periodic evaluation loop
root.order.add_edge(agingSetup,      evaluationLoop)
# After finishing the loop, move to packaging
root.order.add_edge(evaluationLoop,  packagingPrep)
root.order.add_edge(packagingPrep,   labelPrinting)

# From packaging, fork into parallel downstream activities
for nxt in [coldStorage, orderForecast, regCompliance, logisticsPlan, retailSync]:
    root.order.add_edge(labelPrinting, nxt)

# After all downstream activities, gather into feedback review
for prev in [coldStorage, orderForecast, regCompliance, logisticsPlan, retailSync]:
    root.order.add_edge(prev, feedbackReview)