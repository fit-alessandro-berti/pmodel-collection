# Generated from: 494f86f0-9d58-47be-8c81-1b732a55ed84.json
# Description: This process involves integrating unconventional insights from multiple industries to generate breakthrough products or services. It starts by scouting emerging trends across unrelated sectors, followed by collaborative ideation sessions where cross-functional teams reinterpret these insights. Rapid prototyping and iterative testing occur in simulated environments, incorporating real-time data from pilot markets. Feedback loops include external expert evaluations and adaptive refinement of concepts. Final steps encompass strategic alignment with corporate goals and phased market introduction, ensuring scalability and cross-sector adaptability while managing regulatory and cultural nuances effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ts = Transition(label='Trend Scouting')
im = Transition(label='Insight Mapping')
iw = Transition(label='Idea Workshops')
cs = Transition(label='Concept Selection')
pb = Transition(label='Prototype Build')
st = Transition(label='Simulate Testing')
di = Transition(label='Data Integration')
er = Transition(label='Expert Review')
fl = Transition(label='Feedback Loop')
dr = Transition(label='Design Revision')
sa = Transition(label='Strategy Align')
mp = Transition(label='Market Pilot')
sp = Transition(label='Scale Planning')
rc = Transition(label='Regulatory Check')
ca = Transition(label='Cultural Audit')
lp = Transition(label='Launch Prep')

# Build the iterative testing & feedback loop: 
#   * (Simulate Testing, [Data Integration -> Expert Review -> Feedback Loop -> Design Revision])
loop_body = StrictPartialOrder(nodes=[di, er, fl, dr])
loop_body.order.add_edge(di, er)
loop_body.order.add_edge(er, fl)
loop_body.order.add_edge(fl, dr)

loop = OperatorPOWL(operator=Operator.LOOP, children=[st, loop_body])

# Assemble the overall workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[ts, im, iw, cs, pb, loop, sa, mp, sp, rc, ca, lp]
)

# Define the control‐flow dependencies
root.order.add_edge(ts, im)
root.order.add_edge(im, iw)
root.order.add_edge(iw, cs)
root.order.add_edge(cs, pb)
root.order.add_edge(pb, loop)      # enter testing/feedback loop
root.order.add_edge(loop, sa)      # after loop, align strategy
root.order.add_edge(sa, mp)
root.order.add_edge(mp, sp)
root.order.add_edge(sp, rc)
root.order.add_edge(sp, ca)        # regulatory & cultural checks in parallel
root.order.add_edge(rc, lp)
root.order.add_edge(ca, lp)