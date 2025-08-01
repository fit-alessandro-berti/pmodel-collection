# Generated from: 89c8d38c-bb5b-44bd-9300-57f88e71e9dc.json
# Description: This process involves the design, assembly, testing, and deployment of bespoke drones tailored for unique environmental monitoring tasks. It starts with client consultation to gather specific requirements, followed by component sourcing and integration of advanced sensors. After assembly, drones undergo rigorous flight simulation and real-world testing to ensure reliability under diverse conditions. Post-testing includes software calibration and custom firmware updates. Finally, drones are packaged with operation manuals and shipped alongside remote support setup for client training and maintenance scheduling to guarantee optimal long-term performance and compliance with aviation regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Client_Consult = Transition(label='Client Consult')
Requirement_Gather = Transition(label='Requirement Gather')
Component_Sourcing = Transition(label='Component Sourcing')
Sensor_Integration = Transition(label='Sensor Integration')
Frame_Assembly = Transition(label='Frame Assembly')

Flight_Simulate = Transition(label='Flight Simulate')
Real_Test = Transition(label='Real Test')

Firmware_Upload = Transition(label='Firmware Upload')
Data_Calibration = Transition(label='Data Calibration')
Quality_Inspect = Transition(label='Quality Inspect')

Manual_Draft = Transition(label='Manual Draft')
Packaging_Prep = Transition(label='Packaging Prep')
Shipping_Arrange = Transition(label='Shipping Arrange')

Support_Setup = Transition(label='Support Setup')
Training_Schedule = Transition(label='Training Schedule')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Construct partial order for initial design & assembly phase
design_assembly = StrictPartialOrder(nodes=[Client_Consult, Requirement_Gather, Component_Sourcing, Sensor_Integration, Frame_Assembly])
design_assembly.order.add_edge(Client_Consult, Requirement_Gather)
design_assembly.order.add_edge(Requirement_Gather, Component_Sourcing)
design_assembly.order.add_edge(Component_Sourcing, Sensor_Integration)
design_assembly.order.add_edge(Sensor_Integration, Frame_Assembly)

# Construct partial order for testing phase (flight simulation then real test)
testing = StrictPartialOrder(nodes=[Flight_Simulate, Real_Test])
testing.order.add_edge(Flight_Simulate, Real_Test)

# Construct partial order for post-testing calibration & inspection
post_testing = StrictPartialOrder(nodes=[Firmware_Upload, Data_Calibration, Quality_Inspect])
post_testing.order.add_edge(Firmware_Upload, Data_Calibration)
post_testing.order.add_edge(Data_Calibration, Quality_Inspect)

# Construct partial order for packaging & shipping phase
pack_ship = StrictPartialOrder(nodes=[Manual_Draft, Packaging_Prep, Shipping_Arrange])
pack_ship.order.add_edge(Manual_Draft, Packaging_Prep)
pack_ship.order.add_edge(Packaging_Prep, Shipping_Arrange)

# Construct partial order for support & training phase
support_training = StrictPartialOrder(nodes=[Support_Setup, Training_Schedule, Maintenance_Plan])
support_training.order.add_edge(Support_Setup, Training_Schedule)
support_training.order.add_edge(Training_Schedule, Maintenance_Plan)

# Compose the overall process partial order: these phases are sequential:
# design_assembly -> testing -> post_testing -> pack_ship -> support_training
root = StrictPartialOrder(nodes=[design_assembly, testing, post_testing, pack_ship, support_training])
root.order.add_edge(design_assembly, testing)
root.order.add_edge(testing, post_testing)
root.order.add_edge(post_testing, pack_ship)
root.order.add_edge(pack_ship, support_training)