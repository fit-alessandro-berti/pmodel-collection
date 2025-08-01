# Generated from: 527e357b-8769-4cdf-8ecb-a7b53bc323a0.json
# Description: This process involves the bespoke assembly of custom drones tailored to unique client specifications. It begins with requirement gathering and component sourcing, followed by precise frame construction. The next steps include sensor calibration, software integration, and quality assurance testing. Specialized activities such as aerodynamic tuning, battery optimization, and secure communication setup ensure superior performance. Final stages involve pilot training, deployment planning, and ongoing maintenance scheduling. The process requires interdisciplinary coordination between engineering, software development, and customer support teams to deliver fully functional, customized drone solutions efficiently and reliably.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
cb = Transition(label="Client Brief")
ps = Transition(label="Part Sourcing")
fb = Transition(label="Frame Build")
ss = Transition(label="Sensor Setup")
sl = Transition(label="Software Load")
ct = Transition(label="Calibration Test")
qa = Transition(label="Quality Audit")
at = Transition(label="Aerodynamic Tune")
bc = Transition(label="Battery Check")
cs = Transition(label="Comm Setup")
ft = Transition(label="Flight Trial")
pt = Transition(label="Pilot Train")
dp = Transition(label="Deploy Plan")
ml = Transition(label="Maintenance Log")
fr = Transition(label="Feedback Review")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    cb, ps, fb,
    ss, sl, ct,
    qa, at, bc, cs,
    ft, pt, dp, ml, fr
])

# Define the control‐flow dependencies
root.order.add_edge(cb, ps)
root.order.add_edge(ps, fb)

# After frame build, sensor setup and software load can proceed in parallel
root.order.add_edge(fb, ss)
root.order.add_edge(fb, sl)

# Both setup tasks feed into the calibration test
root.order.add_edge(ss, ct)
root.order.add_edge(sl, ct)

# Calibration leads to quality audit
root.order.add_edge(ct, qa)

# After audit, the three specialized tuning steps can run in parallel
root.order.add_edge(qa, at)
root.order.add_edge(qa, bc)
root.order.add_edge(qa, cs)

# All three tuning steps precede the flight trial
root.order.add_edge(at, ft)
root.order.add_edge(bc, ft)
root.order.add_edge(cs, ft)

# After a successful trial, the final four activities can occur (in parallel)
root.order.add_edge(ft, pt)
root.order.add_edge(ft, dp)
root.order.add_edge(ft, ml)
root.order.add_edge(ft, fr)