# Generated from: 9b8263b8-d9c8-4927-9f21-f08141872466.json
# Description: This process outlines the intricate steps involved in designing, assembling, and testing custom drones tailored for specialized industrial applications. It begins with client consultation to define unique specifications, followed by modular component selection, precision 3D printing of custom parts, and advanced circuit programming. Subsequent stages include meticulous mechanical assembly, multi-phase calibration, environmental stress testing, and iterative firmware optimization. Final steps involve comprehensive quality assurance, client demonstration, and deployment logistics planning, ensuring each drone meets exacting performance and safety standards in diverse operational environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
cm  = Transition(label="Client Meeting")
sd  = Transition(label="Spec Definition")
ms  = Transition(label="Module Selection")
p3d = Transition(label="3D Printing")
cd  = Transition(label="Circuit Design")
fc  = Transition(label="Firmware Coding")
mb  = Transition(label="Mechanical Build")
cal = Transition(label="Calibration Phase")
st  = Transition(label="Stress Testing")
stn = Transition(label="Software Tuning")
qc  = Transition(label="Quality Check")
dp  = Transition(label="Demo Preparation")
cr  = Transition(label="Client Review")
pkg = Transition(label="Packaging")
dl  = Transition(label="Deployment Plan")

# Build a strict partial order representing the linear process
root = StrictPartialOrder(nodes=[cm, sd, ms, p3d, cd, fc, mb, cal, st, stn, qc, dp, cr, pkg, dl])

# Add the sequential dependencies
root.order.add_edge(cm, sd)
root.order.add_edge(sd, ms)
root.order.add_edge(ms, p3d)
root.order.add_edge(p3d, cd)
root.order.add_edge(cd, fc)
root.order.add_edge(fc, mb)
root.order.add_edge(mb, cal)
root.order.add_edge(cal, st)
root.order.add_edge(st, stn)
root.order.add_edge(stn, qc)
root.order.add_edge(qc, dp)
root.order.add_edge(dp, cr)
root.order.add_edge(cr, pkg)
root.order.add_edge(pkg, dl)