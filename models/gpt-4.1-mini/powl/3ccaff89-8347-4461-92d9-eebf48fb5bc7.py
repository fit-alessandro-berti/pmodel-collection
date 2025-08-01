# Generated from: 3ccaff89-8347-4461-92d9-eebf48fb5bc7.json
# Description: This process outlines the end-to-end workflow for designing, fabricating, and installing large-scale custom art installations for public and private spaces. It involves initial client consultation, concept ideation, material sourcing including rare and sustainable components, prototype modeling, iterative design approvals, fabrication in specialized workshops, quality assurance checks, logistics planning for transport, on-site assembly coordination, final aesthetic adjustments, and post-installation maintenance scheduling. The process also integrates stakeholder feedback loops and compliance verification for safety and environmental regulations to ensure the artwork is both impactful and durable in diverse environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Meet = Transition(label='Client Meet')
Concept_Brainstorm = Transition(label='Concept Brainstorm')
Material_Source = Transition(label='Material Source')
Prototype_Build = Transition(label='Prototype Build')
Design_Review = Transition(label='Design Review')
Approval_Cycle = Transition(label='Approval Cycle')
Workshop_Fabricate = Transition(label='Workshop Fabricate')
Quality_Inspect = Transition(label='Quality Inspect')
Logistics_Plan = Transition(label='Logistics Plan')
Transport_Arrange = Transition(label='Transport Arrange')
Site_Prep = Transition(label='Site Prep')
Assembly_Lead = Transition(label='Assembly Lead')
Final_Adjust = Transition(label='Final Adjust')
Feedback_Collect = Transition(label='Feedback Collect')
Compliance_Check = Transition(label='Compliance Check')
Maintenance_Setup = Transition(label='Maintenance Setup')

# Loop node for Approval Cycle with Design Review (iterative approvals)
# Loop: execute Design Review, then either exit or Approval Cycle then Design Review again.
approval_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Design_Review, Approval_Cycle]
)

# Partial order describing the main workflow
root = StrictPartialOrder(nodes=[
    Client_Meet,
    Concept_Brainstorm,
    Material_Source,
    Prototype_Build,
    approval_loop,
    Workshop_Fabricate,
    Quality_Inspect,
    Logistics_Plan,
    Transport_Arrange,
    Site_Prep,
    Assembly_Lead,
    Final_Adjust,
    Feedback_Collect,
    Compliance_Check,
    Maintenance_Setup
])

# Define order restrictions according to the process description

# Initial flow
root.order.add_edge(Client_Meet, Concept_Brainstorm)
root.order.add_edge(Concept_Brainstorm, Material_Source)
root.order.add_edge(Material_Source, Prototype_Build)

# Prototype and design approval loop
root.order.add_edge(Prototype_Build, approval_loop)

# After loop, fabrication and quality check
root.order.add_edge(approval_loop, Workshop_Fabricate)
root.order.add_edge(Workshop_Fabricate, Quality_Inspect)

# Logistics planning and transport arrangement
root.order.add_edge(Quality_Inspect, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Transport_Arrange)

# Site preparation and assembly
root.order.add_edge(Transport_Arrange, Site_Prep)
root.order.add_edge(Site_Prep, Assembly_Lead)

# Final adjustments after assembly
root.order.add_edge(Assembly_Lead, Final_Adjust)

# Feedback collection and compliance check (can be concurrent after final adjust)
root.order.add_edge(Final_Adjust, Feedback_Collect)
root.order.add_edge(Final_Adjust, Compliance_Check)

# Maintenance setup after feedback and compliance (both must be completed)
root.order.add_edge(Feedback_Collect, Maintenance_Setup)
root.order.add_edge(Compliance_Check, Maintenance_Setup)