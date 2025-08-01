# Generated from: 4506c20e-853f-4be0-ad38-3250b1816977.json
# Description: This process involves the bespoke assembly of drones tailored to unique client specifications. It begins with detailed requirement gathering followed by prototype design and component sourcing from specialized suppliers. Each drone undergoes precision frame construction, intricate wiring, and sensor calibration. Software integration and flight algorithm customization follow, requiring iterative testing and real-time adjustments. Quality assurance includes environmental stress testing and safety certification. The final steps cover packaging, client training, and post-delivery support to ensure optimal drone operation under varied conditions and use cases.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ra = Transition(label='Requirement Analysis')
pd = Transition(label='Prototype Design')
cs = Transition(label='Component Sourcing')
fa = Transition(label='Frame Assembly')
ws = Transition(label='Wiring Setup')
sc = Transition(label='Sensor Calibration')
sl = Transition(label='Software Loading')
at = Transition(label='Algorithm Tuning')
ft = Transition(label='Flight Testing')
st = Transition(label='Stress Testing')
sr = Transition(label='Safety Review')
pp = Transition(label='Packaging Prep')
ct = Transition(label='Client Training')
ds = Transition(label='Delivery Scheduling')
ss = Transition(label='Support Setup')

# Define the iterative testing loop: do Software Loading then (Algorithm Tuning -> Flight Testing) repeat
body = StrictPartialOrder(nodes=[at, ft])
body.order.add_edge(at, ft)
loop = OperatorPOWL(operator=Operator.LOOP, children=[sl, body])

# Assemble the full partial order
root = StrictPartialOrder(
    nodes=[ra, pd, cs, fa, ws, sc, loop, st, sr, pp, ct, ds, ss]
)

# Define the control-flow edges (strict sequence except for the loop)
root.order.add_edge(ra, pd)
root.order.add_edge(pd, cs)
root.order.add_edge(cs, fa)
root.order.add_edge(fa, ws)
root.order.add_edge(ws, sc)
root.order.add_edge(sc, loop)
root.order.add_edge(loop, st)
root.order.add_edge(st, sr)
root.order.add_edge(sr, pp)
root.order.add_edge(pp, ct)
root.order.add_edge(ct, ds)
root.order.add_edge(ds, ss)