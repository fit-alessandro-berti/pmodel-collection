# Generated from: 995c2cbb-f830-4d59-a07a-db1b594d0e11.json
# Description: This process outlines the intricate journey of artisan cheese from small-scale farms to niche gourmet retailers. It involves unique steps such as microbial culture selection, controlled aging environments, and sensory quality evaluation by expert tasters. The process requires coordination between farmers, microbiologists, transporters, and retailers to maintain product integrity and flavor consistency. Special attention is given to seasonal variations in milk quality and the impact on fermentation. Additionally, packaging includes biodegradable materials to align with sustainability goals. Real-time tracking ensures freshness while bespoke marketing campaigns educate consumers on cheese provenance and pairing suggestions. This atypical supply chain balances traditional craftsmanship with modern logistics and consumer engagement strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms = Transition(label='Milk Sourcing')
sa = Transition(label='Seasonal Adjust')
cp = Transition(label='Culture Prep')
coag = Transition(label='Coagulation')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mp = Transition(label='Molding Press')
isd = Transition(label='Initial Salting')
ca = Transition(label='Controlled Aging')
mt = Transition(label='Microbial Testing')
sp = Transition(label='Sensory Panel')
ep = Transition(label='Eco Packaging')
ct = Transition(label='Cold Transport')
rs = Transition(label='Retail Setup')
ce = Transition(label='Consumer Edu')
fl = Transition(label='Feedback Loop')
ia = Transition(label='Inventory Audit')

# Define the partial order for the testing & evaluation phase
tests_po = StrictPartialOrder(nodes=[mt, sp])
tests_po.order.add_edge(mt, sp)

# Wrap the aging + testing in a loop:
# First do Controlled Aging (ca), then repeatedly do (mt -> sp) and return to ca, or exit.
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ca, tests_po])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[ms, sa, cp, coag, cc, wd, mp, isd, aging_loop,
           ep, ct, rs, ce, fl, ia]
)

# Add the sequential dependencies
seq = [ms, sa, cp, coag, cc, wd, mp, isd, aging_loop,
       ep, ct, rs, ce, fl, ia]
for prv, nxt in zip(seq, seq[1:]):
    root.order.add_edge(prv, nxt)