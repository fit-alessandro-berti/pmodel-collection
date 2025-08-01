# Generated from: a1ad6d6c-4a80-4675-b5ab-e17e19cd138e.json
# Description: This process outlines the steps involved in assembling custom drones tailored to unique client specifications. It begins with requirement analysis and component sourcing, followed by precision frame construction and intricate wiring. Firmware installation and sensor calibration are critical to ensure optimal performance. Rigorous flight testing and quality validation precede packaging. The process concludes with detailed client training and support setup to guarantee operational success and customer satisfaction. Each step demands coordination across engineering, logistics, and customer service teams to meet exacting standards within tight timelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
t1  = Transition(label='Req Analysis')
t2  = Transition(label='Part Sourcing')
t3  = Transition(label='Frame Build')
t4  = Transition(label='Wiring Setup')
t5  = Transition(label='Motor Install')
t6  = Transition(label='Propeller Fit')
t7  = Transition(label='Battery Test')
t8  = Transition(label='Firmware Flash')
t9  = Transition(label='Sensor Calibrate')
t10 = Transition(label='Flight Check')
t11 = Transition(label='Quality Audit')
t12 = Transition(label='Package Prep')
t13 = Transition(label='Client Training')
t14 = Transition(label='Support Setup')
t15 = Transition(label='Delivery Coord')

# Create a strict partial order and add the sequence edges
root = StrictPartialOrder(nodes=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15])
edges = [(t1, t2), (t2, t3), (t3, t4), (t4, t5), (t5, t6), (t6, t7),
         (t7, t8), (t8, t9), (t9, t10), (t10, t11), (t11, t12),
         (t12, t13), (t13, t14), (t14, t15)]
for src, tgt in edges:
    root.order.add_edge(src, tgt)