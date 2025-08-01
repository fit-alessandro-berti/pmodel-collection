# Generated from: fbdab04b-652a-43d2-9acb-1d7ae26aa97f.json
# Description: This process involves the bespoke assembly of drones tailored to individual client specifications that vary greatly in design, purpose, and technology integration. It starts with detailed client consultation to capture unique requirements, followed by modular component selection from diverse suppliers. The assembly phase incorporates precision calibration of sensors, motors, and software systems, ensuring seamless integration of hardware and AI-driven flight control. Throughout, stringent quality checks and iterative testing validate performance under simulated environments. Finally, the process includes personalized user training and remote monitoring setup, providing ongoing support for operational optimization and rapid troubleshooting post-deployment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
sa = Transition(label='Spec Analysis')
ms = Transition(label='Module Select')
co = Transition(label='Component Order')
pi = Transition(label='Parts Inspect')
fa = Transition(label='Frame Assemble')
si = Transition(label='Sensor Install')
ma = Transition(label='Motor Attach')
wc = Transition(label='Wiring Connect')
su = Transition(label='Software Upload')
ct = Transition(label='Calibration Test')
fs = Transition(label='Flight Simulate')
qr = Transition(label='Quality Review')
ut = Transition(label='User Train')
rs = Transition(label='Remote Setup')
fc = Transition(label='Feedback Collect')
ss = Transition(label='Support Schedule')

# Iterative testing loop: calibration and flight simulation
testPO = StrictPartialOrder(nodes=[ct, fs])
testPO.order.add_edge(ct, fs)
loop = OperatorPOWL(operator=Operator.LOOP, children=[testPO, testPO])

# Build the main partial order
root = StrictPartialOrder(nodes=[cc, sa, ms, co, pi, fa,
                                 si, ma, wc, su,
                                 loop, qr, ut, rs, fc, ss])

# Define control-flow order
root.order.add_edge(cc, sa)
root.order.add_edge(sa, ms)
root.order.add_edge(ms, co)
root.order.add_edge(co, pi)
root.order.add_edge(pi, fa)

# After frame assembly: concurrent hardware/software integration
root.order.add_edge(fa, si)
root.order.add_edge(fa, ma)
root.order.add_edge(fa, wc)
root.order.add_edge(fa, su)

# After integration: enter iterative testing loop
root.order.add_edge(si, loop)
root.order.add_edge(ma, loop)
root.order.add_edge(wc, loop)
root.order.add_edge(su, loop)

# After loop: quality review
root.order.add_edge(loop, qr)

# After review: user training and remote setup in parallel
root.order.add_edge(qr, ut)
root.order.add_edge(qr, rs)

# After both: feedback collection
root.order.add_edge(ut, fc)
root.order.add_edge(rs, fc)

# Final support scheduling
root.order.add_edge(fc, ss)