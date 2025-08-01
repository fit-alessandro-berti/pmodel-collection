# Generated from: 61889f1e-007f-44b1-ab9f-cd5e71534a7e.json
# Description: This process details the launch of a niche artisan microbrewery that integrates traditional brewing methods with advanced sensory analytics to create limited edition craft beers. It begins with ingredient sourcing from rare local farms, followed by small-batch brewing cycles tailored through AI-driven recipe adjustments. The process includes sensory panel evaluations, iterative recipe refinement, custom label design reflecting the beer's origin story, and eco-friendly packaging development. Marketing involves engaging local communities via pop-up tastings and digital storytelling campaigns. Finally, distribution leverages a hybrid model combining boutique retail partnerships and direct-to-consumer subscription services, ensuring exclusivity and continuous feedback loops for future batches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
ingredient_sourcing = Transition(label='Ingredient Sourcing')
batch_brewing      = Transition(label='Batch Brewing')
ai_tuning          = Transition(label='AI Tuning')
sensory_panel      = Transition(label='Sensory Panel')
recipe_adjust      = Transition(label='Recipe Adjust')
label_design       = Transition(label='Label Design')
eco_packaging      = Transition(label='Eco Packaging')
pop_up_setup       = Transition(label='Pop-up Setup')
digital_campaign   = Transition(label='Digital Campaign')
retail_partner     = Transition(label='Retail Partner')
subscription       = Transition(label='Subscription')
feedback_loop      = Transition(label='Feedback Loop')
inventory_check    = Transition(label='Inventory Check')
quality_audit      = Transition(label='Quality Audit')
launch_event       = Transition(label='Launch Event')

# Build the brewing cycle as a StrictPartialOrder (A)
cycleA = StrictPartialOrder(
    nodes=[batch_brewing, ai_tuning, sensory_panel, recipe_adjust]
)
cycleA.order.add_edge(batch_brewing, ai_tuning)
cycleA.order.add_edge(ai_tuning, sensory_panel)
cycleA.order.add_edge(sensory_panel, recipe_adjust)

# Build the repeat‐body of the loop as another copy (B)
cycleB = StrictPartialOrder(
    nodes=[batch_brewing, ai_tuning, sensory_panel, recipe_adjust]
)
cycleB.order.add_edge(batch_brewing, ai_tuning)
cycleB.order.add_edge(ai_tuning, sensory_panel)
cycleB.order.add_edge(sensory_panel, recipe_adjust)

# Create the loop operator: do cycleA once, then either exit or do cycleB then cycleA again, etc.
brewing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycleA, cycleB]
)

# Marketing parallel: pop‐up tastings and digital storytelling
marketing = StrictPartialOrder(nodes=[pop_up_setup, digital_campaign])
# no edges => they are concurrent

# Distribution parallel: retail and subscription
distribution = StrictPartialOrder(nodes=[retail_partner, subscription])
# no edges => they are concurrent

# Root partial order assembling the entire process
root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    brewing_loop,
    label_design,
    eco_packaging,
    inventory_check,
    quality_audit,
    marketing,
    distribution,
    feedback_loop,
    launch_event
])

# Define the control‐flow edges
root.order.add_edge(ingredient_sourcing, brewing_loop)
root.order.add_edge(brewing_loop, label_design)
root.order.add_edge(label_design, eco_packaging)
root.order.add_edge(eco_packaging, inventory_check)
root.order.add_edge(inventory_check, quality_audit)
root.order.add_edge(quality_audit, marketing)
root.order.add_edge(marketing, distribution)
root.order.add_edge(distribution, feedback_loop)
# feedback_loop sends control back into the brewing loop for future batches
root.order.add_edge(feedback_loop, brewing_loop)
# final launch event after distribution
root.order.add_edge(distribution, launch_event)