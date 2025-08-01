# Generated from: 774aa3cf-4e49-48b5-9e6c-477d4e186bd4.json
# Description: This process outlines the complex steps involved in establishing an urban drone delivery network for last-mile logistics. It includes regulatory compliance checks, airspace mapping, drone fleet configuration, dynamic route optimization, real-time weather integration, package security protocols, multi-tiered stakeholder coordination, and continuous system feedback loops to ensure safe, efficient, and scalable drone deliveries within densely populated city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
rr = Transition(label="Regulatory Review")
am = Transition(label="Airspace Mapping")
fs = Transition(label="Fleet Setup")
sm = Transition(label="Stakeholder Meet")
pt = Transition(label="Pilot Training")
rp = Transition(label="Route Planning")
ws = Transition(label="Weather Sync")
sc = Transition(label="Security Check")
pp = Transition(label="Package Prep")
st = Transition(label="System Testing")
lt = Transition(label="Live Tracking")
da = Transition(label="Data Analysis")
ir = Transition(label="Incident Report")
fl = Transition(label="Feedback Loop")
mo = Transition(label="Maintenance Ops")
ca = Transition(label="Compliance Audit")
cs = Transition(label="Capacity Scale")

# Build the feedback-analysis loop
# A = Data Analysis -> Incident Report
analysis_po = StrictPartialOrder(nodes=[da, ir])
analysis_po.order.add_edge(da, ir)
# B = Feedback Loop
# LOOP(children=[A, B]) means: do A, then either exit or do B then A again, repeated
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis_po, fl])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[rr, am, fs, sm, pt, rp, ws, sc, pp, st, lt, feedback_loop, mo, ca, cs]
)

# Regulatory review must complete before mapping, setup, and stakeholder meet
root.order.add_edge(rr, am)
root.order.add_edge(rr, fs)
root.order.add_edge(rr, sm)

# Parallel branches sync into Pilot Training
root.order.add_edge(am, pt)
root.order.add_edge(fs, pt)
root.order.add_edge(sm, pt)

# Core workflow sequence
root.order.add_edge(pt, rp)
root.order.add_edge(rp, ws)
root.order.add_edge(ws, sc)
root.order.add_edge(sc, pp)
root.order.add_edge(pp, st)
root.order.add_edge(st, lt)

# Enter the feedback-analysis loop after going live
root.order.add_edge(lt, feedback_loop)

# After the loop, proceed to maintenance, audit, and scaling
root.order.add_edge(feedback_loop, mo)
root.order.add_edge(mo, ca)
root.order.add_edge(ca, cs)