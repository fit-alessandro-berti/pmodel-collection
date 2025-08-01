# Generated from: 65615367-05f9-4d21-a86f-69298ba4575c.json
# Description: This process outlines the complex supply chain for artisan cheese production, focusing on unique sourcing, aging, and distribution steps uncommon in typical food supply chains. It begins with raw milk selection from rare breeds, followed by microflora cultivation, handcrafting curds, controlled aging in variable environments, and ends with bespoke packaging. Quality checkpoints occur at each stage to preserve traditional flavors, while logistics involve temperature-sensitive transport to niche retailers and direct-to-consumer delivery. The process integrates seasonal milk variations and artisan feedback loops to continuously refine product batches and maintain exclusivity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
breed_select = Transition(label='Breed Select')
milk_harvest = Transition(label='Milk Harvest')
microflora_grow = Transition(label='Microflora Grow')
curd_handcraft = Transition(label='Curd Handcraft')
salt_infuse = Transition(label='Salt Infuse')
mold_inoculate = Transition(label='Mold Inoculate')
press_form = Transition(label='Press Form')
aging_control = Transition(label='Aging Control')
flavor_test = Transition(label='Flavor Test')
batch_record = Transition(label='Batch Record')
packaging_design = Transition(label='Packaging Design')
temp_transport = Transition(label='Temp Transport')
retail_deliver = Transition(label='Retail Deliver')
feedback_loop = Transition(label='Feedback Loop')
season_adjust = Transition(label='Season Adjust')
inventory_audit = Transition(label='Inventory Audit')

# Quality checkpoints after key stages = flavor_test + batch_record, treated as a PO (parallel)
quality_check = StrictPartialOrder(nodes=[flavor_test, batch_record])

# Logistics parallel tasks: temp_transport and retail_deliver (concurrent)
logistics = StrictPartialOrder(nodes=[temp_transport, retail_deliver])

# Feedback loop involves iterative refining: 
# Loop on (season_adjust then feedback_loop), looping back to season_adjust
feedback_cycle = OperatorPOWL(operator=Operator.LOOP, children=[
    season_adjust,
    feedback_loop
])

# Supply chain initial selection and preparation steps in sequence:
prep = StrictPartialOrder(nodes=[
    breed_select,
    milk_harvest,
    microflora_grow,
    curd_handcraft,
    salt_infuse,
    mold_inoculate,
    press_form
])
prep.order.add_edge(breed_select, milk_harvest)
prep.order.add_edge(milk_harvest, microflora_grow)
prep.order.add_edge(microflora_grow, curd_handcraft)
prep.order.add_edge(curd_handcraft, salt_infuse)
prep.order.add_edge(salt_infuse, mold_inoculate)
prep.order.add_edge(mold_inoculate, press_form)

# Aging and quality control: aging_control then quality_check (parallel flavor_test & batch_record)
aging_quality = StrictPartialOrder(nodes=[aging_control, quality_check])
aging_quality.order.add_edge(aging_control, quality_check)

# Packaging design after quality check
packaging = packaging_design

# Final logistics after packaging
final_logistics = logistics

# Inventory audit can happen at any time after packaging for control, concurrent with delivery/logistics
post_pack_control = StrictPartialOrder(nodes=[inventory_audit, final_logistics])

# Connect edges in post_pack_control as concurrent (no edges)

# Form the main partial order:
# prep -> aging_quality -> packaging -> post_pack_control -> feedback_cycle (feedback loop is after inventory audit and logistics)
root = StrictPartialOrder(nodes=[
    prep,
    aging_quality,
    packaging,
    post_pack_control,
    feedback_cycle
])

# Define orders:
root.order.add_edge(prep, aging_quality)
root.order.add_edge(aging_quality, packaging)
root.order.add_edge(packaging, post_pack_control)
root.order.add_edge(post_pack_control, feedback_cycle)