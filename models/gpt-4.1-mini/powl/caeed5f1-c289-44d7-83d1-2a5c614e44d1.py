# Generated from: caeed5f1-c289-44d7-83d1-2a5c614e44d1.json
# Description: This process outlines the detailed workflow for managing bespoke art commissions for high-profile clients. It involves initial consultation to understand client vision, iterative concept development with frequent feedback, material sourcing from specialized vendors, and coordinating multiple artisans including painters, framers, and restorers. Quality assurance includes both artistic critique and technical inspections to ensure durability and aesthetic standards. After completion, logistics for secure transport and installation are arranged, followed by post-delivery client support and archival documentation for provenance and future reference. This atypical process combines creative design with project management and technical craftsmanship, requiring close collaboration across diverse teams and external partners to deliver a truly unique art piece that meets exacting client specifications.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Meet = Transition(label='Client Meet')
Vision_Capture = Transition(label='Vision Capture')
Concept_Draft = Transition(label='Concept Draft')
Feedback_Loop = Transition(label='Feedback Loop')
Material_Sourcing = Transition(label='Material Sourcing')
Vendor_Selection = Transition(label='Vendor Selection')
Artisan_Assign = Transition(label='Artisan Assign')
Prototype_Build = Transition(label='Prototype Build')
Quality_Review = Transition(label='Quality Review')
Technical_Check = Transition(label='Technical Check')
Final_Approval = Transition(label='Final Approval')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Secure_Transport = Transition(label='Secure Transport')
Installation_Set = Transition(label='Installation Set')
Client_Support = Transition(label='Client Support')
Archival_Record = Transition(label='Archival Record')

# Create the feedback loop: concept draft and then feedback loop, repeat until exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Concept_Draft, Feedback_Loop])

# Material sourcing branch: Material Sourcing --> Vendor Selection
material_branch = StrictPartialOrder(nodes=[Material_Sourcing, Vendor_Selection])
material_branch.order.add_edge(Material_Sourcing, Vendor_Selection)

# Artisan assignments, prototype build (in sequence)
artisan_branch = StrictPartialOrder(nodes=[Artisan_Assign, Prototype_Build])
artisan_branch.order.add_edge(Artisan_Assign, Prototype_Build)

# Quality assurance: Artistic critique (Quality Review) and Technical Check run in parallel,
# then join to Final Approval
qa_parallel = StrictPartialOrder(nodes=[Quality_Review, Technical_Check, Final_Approval])
qa_parallel.order.add_edge(Quality_Review, Final_Approval)
qa_parallel.order.add_edge(Technical_Check, Final_Approval)

# Packaging and logistics sequence
packaging_logistics = StrictPartialOrder(nodes=[Packaging_Prep, Logistics_Plan, Secure_Transport, Installation_Set])
packaging_logistics.order.add_edge(Packaging_Prep, Logistics_Plan)
packaging_logistics.order.add_edge(Logistics_Plan, Secure_Transport)
packaging_logistics.order.add_edge(Secure_Transport, Installation_Set)

# Final post-delivery activities in parallel: Client Support and Archival Record
post_delivery = StrictPartialOrder(nodes=[Client_Support, Archival_Record])

# Compose the main partial order:
# Start with client meet -> vision capture
start_seq = StrictPartialOrder(nodes=[Client_Meet, Vision_Capture])
start_seq.order.add_edge(Client_Meet, Vision_Capture)

# Then vision capture leads to feedback loop
# feedback_loop is a LOOP node handling concept draft and feedback as repeatable

# After feedback loop completes, start material sourcing and artisan assignment in parallel

# Then their results join before quality assurance (for simplicity, material_branch and artisan_branch run concurrently,
# both precede quality assurance)

# Finally quality assurance -> final approval, then packaging/logistics -> installation

# After installation, post delivery happens in parallel

# Building main model nodes
nodes_main = [
    start_seq,               # client meet -> vision capture
    feedback_loop,           # loop on concept draft and feedback
    material_branch,         # material sourcing sequence
    artisan_branch,          # artisan assignment sequence
    qa_parallel,             # quality review + tech check in parallel then final approval
    packaging_logistics,     # packaging and installation steps sequence
    post_delivery            # client support, archival record in parallel
]

root = StrictPartialOrder(nodes=nodes_main)

# Connect edges according to the description:
# start_seq -> feedback_loop
root.order.add_edge(start_seq, feedback_loop)

# feedback_loop -> material_branch and artisan_branch (both concurrent)
root.order.add_edge(feedback_loop, material_branch)
root.order.add_edge(feedback_loop, artisan_branch)

# material_branch and artisan_branch both lead to qa_parallel
root.order.add_edge(material_branch, qa_parallel)
root.order.add_edge(artisan_branch, qa_parallel)

# qa_parallel -> packaging_logistics
root.order.add_edge(qa_parallel, packaging_logistics)

# packaging_logistics -> post_delivery
root.order.add_edge(packaging_logistics, post_delivery)