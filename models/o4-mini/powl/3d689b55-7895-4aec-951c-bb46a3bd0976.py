# Generated from: 3d689b55-7895-4aec-951c-bb46a3bd0976.json
# Description: This process outlines the complex, multi-stage supply chain for artisanal cheese production and distribution. It begins with sourcing rare milk varieties from niche farms, followed by precise curdling under controlled conditions. The cheese undergoes unique aging in microclimates, requiring regular quality inspections and environmental adjustments. Packaging involves sustainable, handcrafted materials to maintain freshness and brand ethos. Distribution channels include exclusive boutique stores and direct-to-consumer delivery with temperature monitoring. Throughout, traceability is ensured via blockchain logging to certify authenticity and origin, while customer feedback is gathered post-sale to refine future batches and marketing strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as transitions
ms = Transition(label="Milk Sourcing")
cf = Transition(label="Curd Formation")
tc1 = Transition(label="Temperature Control")
au = Transition(label="Aging Setup")
hc = Transition(label="Humidity Check")
qi = Transition(label="Quality Inspect")
ma = Transition(label="Microclimate Adjust")
rt = Transition(label="Rind Treatment")
pp = Transition(label="Packaging Prep")
ew = Transition(label="Eco Wrap")
bl = Transition(label="Batch Labeling")
bcl = Transition(label="Blockchain Log")

# Define the two distribution‐channel branches
# 1) Boutique store delivery
sd1 = Transition(label="Store Delivery")
# 2) Direct‐to‐consumer with temperature monitoring
#    (we reuse the Temperature Control activity as tc2 here, then deliver)
tc2 = Transition(label="Temperature Control")
sd2 = Transition(label="Store Delivery")
direct_po = StrictPartialOrder(nodes=[tc2, sd2])
direct_po.order.add_edge(tc2, sd2)

# Exclusive choice between the two distribution channels
distribution = OperatorPOWL(operator=Operator.XOR, children=[sd1, direct_po])

# Post‐sale feedback sequence
cs = Transition(label="Customer Survey")
fr = Transition(label="Feedback Review")
ru = Transition(label="Recipe Update")

# Assemble the global workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[
        ms, cf, tc1, au, hc, qi, ma, rt, pp, ew, bl,
        bcl,
        distribution,
        cs, fr, ru
    ]
)

# Add the main ordering (the cheese‐making & packaging pipeline)
root.order.add_edge(ms, cf)
root.order.add_edge(cf, tc1)
root.order.add_edge(tc1, au)
root.order.add_edge(au, hc)
root.order.add_edge(hc, qi)
root.order.add_edge(qi, ma)
root.order.add_edge(ma, rt)
root.order.add_edge(rt, pp)
root.order.add_edge(pp, ew)
root.order.add_edge(ew, bl)

# Blockchain logging after batch labeling
root.order.add_edge(bl, bcl)

# After logging, choose a distribution channel
root.order.add_edge(bcl, distribution)

# After distribution, gather feedback and update the recipe
root.order.add_edge(distribution, cs)
root.order.add_edge(cs, fr)
root.order.add_edge(fr, ru)