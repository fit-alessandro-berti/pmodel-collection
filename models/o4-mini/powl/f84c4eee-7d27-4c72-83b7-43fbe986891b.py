# Generated from: f84c4eee-7d27-4c72-83b7-43fbe986891b.json
# Description: This process involves the end-to-end assembly and calibration of highly customized drones tailored to specific client requirements. It begins with component sourcing, followed by frame assembly, electronics integration, and software loading. Quality assurance includes multiple test flights under varied conditions. Specialized calibration ensures optimal sensor accuracy and flight stability. Final packaging is designed to accommodate delicate parts and personalized documentation, while post-delivery support schedules remote diagnostics and firmware updates to maintain peak performance throughout the drone’s lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Component Sourcing')
fa = Transition(label='Frame Assembly')
sm = Transition(label='Sensor Mounting')
wh = Transition(label='Wiring Harness')
ct = Transition(label='Circuit Testing')
fl = Transition(label='Firmware Loading')
si = Transition(label='Software Integration')
ic = Transition(label='Initial Calibration')
ft = Transition(label='Flight Testing')
dl = Transition(label='Data Logging')
pt = Transition(label='Performance Tuning')
pp = Transition(label='Packaging Prep')
cl = Transition(label='Custom Labeling')
dp = Transition(label='Documentation Print')
qr = Transition(label='Quality Review')
ctn = Transition(label='Client Training')
rm = Transition(label='Remote Monitoring')
fu = Transition(label='Firmware Update')

# Electronics integration happens in parallel
elec = StrictPartialOrder(nodes=[sm, wh])
# Testing & logging in sequence, then loop with performance tuning
test_pair = StrictPartialOrder(nodes=[ft, dl])
test_pair.order.add_edge(ft, dl)
loop_tests = OperatorPOWL(operator=Operator.LOOP, children=[test_pair, pt])

# Packaging: prep, then labeling & docs in parallel
pack = StrictPartialOrder(nodes=[pp, cl, dp])
pack.order.add_edge(pp, cl)
pack.order.add_edge(pp, dp)

# Post-delivery support: training then monitoring & firmware update in parallel
support = StrictPartialOrder(nodes=[ctn, rm, fu])
support.order.add_edge(ctn, rm)
support.order.add_edge(ctn, fu)

# Assemble the overall process as a partial order
root = StrictPartialOrder(
    nodes=[
        cs, fa, elec, ct, fl, si, ic,
        loop_tests, pack, qr, support
    ]
)
root.order.add_edge(cs, fa)
root.order.add_edge(fa, elec)
root.order.add_edge(elec, ct)
root.order.add_edge(ct, fl)
root.order.add_edge(fl, si)
root.order.add_edge(si, ic)
root.order.add_edge(ic, loop_tests)
root.order.add_edge(loop_tests, pack)
root.order.add_edge(pack, qr)
root.order.add_edge(qr, support)