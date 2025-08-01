# Generated from: 4ad59123-736d-4d4d-8a1c-b472e119b654.json
# Description: This process involves the bespoke assembly of drones tailored to individual client specifications. It begins with requirement analysis, followed by component sourcing from multiple suppliers with varying lead times. Custom firmware is developed in parallel while mechanical assembly and initial calibration occur. Rigorous multi-environment testing is conducted, including wind tunnel and obstacle navigation simulations. After successful testing, final quality assurance and packaging are performed before shipment scheduling and delivery confirmation. Post-delivery, remote diagnostics and software updates are managed to ensure optimal performance and client satisfaction throughout the drone's operational lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Intake = Transition(label='Client Intake')
Specs_Review = Transition(label='Specs Review')
Component_Order = Transition(label='Component Order')
Firmware_Dev = Transition(label='Firmware Dev')
Chassis_Build = Transition(label='Chassis Build')
Motor_Install = Transition(label='Motor Install')
Sensor_Align = Transition(label='Sensor Align')
Initial_Calib = Transition(label='Initial Calib')
Wind_Test = Transition(label='Wind Test')
Nav_Sim = Transition(label='Nav Sim')
Quality_Check = Transition(label='Quality Check')
Final_Assembly = Transition(label='Final Assembly')
Packaging_Prep = Transition(label='Packaging Prep')
Ship_Schedule = Transition(label='Ship Schedule')
Delivery_Confirm = Transition(label='Delivery Confirm')
Remote_Support = Transition(label='Remote Support')

# Component sourcing partial order (concurrent suppliers):
# Component_Order may reflect multiple suppliers with varying lead times, we model as a single activity here.

# Mechanical assembly and initial calibration happen concurrently with firmware development
# Mechanical assembly = Chassis_Build -> Motor_Install -> Sensor_Align -> Initial_Calib (sequential)
Mechanical_Assembly = StrictPartialOrder(nodes=[Chassis_Build, Motor_Install, Sensor_Align, Initial_Calib])
Mechanical_Assembly.order.add_edge(Chassis_Build, Motor_Install)
Mechanical_Assembly.order.add_edge(Motor_Install, Sensor_Align)
Mechanical_Assembly.order.add_edge(Sensor_Align, Initial_Calib)

# Firmware development is concurrent with mechanical assembly and initial calibration
Firmware_and_Mech_Assembly = StrictPartialOrder(nodes=[Firmware_Dev, Mechanical_Assembly])
# No order edges -> concurrency

# Testing consists of Wind_Test and Nav_Sim and are concurrent
Testing = StrictPartialOrder(nodes=[Wind_Test, Nav_Sim])
# No edges -> concurrency

# After testing, do Quality Check -> Final Assembly -> Packaging Prep
Post_Test = StrictPartialOrder(
    nodes=[Quality_Check, Final_Assembly, Packaging_Prep])
Post_Test.order.add_edge(Quality_Check, Final_Assembly)
Post_Test.order.add_edge(Final_Assembly, Packaging_Prep)

# After Packaging_Prep, Ship_Schedule then Delivery_Confirm
Shipping = StrictPartialOrder(nodes=[Ship_Schedule, Delivery_Confirm])
Shipping.order.add_edge(Ship_Schedule, Delivery_Confirm)

# After delivery, Remote Support runs (can be concurrent or after Delivery Confirm)
# Model as sequential for clarity: Delivery_Confirm -> Remote_Support
After_Delivery = StrictPartialOrder(nodes=[Delivery_Confirm, Remote_Support])
After_Delivery.order.add_edge(Delivery_Confirm, Remote_Support)

# Construct the main partial order

# First, Client Intake -> Specs Review -> Component Order
# Then Component_Order concurrent with Firmware_and_Mech_Assembly
# Firmware_and_Mech_Assembly -> Testing -> Post_Test -> Shipping -> Remote_Support

# We embed Firmware_and_Mech_Assembly as nodes:
# it contains Firmware_Dev and Mechanical_Assembly (which itself is a PO)
# so nodes include the nested POs accordingly.

# Compose main process nodes:
root_nodes = [
    Client_Intake,
    Specs_Review,
    Component_Order,
    Firmware_and_Mech_Assembly,
    Testing,
    Post_Test,
    Shipping,
    Remote_Support
]

root = StrictPartialOrder(nodes=root_nodes)

# Define order relations:
root.order.add_edge(Client_Intake, Specs_Review)
root.order.add_edge(Specs_Review, Component_Order)

# Component_Order concurrent with Firmware_and_Mech_Assembly
# So no edge between them

root.order.add_edge(Component_Order, Testing)
root.order.add_edge(Firmware_and_Mech_Assembly, Testing)

root.order.add_edge(Testing, Post_Test)
root.order.add_edge(Post_Test, Shipping)
root.order.add_edge(Shipping, Remote_Support)