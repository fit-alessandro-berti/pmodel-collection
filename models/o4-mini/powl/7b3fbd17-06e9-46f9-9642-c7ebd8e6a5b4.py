# Generated from: 7b3fbd17-06e9-46f9-9642-c7ebd8e6a5b4.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to niche gourmet shops. It starts with careful milk sourcing from heritage breeds, continues through precise fermentation and aging conditions tailored for flavor profiles, includes intermittent quality tastings by expert affineurs, and integrates sustainable packaging choices. The process also manages limited batch production scheduling, coordinates with local transport for freshness, involves direct communications with specialty retailers, and incorporates consumer feedback loops to refine future batches. Each stage demands close attention to detail to preserve the unique qualities that differentiate artisanal cheese from mass-produced alternatives, ensuring a premium product reaches discerning customers in optimal condition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
starter_prep     = Transition(label='Starter Prep')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
mold_inoculation = Transition(label='Mold Inoculation')
pressing_cheese  = Transition(label='Pressing Cheese')
salt_brining     = Transition(label='Salt Brining')
fermentation     = Transition(label='Fermentation')
aging_control    = Transition(label='Aging Control')
taste_sampling   = Transition(label='Taste Sampling')
batch_labeling   = Transition(label='Batch Labeling')
sustainable_pack = Transition(label='Sustainable Pack')
order_scheduling = Transition(label='Order Scheduling')
local_shipping   = Transition(label='Local Shipping')
retail_liaison   = Transition(label='Retail Liaison')
feedback_review  = Transition(label='Feedback Review')

# 1) Milk sourcing then quality testing
po1 = StrictPartialOrder(nodes=[milk_sourcing, quality_testing])
po1.order.add_edge(milk_sourcing, quality_testing)

# 2) Starter prep through salt brining
po2 = StrictPartialOrder(nodes=[
    starter_prep, curd_cutting, whey_draining,
    mold_inoculation, pressing_cheese, salt_brining
])
po2.order.add_edge(starter_prep, curd_cutting)
po2.order.add_edge(curd_cutting, whey_draining)
po2.order.add_edge(whey_draining, mold_inoculation)
po2.order.add_edge(mold_inoculation, pressing_cheese)
po2.order.add_edge(pressing_cheese, salt_brining)

# 3) Fermentation then aging
po_ferment = StrictPartialOrder(nodes=[fermentation, aging_control])
po_ferment.order.add_edge(fermentation, aging_control)

# Loop for intermittent taste sampling during fermentation/aging
loop_quality = OperatorPOWL(
    operator=Operator.LOOP,
    children=[po_ferment, taste_sampling]
)

# 4) Post‐processing: labeling → packaging → scheduling → shipping → liaison
po_body = StrictPartialOrder(nodes=[
    batch_labeling, sustainable_pack,
    order_scheduling, local_shipping, retail_liaison
])
po_body.order.add_edge(batch_labeling, sustainable_pack)
po_body.order.add_edge(sustainable_pack, order_scheduling)
po_body.order.add_edge(order_scheduling, local_shipping)
po_body.order.add_edge(local_shipping, retail_liaison)

# Loop for consumer feedback to refine future batches
loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[po_body, feedback_review]
)

# 5) Combine everything into the root partial order
root = StrictPartialOrder(nodes=[po1, po2, loop_quality, loop_feedback])
root.order.add_edge(po1, po2)
root.order.add_edge(po2, loop_quality)
root.order.add_edge(loop_quality, loop_feedback)