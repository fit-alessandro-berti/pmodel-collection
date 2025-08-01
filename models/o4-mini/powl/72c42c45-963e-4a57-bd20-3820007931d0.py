# Generated from: 72c42c45-963e-4a57-bd20-3820007931d0.json
# Description: This process outlines the end-to-end workflow for assembling bespoke drones tailored to client specifications. It begins with design consultation and component sourcing, followed by precision machining and custom firmware development. Each drone undergoes iterative calibration and environmental testing to ensure performance under diverse conditions. The process integrates real-time feedback loops between assembly and software teams to address emerging issues. Final steps include packaging with personalized branding and coordinated logistics for delivery, ensuring each unit meets stringent quality and regulatory standards before reaching the customer. This atypical yet practical process combines hardware craft, software innovation, and supply chain agility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cb = Transition(label='Client Brief')
dd = Transition(label='Design Draft')
ps = Transition(label='Part Sourcing')
mp = Transition(label='Machining Parts')
fd = Transition(label='Firmware Dev')
ha = Transition(label='Hardware Assembling')
it = Transition(label='Initial Testing')
cl = Transition(label='Calibration Loop')
et = Transition(label='Enviro Testing')
st = Transition(label='Software Tuning')
qa = Transition(label='Quality Audit')
bp = Transition(label='Brand Packaging')
lp = Transition(label='Logistics Plan')
fr = Transition(label='Final Review')
ch = Transition(label='Customer Handover')

# Loop: iterative calibration and testing with software tuning feedback
cal_env = StrictPartialOrder(nodes=[cl, et])
cal_env.order.add_edge(cl, et)
loop = OperatorPOWL(operator=Operator.LOOP, children=[cal_env, st])

# Build the overall partial order
root = StrictPartialOrder(nodes=[cb, dd, ps, mp, fd, ha, it, loop, qa, bp, lp, fr, ch])
root.order.add_edge(cb, dd)
root.order.add_edge(dd, ps)
root.order.add_edge(dd, fd)
root.order.add_edge(ps, mp)
root.order.add_edge(mp, ha)
root.order.add_edge(fd, ha)
root.order.add_edge(ha, it)
root.order.add_edge(it, loop)
root.order.add_edge(loop, qa)
root.order.add_edge(qa, bp)
root.order.add_edge(bp, lp)
root.order.add_edge(lp, fr)
root.order.add_edge(fr, ch)