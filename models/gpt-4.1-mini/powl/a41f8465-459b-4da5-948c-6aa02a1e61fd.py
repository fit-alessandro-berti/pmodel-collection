# Generated from: a41f8465-459b-4da5-948c-6aa02a1e61fd.json
# Description: This process outlines the intricate steps involved in designing, assembling, and testing customized drones tailored for specific client requirements. It begins with requirement gathering and concept design, followed by component sourcing that involves rare materials and specialized suppliers. The assembly phase integrates advanced electronics and precision mechanical parts, necessitating rigorous quality checks at each stage. Post-assembly, drones undergo environmental stress testing and software calibration to ensure optimal performance in diverse conditions. Final approval includes client demonstration and feedback incorporation before shipment. This atypical process demands coordination across engineering, procurement, and quality assurance teams to deliver bespoke unmanned aerial vehicles that meet stringent operational standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Req_Gathering = Transition(label='Req Gathering')
Concept_Design = Transition(label='Concept Design')
Supplier_Vetting = Transition(label='Supplier Vetting')
Material_Sourcing = Transition(label='Material Sourcing')
Component_Testing = Transition(label='Component Testing')
Frame_Assembly = Transition(label='Frame Assembly')
Electronics_Install = Transition(label='Electronics Install')
Wiring_Setup = Transition(label='Wiring Setup')
Software_Upload = Transition(label='Software Upload')
Calibration_Check = Transition(label='Calibration Check')
Stress_Testing = Transition(label='Stress Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Client_Demo = Transition(label='Client Demo')
Feedback_Fix = Transition(label='Feedback Fix')
Final_Approval = Transition(label='Final Approval')
Packaging_Ship = Transition(label='Packaging Ship')

# Build the process:

# Requirement gathering and concept design sequential
req_concept = StrictPartialOrder(nodes=[Req_Gathering, Concept_Design])
req_concept.order.add_edge(Req_Gathering, Concept_Design)

# Component sourcing involves two activities in partial order (Supplier Vetting and Material Sourcing) 
# but realistically Supplier Vetting should precede Material Sourcing:
supplier_material = StrictPartialOrder(nodes=[Supplier_Vetting, Material_Sourcing])
supplier_material.order.add_edge(Supplier_Vetting, Material_Sourcing)

# Assembly phase: Component Testing -> Frame Assembly -> (Electronics Install + Wiring Setup concurrent)
# Followed by quality check (Calibration Check is done after software upload, per description so let's separate that)
electronics_wiring = StrictPartialOrder(nodes=[Electronics_Install, Wiring_Setup])
# no order edges between Electronics Install and Wiring Setup - concurrent
assembly = StrictPartialOrder(
    nodes=[Component_Testing, Frame_Assembly, electronics_wiring]
)
assembly.order.add_edge(Component_Testing, Frame_Assembly)
assembly.order.add_edge(Frame_Assembly, electronics_wiring)

# Software calibration phase: Software Upload + Calibration Check sequential
software_calibration = StrictPartialOrder(nodes=[Software_Upload, Calibration_Check])
software_calibration.order.add_edge(Software_Upload, Calibration_Check)

# Testing phase: Stress Testing -> Flight Simulation sequential
testing = StrictPartialOrder(nodes=[Stress_Testing, Flight_Simulation])
testing.order.add_edge(Stress_Testing, Flight_Simulation)

# Client approval phase: Client Demo -> Feedback Fix -> Final Approval sequential
client_approval = StrictPartialOrder(nodes=[Client_Demo, Feedback_Fix, Final_Approval])
client_approval.order.add_edge(Client_Demo, Feedback_Fix)
client_approval.order.add_edge(Feedback_Fix, Final_Approval)

# Packaging and shipment (final)
packaging_ship = Packaging_Ship

# Combine assembly + software calibration + testing phases in order:
assembly_software_testing = StrictPartialOrder(nodes=[assembly, software_calibration, testing])
assembly_software_testing.order.add_edge(assembly, software_calibration)
assembly_software_testing.order.add_edge(software_calibration, testing)

# Combine all main phases in strict partial order:
# Req_gathering + concept design (req_concept)
# -> Supplier vetting/material sourcing (supplier_material)
# -> assembly + software + testing (assembly_software_testing)
# -> client approval (client_approval)
# -> packaging_ship

root = StrictPartialOrder(
    nodes=[req_concept, supplier_material, assembly_software_testing, client_approval, packaging_ship]
)
root.order.add_edge(req_concept, supplier_material)
root.order.add_edge(supplier_material, assembly_software_testing)
root.order.add_edge(assembly_software_testing, client_approval)
root.order.add_edge(client_approval, packaging_ship)