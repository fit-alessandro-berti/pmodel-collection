# Generated from: a453cf7b-28c2-4143-8797-a5cadb84241b.json
# Description: This process involves the meticulous crafting of bespoke artisanal perfumes, combining traditional techniques with modern sensory analysis. Starting from raw botanical sourcing, the process moves through extraction, blending, maturation, and iterative scent testing. Each batch undergoes quality validation and customer profiling to tailor unique fragrance profiles. Packaging incorporates sustainable materials, followed by marketing strategy alignment and distribution to select boutiques. Post-launch feedback collection ensures continuous refinement of formulas, maintaining exclusivity and brand heritage in a niche luxury market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
botanical = Transition(label='Botanical Sourcing')
extract = Transition(label='Extract Oils')
blend = Transition(label='Blend Scents')
mature = Transition(label='Mature Blend')
test = Transition(label='Scent Testing')
quality = Transition(label='Quality Check')
profile = Transition(label='Profile Customer')
adjust = Transition(label='Adjust Formula')
design = Transition(label='Design Bottle')
packaging = Transition(label='Select Packaging')
labels = Transition(label='Print Labels')
market = Transition(label='Market Strategy')
launch = Transition(label='Launch Campaign')
distribute = Transition(label='Distribute Stock')
feedback = Transition(label='Collect Feedback')
refine = Transition(label='Refine Formula')

# Loop 1: iterative scent testing cycle
#   A = Scent Testing -> Quality Check -> Profile Customer
seq_test_cycle = StrictPartialOrder(nodes=[test, quality, profile])
seq_test_cycle.order.add_edge(test, quality)
seq_test_cycle.order.add_edge(quality, profile)
#   B = Adjust Formula
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seq_test_cycle, adjust])

# Loop 2: post-launch feedback refinement
#   A = Collect Feedback
#   B = Refine Formula
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[feedback, refine])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        botanical,
        extract,
        blend,
        mature,
        loop1,
        design,
        packaging,
        labels,
        market,
        launch,
        distribute,
        loop2
    ]
)

# Define the sequential dependencies
root.order.add_edge(botanical, extract)
root.order.add_edge(extract, blend)
root.order.add_edge(blend, mature)
root.order.add_edge(mature, loop1)
root.order.add_edge(loop1, design)
root.order.add_edge(design, packaging)
root.order.add_edge(packaging, labels)
root.order.add_edge(labels, market)
root.order.add_edge(market, launch)
root.order.add_edge(launch, distribute)
root.order.add_edge(distribute, loop2)