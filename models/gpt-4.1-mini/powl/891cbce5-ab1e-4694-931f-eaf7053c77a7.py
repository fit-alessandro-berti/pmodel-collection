# Generated from: 891cbce5-ab1e-4694-931f-eaf7053c77a7.json
# Description: This process outlines the intricate steps involved in sourcing, crafting, and delivering bespoke artisan goods. It begins with raw material scouting in remote regions, followed by quality validation using non-standardized criteria. Artisans receive personalized design briefs, enabling handcrafting with adaptive techniques. Finished items undergo multi-stage authenticity and durability testing, including community feedback loops. Packaging is customized per client preferences using eco-friendly materials. The logistics phase integrates unconventional transport methods like local courier networks and barter exchanges. Finally, a post-delivery artisan-client interaction ensures satisfaction and future collaboration, fostering a sustainable and culturally rich business ecosystem that defies mainstream mass production models.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Material_Scout = Transition(label='Material Scout')
Quality_Check = Transition(label='Quality Check')
Design_Brief = Transition(label='Design Brief')
Artisan_Assign = Transition(label='Artisan Assign')
Crafting_Phase = Transition(label='Crafting Phase')
Midway_Review = Transition(label='Midway Review')
Authenticity_Test = Transition(label='Authenticity Test')
Durability_Check = Transition(label='Durability Check')
Community_Feedback = Transition(label='Community Feedback')
Package_Design = Transition(label='Package Design')
Eco_Packaging = Transition(label='Eco Packaging')
Local_Courier = Transition(label='Local Courier')
Barter_Exchange = Transition(label='Barter Exchange')
Delivery_Confirm = Transition(label='Delivery Confirm')
Client_Followup = Transition(label='Client Followup')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Multi-stage authenticity and durability testing, including community feedback loops:
# Model testing loop as LOOP: do Authenticity_Test & Durability_Check & Community_Feedback, then choose to exit or repeat community feedback and durability then testing again  
# To model "multi-stage" we consider Authenticity_Test and Durability_Check and Community_Feedback as a partial order first (concurrent or partially ordered)
# Because community feedback loops, we create a LOOP for Community Feedback+Durability Check before starting again

# Define a partial order for Authenticity_Test and Durability_Check (possibly concurrent)
auth_dur_test = StrictPartialOrder(nodes=[Authenticity_Test, Durability_Check])
# no order edges: tests can be concurrent

# Define Community Feedback + Durability Check sequence (order: Community_Feedback --> Durability_Check)
comm_dur_feedback = StrictPartialOrder(nodes=[Community_Feedback, Durability_Check])
comm_dur_feedback.order.add_edge(Community_Feedback, Durability_Check)

# Loop: after Authenticity_Test, Durability_Check, Community_Feedback, choose to exit or do Community_Feedback+Durability_Check then again Authenticity_Test & Durability_Check
# We combine this as LOOP( body=A, redo=B ) where:
# - A = auth_dur_test
# - B = comm_dur_feedback

# However, durability_check is repeated in A and B, let's consider:

# A = Authenticity_Test + Durability_Check in parallel
# B = Community_Feedback followed by Durability_Check (sequential)

# We'll define loop like: LOOP(A, B) with this semantics:
# First execute A (auth/dur), then choose exit or do B and then A again.

testing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[auth_dur_test, comm_dur_feedback]
)

# Design Brief and Artisan Assign precede Crafting Phase and Midway Review
# Crafting Phase and Midway Review can be modeled as partial order (perhaps sequential or concurrent?)
crafting_phase_and_review = StrictPartialOrder(nodes=[Crafting_Phase, Midway_Review])
# Let's assume Crafting_Phase --> Midway_Review (logical sequence)
crafting_phase_and_review.order.add_edge(Crafting_Phase, Midway_Review)

# Material Scout --> Quality Check
mat_scout_to_quality = StrictPartialOrder(nodes=[Material_Scout, Quality_Check])
mat_scout_to_quality.order.add_edge(Material_Scout, Quality_Check)

# Quality Check --> Design Brief --> Artisan Assign
design_path = StrictPartialOrder(nodes=[Quality_Check, Design_Brief, Artisan_Assign])
design_path.order.add_edge(Quality_Check, Design_Brief)
design_path.order.add_edge(Design_Brief, Artisan_Assign)

# Artisan Assign --> Crafting Phase & Midway Review partial order
assign_to_crafting = StrictPartialOrder(nodes=[Artisan_Assign, crafting_phase_and_review])
assign_to_crafting.order.add_edge(Artisan_Assign, crafting_phase_and_review)

# Packaging: Package Design and Eco Packaging can be parallel/partial order
packaging = StrictPartialOrder(nodes=[Package_Design, Eco_Packaging])
# no edges: concurrent

# Logistics: choice between Local Courier and Barter Exchange
logistics_choice = OperatorPOWL(operator=Operator.XOR, children=[Local_Courier, Barter_Exchange])

# Logistics choice --> Delivery Confirm
logistics_to_delivery = StrictPartialOrder(nodes=[logistics_choice, Delivery_Confirm])
logistics_to_delivery.order.add_edge(logistics_choice, Delivery_Confirm)

# Post-delivery: Client Followup --> Sustainability Audit
post_delivery = StrictPartialOrder(nodes=[Client_Followup, Sustainability_Audit])
post_delivery.order.add_edge(Client_Followup, Sustainability_Audit)

# Now put all pieces in order per the description:
# Material Scout --> Quality Check --> Design Brief --> Artisan Assign --> Crafting Phase & Midway Review --> Testing Loop --> Packaging --> Logistics --> Delivery Confirm --> Post Delivery

# The previous partial orders already model some sequences, we'll now connect them in a big PO:

root = StrictPartialOrder(
    nodes=[
        Material_Scout,
        Quality_Check,
        Design_Brief,
        Artisan_Assign,
        crafting_phase_and_review,
        testing_loop,
        packaging,
        logistics_choice,
        Delivery_Confirm,
        post_delivery,
    ]
)

# Add edges linking the pieces:

# Material Scout --> Quality Check
root.order.add_edge(Material_Scout, Quality_Check)

# Quality Check --> Design Brief
root.order.add_edge(Quality_Check, Design_Brief)

# Design Brief --> Artisan Assign
root.order.add_edge(Design_Brief, Artisan_Assign)

# Artisan Assign --> crafting_phase_and_review
root.order.add_edge(Artisan_Assign, crafting_phase_and_review)

# crafting_phase_and_review --> testing_loop
root.order.add_edge(crafting_phase_and_review, testing_loop)

# testing_loop --> packaging
root.order.add_edge(testing_loop, packaging)

# packaging --> logistics_choice
root.order.add_edge(packaging, logistics_choice)

# logistics_choice --> Delivery Confirm
root.order.add_edge(logistics_choice, Delivery_Confirm)

# Delivery Confirm --> post_delivery
root.order.add_edge(Delivery_Confirm, post_delivery)