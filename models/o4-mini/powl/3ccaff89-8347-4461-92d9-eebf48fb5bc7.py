# Generated from: 3ccaff89-8347-4461-92d9-eebf48fb5bc7.json
# Description: This process outlines the end-to-end workflow for designing, fabricating, and installing large-scale custom art installations for public and private spaces. It involves initial client consultation, concept ideation, material sourcing including rare and sustainable components, prototype modeling, iterative design approvals, fabrication in specialized workshops, quality assurance checks, logistics planning for transport, on-site assembly coordination, final aesthetic adjustments, and post-installation maintenance scheduling. The process also integrates stakeholder feedback loops and compliance verification for safety and environmental regulations to ensure the artwork is both impactful and durable in diverse environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
client_meet      = Transition(label='Client Meet')
concept_brain    = Transition(label='Concept Brainstorm')
material_source  = Transition(label='Material Source')
prototype_build  = Transition(label='Prototype Build')
design_review    = Transition(label='Design Review')
approval_cycle   = Transition(label='Approval Cycle')
workshop_fab     = Transition(label='Workshop Fabricate')
quality_inspect  = Transition(label='Quality Inspect')
logistics_plan   = Transition(label='Logistics Plan')
transport_arr    = Transition(label='Transport Arrange')
site_prep        = Transition(label='Site Prep')
assembly_lead    = Transition(label='Assembly Lead')
final_adjust     = Transition(label='Final Adjust')
feedback_collect = Transition(label='Feedback Collect')
compliance_check = Transition(label='Compliance Check')
maintenance_set  = Transition(label='Maintenance Setup')

# Define the rework subprocess (feedback + compliance) as a strict partial order
rework = StrictPartialOrder(nodes=[feedback_collect, compliance_check])
rework.order.add_edge(feedback_collect, compliance_check)

# Define the approval loop: do Approval Cycle, then either exit or perform rework then Approval Cycle again
approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[approval_cycle, rework])

# Define the top‐level workflow as a strict partial order, sequencing all main steps
root = StrictPartialOrder(nodes=[
    client_meet,
    concept_brain,
    material_source,
    prototype_build,
    design_review,
    approval_loop,
    workshop_fab,
    quality_inspect,
    logistics_plan,
    transport_arr,
    site_prep,
    assembly_lead,
    final_adjust,
    maintenance_set
])

# Add the sequential dependencies
root.order.add_edge(client_meet,      concept_brain)
root.order.add_edge(concept_brain,    material_source)
root.order.add_edge(material_source,  prototype_build)
root.order.add_edge(prototype_build,  design_review)
root.order.add_edge(design_review,    approval_loop)
root.order.add_edge(approval_loop,    workshop_fab)
root.order.add_edge(workshop_fab,     quality_inspect)
root.order.add_edge(quality_inspect,  logistics_plan)
root.order.add_edge(logistics_plan,   transport_arr)
root.order.add_edge(transport_arr,    site_prep)
root.order.add_edge(site_prep,        assembly_lead)
root.order.add_edge(assembly_lead,    final_adjust)
root.order.add_edge(final_adjust,     maintenance_set)