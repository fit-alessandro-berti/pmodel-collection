# Generated from: 24853da3-5623-4031-bc05-3849e19eb69e.json
# Description: This process outlines the intricate steps involved in designing and assembling bespoke drones tailored for specialized industrial applications. It begins with client consultation to determine precise specifications, followed by iterative design adjustments using advanced CAD tools. Components are sourced from multiple niche suppliers ensuring optimal performance. Assembly requires precision alignment of sensors, motors, and control units, followed by rigorous multi-phase testing including environmental stress and flight simulation. Calibration is fine-tuned according to test results, and final quality assurance ensures compliance with safety and operational standards before packaging and delivery coordination. Post-delivery support includes remote diagnostics and firmware updates to adapt to evolving user needs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Client_Consult = Transition(label='Client Consult')
Design_Draft = Transition(label='Design Draft')
Spec_Review = Transition(label='Spec Review')
Supplier_Select = Transition(label='Supplier Select')
Component_Order = Transition(label='Component Order')
Parts_Inspect = Transition(label='Parts Inspect')
Frame_Assemble = Transition(label='Frame Assemble')
Sensor_Mount = Transition(label='Sensor Mount')
Motor_Install = Transition(label='Motor Install')
Control_Setup = Transition(label='Control Setup')
Initial_Test = Transition(label='Initial Test')
Stress_Test = Transition(label='Stress Test')
Flight_Sim = Transition(label='Flight Sim')
Calibration = Transition(label='Calibration')
QA_Inspect = Transition(label='QA Inspect')
Package_Ship = Transition(label='Package Ship')
Post_Support = Transition(label='Post Support')

# Design loop: iterative design adjustments using Design Draft & Spec Review
# Loop structure: execute Design Draft, then Spec Review, then choose either to exit or loop again
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Draft, Spec_Review])

# Assembly partial order: Frame Assemble then (Sensor Mount, Motor Install, Control Setup) in parallel
assembly_PO = StrictPartialOrder(nodes=[Frame_Assemble, Sensor_Mount, Motor_Install, Control_Setup])
assembly_PO.order.add_edge(Frame_Assemble, Sensor_Mount)
assembly_PO.order.add_edge(Frame_Assemble, Motor_Install)
assembly_PO.order.add_edge(Frame_Assemble, Control_Setup)

# Testing partial order: Initial Test, then Stress Test and Flight Sim in parallel
testing_PO = StrictPartialOrder(nodes=[Initial_Test, Stress_Test, Flight_Sim])
testing_PO.order.add_edge(Initial_Test, Stress_Test)
testing_PO.order.add_edge(Initial_Test, Flight_Sim)

# Calibration and QA Inspect sequential
calibration_QA_PO = StrictPartialOrder(nodes=[Calibration, QA_Inspect])
calibration_QA_PO.order.add_edge(Calibration, QA_Inspect)

# Packaging and shipping after QA
package_ship_PO = StrictPartialOrder(nodes=[Package_Ship])
# Just a node, no edges needed

# Post delivery support - after shipping
post_support_PO = StrictPartialOrder(nodes=[Post_Support])

# Procurement partial order: Supplier Select > Component Order > Parts Inspect
procurement_PO = StrictPartialOrder(nodes=[Supplier_Select, Component_Order, Parts_Inspect])
procurement_PO.order.add_edge(Supplier_Select, Component_Order)
procurement_PO.order.add_edge(Component_Order, Parts_Inspect)

# Main workflow partial order
# Begin: Client Consult > design_loop > procurement_PO > assembly_PO > testing_PO > calibration_QA_PO > package_ship_PO > post_support_PO
nodes_main = [
    Client_Consult, 
    design_loop, 
    procurement_PO, 
    assembly_PO, 
    testing_PO, 
    calibration_QA_PO, 
    package_ship_PO, 
    post_support_PO,
]

root = StrictPartialOrder(nodes=nodes_main)
root.order.add_edge(Client_Consult, design_loop)
root.order.add_edge(design_loop, procurement_PO)
root.order.add_edge(procurement_PO, assembly_PO)
root.order.add_edge(assembly_PO, testing_PO)
root.order.add_edge(testing_PO, calibration_QA_PO)
root.order.add_edge(calibration_QA_PO, package_ship_PO)
root.order.add_edge(package_ship_PO, post_support_PO)