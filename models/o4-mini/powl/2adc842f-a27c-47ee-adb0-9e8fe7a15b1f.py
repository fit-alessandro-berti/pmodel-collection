# Generated from: 2adc842f-a27c-47ee-adb0-9e8fe7a15b1f.json
# Description: This process describes the sourcing, production, and distribution of artisanal cheese from rare breeds of goats. It involves selective breeding coordination, specialized feeding schedules, milk quality testing, traditional curdling methods, precise aging conditions, and custom packaging. The process ensures traceable origin, seasonal variation adjustments, and direct delivery to niche markets and exclusive retailers, maintaining exceptional quality and artisanal integrity throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
breed_selection    = Transition(label='Breed Selection')
feed_planning      = Transition(label='Feed Planning')
milk_collection    = Transition(label='Milk Collection')
quality_testing    = Transition(label='Quality Testing')
curd_preparation   = Transition(label='Curd Preparation')
mold_inoculation   = Transition(label='Mold Inoculation')
pressing_cheese    = Transition(label='Pressing Cheese')
salting_process    = Transition(label='Salting Process')
controlled_aging   = Transition(label='Controlled Aging')
humidity_check     = Transition(label='Humidity Check')
texture_sampling   = Transition(label='Texture Sampling')
packaging_design   = Transition(label='Packaging Design')
label_printing     = Transition(label='Label Printing')
order_processing   = Transition(label='Order Processing')
retail_delivery    = Transition(label='Retail Delivery')
feedback_gathering = Transition(label='Feedback Gathering')

# Define the sub-process for the aging checks (humidity check -> texture sampling)
aging_checks = StrictPartialOrder(nodes=[humidity_check, texture_sampling])
aging_checks.order.add_edge(humidity_check, texture_sampling)

# Define the loop for controlled aging: do Controlled Aging, then either exit or perform checks and repeat
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, aging_checks])

# Build the overall workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    breed_selection,
    feed_planning,
    milk_collection,
    quality_testing,
    curd_preparation,
    mold_inoculation,
    pressing_cheese,
    salting_process,
    loop_aging,
    packaging_design,
    label_printing,
    order_processing,
    retail_delivery,
    feedback_gathering
])

# Sequence edges
sequence = [
    breed_selection,
    feed_planning,
    milk_collection,
    quality_testing,
    curd_preparation,
    mold_inoculation,
    pressing_cheese,
    salting_process,
    loop_aging,
    packaging_design,
    label_printing,
    order_processing,
    retail_delivery,
    feedback_gathering
]
for src, tgt in zip(sequence, sequence[1:]):
    root.order.add_edge(src, tgt)