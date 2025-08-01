# Generated from: 9ec40e0c-0604-4537-8fc5-2983b2b45c88.json
# Description: This process outlines the intricate lifecycle of producing artisanal cheese, starting from sourcing rare local milk, through precise fermentation and aging stages, to quality evaluation and bespoke packaging. Each step requires specialized craftsmanship and environmental monitoring to ensure distinctive flavor profiles. The process incorporates traditional methods alongside modern quality controls, involving seasonal adjustments and customer feedback loops to maintain authenticity and excellence across batches, culminating in distribution to niche markets and exclusive retailers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
milk      = Transition(label='Milk Sourcing')
quality   = Transition(label='Quality Testing')
starter   = Transition(label='Starter Culture')
pasteurize= Transition(label='Milk Pasteurize')
curd      = Transition(label='Curd Formation')
cut       = Transition(label='Cutting Curd')
drain     = Transition(label='Whey Drain')
mold      = Transition(label='Molding Cheese')
press     = Transition(label='Pressing Blocks')
salt      = Transition(label='Salting Surface')
aging     = Transition(label='Aging Control')
flavor    = Transition(label='Flavor Sampling')
rind      = Transition(label='Rind Treatment')
pack      = Transition(label='Packaging Design')
market    = Transition(label='Market Distribution')
feedback  = Transition(label='Customer Feedback')

# Silent transition for loop exits
skip = SilentTransition()

# Build the fermentation & aging phase as a strict partial order
fermentationPhase = StrictPartialOrder(nodes=[
    starter, pasteurize, curd, cut, drain, mold, press, salt, aging, flavor, rind
])
fermentationPhase.order.add_edge(starter,   pasteurize)
fermentationPhase.order.add_edge(pasteurize,curd)
fermentationPhase.order.add_edge(curd,      cut)
fermentationPhase.order.add_edge(cut,       drain)
fermentationPhase.order.add_edge(drain,     mold)
fermentationPhase.order.add_edge(mold,      press)
fermentationPhase.order.add_edge(press,     salt)
fermentationPhase.order.add_edge(salt,      aging)
fermentationPhase.order.add_edge(aging,     flavor)
fermentationPhase.order.add_edge(flavor,    rind)

# Loop to model seasonal adjustments around fermentation & aging
seasonalLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[fermentationPhase, skip]
)

# Build the packaging, distribution & feedback phase
packagingPhase = StrictPartialOrder(nodes=[pack, market, feedback])
packagingPhase.order.add_edge(pack,   market)
packagingPhase.order.add_edge(market, feedback)

# Loop to model customer–feedback cycle
feedbackLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[packagingPhase, skip]
)

# Compose the overall process
root = StrictPartialOrder(nodes=[milk, quality, seasonalLoop, feedbackLoop])
root.order.add_edge(milk,           quality)
root.order.add_edge(quality,        seasonalLoop)
root.order.add_edge(seasonalLoop,   feedbackLoop)