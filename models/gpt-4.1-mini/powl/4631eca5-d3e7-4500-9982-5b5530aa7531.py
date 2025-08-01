# Generated from: 4631eca5-d3e7-4500-9982-5b5530aa7531.json
# Description: This process involves the custom assembly of drones tailored to individual client specifications. It starts with detailed requirement gathering and design adaptation, followed by component sourcing from multiple suppliers, quality verification, and firmware customization. The assembly line incorporates manual and automated steps ensuring precision fitting of sensors, motors, and batteries. Post assembly, each drone undergoes rigorous flight testing in various conditions, calibration of navigation systems, and software integration. Final packaging includes client-specific documentation and configuration files. The entire process requires iterative feedback loops between design and production teams to accommodate rapid changes and ensure compliance with aviation regulations before shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
Req_Gathering = Transition(label='Req Gathering')
Design_Adapt = Transition(label='Design Adapt')

Supplier_Vetting = Transition(label='Supplier Vetting')
Component_Order = Transition(label='Component Order')

Quality_Check = Transition(label='Quality Check')
Firmware_Load = Transition(label='Firmware Load')

Sensor_Fit = Transition(label='Sensor Fit')
Motor_Install = Transition(label='Motor Install')
Battery_Mount = Transition(label='Battery Mount')

Assembly_Test = Transition(label='Assembly Test')

Flight_Trial = Transition(label='Flight Trial')
Nav_Calibrate = Transition(label='Nav Calibrate')
Software_Sync = Transition(label='Software Sync')

Doc_Prepare = Transition(label='Doc Prepare')
Client_Review = Transition(label='Client Review')

Final_Package = Transition(label='Final Package')
Compliance_Audit = Transition(label='Compliance Audit')

# Define loop condition: iterative feedback loops between design and production teams
# Loop: after Compliance Audit, possibly go back to Design Adapt
# Loop structure: LOOP(Req_Gathering + Design_Adapt + ... + Compliance_Audit, Feedback)
# We model the body as partial order of all activities and the feedback as a silent transition that "loops" back

# Build initial PO for requirement gathering and design adaptation
req_design_po = StrictPartialOrder(nodes=[Req_Gathering, Design_Adapt])
req_design_po.order.add_edge(Req_Gathering, Design_Adapt)

# Build PO for sourcing components
sourcing_po = StrictPartialOrder(nodes=[Supplier_Vetting, Component_Order])
sourcing_po.order.add_edge(Supplier_Vetting, Component_Order)

# Quality check and firmware load can be done in parallel after component order
quality_firmware_po = StrictPartialOrder(nodes=[Quality_Check, Firmware_Load])
# No order edge between them -> concurrent

# Manual and automated assembly steps to fit sensors, motors, batteries in sequence
assembly_po = StrictPartialOrder(
    nodes=[Sensor_Fit, Motor_Install, Battery_Mount]
)
assembly_po.order.add_edge(Sensor_Fit, Motor_Install)
assembly_po.order.add_edge(Motor_Install, Battery_Mount)

# Assembly test after assembly
assembly_test_po = StrictPartialOrder(nodes=[Assembly_Test])
# Will connect after assembly PO

# Post assembly testing - Flight Trial, Nav Calibrate, Software Sync in sequence
post_assembly_po = StrictPartialOrder(
    nodes=[Flight_Trial, Nav_Calibrate, Software_Sync]
)
post_assembly_po.order.add_edge(Flight_Trial, Nav_Calibrate)
post_assembly_po.order.add_edge(Nav_Calibrate, Software_Sync)

# Documentation preparation and client review in sequence
doc_client_po = StrictPartialOrder(nodes=[Doc_Prepare, Client_Review])
doc_client_po.order.add_edge(Doc_Prepare, Client_Review)

# Final package and compliance audit in sequence
final_compliance_po = StrictPartialOrder(nodes=[Final_Package, Compliance_Audit])
final_compliance_po.order.add_edge(Final_Package, Compliance_Audit)

# Construct main linear flow for the loop body as partial order combining above steps with order edges

# Gather all nodes
body_nodes = [
    req_design_po, 
    sourcing_po, 
    quality_firmware_po, 
    assembly_po, 
    assembly_test_po,
    post_assembly_po,
    doc_client_po,
    final_compliance_po
]

# To flatten the partial orders, treat them as nodes in a PO and order them accordingly
# Define a PO where each sub-PO is a "node", then flatten nodes

body_po = StrictPartialOrder(nodes=[])
# Add all individual activities as nodes:
# We'll need all individual activities to be nodes of the final PO
# So merging all activities in order with edges per the process

# Collect all activities
all_activities = [
    Req_Gathering, Design_Adapt,
    Supplier_Vetting, Component_Order,
    Quality_Check, Firmware_Load,
    Sensor_Fit, Motor_Install, Battery_Mount,
    Assembly_Test,
    Flight_Trial, Nav_Calibrate, Software_Sync,
    Doc_Prepare, Client_Review,
    Final_Package, Compliance_Audit
]
body_po = StrictPartialOrder(nodes=all_activities)

# Now define the edges to respect process order and concurrency

# Req Gathering --> Design Adapt
body_po.order.add_edge(Req_Gathering, Design_Adapt)

# Design Adapt --> Supplier Vetting and Component Order (supplier vetting first)
body_po.order.add_edge(Design_Adapt, Supplier_Vetting)
body_po.order.add_edge(Supplier_Vetting, Component_Order)

# Component Order --> Quality Check and Firmware Load (concurrent)
body_po.order.add_edge(Component_Order, Quality_Check)
body_po.order.add_edge(Component_Order, Firmware_Load)

# Quality Check and Firmware Load can be concurrent, no edge between them

# Quality Check and Firmware Load --> Sensor Fit (assembly start)
body_po.order.add_edge(Quality_Check, Sensor_Fit)
body_po.order.add_edge(Firmware_Load, Sensor_Fit)

# Assembly steps sequential: Sensor Fit --> Motor Install --> Battery Mount
body_po.order.add_edge(Sensor_Fit, Motor_Install)
body_po.order.add_edge(Motor_Install, Battery_Mount)

# Battery Mount --> Assembly Test
body_po.order.add_edge(Battery_Mount, Assembly_Test)

# Assembly Test --> Flight Trial
body_po.order.add_edge(Assembly_Test, Flight_Trial)

# Flight Trial --> Nav Calibrate --> Software Sync
body_po.order.add_edge(Flight_Trial, Nav_Calibrate)
body_po.order.add_edge(Nav_Calibrate, Software_Sync)

# Software Sync --> Doc Prepare
body_po.order.add_edge(Software_Sync, Doc_Prepare)

# Doc Prepare --> Client Review
body_po.order.add_edge(Doc_Prepare, Client_Review)

# Client Review --> Final Package
body_po.order.add_edge(Client_Review, Final_Package)

# Final Package --> Compliance Audit
body_po.order.add_edge(Final_Package, Compliance_Audit)

# Loop (iterative feedback) from Compliance Audit back to Design Adapt
# The LOOP construct is LOOP(body, feedback)
# feedback is typically a silent transition here to represent the choice to repeat or exit

feedback = SilentTransition()

root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        body_po,
        feedback,
    ]
)

# Connect edges required for the LOOP semantics:
# LOOP expects children[0] (body) and children[1] (feedback)
# The LOOP semantics executes body first, then either exits or executes feedback then body again.

# The above POWL instantiation completes the model.