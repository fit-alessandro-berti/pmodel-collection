# Generated from: 89333b83-4ecd-4e6f-b171-1c8c3d5cebd4.json
# Description: This process involves verifying the authenticity and provenance of historical artifacts through a multi-step evaluation combining scientific analysis, archival research, expert consultations, and cross-referencing with digital databases. It begins with initial artifact inspection and sampling, followed by radiocarbon dating and material composition analysis. Concurrently, archival research is conducted to trace the artifact’s documented history, including ownership and exhibition records. Expert panels review findings to assess stylistic consistency and historical context. Parallelly, digital provenance databases are queried to identify known forgeries or ownership disputes. Subsequent steps include legal clearance for export or sale, condition reporting, and preparing certification documents. The process concludes with secure artifact storage or transfer to authorized parties, ensuring chain-of-custody integrity and compliance with international cultural property laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
initial = Transition(label='Initial Inspection')
sample = Transition(label='Sample Collection')
rad = Transition(label='Radiocarbon Test')
mat = Transition(label='Material Analysis')
arch = Transition(label='Archival Search')
own = Transition(label='Ownership Trace')
style = Transition(label='Stylistic Review')
expert = Transition(label='Expert Panel')
dbq = Transition(label='Database Query')
forge = Transition(label='Forgery Check')
legal = Transition(label='Legal Clearance')
cond = Transition(label='Condition Report')
cert = Transition(label='Certification Prep')
chain = Transition(label='Chain Custody')
store = Transition(label='Secure Storage')

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial, sample, rad, mat, arch, own,
    style, expert, dbq, forge, legal,
    cond, cert, chain, store
])

# Add dependencies
root.order.add_edge(initial, sample)

# After sampling, scientific and archival and digital checks run in parallel
root.order.add_edge(sample, rad)
root.order.add_edge(sample, mat)
root.order.add_edge(sample, arch)
root.order.add_edge(sample, dbq)

# Archival branch
root.order.add_edge(arch, own)

# Scientific + archival feed into stylistic review
root.order.add_edge(rad, style)
root.order.add_edge(mat, style)
root.order.add_edge(own, style)

# Digital branch
root.order.add_edge(dbq, forge)

# Expert panel depends on stylistic review and forgery check
root.order.add_edge(style, expert)
root.order.add_edge(forge, expert)

# Subsequent steps
root.order.add_edge(expert, legal)
root.order.add_edge(legal, cond)
root.order.add_edge(cond, cert)
root.order.add_edge(cert, chain)
root.order.add_edge(chain, store)