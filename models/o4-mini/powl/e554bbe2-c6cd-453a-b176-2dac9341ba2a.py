# Generated from: e554bbe2-c6cd-453a-b176-2dac9341ba2a.json
# Description: This process outlines the intricate steps involved in sourcing rare cheeses from small-scale artisanal farms, ensuring quality through custom aging, managing seasonal variations, and coordinating with niche gourmet retailers. It includes unique tasks such as microbial profiling, traditional hand-wrapping, climate-controlled transport logistics, and consumer feedback integration to maintain authenticity and exclusivity. The process demands close collaboration between farmers, microbiologists, logistics experts, and marketing teams to preserve the cheese's heritage while scaling distribution sustainably across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the main workflow transitions
fs = Transition(label='Farm Selection')
mt = Transition(label='Milk Testing')
sc = Transition(label='Starter Culture')
cf = Transition(label='Curd Formation')
pc = Transition(label='Pressing Cheese')
mp = Transition(label='Microbial Profiling')
ac = Transition(label='Aging Control')
hw = Transition(label='Hand Wrapping')
qa = Transition(label='Quality Audit')
pp = Transition(label='Packaging Prep')
cs = Transition(label='Climate Shipping')
rc = Transition(label='Retail Coordination')

# Define the loop for seasonal review and feedback-driven adjustments
sr = Transition(label='Seasonal Review')
cus = Transition(label='Consumer Survey')
fa = Transition(label='Feedback Analysis')
ma = Transition(label='Market Adjustment')

# Sequence inside the loop: Consumer Survey -> Feedback Analysis -> Market Adjustment
feedback_seq = StrictPartialOrder(nodes=[cus, fa, ma])
feedback_seq.order.add_edge(cus, fa)
feedback_seq.order.add_edge(fa, ma)

# Loop operator: do Seasonal Review, then either exit or do feedback_seq and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[sr, feedback_seq])

# Assemble the root partial order with the main sequence and the loop
root = StrictPartialOrder(nodes=[fs, mt, sc, cf, pc, mp, ac, hw, qa, pp, cs, rc, loop])

# Add ordering constraints for the main cheese‐sourcing workflow
root.order.add_edge(fs, mt)
root.order.add_edge(mt, sc)
root.order.add_edge(sc, cf)
root.order.add_edge(cf, pc)
root.order.add_edge(pc, mp)
root.order.add_edge(mp, ac)
root.order.add_edge(ac, hw)
root.order.add_edge(hw, qa)
root.order.add_edge(qa, pp)
root.order.add_edge(pp, cs)
root.order.add_edge(cs, rc)
root.order.add_edge(rc, loop)