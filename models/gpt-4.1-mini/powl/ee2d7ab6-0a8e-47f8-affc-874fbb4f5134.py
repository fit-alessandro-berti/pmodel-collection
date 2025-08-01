# Generated from: ee2d7ab6-0a8e-47f8-affc-874fbb4f5134.json
# Description: This process involves the end-to-end creation of custom drones tailored to specific client requirements. It starts with client consultation to gather bespoke specifications, followed by component sourcing from specialized suppliers. Engineering teams then validate design feasibility and perform simulations before prototype assembly. Quality inspections ensure compliance with safety standards. Firmware customization and integration of unique sensors are conducted prior to final testing in controlled environments. Packaging includes personalized branding and documentation. Finally, logistics coordinate delivery and post-sale support initiates with client training and remote diagnostics setup to guarantee operational success and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Client_Consult = Transition(label='Client Consult')
Spec_Gathering = Transition(label='Spec Gathering')
Supplier_Sourcing = Transition(label='Supplier Sourcing')
Design_Review = Transition(label='Design Review')
Simulation_Test = Transition(label='Simulation Test')
Proto_Assembly = Transition(label='Proto Assembly')
Quality_Check = Transition(label='Quality Check')
Firmware_Flash = Transition(label='Firmware Flash')
Sensor_Install = Transition(label='Sensor Install')
Final_Testing = Transition(label='Final Testing')
Brand_Packaging = Transition(label='Brand Packaging')
Shipping_Prep = Transition(label='Shipping Prep')
Delivery_Schedule = Transition(label='Delivery Schedule')
Client_Training = Transition(label='Client Training')
Diagnostics_Setup = Transition(label='Diagnostics Setup')

# Construct the sequence inside engineering teams validation: Design Review then Simulation Test
engineering_validation = StrictPartialOrder(
    nodes=[Design_Review, Simulation_Test]
)
engineering_validation.order.add_edge(Design_Review, Simulation_Test)

# Construct firmware and sensors integration partial order, they are done before Final Testing but can be concurrent
firmware_sensor = StrictPartialOrder(
    nodes=[Firmware_Flash, Sensor_Install]
)
# no order edges: concurrent

# Construct packaging partial order: Brand Packaging then Shipping Prep
packaging = StrictPartialOrder(
    nodes=[Brand_Packaging, Shipping_Prep]
)
packaging.order.add_edge(Brand_Packaging, Shipping_Prep)

# Construct post-sale support partial order: Client Training then Diagnostics Setup
post_sale_support = StrictPartialOrder(
    nodes=[Client_Training, Diagnostics_Setup]
)
post_sale_support.order.add_edge(Client_Training, Diagnostics_Setup)

# Assemble the main workflow partial order with the dependencies:
# Client Consult --> Spec Gathering --> Supplier Sourcing
# Supplier Sourcing --> engineering_validation (Design Review -> Simulation Test)
# engineering_validation --> Proto Assembly
# Proto Assembly --> Quality Check
# Quality Check --> firmware_sensor (Firmware Flash & Sensor Install concurrent)
# firmware_sensor --> Final Testing
# Final Testing --> packaging (Brand Packaging -> Shipping Prep)
# packaging --> Delivery Schedule
# Delivery Schedule --> post_sale_support (Client Training -> Diagnostics Setup)

root = StrictPartialOrder(
    nodes=[
        Client_Consult, Spec_Gathering, Supplier_Sourcing,
        engineering_validation, Proto_Assembly, Quality_Check,
        firmware_sensor, Final_Testing, packaging,
        Delivery_Schedule, post_sale_support
    ]
)

# Add edges for the total order and precedence according to description
root.order.add_edge(Client_Consult, Spec_Gathering)
root.order.add_edge(Spec_Gathering, Supplier_Sourcing)
root.order.add_edge(Supplier_Sourcing, engineering_validation)
root.order.add_edge(engineering_validation, Proto_Assembly)
root.order.add_edge(Proto_Assembly, Quality_Check)
root.order.add_edge(Quality_Check, firmware_sensor)
root.order.add_edge(firmware_sensor, Final_Testing)
root.order.add_edge(Final_Testing, packaging)
root.order.add_edge(packaging, Delivery_Schedule)
root.order.add_edge(Delivery_Schedule, post_sale_support)