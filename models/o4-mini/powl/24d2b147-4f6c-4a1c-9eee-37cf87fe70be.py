# Generated from: 24d2b147-4f6c-4a1c-9eee-37cf87fe70be.json
# Description: This process outlines the comprehensive steps involved in assembling custom drones tailored to specific client requirements. It begins with component sourcing based on specialized criteria, followed by firmware customization to match unique operational parameters. Quality assurance includes both automated and manual inspections to ensure compliance with safety and performance standards. The assembly incorporates modular parts to allow for future upgrades. After initial assembly, drones undergo environmental stress testing simulating various weather conditions. Post-testing, final calibration adjusts sensors and flight controls. Documentation is generated for maintenance and client training. The process concludes with packaging optimized for fragile electronics and coordinating logistics with specialized carriers to ensure secure delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
cs = Transition(label='Component Sourcing')
fs = Transition(label='Firmware Setup')
pt = Transition(label='Preliminary Testing')
qa = Transition(label='Quality Audit')
ma = Transition(label='Module Assembly')
st = Transition(label='Stress Testing')
ca = Transition(label='Calibration Adjust')
sc = Transition(label='Sensor Check')
fc = Transition(label='Flight Control')
doc = Transition(label='Documentation')
cr = Transition(label='Client Review')
pp = Transition(label='Packaging Prep')
lp = Transition(label='Logistics Plan')
sa = Transition(label='Shipping Arrange')
as_ = Transition(label='After-Sales Support')

# Build the partial order
root = StrictPartialOrder(nodes=[
    cs, fs, pt, qa, ma, st, ca, sc, fc, doc, cr, pp, lp, sa, as_
])

# Define control-flow relations
root.order.add_edge(cs, fs)
root.order.add_edge(fs, pt)
root.order.add_edge(fs, qa)
root.order.add_edge(pt, ma)
root.order.add_edge(qa, ma)
root.order.add_edge(ma, st)
root.order.add_edge(st, ca)
root.order.add_edge(ca, sc)
root.order.add_edge(ca, fc)
root.order.add_edge(sc, doc)
root.order.add_edge(fc, doc)
root.order.add_edge(doc, cr)
root.order.add_edge(cr, pp)
root.order.add_edge(pp, lp)
root.order.add_edge(lp, sa)
root.order.add_edge(sa, as_)