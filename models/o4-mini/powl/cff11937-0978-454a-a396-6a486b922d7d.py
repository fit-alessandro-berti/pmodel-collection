# Generated from: cff11937-0978-454a-a396-6a486b922d7d.json
# Description: This process describes the end-to-end supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise fermentation and aging in controlled cave environments. The process includes quality sampling, custom packaging design, cold-chain logistics coordination, market trend analysis for flavor adjustments, direct-to-consumer sales via pop-up events, and feedback incorporation for continuous product refinement. It ensures the preservation of traditional methods while leveraging modern technology for traceability and customer engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk         = Transition(label='Milk Sourcing')
quality      = Transition(label='Quality Testing')
starter      = Transition(label='Starter Culture')
fermentation = Transition(label='Milk Fermentation')
curd         = Transition(label='Curd Cutting')
whey         = Transition(label='Whey Draining')
press        = Transition(label='Pressing Cheese')
aging        = Transition(label='Cave Aging')
sample       = Transition(label='Sample Tasting')
profile      = Transition(label='Flavor Profiling')
packaging    = Transition(label='Packaging Design')
cold         = Transition(label='Cold Storage')
logistics    = Transition(label='Logistics Planning')
pop_up       = Transition(label='Pop-up Sales')
feedback     = Transition(label='Customer Feedback')
adjust       = Transition(label='Recipe Adjusting')
skip         = SilentTransition()

# 1) Define the tasting+profiling as a strict partial order
taste_profile = StrictPartialOrder(nodes=[sample, profile])
taste_profile.order.add_edge(sample, profile)

# 2) Define a XOR between custom packaging design or skip
pack_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging, skip])

# 3) Define the feedback sequence (pop-up sales → customer feedback)
feedback_seq = StrictPartialOrder(nodes=[pop_up, feedback])
feedback_seq.order.add_edge(pop_up, feedback)

# 4) Wrap the feedback loop: do (pop-up→feedback), then optionally adjust and repeat
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_seq, adjust])

# 5) Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    milk, quality, starter, fermentation, curd, whey, press, aging,
    taste_profile, pack_choice, cold, logistics, feedback_loop
])

# 6) Add the sequential dependencies
root.order.add_edge(milk,        quality)
root.order.add_edge(quality,     starter)
root.order.add_edge(starter,     fermentation)
root.order.add_edge(fermentation, curd)
root.order.add_edge(curd,        whey)
root.order.add_edge(whey,        press)
root.order.add_edge(press,       aging)
root.order.add_edge(aging,       taste_profile)
root.order.add_edge(taste_profile, pack_choice)
root.order.add_edge(pack_choice, cold)
root.order.add_edge(cold,        logistics)
root.order.add_edge(logistics,   feedback_loop)