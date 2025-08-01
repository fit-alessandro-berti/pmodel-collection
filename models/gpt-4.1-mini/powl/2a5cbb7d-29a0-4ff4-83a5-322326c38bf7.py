# Generated from: 2a5cbb7d-29a0-4ff4-83a5-322326c38bf7.json
# Description: This process involves the design, sourcing, and assembly of custom drones tailored for specialized industrial applications such as agriculture, surveillance, and delivery. It begins with client requirement analysis, followed by prototype design and iterative testing. Components are sourced globally through a vetting process ensuring quality and compliance. Skilled technicians perform modular assembly, integrating avionics, propulsion, and sensor systems. Each unit undergoes rigorous calibration, flight simulation, and safety validation. The process concludes with packaging, client training, and after-sales support planning to ensure optimal operational performance and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Client_Brief = Transition(label='Client Brief')
Draft_Design = Transition(label='Draft Design')
Component_Sourcing = Transition(label='Component Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Prototype_Build = Transition(label='Prototype Build')
Initial_Testing = Transition(label='Initial Testing')
Design_Revision = Transition(label='Design Revision')
Final_Assembly = Transition(label='Final Assembly')
System_Integration = Transition(label='System Integration')
Calibration_Setup = Transition(label='Calibration Setup')
Flight_Simulation = Transition(label='Flight Simulation')
Safety_Check = Transition(label='Safety Check')
Packaging_Prep = Transition(label='Packaging Prep')
Client_Training = Transition(label='Client Training')
Support_Setup = Transition(label='Support Setup')

# Design iteration loop: after Initial Testing, either exit or do Design Revision then Prototype Build and Initial Testing again
design_revision_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Initial_Testing,
    Design_Revision
])

# Since the loop requires A then branching B, but the revision loop requires looping on Prototype Build -> Initial Testing with revision in between,
# we wrap Prototype Build followed by design_revision_loop, since loop executes A then either exits or does B then A again.
# So the iterative design part is:
# A: Prototype Build
# B: Design Revision + Prototype Build (loop returns to Prototype Build via loop semantics)
# 
# But the semantic here is slightly tricky as Design Revision is done before re-building prototype and testing.
# According to description, "prototype design and iterative testing":
# - Prototype Build
# - Initial Testing
# - If revision needed: Design Revision, then again Prototype Build + Initial Testing (repeat)
# So loop node should be: * (Initial Testing, Design Revision)

# But loop node from pm4py LOOP operator definition:
# LOOP(A,B) means: do A, then choose either to exit or do B followed by A again (i.e., run A, then loop or exit)
# So we model iterative testing and revision as:
# A = Initial Testing
# B = Design Revision

# However we need to wrap the Prototype Build before this loop and after Design Revision before next loop
# We can do this by building a sequence: Prototype Build, then loop(Initial Testing, Design Revision)
# But POWL model has no explicit sequence operator: sequences modeled by partial order edges.

# Let's define the loop node:
loop_testing_revision = OperatorPOWL(operator=Operator.LOOP, children=[Initial_Testing, Design_Revision])

# So the design process partial order is:
# Client Brief --> Draft Design --> Component Sourcing --> Supplier Vetting --> Prototype Build --> loop_testing_revision

# After finishing the design iteration loop, process proceeds to Final Assembly and subsequent steps

# Partial order for sourcing: Component Sourcing --> Supplier Vetting

# Partial order for assembly:
# Final Assembly --> System Integration --> Calibration Setup --> Flight Simulation --> Safety Check

# Final steps: Safety Check --> Packaging Prep --> Client Training --> Support Setup

# Model concurrency and ordering in partial order:

# Nodes for all except loop
nodes = [
    Client_Brief,
    Draft_Design,
    Component_Sourcing,
    Supplier_Vetting,
    Prototype_Build,
    loop_testing_revision,
    Final_Assembly,
    System_Integration,
    Calibration_Setup,
    Flight_Simulation,
    Safety_Check,
    Packaging_Prep,
    Client_Training,
    Support_Setup
]

root = StrictPartialOrder(nodes=nodes)
order = root.order.add_edge

# Define order edges
order(Client_Brief, Draft_Design)
order(Draft_Design, Component_Sourcing)
order(Component_Sourcing, Supplier_Vetting)
order(Supplier_Vetting, Prototype_Build)
order(Prototype_Build, loop_testing_revision)  # Prototype Build before iterative testing + revision loop

order(loop_testing_revision, Final_Assembly)
order(Final_Assembly, System_Integration)
order(System_Integration, Calibration_Setup)
order(Calibration_Setup, Flight_Simulation)
order(Flight_Simulation, Safety_Check)
order(Safety_Check, Packaging_Prep)
order(Packaging_Prep, Client_Training)
order(Client_Training, Support_Setup)