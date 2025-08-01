# Generated from: b705efee-6a47-47ca-b37b-48923c414aa6.json
# Description: This process outlines the comprehensive steps involved in converting physical and digital assets into blockchain-based tokens for fractional ownership and trading. It begins with asset verification and legal compliance checks, followed by smart contract development tailored to asset type and investor requirements. The workflow includes multi-party approval, dynamic pricing algorithms, and integration with decentralized exchanges. Post-token issuance, the process manages continuous asset auditing, dividend distribution automation, and secondary market monitoring to ensure transparency and regulatory adherence throughout the asset lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
av = Transition(label='Asset Verify')
lr = Transition(label='Legal Review')
ra = Transition(label='Risk Assess')
cd = Transition(label='Contract Draft')
td = Transition(label='Token Design')
pm = Transition(label='Price Model')
iq = Transition(label='Investor Qualify')
ma = Transition(label='Multi Approve')
sd = Transition(label='Smart Deploy')
el = Transition(label='Exchange Link')
io = Transition(label='Initial Offer')

# Post‐issuance activities
as_ = Transition(label='Audit Schedule')
ds = Transition(label='Dividend Set')
mw = Transition(label='Market Watch')
cu = Transition(label='Compliance Update')
rg = Transition(label='Report Generate')

# Silent transition for loop exit
skip = SilentTransition()

# Build the post‐issuance sequence
post_body = StrictPartialOrder(nodes=[as_, ds, mw, cu, rg])
post_body.order.add_edge(as_, ds)
post_body.order.add_edge(ds, mw)
post_body.order.add_edge(mw, cu)
post_body.order.add_edge(cu, rg)

# Loop operator: repeat post‐issuance sequence until exit
post_loop = OperatorPOWL(operator=Operator.LOOP, children=[post_body, skip])

# Build the initial workflow with partial order
root = StrictPartialOrder(
    nodes=[av, lr, ra, cd, td, pm, iq, ma, sd, el, io, post_loop]
)

# Asset Verify and Legal Review in parallel, both precede Risk Assess
root.order.add_edge(av, ra)
root.order.add_edge(lr, ra)

# Then a strict sequence through to Initial Offer
root.order.add_edge(ra, cd)
root.order.add_edge(cd, td)
root.order.add_edge(td, pm)
root.order.add_edge(pm, iq)
root.order.add_edge(iq, ma)
root.order.add_edge(ma, sd)
root.order.add_edge(sd, el)
root.order.add_edge(el, io)

# From Initial Offer into the post‐issuance loop
root.order.add_edge(io, post_loop)