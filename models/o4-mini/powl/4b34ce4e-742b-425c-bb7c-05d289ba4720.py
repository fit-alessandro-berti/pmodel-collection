# Generated from: 4b34ce4e-742b-425c-bb7c-05d289ba4720.json
# Description: This business process manages the end-to-end supply chain activities for a large-scale event involving multiple vendors, fluctuating demand, and last-minute changes. It includes sourcing unique materials, coordinating with international logistics, handling custom regulations, real-time inventory adjustments, and ensuring timely setup on-site. The process must also integrate unexpected disruptions like weather delays or vendor cancellations, requiring dynamic rescheduling and resource reallocation while maintaining cost controls and stakeholder communication throughout the event lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
vs = Transition(label='Vendor Sourcing')
cr = Transition(label='Contract Review')
mo = Transition(label='Material Ordering')
cc = Transition(label='Customs Clearance')
ic = Transition(label='Inventory Check')
df = Transition(label='Demand Forecast')
lp = Transition(label='Logistics Planning')
tb = Transition(label='Transport Booking')
qi = Transition(label='Quality Inspect')
sc = Transition(label='Setup Coordination')
rt = Transition(label='Real-time Tracking')
ra = Transition(label='Risk Assessment')
rs = Transition(label='Reschedule Tasks')
cp = Transition(label='Contingency Plan')
realloc = Transition(label='Resource Allocate')
su = Transition(label='Stakeholder Update')
cm = Transition(label='Cost Monitoring')

# Define the XOR choice for disruption handling
xor_disruption = OperatorPOWL(operator=Operator.XOR, children=[rs, cp])

# Define the body of the monitoring/rescheduling loop
loop_body = StrictPartialOrder(
    nodes=[ra, realloc, xor_disruption, su, cm]
)
loop_body.order.add_edge(ra, realloc)
loop_body.order.add_edge(realloc, xor_disruption)
loop_body.order.add_edge(xor_disruption, su)
loop_body.order.add_edge(su, cm)

# Define the loop: perform real-time tracking, then optionally do the body then track again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[rt, loop_body])

# Assemble the full process in a single partial order
root = StrictPartialOrder(
    nodes=[df, vs, cr, mo, cc, ic, lp, tb, qi, sc, monitor_loop]
)

# Define control-flow dependencies
root.order.add_edge(df, mo)
root.order.add_edge(vs, cr)
root.order.add_edge(cr, mo)
root.order.add_edge(mo, cc)
root.order.add_edge(cc, ic)
root.order.add_edge(ic, lp)
root.order.add_edge(lp, tb)
root.order.add_edge(tb, qi)
root.order.add_edge(qi, sc)
root.order.add_edge(sc, monitor_loop)