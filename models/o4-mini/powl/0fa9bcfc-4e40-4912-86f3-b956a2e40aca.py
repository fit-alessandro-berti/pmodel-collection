# Generated from: 0fa9bcfc-4e40-4912-86f3-b956a2e40aca.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponic systems, IoT-based environmental controls, and renewable energy sources. It involves initial site analysis in dense city environments, modular infrastructure assembly, nutrient solution formulation, and continuous monitoring to optimize crop yield. The process also includes community engagement for local sourcing, regulatory compliance with urban agricultural policies, and integration with local distribution networks to ensure fresh produce delivery. This atypical business process requires coordination across agriculture, technology, and urban planning domains to create a sustainable food production model within metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss  = Transition(label='Site Survey')
dl  = Transition(label='Design Layout')
pc  = Transition(label='Permitting Check')
rr  = Transition(label='Regulation Review')
cm  = Transition(label='Community Meet')
mb  = Transition(label='Modular Build')
si  = Transition(label='System Install')
cs  = Transition(label='Climate Setup')
ic  = Transition(label='IoT Config')
np  = Transition(label='Nutrient Prep')
wt  = Transition(label='Water Testing')
sp  = Transition(label='Seed Planting')
gm  = Transition(label='Growth Monitor')
ea  = Transition(label='Energy Audit')
hp  = Transition(label='Harvest Plan')
dlk = Transition(label='Distribution Link')
wm  = Transition(label='Waste Manage')

# Define the loop body: Energy Audit -> Water Testing
loop_body = StrictPartialOrder(nodes=[ea, wt])
loop_body.order.add_edge(ea, wt)

# Define the growth-monitoring loop: gm then (ea->wt then gm)*
loop = OperatorPOWL(operator=Operator.LOOP, children=[gm, loop_body])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    ss, dl, pc, rr, cm,
    mb, si, cs, ic, np,
    wt, sp, loop, hp, dlk, wm
])

# Pre‐build sequence: Site Survey -> Design Layout
root.order.add_edge(ss, dl)

# After design, do Permitting Check, Regulation Review, Community Meet in parallel
root.order.add_edge(dl, pc)
root.order.add_edge(dl, rr)
root.order.add_edge(dl, cm)

# Once permits, regs, community meet are done, start infrastructure tasks in parallel
for prev in (pc, rr, cm):
    root.order.add_edge(prev, mb)
    root.order.add_edge(prev, si)
    root.order.add_edge(prev, cs)

# After build/install/setup, configure IoT and prep nutrients in parallel
for prev in (mb, si, cs):
    root.order.add_edge(prev, ic)
    root.order.add_edge(prev, np)

# Nutrient Prep and IoT Config must finish before first Water Testing, then Seed Planting
root.order.add_edge(ic, wt)
root.order.add_edge(np, wt)
root.order.add_edge(wt, sp)

# After planting, enter the growth‐monitoring loop
root.order.add_edge(sp, loop)

# After exiting the loop, finalize harvest and distribution
root.order.add_edge(loop, hp)
root.order.add_edge(hp, dlk)
root.order.add_edge(dlk, wm)