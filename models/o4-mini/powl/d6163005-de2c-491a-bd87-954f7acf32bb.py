# Generated from: d6163005-de2c-491a-bd87-954f7acf32bb.json
# Description: This process outlines the detailed steps involved in assembling custom drones tailored to specific client requirements. It begins with requirement analysis followed by component sourcing and quality verification. Next, the frame is constructed and integrated with motors, sensors, and control units. Firmware installation and calibration are performed before conducting multiple flight tests to ensure stability and performance. After successful validation, the drone undergoes final cosmetic finishing and packaging. The process concludes with documentation, client training, and post-delivery support scheduling, ensuring the drone meets operational expectations and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_req = Transition(label='Requirement Analysis')
t_comp = Transition(label='Component Sourcing')
t_qc = Transition(label='Quality Check')
t_fa = Transition(label='Frame Assembly')
t_mi = Transition(label='Motor Installation')
t_ss = Transition(label='Sensor Setup')
t_cu = Transition(label='Control Unit')
t_fu = Transition(label='Firmware Upload')
t_cal = Transition(label='System Calibration')
t_ft = Transition(label='Flight Testing')
t_ec = Transition(label='Error Correction')
t_cf = Transition(label='Cosmetic Finish')
t_pp = Transition(label='Packaging Prep')
t_um = Transition(label='User Manual')
t_ct = Transition(label='Client Training')
t_ssched = Transition(label='Support Scheduling')

# Loop for repeated flight testing and error correction
loop_ft = OperatorPOWL(operator=Operator.LOOP, children=[t_ft, t_ec])

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_req, t_comp, t_qc, t_fa, t_mi, t_ss, t_cu,
    t_fu, t_cal, loop_ft, t_cf, t_pp, t_um, t_ct, t_ssched
])

# Define the control-flow/order edges
root.order.add_edge(t_req, t_comp)
root.order.add_edge(t_comp, t_qc)
root.order.add_edge(t_qc, t_fa)
root.order.add_edge(t_fa, t_mi)
root.order.add_edge(t_mi, t_ss)
root.order.add_edge(t_ss, t_cu)
root.order.add_edge(t_cu, t_fu)
root.order.add_edge(t_fu, t_cal)
root.order.add_edge(t_cal, loop_ft)
root.order.add_edge(loop_ft, t_cf)
root.order.add_edge(t_cf, t_pp)
root.order.add_edge(t_pp, t_um)
root.order.add_edge(t_um, t_ct)
root.order.add_edge(t_ct, t_ssched)