# Generated from: d6163005-de2c-491a-bd87-954f7acf32bb.json
# Description: This process outlines the detailed steps involved in assembling custom drones tailored to specific client requirements. It begins with requirement analysis followed by component sourcing and quality verification. Next, the frame is constructed and integrated with motors, sensors, and control units. Firmware installation and calibration are performed before conducting multiple flight tests to ensure stability and performance. After successful validation, the drone undergoes final cosmetic finishing and packaging. The process concludes with documentation, client training, and post-delivery support scheduling, ensuring the drone meets operational expectations and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Requirement_Analysis = Transition(label='Requirement Analysis')
Component_Sourcing = Transition(label='Component Sourcing')
Quality_Check = Transition(label='Quality Check')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Sensor_Setup = Transition(label='Sensor Setup')
Control_Unit = Transition(label='Control Unit')
Firmware_Upload = Transition(label='Firmware Upload')
System_Calibration = Transition(label='System Calibration')
Flight_Testing = Transition(label='Flight Testing')
Error_Correction = Transition(label='Error Correction')
Cosmetic_Finish = Transition(label='Cosmetic Finish')
Packaging_Prep = Transition(label='Packaging Prep')
User_Manual = Transition(label='User Manual')
Client_Training = Transition(label='Client Training')
Support_Scheduling = Transition(label='Support Scheduling')

# Compose concurrent motor, sensor, control unit installations after frame assembly
parallel_installations = StrictPartialOrder(nodes=[Motor_Installation, Sensor_Setup, Control_Unit])
# no order edges, so Motor_Installation, Sensor_Setup, Control_Unit are concurrent

# Compose post-flight testing: loop with error correction repeated until exit
loop_flight = OperatorPOWL(operator=Operator.LOOP, children=[Flight_Testing, Error_Correction])

# Compose the sequence before the loop
pre_loop = StrictPartialOrder(nodes=[Requirement_Analysis, Component_Sourcing, Quality_Check, Frame_Assembly, parallel_installations,
                                     Firmware_Upload, System_Calibration])
pre_loop.order.add_edge(Requirement_Analysis, Component_Sourcing)
pre_loop.order.add_edge(Component_Sourcing, Quality_Check)
pre_loop.order.add_edge(Quality_Check, Frame_Assembly)
pre_loop.order.add_edge(Frame_Assembly, parallel_installations)
pre_loop.order.add_edge(parallel_installations, Firmware_Upload)
pre_loop.order.add_edge(Firmware_Upload, System_Calibration)

# Compose the sequence after the loop
post_loop = StrictPartialOrder(nodes=[Cosmetic_Finish, Packaging_Prep, User_Manual, Client_Training, Support_Scheduling])
post_loop.order.add_edge(Cosmetic_Finish, Packaging_Prep)
post_loop.order.add_edge(Packaging_Prep, User_Manual)
post_loop.order.add_edge(User_Manual, Client_Training)
post_loop.order.add_edge(Client_Training, Support_Scheduling)

# Compose overall order with edges pre_loop --> loop_flight --> post_loop
root = StrictPartialOrder(nodes=[pre_loop, loop_flight, post_loop])
root.order.add_edge(pre_loop, loop_flight)
root.order.add_edge(loop_flight, post_loop)