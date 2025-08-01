# Generated from: 36a071f5-d3b1-4d94-af8b-560b64847f46.json
# Description: This process involves the complex orchestration of sourcing rare milk varieties, aging cheese in controlled microclimates, and managing artisanal packaging to preserve flavor integrity. It includes farm inspections, microbial testing, seasonal variation adjustments, and bespoke logistics coordination to ensure freshness and compliance with gourmet food regulations. The process also incorporates consumer feedback loops and limited edition releases to maintain exclusivity and market demand, requiring tight collaboration between dairy farmers, microbiologists, logistics teams, and marketing units.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms  = Transition(label='Milk Sourcing')
fi  = Transition(label='Farm Inspection')
mt  = Transition(label='Microbial Test')
mp  = Transition(label='Milk Pasteurize')
cf  = Transition(label='Curd Formation')
ws  = Transition(label='Whey Separation')
cm  = Transition(label='Cheese Molding')
ss  = Transition(label='Salting Stage')
ac  = Transition(label='Aging Control')
cad = Transition(label='Climate Adjust')
qc  = Transition(label='Quality Check')
pd  = Transition(label='Packaging Design')
lp  = Transition(label='Label Printing')
lg  = Transition(label='Logistics Plan')
rd  = Transition(label='Retail Dispatch')
cfb = Transition(label='Customer Feedback')
ma  = Transition(label='Market Analysis')

# Loop for the aging + climate adjustment cycle
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ac, cad]
)

# Main production pipeline (A)
A = StrictPartialOrder(nodes=[
    ms, fi, mt, mp, cf, ws, cm, ss,
    aging_loop,
    qc, pd, lp, lg, rd
])
A.order.add_edge(ms,  fi)
A.order.add_edge(fi,  mt)
A.order.add_edge(mt,  mp)
A.order.add_edge(mp,  cf)
A.order.add_edge(cf,  ws)
A.order.add_edge(ws,  cm)
A.order.add_edge(cm,  ss)
A.order.add_edge(ss,  aging_loop)
A.order.add_edge(aging_loop, qc)
A.order.add_edge(qc,  pd)
A.order.add_edge(pd,  lp)
A.order.add_edge(lp,  lg)
A.order.add_edge(lg,  rd)

# Feedback subprocess (B)
B = StrictPartialOrder(nodes=[cfb, ma])
B.order.add_edge(cfb, ma)

# Top‐level loop: run A, then optionally run B and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, B]
)