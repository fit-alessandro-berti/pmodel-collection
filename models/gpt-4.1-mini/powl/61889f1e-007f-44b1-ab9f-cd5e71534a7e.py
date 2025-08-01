# Generated from: 61889f1e-007f-44b1-ab9f-cd5e71534a7e.json
# Description: This process details the launch of a niche artisan microbrewery that integrates traditional brewing methods with advanced sensory analytics to create limited edition craft beers. It begins with ingredient sourcing from rare local farms, followed by small-batch brewing cycles tailored through AI-driven recipe adjustments. The process includes sensory panel evaluations, iterative recipe refinement, custom label design reflecting the beer's origin story, and eco-friendly packaging development. Marketing involves engaging local communities via pop-up tastings and digital storytelling campaigns. Finally, distribution leverages a hybrid model combining boutique retail partnerships and direct-to-consumer subscription services, ensuring exclusivity and continuous feedback loops for future batches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
ingredient_sourcing = Transition(label='Ingredient Sourcing')
batch_brewing = Transition(label='Batch Brewing')
ai_tuning = Transition(label='AI Tuning')
sensory_panel = Transition(label='Sensory Panel')
recipe_adjust = Transition(label='Recipe Adjust')
label_design = Transition(label='Label Design')
eco_packaging = Transition(label='Eco Packaging')
popup_setup = Transition(label='Pop-up Setup')
digital_campaign = Transition(label='Digital Campaign')
retail_partner = Transition(label='Retail Partner')
subscription = Transition(label='Subscription')
feedback_loop = Transition(label='Feedback Loop')
inventory_check = Transition(label='Inventory Check')
quality_audit = Transition(label='Quality Audit')
launch_event = Transition(label='Launch Event')

# Loop for small-batch brewing cycles:
# loop = * (Batch Brewing + AI Tuning + Sensory Panel + Recipe Adjust) repeated
# Structure for loop in POWL: *(do A, then either exit or do B then repeat)
# Here, we model:
# A = Batch Brewing
# B = partial order of AI Tuning --> Sensory Panel --> Recipe Adjust

inner_b = StrictPartialOrder(nodes=[ai_tuning, sensory_panel, recipe_adjust])
inner_b.order.add_edge(ai_tuning, sensory_panel)
inner_b.order.add_edge(sensory_panel, recipe_adjust)

brew_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_brewing, inner_b])

# After Ingredient Sourcing, proceed to the loop
# After loop, continue with:
# Label Design
# Eco Packaging

# Marketing activities are two parallel nodes:
# Pop-up Setup and Digital Campaign (concurrent)

marketing = StrictPartialOrder(nodes=[popup_setup, digital_campaign])

# Distribution is a choice (XOR) between Retail Partner and Subscription
distribution = OperatorPOWL(operator=Operator.XOR, children=[retail_partner, subscription])

# After distribution, Feedback Loop happens (feedback on batches)

# Finally, Inventory Check, Quality Audit and Launch Event
# Let's assume Inventory Check and Quality Audit happen concurrently before Launch Event

pre_launch = StrictPartialOrder(nodes=[inventory_check, quality_audit])
launch_seq = StrictPartialOrder(nodes=[pre_launch, launch_event])
launch_seq.order.add_edge(pre_launch, launch_event)  # pre_launch nodes --> launch_event node

# Build main sequence partial order from:
# Ingredient Sourcing --> brew_loop --> Label Design --> Eco Packaging --> marketing --> distribution --> Feedback Loop --> pre_launch --> Launch Event

root = StrictPartialOrder(
    nodes=[ingredient_sourcing, brew_loop, label_design, eco_packaging, marketing, distribution, feedback_loop, pre_launch, launch_event]
)

root.order.add_edge(ingredient_sourcing, brew_loop)
root.order.add_edge(brew_loop, label_design)
root.order.add_edge(label_design, eco_packaging)
root.order.add_edge(eco_packaging, marketing)
root.order.add_edge(marketing, distribution)
root.order.add_edge(distribution, feedback_loop)
root.order.add_edge(feedback_loop, pre_launch)
root.order.add_edge(pre_launch, launch_event)

# Note: The pre_launch is a PO with inventory_check and quality_audit concurrent, connected to launch_event by adding an edge pre_launch --> launch_event inside that PO.
# In root, pre_launch is a single node representing that composite.

# This completes the POWL model