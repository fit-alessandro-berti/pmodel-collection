# Generated from: 34ecacb5-56de-4a06-8f05-bbd7c9b4ec81.json
# Description: This process details the end-to-end assembly and deployment of custom drones tailored for specialized environmental monitoring. It begins with client consultation to specify unique sensor and flight requirements, followed by component sourcing from niche suppliers. The assembly phase involves precision integration of avionics, sensors, and bespoke software modules. Rigorous multi-stage testing ensures operational reliability under diverse environmental conditions. Subsequent calibration aligns sensor outputs with client specifications. Finally, the process concludes with drone packaging, pilot training sessions, and remote deployment planning, ensuring seamless field operation and data acquisition for research or industrial applications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
sf = Transition(label='Specs Finalize')
cs = Transition(label='Component Sourcing')
fa = Transition(label='Frame Assembly')
ai = Transition(label='Avionics Install')
sm = Transition(label='Sensor Mounting')
su = Transition(label='Software Upload')
it = Transition(label='Initial Testing')
et = Transition(label='Environmental Test')
dv = Transition(label='Data Validation')
fc = Transition(label='Flight Calibration')
pp = Transition(label='Packaging Prep')
pt = Transition(label='Pilot Training')
dp = Transition(label='Deployment Plan')
fs = Transition(label='Field Support')

# Create the partial order model
root = StrictPartialOrder(nodes=[
    cc, sf, cs, fa,
    ai, sm, su,
    it, et, dv, fc,
    pp, pt, dp, fs
])

# Client consult -> finalize specs -> sourcing -> frame assembly
root.order.add_edge(cc, sf)
root.order.add_edge(sf, cs)
root.order.add_edge(cs, fa)

# Parallel assembly tasks after frame assembly
for node in [ai, sm, su]:
    root.order.add_edge(fa, node)

# Testing phase after assembly tasks
for node in [ai, sm, su]:
    root.order.add_edge(node, it)

# Multi-stage testing: initial -> environmental -> data validation
root.order.add_edge(it, et)
root.order.add_edge(et, dv)

# Calibration after testing
root.order.add_edge(dv, fc)

# Final activities in parallel: packaging, training, deployment planning
for node in [pp, pt, dp]:
    root.order.add_edge(fc, node)

# Field support starts after all final activities
for node in [pp, pt, dp]:
    root.order.add_edge(node, fs)