# Generated from: f21c1481-c6ba-490a-8659-af67394d09af.json
# Description: This process involves the detailed verification and authentication of historical artifacts sourced from multiple private collections and public auctions worldwide. It includes multidisciplinary scientific testing, provenance research, legal ownership validation, and ethical compliance checks before final acquisition or exhibition. The process ensures that artifacts are genuine, legally obtained, and preserved according to international standards, involving coordination among historians, scientists, legal teams, and curators. Complex logistics and secure transport arrangements are also integral to maintain artifact integrity throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
cs = Transition(label='Collection Survey')
pc = Transition(label='Provenance Check')
lr = Transition(label='Legal Review')
st = Transition(label='Scientific Test')
ma = Transition(label='Material Analysis')
oa = Transition(label='Ownership Audit')
es = Transition(label='Ethical Screening')
cr = Transition(label='Condition Report')
ec = Transition(label='Expert Consultation')
tp = Transition(label='Transport Planning')
sp = Transition(label='Secure Packing')
cc = Transition(label='Customs Clearance')
ins = Transition(label='Insurance Setup')
ep = Transition(label='Exhibit Preparation')
fa = Transition(label='Final Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[cs, pc, lr, st, ma, oa, es, cr, ec, tp, sp, cc, ins, ep, fa])

# Phase 1: after Collection Survey, several checks and reports can proceed in parallel
root.order.add_edge(cs, pc)
root.order.add_edge(cs, lr)
root.order.add_edge(cs, st)
root.order.add_edge(cs, cr)
root.order.add_edge(cs, ec)
root.order.add_edge(cs, es)

# Phase 2: provenance & legal feed into ownership audit; scientific test feeds into material analysis
root.order.add_edge(pc, oa)
root.order.add_edge(lr, oa)
root.order.add_edge(st, ma)

# Phase 3: once all checks & analyses are done, plan transport
root.order.add_edge(oa, tp)
root.order.add_edge(ma, tp)
root.order.add_edge(es, tp)
root.order.add_edge(cr, tp)
root.order.add_edge(ec, tp)

# Logistics sequence
root.order.add_edge(tp, sp)
root.order.add_edge(sp, cc)
root.order.add_edge(sp, ins)

# Legal review must complete before customs clearance
root.order.add_edge(lr, cc)

# Prepare exhibit after customs & insurance
root.order.add_edge(cc, ep)
root.order.add_edge(ins, ep)

# Final approval after exhibit preparation
root.order.add_edge(ep, fa)