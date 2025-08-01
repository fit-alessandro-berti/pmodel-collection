# Generated from: 94526029-9d68-4e0b-b1ca-718620e2fbe4.json
# Description: This process involves locating, authenticating, and reclaiming lost or stolen antique assets from private collections or public sales. It requires extensive provenance research, legal clearance, negotiation with current holders, coordination with law enforcement, and meticulous documentation. The process also includes restoration assessment, insurance appraisal, and final asset repatriation to rightful owners or museums. Each step demands expert collaboration, risk management, and compliance with international cultural property laws to ensure ethical and legal recovery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define activities
al = Transition(label='Asset Locate')
pc = Transition(label='Provenance Check')
fa = Transition(label='Forensic Audit')
lr = Transition(label='Legal Review')
ov = Transition(label='Ownership Verify')
lc = Transition(label='Law Consult')
hc = Transition(label='Holder Contact')
nl = Transition(label='Negotiation Lead')
rp = Transition(label='Restoration Plan')
ia = Transition(label='Insurance Assess')
cc = Transition(label='Customs Clear')
ta = Transition(label='Transport Arrange')
ra = Transition(label='Repatriate Asset')
doc = Transition(label='Documentation')
fr = Transition(label='Final Report')

# build the partial‐order workflow
root = StrictPartialOrder(nodes=[al, pc, fa, lr, ov, lc, hc, nl, rp, ia, cc, ta, ra, doc, fr])

# Asset Locate must happen before Provenance Check and Forensic Audit
root.order.add_edge(al, pc)
root.order.add_edge(al, fa)

# Provenance Check and Forensic Audit must both complete before Legal Review and Ownership Verify
root.order.add_edge(pc, lr)
root.order.add_edge(fa, lr)
root.order.add_edge(pc, ov)
root.order.add_edge(fa, ov)

# Legal Review and Ownership Verify must both complete before Law Consult
root.order.add_edge(lr, lc)
root.order.add_edge(ov, lc)

# sequential continuation
root.order.add_edge(lc, hc)   # Law Consult → Holder Contact
root.order.add_edge(hc, nl)   # Holder Contact → Negotiation Lead

# after negotiation, Restoration Plan and Insurance Assess can proceed in parallel
root.order.add_edge(nl, rp)
root.order.add_edge(nl, ia)

# both Restoration Plan and Insurance Assess must complete before Customs Clear
root.order.add_edge(rp, cc)
root.order.add_edge(ia, cc)

# then Transport Arrange → Repatriate Asset → Documentation → Final Report
root.order.add_edge(cc, ta)
root.order.add_edge(ta, ra)
root.order.add_edge(ra, doc)
root.order.add_edge(doc, fr)