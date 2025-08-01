# Generated from: fbdab04b-652a-43d2-9acb-1d7ae26aa97f.json
# Description: This process involves the bespoke assembly of drones tailored to individual client specifications that vary greatly in design, purpose, and technology integration. It starts with detailed client consultation to capture unique requirements, followed by modular component selection from diverse suppliers. The assembly phase incorporates precision calibration of sensors, motors, and software systems, ensuring seamless integration of hardware and AI-driven flight control. Throughout, stringent quality checks and iterative testing validate performance under simulated environments. Finally, the process includes personalized user training and remote monitoring setup, providing ongoing support for operational optimization and rapid troubleshooting post-deployment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Client_Consult = Transition(label='Client Consult')
Spec_Analysis = Transition(label='Spec Analysis')
Module_Select = Transition(label='Module Select')
Component_Order = Transition(label='Component Order')
Parts_Inspect = Transition(label='Parts Inspect')
Frame_Assemble = Transition(label='Frame Assemble')
Sensor_Install = Transition(label='Sensor Install')
Motor_Attach = Transition(label='Motor Attach')
Wiring_Connect = Transition(label='Wiring Connect')
Software_Upload = Transition(label='Software Upload')
Calibration_Test = Transition(label='Calibration Test')
Flight_Simulate = Transition(label='Flight Simulate')
Quality_Review = Transition(label='Quality Review')
User_Train = Transition(label='User Train')
Remote_Setup = Transition(label='Remote Setup')
Feedback_Collect = Transition(label='Feedback Collect')
Support_Schedule = Transition(label='Support Schedule')

# Strict partial order modeling the process:

# Phase 1: Client consult and specification analysis
phase1 = StrictPartialOrder(nodes=[Client_Consult, Spec_Analysis])
phase1.order.add_edge(Client_Consult, Spec_Analysis)

# Phase 2: Component selection and ordering (concurrent with phase 1 ending)
phase2 = StrictPartialOrder(nodes=[Module_Select, Component_Order])
phase2.order.add_edge(Module_Select, Component_Order)

# Phase 3: Parts inspect before assembly
phase3 = Parts_Inspect

# Phase 4: Assembly steps which are sequential but some can be concurrent internally
# Frame assemble first
# Then Sensor install, Motor attach, Wiring connect, Software upload can be partially concurrent after frame assemble

assembly_subnodes = [Sensor_Install, Motor_Attach, Wiring_Connect, Software_Upload]
assembly = StrictPartialOrder(nodes=[Frame_Assemble] + assembly_subnodes)
assembly.order.add_edge(Frame_Assemble, Sensor_Install)
assembly.order.add_edge(Frame_Assemble, Motor_Attach)
assembly.order.add_edge(Frame_Assemble, Wiring_Connect)
assembly.order.add_edge(Frame_Assemble, Software_Upload)

# Phase 5: Calibration test and flight simulate sequential
phase5 = StrictPartialOrder(nodes=[Calibration_Test, Flight_Simulate])
phase5.order.add_edge(Calibration_Test, Flight_Simulate)

# Phase 6: Quality review
phase6 = Quality_Review

# Phase 7: User Training and Remote Monitoring setup (can be concurrent)
phase7 = StrictPartialOrder(nodes=[User_Train, Remote_Setup])

# Phase 8: Feedback collect and support schedule loop (support ongoing after feedback)
# Model loop: feedback collect then choice to continue support schedule / exit loop
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Collect, Support_Schedule]
)

# Compose the overall process partial order

nodes = [phase1, phase2, phase3, assembly, phase5, phase6, phase7, loop]

root = StrictPartialOrder(nodes=nodes)

# Define edges for overall ordering based on the description:

# Phase 1 then phase 2
root.order.add_edge(phase1, phase2)
# Phase 2 then parts inspect
root.order.add_edge(phase2, phase3)
# Parts inspect then assembly
root.order.add_edge(phase3, assembly)
# Assembly then calibration and flight simulate
root.order.add_edge(assembly, phase5)
# Phase 5 then quality review
root.order.add_edge(phase5, phase6)
# Quality review then user train and remote setup (concurrent)
root.order.add_edge(phase6, phase7)
# User train and remote setup then feedback loop
root.order.add_edge(phase7, loop)