# Generated from: caeed5f1-c289-44d7-83d1-2a5c614e44d1.json
# Description: This process outlines the detailed workflow for managing bespoke art commissions for high-profile clients. It involves initial consultation to understand client vision, iterative concept development with frequent feedback, material sourcing from specialized vendors, and coordinating multiple artisans including painters, framers, and restorers. Quality assurance includes both artistic critique and technical inspections to ensure durability and aesthetic standards. After completion, logistics for secure transport and installation are arranged, followed by post-delivery client support and archival documentation for provenance and future reference. This atypical process combines creative design with project management and technical craftsmanship, requiring close collaboration across diverse teams and external partners to deliver a truly unique art piece that meets exacting client specifications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
client_meet      = Transition(label='Client Meet')
vision_capture   = Transition(label='Vision Capture')
concept_draft    = Transition(label='Concept Draft')
feedback_loop    = Transition(label='Feedback Loop')
material_sourcing= Transition(label='Material Sourcing')
vendor_selection = Transition(label='Vendor Selection')
artisan_assign   = Transition(label='Artisan Assign')
prototype_build  = Transition(label='Prototype Build')
quality_review   = Transition(label='Quality Review')
technical_check  = Transition(label='Technical Check')
final_approval   = Transition(label='Final Approval')
packaging_prep   = Transition(label='Packaging Prep')
logistics_plan   = Transition(label='Logistics Plan')
secure_transport = Transition(label='Secure Transport')
installation_set = Transition(label='Installation Set')
client_support   = Transition(label='Client Support')
archival_record  = Transition(label='Archival Record')

# Loop for iterative concept development: do Concept Draft, then either exit or do Feedback Loop + repeat
concept_loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_draft, feedback_loop])

# Build the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    client_meet,
    vision_capture,
    concept_loop,
    material_sourcing,
    vendor_selection,
    artisan_assign,
    prototype_build,
    quality_review,
    technical_check,
    final_approval,
    packaging_prep,
    logistics_plan,
    secure_transport,
    installation_set,
    client_support,
    archival_record
])

# Define the control‐flow (order) edges
o = root.order
o.add_edge(client_meet,      vision_capture)
o.add_edge(vision_capture,   concept_loop)
o.add_edge(concept_loop,     material_sourcing)
o.add_edge(material_sourcing,vendor_selection)
o.add_edge(vendor_selection, artisan_assign)
o.add_edge(artisan_assign,   prototype_build)
o.add_edge(prototype_build,  quality_review)
o.add_edge(prototype_build,  technical_check)
o.add_edge(quality_review,   final_approval)
o.add_edge(technical_check,  final_approval)
o.add_edge(final_approval,   packaging_prep)
o.add_edge(packaging_prep,   logistics_plan)
o.add_edge(logistics_plan,   secure_transport)
o.add_edge(secure_transport, installation_set)
o.add_edge(installation_set, client_support)
o.add_edge(installation_set, archival_record)