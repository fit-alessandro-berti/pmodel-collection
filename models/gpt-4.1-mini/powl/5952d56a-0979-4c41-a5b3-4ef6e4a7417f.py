# Generated from: 5952d56a-0979-4c41-a5b3-4ef6e4a7417f.json
# Description: This process outlines the end-to-end production of custom drones tailored for specialized industrial applications. It begins with client consultation to gather detailed requirements, followed by design customization using advanced CAD tools. The production phase involves precision component fabrication, including 3D printing of unique parts and selective material treatments. Assembly is conducted in a controlled environment to ensure optimal integration of electronics and mechanical systems. Quality assurance includes rigorous flight testing and software calibration. Finally, the process concludes with packaging, client training, and post-delivery support to ensure operational success and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Client_Brief = Transition(label='Client Brief')
Design_Draft = Transition(label='Design Draft')
Material_Sourcing = Transition(label='Material Sourcing')
Part_Fabrication = Transition(label='Part Fabrication')
D_Printing = Transition(label='3D Printing')
Surface_Treat = Transition(label='Surface Treat')
Component_Test = Transition(label='Component Test')
System_Assembly = Transition(label='System Assembly')
Firmware_Load = Transition(label='Firmware Load')
Calibration_Setup = Transition(label='Calibration Setup')
Flight_Testing = Transition(label='Flight Testing')
Quality_Review = Transition(label='Quality Review')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Delivery_Setup = Transition(label='Delivery Setup')
Support_Launch = Transition(label='Support Launch')

# Production phase partial order:
# Material Sourcing precedes 3D Printing and Surface Treat
# 3D Printing and Surface Treat are concurrent
# Both precede Part Fabrication (assumed Part Fabrication includes general fabrication steps)
fabrication_PO = StrictPartialOrder(nodes=[Material_Sourcing, D_Printing, Surface_Treat, Part_Fabrication])
fabrication_PO.order.add_edge(Material_Sourcing, D_Printing)
fabrication_PO.order.add_edge(Material_Sourcing, Surface_Treat)
fabrication_PO.order.add_edge(D_Printing, Part_Fabrication)
fabrication_PO.order.add_edge(Surface_Treat, Part_Fabrication)

# Assembly phase concurrency:
# Component Test precedes System Assembly and Firmware Load, which are concurrent
# Both System Assembly and Firmware Load precede Calibration Setup
assembly_PO = StrictPartialOrder(nodes=[Component_Test, System_Assembly, Firmware_Load, Calibration_Setup])
assembly_PO.order.add_edge(Component_Test, System_Assembly)
assembly_PO.order.add_edge(Component_Test, Firmware_Load)
assembly_PO.order.add_edge(System_Assembly, Calibration_Setup)
assembly_PO.order.add_edge(Firmware_Load, Calibration_Setup)

# QA phase partial order:
# Calibration Setup precedes Flight Testing, which precedes Quality Review
qa_PO = StrictPartialOrder(nodes=[Calibration_Setup, Flight_Testing, Quality_Review])
qa_PO.order.add_edge(Calibration_Setup, Flight_Testing)
qa_PO.order.add_edge(Flight_Testing, Quality_Review)

# Final phase partial order:
# Packaging Prep precedes Client Training and Delivery Setup concurrently
# Both precede Support Launch
final_PO = StrictPartialOrder(nodes=[Packaging_Prep, Client_Training, Delivery_Setup, Support_Launch])
final_PO.order.add_edge(Packaging_Prep, Client_Training)
final_PO.order.add_edge(Packaging_Prep, Delivery_Setup)
final_PO.order.add_edge(Client_Training, Support_Launch)
final_PO.order.add_edge(Delivery_Setup, Support_Launch)

# Entire process partial order nodes
nodes = [Client_Brief, Design_Draft,
         fabrication_PO,  # production phase partial order
         Part_Fabrication,  # note Part_Fabrication is already in fabrication_PO nodes, so don't double add
         Component_Test, assembly_PO, Calibration_Setup,
         qa_PO,
         final_PO]

# The issue: fabrication_PO includes Part_Fabrication, so don't add it twice.
# Also, Component_Test and Calibration_Setup are already in assembly_PO and qa_PO respectively.
# So better to build from individual submodels consistently to avoid duplicates.

# Prefer to create a single root PO with:
# Step 1: Client Brief --> Design Draft
# Step 2: Design Draft --> fabrication_PO (Material Sourcing and subsequent)
# Step 3: Part Fabrication completes fabrication_PO and leads to Component Test
# Step 4: Component Test --> assembly_PO (System Assembly and Firmware Load)
# Step 5: calibration setup, flight testing and quality review (qa_PO)
# Step 6: final_PO (packaging and following)

# To avoid duplication, use the top-level nodes as:
nodes = [
    Client_Brief,
    Design_Draft,
    fabrication_PO,
    Component_Test,
    assembly_PO,
    Flight_Testing,
    Quality_Review,
    final_PO
]

root = StrictPartialOrder(nodes=nodes)

# Define edges between these high-level steps
root.order.add_edge(Client_Brief, Design_Draft)
root.order.add_edge(Design_Draft, fabrication_PO)
root.order.add_edge(fabrication_PO, Component_Test)
root.order.add_edge(Component_Test, assembly_PO)
root.order.add_edge(assembly_PO, Flight_Testing)
root.order.add_edge(Flight_Testing, Quality_Review)
root.order.add_edge(Quality_Review, final_PO)