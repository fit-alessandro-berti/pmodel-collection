# Generated from: 83949f83-41f0-4238-9d5f-75e2b1c86095.json
# Description: This process outlines the multi-disciplinary steps involved in authenticating historical artifacts for a museum acquisition. It begins with preliminary research and provenance verification, followed by scientific analysis including material composition and radiocarbon dating. Concurrently, expert stylistic evaluation and comparative studies are performed. Legal clearance and export permits are secured, while conservation specialists assess restoration needs. The artifact's digital archiving and cataloging are completed before final acquisition approval. Throughout, risk assessments and stakeholder communications ensure integrity and compliance with international regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
pr  = Transition(label='Preliminary Research')
pc  = Transition(label='Provenance Check')
ma  = Transition(label='Material Analysis')
rt  = Transition(label='Radiocarbon Test')
sr  = Transition(label='Stylistic Review')
cs  = Transition(label='Comparative Study')
lc  = Transition(label='Legal Clearance')
ep  = Transition(label='Export Permit')
cev = Transition(label='Conservation Eval')
rp  = Transition(label='Restoration Plan')
ra  = Transition(label='Risk Assessment')
ss  = Transition(label='Stakeholder Sync')
da  = Transition(label='Digital Archive')
ce2 = Transition(label='Catalog Entry')
av  = Transition(label='Acquisition Vote')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    pr, pc, ma, rt, sr, cs, lc, ep, cev, rp, ra, ss, da, ce2, av
])

# Core sequence: preliminary research → provenance check → scientific analysis
root.order.add_edge(pr, pc)
root.order.add_edge(pc, ma)
root.order.add_edge(ma, rt)

# Concurrent stylistic & comparative studies after provenance check
root.order.add_edge(pc, sr)
root.order.add_edge(pc, cs)

# Legal, export and conservation after scientific analysis
root.order.add_edge(rt, lc)
root.order.add_edge(rt, ep)
root.order.add_edge(rt, cev)
root.order.add_edge(cev, rp)

# Archiving and cataloging before final acquisition vote
root.order.add_edge(lc, da)
root.order.add_edge(ep, da)
root.order.add_edge(rp, da)
root.order.add_edge(da, ce2)
root.order.add_edge(ce2, av)

# Risk assessment and stakeholder synchronization run throughout
root.order.add_edge(pr, ra)
root.order.add_edge(pr, ss)
root.order.add_edge(ra, av)
root.order.add_edge(ss, av)