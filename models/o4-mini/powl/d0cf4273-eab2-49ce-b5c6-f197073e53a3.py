# Generated from: d0cf4273-eab2-49ce-b5c6-f197073e53a3.json
# Description: This process details the intricate and atypical supply chain management of hand-crafted artisan goods, where raw materials are sourced from remote, sustainable locations, verified by cultural custodians, then transported using eco-friendly methods. Each batch undergoes quality storytelling sessions to preserve origin narratives before craftsmen transform them into unique products. Post-production, items are cataloged with provenance data, then marketed via niche community platforms targeting collectors. Finally, bespoke packaging is assembled by local cooperatives, ensuring minimal environmental impact and fostering social responsibility, followed by global distribution handled in collaboration with ethical logistics partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
ms      = Transition(label='Material Sourcing')
cv      = Transition(label='Cultural Verify')
et      = Transition(label='Eco Transport')
bs      = Transition(label='Batch Storytelling')
ca      = Transition(label='Craftsman Assignment')
pc      = Transition(label='Product Creation')
prov    = Transition(label='Provenance Catalog')
comm    = Transition(label='Community Marketing')
ct      = Transition(label='Collector Targeting')
pack    = Transition(label='Package Assembly')
coop    = Transition(label='Local Cooperatives')
audit   = Transition(label='Environmental Audit')
elog    = Transition(label='Ethical Logistics')
ship    = Transition(label='Global Shipping')
feedback= Transition(label='Feedback Collection')

# Build a strict partial order over the workflow
root = StrictPartialOrder(nodes=[
    ms, cv, et, bs, ca, pc, prov, comm, ct,
    pack, coop, audit, elog, ship, feedback
])

# Add the sequential dependencies
root.order.add_edge(ms,       cv)
root.order.add_edge(cv,       et)
root.order.add_edge(et,       bs)
root.order.add_edge(bs,       ca)
root.order.add_edge(ca,       pc)
root.order.add_edge(pc,       prov)
root.order.add_edge(prov,     comm)
root.order.add_edge(comm,     ct)
root.order.add_edge(ct,       pack)
root.order.add_edge(pack,     coop)
root.order.add_edge(coop,     audit)
root.order.add_edge(audit,    elog)
root.order.add_edge(elog,     ship)
root.order.add_edge(ship,     feedback)