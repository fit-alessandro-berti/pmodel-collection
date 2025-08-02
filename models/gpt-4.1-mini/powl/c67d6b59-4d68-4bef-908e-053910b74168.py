# Generated from: c67d6b59-4d68-4bef-908e-053910b74168.json
# Description: This process outlines the intricate steps involved in designing, assembling, and delivering custom drones tailored to unique client specifications. It includes initial consultation, component sourcing from multiple vendors, precision assembly, multi-phase quality testing including flight simulation, software integration, and final client demonstration. The process also involves iterative adjustments based on client feedback, regulatory compliance checks, and specialized packaging for sensitive drone components. Each stage requires cross-functional collaboration between engineering, procurement, quality assurance, and customer service teams to ensure the drone meets all performance and safety standards before shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Meet = Transition(label='Client Meet')
Design_Draft = Transition(label='Design Draft')
Vendor_Select = Transition(label='Vendor Select')
Component_Order = Transition(label='Component Order')
Parts_Inspect = Transition(label='Parts Inspect')
Frame_Build = Transition(label='Frame Build')
Wiring_Setup = Transition(label='Wiring Setup')
Software_Load = Transition(label='Software Load')
Flight_Sim = Transition(label='Flight Sim')
Quality_Test = Transition(label='Quality Test')
Feedback_Review = Transition(label='Feedback Review')
Adjust_Design = Transition(label='Adjust Design')
Compliance_Check = Transition(label='Compliance Check')
Packaging_Prep = Transition(label='Packaging Prep')
Final_Demo = Transition(label='Final Demo')
Ship_Drone = Transition(label='Ship Drone')

# Partial order for sourcing and inspection after vendor selection
sourcing = StrictPartialOrder(nodes=[Vendor_Select, Component_Order, Parts_Inspect])
sourcing.order.add_edge(Vendor_Select, Component_Order)
sourcing.order.add_edge(Component_Order, Parts_Inspect)

# Partial order for the assembly stage after inspection
assembly = StrictPartialOrder(nodes=[Frame_Build, Wiring_Setup])
# no edge => concurrent assembly activities

# Partial order for software and testing after assembly
software_and_testing = StrictPartialOrder(nodes=[Software_Load, Flight_Sim, Quality_Test])
software_and_testing.order.add_edge(Software_Load, Flight_Sim)
software_and_testing.order.add_edge(Flight_Sim, Quality_Test)

# Partial order for compliance, packaging, demo and shipment (sequential)
finalization = StrictPartialOrder(nodes=[Compliance_Check, Packaging_Prep, Final_Demo, Ship_Drone])
finalization.order.add_edge(Compliance_Check, Packaging_Prep)
finalization.order.add_edge(Packaging_Prep, Final_Demo)
finalization.order.add_edge(Final_Demo, Ship_Drone)

# Loop for feedback-based adjustment iteration:
# Loop(A=Adjust Design, B=(Feedback Review, Design Draft))
# The loop means: execute Adjust Design once, then repeat (Feedback Review and Design Draft) followed by Adjust Design until exit.
feedback_subloop = StrictPartialOrder(nodes=[Feedback_Review, Design_Draft])
feedback_subloop.order.add_edge(Feedback_Review, Design_Draft)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Adjust_Design, feedback_subloop])

# Main workflow partial order:
# Client Meet -> Design Draft -> (sourcing) -> (Parts Inspect)
# Then assembly (Frame Build, Wiring Setup) concurrent
# Then software_and_testing (software load etc)
# Then feedback loop
# Then compliance and finalization

# We combine Design Draft with sourcing after it
design_to_sourcing = StrictPartialOrder(
    nodes=[Design_Draft, sourcing]
)
design_to_sourcing.order.add_edge(Design_Draft, sourcing)

# After sourcing comes parts inspect is inside sourcing order already,
# so after sourcing (including Parts Inspect) comes assembly
assembly_after_sourcing = StrictPartialOrder(
    nodes=[sourcing, assembly]
)
assembly_after_sourcing.order.add_edge(sourcing, assembly)

# After assembly is software and testing
softtest_after_assembly = StrictPartialOrder(
    nodes=[assembly, software_and_testing]
)
softtest_after_assembly.order.add_edge(assembly, software_and_testing)

# After software and testing comes loop of adjustment
loop_after_softtest = StrictPartialOrder(
    nodes=[software_and_testing, loop]
)
loop_after_softtest.order.add_edge(software_and_testing, loop)

# After loop comes compliance and finalization
final_after_loop = StrictPartialOrder(
    nodes=[loop, finalization]
)
final_after_loop.order.add_edge(loop, finalization)

# Combine all parts with Client Meet at the start
root = StrictPartialOrder(
    nodes=[Client_Meet, design_to_sourcing, assembly_after_sourcing, softtest_after_assembly, loop_after_softtest, final_after_loop]
)
root.order.add_edge(Client_Meet, design_to_sourcing)
root.order.add_edge(design_to_sourcing, assembly_after_sourcing)
root.order.add_edge(assembly_after_sourcing, softtest_after_assembly)
root.order.add_edge(softtest_after_assembly, loop_after_softtest)
root.order.add_edge(loop_after_softtest, final_after_loop)