# Generated from: 9d6035cc-9b2f-4568-a452-6d8ae5308acd.json
# Description: This process involves leveraging a diverse, global community to generate, refine, and validate innovative product ideas. It starts with idea solicitation from contributors, followed by collaborative filtering, prototyping, and iterative feedback loops. The process integrates automated sentiment analysis and expert reviews to prioritize concepts. Selected ideas undergo rapid development cycles with continuous input from the crowd, culminating in pilot launches and scalability assessments. The approach balances creative freedom with structured evaluation to minimize risks and maximize market fit, creating a dynamic innovation pipeline fueled by collective intelligence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ic = Transition(label='Idea Collection')
cv = Transition(label='Community Voting')
ss = Transition(label='Sentiment Scan')
er = Transition(label='Expert Review')
cf = Transition(label='Concept Filtering')
pl = Transition(label='Pilot Launch')
da = Transition(label='Data Analysis')
st = Transition(label='Scalability Test')
ms = Transition(label='Market Survey')
ra = Transition(label='Risk Assessment')
fs = Transition(label='Final Selection')
ka = Transition(label='Knowledge Archive')

# Define the first iteration of the rapid development cycle
pb1 = Transition(label='Prototype Build')
ci1 = Transition(label='Crowd Incentives')
fl1 = Transition(label='Feedback Loop')
id1 = Transition(label='Iterative Design')
cycle1 = StrictPartialOrder(nodes=[pb1, ci1, fl1, id1])
cycle1.order.add_edge(pb1, ci1)
cycle1.order.add_edge(ci1, fl1)
cycle1.order.add_edge(fl1, id1)

# Define the repeat part of the cycle (identical structure)
pb2 = Transition(label='Prototype Build')
ci2 = Transition(label='Crowd Incentives')
fl2 = Transition(label='Feedback Loop')
id2 = Transition(label='Iterative Design')
cycle2 = StrictPartialOrder(nodes=[pb2, ci2, fl2, id2])
cycle2.order.add_edge(pb2, ci2)
cycle2.order.add_edge(ci2, fl2)
cycle2.order.add_edge(fl2, id2)

# Build the LOOP operator for iterative development
development_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle1, cycle2])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    ic, cv, ss, er, cf,
    development_loop,
    pl, da, st, ms, ra, fs, ka
])

# Define the control-flow edges
root.order.add_edge(ic, cv)
root.order.add_edge(ic, ss)
root.order.add_edge(cv, er)
root.order.add_edge(ss, er)
root.order.add_edge(er, cf)
root.order.add_edge(cf, development_loop)
root.order.add_edge(development_loop, pl)
root.order.add_edge(pl, da)
root.order.add_edge(da, st)
root.order.add_edge(st, ms)
root.order.add_edge(ms, ra)
root.order.add_edge(ra, fs)
root.order.add_edge(fs, ka)