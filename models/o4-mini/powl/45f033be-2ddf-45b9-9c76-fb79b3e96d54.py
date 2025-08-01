# Generated from: 45f033be-2ddf-45b9-9c76-fb79b3e96d54.json
# Description: This process outlines the complex journey of artisanal cheese from farm to international markets, involving intricate steps such as raw milk sourcing, microbial culture management, controlled aging, quality certification, packaging customization, and compliance with diverse export regulations. The process also integrates seasonal production adjustments, artisan skill assessments, and dynamic logistics coordination to ensure product integrity and timely delivery across multiple countries with varying import standards and consumer preferences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ms = Transition(label='Milk Sourcing')
cp = Transition(label='Culture Prep')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
pf = Transition(label='Press Forming')
ca = Transition(label='Controlled Aging')
ss = Transition(label='Season Adjust')
sa = Transition(label='Skill Assess')
qi = Transition(label='Quality Inspect')
va = Transition(label='Vendor Audit')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
el = Transition(label='Export License')
cf = Transition(label='Customs Filing')
lp = Transition(label='Logistics Plan')
dt = Transition(label='Delivery Track')

# Loop for seasonal adjustments and skill assessments
loop = OperatorPOWL(operator=Operator.LOOP, children=[ss, sa])

# Exclusive choice between obtaining export license or filing customs
export_choice = OperatorPOWL(operator=Operator.XOR, children=[el, cf])

# Build the partial-order workflow
root = StrictPartialOrder(
    nodes=[ms, cp, mp, cc, wd, mi, pf, ca, loop, qi, va, pd, la, export_choice, lp, dt]
)

# Define the control-flow dependencies
root.order.add_edge(ms, cp)
root.order.add_edge(cp, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pf)
root.order.add_edge(pf, ca)
root.order.add_edge(ca, loop)
root.order.add_edge(loop, qi)
root.order.add_edge(qi, va)
root.order.add_edge(va, pd)
root.order.add_edge(pd, la)
root.order.add_edge(la, export_choice)
root.order.add_edge(export_choice, lp)
root.order.add_edge(lp, dt)