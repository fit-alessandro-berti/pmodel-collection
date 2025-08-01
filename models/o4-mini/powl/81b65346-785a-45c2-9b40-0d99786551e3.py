# Generated from: 81b65346-785a-45c2-9b40-0d99786551e3.json
# Description: This process outlines the comprehensive steps required to establish an urban drone delivery service that integrates regulatory compliance, advanced route optimization, dynamic weather adaptation, and stakeholder coordination. It begins with market analysis and regulatory approval, followed by drone fleet customization and software integration. The process includes real-time data monitoring, emergency protocol design, and customer feedback integration to ensure efficient, safe, and scalable operations within complex urban environments. Continuous improvement cycles based on performance metrics and evolving technology standards complete the framework.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms = Transition(label='Market Survey')
rc = Transition(label='Regulatory Check')
fd = Transition(label='Fleet Design')
rm = Transition(label='Route Mapping')
ss = Transition(label='Software Setup')
pt = Transition(label='Pilot Training')
sa = Transition(label='Safety Audit')
ws = Transition(label='Weather Sync')
tf = Transition(label='Test Flights')
ed = Transition(label='Emergency Drill')
co = Transition(label='Customer Onboard')

# Define the activities for the improvement cycle
dt = Transition(label='Data Tracking')
pr = Transition(label='Performance Review')
tu = Transition(label='Tech Upgrade')
fl = Transition(label='Feedback Loop')
sm = Transition(label='Stakeholder Meet')

# Build the strict partial order for one iteration of the continuous improvement cycle
cycle_body = StrictPartialOrder(nodes=[dt, pr, tu, fl, sm])
cycle_body.order.add_edge(dt, pr)
cycle_body.order.add_edge(pr, tu)
cycle_body.order.add_edge(tu, fl)
cycle_body.order.add_edge(fl, sm)

# Silent transition to enable repetition
skip = SilentTransition()

# Loop operator: repeat the cycle_body until exit
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, skip])

# Top‐level partial order for the main process
root = StrictPartialOrder(nodes=[
    ms, rc, fd, ss, rm, pt, sa, ws, tf, ed, co, loop_cycle
])

# Define the control‐flow dependencies
root.order.add_edge(ms, rc)

# After regulatory check, customize fleet and set up software (in parallel)
root.order.add_edge(rc, fd)
root.order.add_edge(rc, ss)

# Fleet design & software setup complete before mapping, training, audit, weather sync
for prec in [fd, ss]:
    root.order.add_edge(prec, rm)
    root.order.add_edge(prec, pt)
    root.order.add_edge(prec, sa)
    root.order.add_edge(prec, ws)

# Those four preparatory tasks complete before test flights
for prec in [rm, pt, sa, ws]:
    root.order.add_edge(prec, tf)

# Then emergency drill, customer onboard, then enter the continuous improvement loop
root.order.add_edge(tf, ed)
root.order.add_edge(ed, co)
root.order.add_edge(co, loop_cycle)