# Generated from: 0efaee8e-e517-4175-b9ea-2cb18bce2c48.json
# Description: This process involves collaboratively developing a new artisan cheese recipe by engaging a global community of cheese enthusiasts, dairy farmers, and food scientists. It begins with ideation where participants submit flavor profiles and ingredient suggestions, followed by crowd voting to select the top concepts. Selected concepts undergo prototype development by local cheesemakers, with iterative feedback collected through virtual tastings. Quality control experts analyze feedback and adjust processes accordingly. Legal teams ensure compliance with food safety standards and intellectual property rights. Marketing specialists then craft storytelling campaigns highlighting the collaborative nature of the cheese creation. Finally, distribution partners coordinate limited release shipments to backers and specialty retailers, maintaining traceability and customer engagement throughout the launch phase.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
idea_submit      = Transition(label='Idea Submit')
flavor_vote      = Transition(label='Flavor Vote')
concept_select   = Transition(label='Concept Select')
prototype_make   = Transition(label='Prototype Make')
feedback_gather  = Transition(label='Feedback Gather')
taste_test       = Transition(label='Taste Test')
quality_check    = Transition(label='Quality Check')
adjust_recipe    = Transition(label='Adjust Recipe')
regulation_review= Transition(label='Regulation Review')
ip_register      = Transition(label='IP Register')
story_craft      = Transition(label='Story Craft')
campaign_launch  = Transition(label='Campaign Launch')
order_manage     = Transition(label='Order Manage')
shipment_plan    = Transition(label='Shipment Plan')
customer_engage  = Transition(label='Customer Engage')
traceability_log = Transition(label='Traceability Log')

# Build the loop body for iterative prototyping
loop_body = StrictPartialOrder(
    nodes=[feedback_gather, taste_test, quality_check, adjust_recipe]
)
loop_body.order.add_edge(feedback_gather, taste_test)
loop_body.order.add_edge(taste_test, quality_check)
loop_body.order.add_edge(quality_check, adjust_recipe)

# Define the LOOP operator: prototype_make followed by zero-or-more iterations of loop_body
prototype_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prototype_make, loop_body]
)

# Top‐level partial order
root = StrictPartialOrder(
    nodes=[
        idea_submit, flavor_vote, concept_select,
        prototype_loop,
        regulation_review, ip_register,
        story_craft, campaign_launch,
        order_manage, shipment_plan,
        customer_engage, traceability_log
    ]
)

# Add control‐flow edges
root.order.add_edge(idea_submit,      flavor_vote)
root.order.add_edge(flavor_vote,      concept_select)
root.order.add_edge(concept_select,   prototype_loop)

root.order.add_edge(prototype_loop,   regulation_review)
root.order.add_edge(prototype_loop,   ip_register)

root.order.add_edge(regulation_review, story_craft)
root.order.add_edge(ip_register,       story_craft)

root.order.add_edge(story_craft,      campaign_launch)
root.order.add_edge(campaign_launch,  order_manage)
root.order.add_edge(order_manage,     shipment_plan)

root.order.add_edge(shipment_plan,    customer_engage)
root.order.add_edge(shipment_plan,    traceability_log)