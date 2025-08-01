# Generated from: c6ff4518-567f-4cc2-b229-9e54e380a22d.json
# Description: This process describes the end-to-end supply chain for artisanal cheese production, starting from sourcing rare local milk varieties to aging cheese in controlled microclimates. It involves unique activities such as microbial culture selection, hand molding, natural rind treatment, and seasonal flavor profiling. Quality control is conducted through sensory panel reviews and microscopic texture inspections. Packaging is eco-friendly and customized per batch, followed by niche market distribution targeting specialty food stores and luxury restaurants. The process ensures traceability of every cheese wheel through blockchain-enabled records, enhancing transparency and consumer trust in a highly specialized product category.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milkSourcing      = Transition(label='Milk Sourcing')
culturePrep       = Transition(label='Culture Prep')
milkPasteurize    = Transition(label='Milk Pasteurize')
coagulation       = Transition(label='Coagulation')
curdCutting       = Transition(label='Curd Cutting')
wheyDraining      = Transition(label='Whey Draining')
handMolding       = Transition(label='Hand Molding')
pressing          = Transition(label='Pressing')
salting           = Transition(label='Salting')
rindTreatment     = Transition(label='Rind Treatment')
agingSetup        = Transition(label='Aging Setup')
microclimateCtrl  = Transition(label='Microclimate Control')
flavorProfiling   = Transition(label='Flavor Profiling')
qualityCheck      = Transition(label='Quality Check')
sensoryReview     = Transition(label='Sensory Review')
textureInspect    = Transition(label='Texture Inspect')
ecoPackaging      = Transition(label='Eco Packaging')
batchLabeling     = Transition(label='Batch Labeling')
blockchainLog     = Transition(label='Blockchain Log')
nicheShipping     = Transition(label='Niche Shipping')

# Loop for repeated microclimate adjustments & profiling
loop = OperatorPOWL(operator=Operator.LOOP, children=[microclimateCtrl, flavorProfiling])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milkSourcing, culturePrep, milkPasteurize, coagulation, curdCutting,
    wheyDraining, handMolding, pressing, salting, rindTreatment,
    agingSetup, loop, qualityCheck, sensoryReview, textureInspect,
    ecoPackaging, batchLabeling, blockchainLog, nicheShipping
])

# Sequence up to aging setup
seq = [
    milkSourcing, culturePrep, milkPasteurize, coagulation, curdCutting,
    wheyDraining, handMolding, pressing, salting, rindTreatment, agingSetup
]
for a, b in zip(seq, seq[1:]):
    root.order.add_edge(a, b)

# From aging setup into the loop
root.order.add_edge(agingSetup, loop)
# After loop, do quality check
root.order.add_edge(loop, qualityCheck)
# Quality check splits into sensory review and texture inspection (concurrent)
root.order.add_edge(qualityCheck, sensoryReview)
root.order.add_edge(qualityCheck, textureInspect)

# Both QC activities must complete before packaging steps
for qc in [sensoryReview, textureInspect]:
    for pkg in [ecoPackaging, batchLabeling, blockchainLog]:
        root.order.add_edge(qc, pkg)

# Packaging steps must complete before final shipping
for pkg in [ecoPackaging, batchLabeling, blockchainLog]:
    root.order.add_edge(pkg, nicheShipping)