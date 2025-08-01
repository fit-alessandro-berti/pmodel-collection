# Generated from: acdbef5f-82bd-4032-8513-76f7f49cb397.json
# Description: This process involves sourcing rare milk varieties from multiple micro-dairies, followed by precision aging in controlled environments. Each batch undergoes microbiological testing and sensory evaluation before packaging. The logistics team coordinates temperature-sensitive transport to specialty retailers, while marketing crafts bespoke campaigns targeting niche gourmet consumers. Inventory management adapts dynamically according to seasonal milk yields and demand fluctuations. Regulatory compliance checks ensure adherence to evolving food safety standards. The process culminates in customer feedback collection to refine future production cycles, balancing artisanal quality with scalable distribution challenges.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
mp = Transition(label='Milk Pasteurize')
cf = Transition(label='Curd Formation')
pc = Transition(label='Press Cheese')
ca = Transition(label='Controlled Aging')
bt = Transition(label='Batch Testing')
mc = Transition(label='Microbial Check')
sr = Transition(label='Sensory Review')
pk = Transition(label='Package Cheese')
tt = Transition(label='Temp Transport')
rd = Transition(label='Retail Distribution')
mcamp = Transition(label='Market Campaign')
cm = Transition(label='Compliance Audit')
im = Transition(label='Inventory Monitor')
df = Transition(label='Demand Forecast')
fc = Transition(label='Feedback Collect')

# Loop for dynamic inventory/demand adaptation
inv_loop = OperatorPOWL(operator=Operator.LOOP, children=[im, df])

# Build the overall partial order
root = StrictPartialOrder(nodes=[ms, mp, cf, pc, ca,
                                 bt, mc, sr, pk,
                                 tt, rd, mcamp, cm,
                                 inv_loop, fc])

# Sequence of production steps
root.order.add_edge(ms, mp)
root.order.add_edge(mp, cf)
root.order.add_edge(cf, pc)
root.order.add_edge(pc, ca)
root.order.add_edge(ca, bt)

# Testing and evaluation in parallel
root.order.add_edge(bt, mc)
root.order.add_edge(bt, sr)
root.order.add_edge(mc, pk)
root.order.add_edge(sr, pk)

# Logistics, marketing, compliance concurrent after packaging
root.order.add_edge(pk, tt)
root.order.add_edge(pk, mcamp)
root.order.add_edge(pk, cm)

# Transport to retail
root.order.add_edge(tt, rd)

# After retail, run inventory loop then collect feedback
root.order.add_edge(rd, inv_loop)
root.order.add_edge(inv_loop, fc)

# Marketing campaign also flows into feedback
root.order.add_edge(mcamp, fc)