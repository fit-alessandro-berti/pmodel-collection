# Generated from: f43b35e4-f493-452b-918e-6f2bb594fac9.json
# Description: This process outlines the intricate steps involved in custom drone assembly, which includes initial client consultation, bespoke component design, precision part fabrication, iterative software calibration, and rigorous quality assurance testing. The workflow incorporates multiple feedback loops between hardware adjustments and software tuning to ensure optimal flight performance. Post-assembly, drones undergo environmental stress testing and client-specific payload integration, followed by final certification and delivery scheduling. This atypical process demands close coordination between engineering, design, and logistics teams to meet unique client specifications within tight deadlines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Transitions for activities
Client_Brief = Transition(label='Client Brief')
Design_Draft = Transition(label='Design Draft')
Part_Sourcing = Transition(label='Part Sourcing')
Component_Fabric = Transition(label='Component Fabric')
Circuit_Assembly = Transition(label='Circuit Assembly')
Software_Upload = Transition(label='Software Upload')
Initial_Testing = Transition(label='Initial Testing')
Flight_Calibrate = Transition(label='Flight Calibrate')
Payload_Mount = Transition(label='Payload Mount')
Stress_Testing = Transition(label='Stress Testing')
Feedback_Loop = Transition(label='Feedback Loop')  # Will model as loop component (symbolic)
Quality_Check = Transition(label='Quality Check')
Certification = Transition(label='Certification')
Packaging = Transition(label='Packaging')
Delivery_Plan = Transition(label='Delivery Plan')
Post_Support = Transition(label='Post Support')

# Model the core feedback loop between hardware adjustments and software tuning:
# The description: iterative calibration - likely between Flight Calibrate (hardware adj), 
# Feedback Loop (symbolic activity representing iterative process), and Software Upload (software tuning).
# We will model a LOOP with:
#  - body: Flight Calibrate
#  - redo loop activity: Feedback Loop followed by Software Upload, then back to Flight Calibrate

# Since Feedback_Loop is an activity, but conceptually is part of loop,
# we model loop children as [Flight_Calibrate, StrictPartialOrder([Feedback_Loop, Software_Upload])] so the redo is those two in sequence.

redo_seq = StrictPartialOrder(nodes=[Feedback_Loop, Software_Upload])
redo_seq.order.add_edge(Feedback_Loop, Software_Upload)

loop_calibration = OperatorPOWL(operator=Operator.LOOP, children=[Flight_Calibrate, redo_seq])

# Main partial order construction:

# Steps:
# Client Brief
#  -> Design Draft
#  -> Part Sourcing
#  -> Component Fabric
#  -> Circuit Assembly
#  -> Software Upload (initial)
#  -> Initial Testing
#  -> loop_calibration
#  -> Quality Check
#  -> Stress Testing
#  -> Payload Mount
#  -> Certification
#  -> Packaging
#  -> Delivery Plan
#  -> Post Support

# We incorporate Software Upload twice: first initial upload, then iterative tuning inside loop_calibration

# Assemble nodes (all activities + the loop node)
nodes = [
    Client_Brief,
    Design_Draft,
    Part_Sourcing,
    Component_Fabric,
    Circuit_Assembly,
    Software_Upload,    # initial upload
    Initial_Testing,
    loop_calibration,   # iterative tuning loop
    Quality_Check,
    Stress_Testing,
    Payload_Mount,
    Certification,
    Packaging,
    Delivery_Plan,
    Post_Support,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to define order

root.order.add_edge(Client_Brief, Design_Draft)
root.order.add_edge(Design_Draft, Part_Sourcing)
root.order.add_edge(Part_Sourcing, Component_Fabric)
root.order.add_edge(Component_Fabric, Circuit_Assembly)
root.order.add_edge(Circuit_Assembly, Software_Upload)
root.order.add_edge(Software_Upload, Initial_Testing)
root.order.add_edge(Initial_Testing, loop_calibration)
root.order.add_edge(loop_calibration, Quality_Check)
root.order.add_edge(Quality_Check, Stress_Testing)
root.order.add_edge(Stress_Testing, Payload_Mount)
root.order.add_edge(Payload_Mount, Certification)
root.order.add_edge(Certification, Packaging)
root.order.add_edge(Packaging, Delivery_Plan)
root.order.add_edge(Delivery_Plan, Post_Support)