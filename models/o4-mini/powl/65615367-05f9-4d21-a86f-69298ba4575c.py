# Generated from: 65615367-05f9-4d21-a86f-69298ba4575c.json
# Description: This process outlines the complex supply chain for artisan cheese production, focusing on unique sourcing, aging, and distribution steps uncommon in typical food supply chains. It begins with raw milk selection from rare breeds, followed by microflora cultivation, handcrafting curds, controlled aging in variable environments, and ends with bespoke packaging. Quality checkpoints occur at each stage to preserve traditional flavors, while logistics involve temperature-sensitive transport to niche retailers and direct-to-consumer delivery. The process integrates seasonal milk variations and artisan feedback loops to continuously refine product batches and maintain exclusivity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# 1. Define all activity transitions
breed_select     = Transition(label='Breed Select')
milk_harvest     = Transition(label='Milk Harvest')
season_adjust    = Transition(label='Season Adjust')
microflora_grow  = Transition(label='Microflora Grow')
curd_handcraft   = Transition(label='Curd Handcraft')
salt_infuse      = Transition(label='Salt Infuse')
mold_inoculate   = Transition(label='Mold Inoculate')
press_form       = Transition(label='Press Form')
aging_control    = Transition(label='Aging Control')
flavor_test      = Transition(label='Flavor Test')
batch_record     = Transition(label='Batch Record')
packaging_design = Transition(label='Packaging Design')
temp_transport   = Transition(label='Temp Transport')
retail_deliver   = Transition(label='Retail Deliver')
feedback_loop    = Transition(label='Feedback Loop')
inventory_audit  = Transition(label='Inventory Audit')

# 2. Build the main (body) partial order
body = StrictPartialOrder(nodes=[
    breed_select, milk_harvest, season_adjust, microflora_grow,
    curd_handcraft, salt_infuse, mold_inoculate, press_form,
    aging_control, flavor_test, batch_record, packaging_design,
    temp_transport, retail_deliver
])

# Define the sequential dependencies
body.order.add_edge(breed_select,    milk_harvest)
body.order.add_edge(milk_harvest,    season_adjust)
body.order.add_edge(season_adjust,   microflora_grow)
body.order.add_edge(microflora_grow, curd_handcraft)
body.order.add_edge(curd_handcraft,  salt_infuse)
body.order.add_edge(salt_infuse,     mold_inoculate)
body.order.add_edge(mold_inoculate,  press_form)
body.order.add_edge(press_form,      aging_control)
body.order.add_edge(aging_control,   flavor_test)
body.order.add_edge(flavor_test,     batch_record)
body.order.add_edge(batch_record,    packaging_design)
body.order.add_edge(packaging_design, temp_transport)
body.order.add_edge(temp_transport,  retail_deliver)

# 3. Build the feedback-loop partial order (redo branch)
feedback_flow = StrictPartialOrder(nodes=[feedback_loop, inventory_audit])
feedback_flow.order.add_edge(feedback_loop, inventory_audit)

# 4. Wrap the full process in a LOOP: do the body, then either exit or do feedback_flow and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body, feedback_flow]
)