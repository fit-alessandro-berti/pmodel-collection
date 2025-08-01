# Generated from: fa2a8680-8911-4632-9895-876066879230.json
# Description: This process outlines the end-to-end workflow for deploying a custom drone fleet tailored to environmental monitoring in remote areas. It involves initial client consultation to gather unique requirements, followed by modular drone design and component sourcing from specialized suppliers. Prototype assembly and rigorous field testing ensure operational reliability under extreme conditions. After validation, software integration for real-time data analytics and autonomous navigation is conducted. The fleet undergoes pilot training and regulatory compliance verification before final deployment. Post-deployment includes continuous remote monitoring, maintenance scheduling, and iterative performance optimization through AI-driven feedback mechanisms, ensuring the drones adapt to evolving environmental challenges effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Meet = Transition(label='Client Meet')
Requirement_Gather = Transition(label='Requirement Gather')

Module_Design = Transition(label='Module Design')
Supplier_Vetting = Transition(label='Supplier Vetting')
Component_Order = Transition(label='Component Order')

Prototype_Build = Transition(label='Prototype Build')
Field_Testing = Transition(label='Field Testing')
Test_Analysis = Transition(label='Test Analysis')

Software_Setup = Transition(label='Software Setup')
Data_Integration = Transition(label='Data Integration')

Pilot_Train = Transition(label='Pilot Train')
Compliance_Check = Transition(label='Compliance Check')

Fleet_Deploy = Transition(label='Fleet Deploy')

Remote_Monitor = Transition(label='Remote Monitor')
Maintenance_Plan = Transition(label='Maintenance Plan')
Performance_Tune = Transition(label='Performance Tune')

# Stage 1: Client consultation
stage1 = StrictPartialOrder(nodes=[Client_Meet, Requirement_Gather])
stage1.order.add_edge(Client_Meet, Requirement_Gather)

# Stage 2: Modular drone design and component sourcing
stage2 = StrictPartialOrder(nodes=[Module_Design, Supplier_Vetting, Component_Order])
stage2.order.add_edge(Module_Design, Supplier_Vetting)
stage2.order.add_edge(Supplier_Vetting, Component_Order)

# Stage 3: Prototype assembly and field testing
stage3 = StrictPartialOrder(nodes=[Prototype_Build, Field_Testing, Test_Analysis])
stage3.order.add_edge(Prototype_Build, Field_Testing)
stage3.order.add_edge(Field_Testing, Test_Analysis)

# Stage 4: Software integration for real-time data analytics and autonomous navigation
stage4 = StrictPartialOrder(nodes=[Software_Setup, Data_Integration])
stage4.order.add_edge(Software_Setup, Data_Integration)

# Stage 5: Pilot training and regulatory compliance verification
stage5 = StrictPartialOrder(nodes=[Pilot_Train, Compliance_Check])
stage5.order.add_edge(Pilot_Train, Compliance_Check)

# Stage 6: Final deployment
stage6 = Fleet_Deploy  # Single activity

# Stage 7: Post-deployment activities in partial order (concurrent)
stage7 = StrictPartialOrder(nodes=[Remote_Monitor, Maintenance_Plan, Performance_Tune])
# No order constraints = fully concurrent

# Compose all stages in strict partial order (from start to end)
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, stage5, stage6, stage7])
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, stage5)
root.order.add_edge(stage5, stage6)
root.order.add_edge(stage6, stage7)