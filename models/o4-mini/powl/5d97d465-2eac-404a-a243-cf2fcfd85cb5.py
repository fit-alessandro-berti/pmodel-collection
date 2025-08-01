# Generated from: 5d97d465-2eac-404a-a243-cf2fcfd85cb5.json
# Description: This process outlines the intricate steps involved in producing and distributing high-quality artisanal cheese from small-scale farms to niche gourmet shops. It begins with raw milk sourcing from selected herds, followed by precise fermentation control and handcrafted curd formation. The cheese undergoes aging in controlled environments with specific humidity and temperature settings, monitored regularly for flavor development. Packaging involves eco-friendly materials with unique branding, after which the product is distributed through specialty logistics channels prioritizing freshness. Marketing targets connoisseurs via curated events and digital storytelling, while customer feedback loops help refine future batches. Regulatory compliance, seasonal variations, and artisanal authenticity checks are integrated throughout to maintain product integrity and exclusivity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
hs  = Transition(label='Herd Selection')
ms  = Transition(label='Milk Sourcing')
mt  = Transition(label='Milk Testing')
cf  = Transition(label='Curd Formation')
fc  = Transition(label='Fermentation Check')
ps  = Transition(label='Pressing Stage')
ac  = Transition(label='Aging Control')
hm  = Transition(label='Humidity Monitor')
ta  = Transition(label='Temperature Adjust')
fs  = Transition(label='Flavor Sampling')
ep  = Transition(label='Eco Packaging')
bl  = Transition(label='Brand Labeling')
ss  = Transition(label='Specialty Shipping')
em  = Transition(label='Event Marketing')
cfb = Transition(label='Customer Feedback')
qa  = Transition(label='Quality Audits')
rr  = Transition(label='Regulation Review')

# Loop for marketing & feedback cycles:
# do Event Marketing (A), then either exit or do Customer Feedback (B) then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[em, cfb])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    hs, ms, mt, cf, fc, ps, ac,
    hm, ta, fs, ep, bl, ss, loop,
    qa, rr
])

# Define the control‐flow edges
root.order.add_edge(hs,  ms)
root.order.add_edge(ms,  mt)

# Parallel branching into formation and fermentation
root.order.add_edge(mt,  cf)
root.order.add_edge(mt,  fc)

# Continue the main cheese process
root.order.add_edge(cf,  ps)
root.order.add_edge(ps,  ac)

# Aging sub‐activities in parallel
root.order.add_edge(ac,  hm)
root.order.add_edge(ac,  ta)
root.order.add_edge(ac,  fs)

# Packaging then distribution
root.order.add_edge(hm,  ep)
root.order.add_edge(ta,  ep)
root.order.add_edge(fs,  ep)
root.order.add_edge(ep,  bl)
root.order.add_edge(bl,  ss)

# Distribution leads into the marketing/feedback loop
root.order.add_edge(ss,  loop)

# Quality audits and regulatory review run concurrently after testing
root.order.add_edge(mt,  qa)
root.order.add_edge(mt,  rr)