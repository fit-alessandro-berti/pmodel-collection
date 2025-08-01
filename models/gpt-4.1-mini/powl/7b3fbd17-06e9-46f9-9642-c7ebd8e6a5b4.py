# Generated from: 7b3fbd17-06e9-46f9-9642-c7ebd8e6a5b4.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to niche gourmet shops. It starts with careful milk sourcing from heritage breeds, continues through precise fermentation and aging conditions tailored for flavor profiles, includes intermittent quality tastings by expert affineurs, and integrates sustainable packaging choices. The process also manages limited batch production scheduling, coordinates with local transport for freshness, involves direct communications with specialty retailers, and incorporates consumer feedback loops to refine future batches. Each stage demands close attention to detail to preserve the unique qualities that differentiate artisanal cheese from mass-produced alternatives, ensuring a premium product reaches discerning customers in optimal condition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all individual activities as POWL transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculation = Transition(label='Mold Inoculation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Brining = Transition(label='Salt Brining')
Fermentation = Transition(label='Fermentation')
Aging_Control = Transition(label='Aging Control')
Taste_Sampling = Transition(label='Taste Sampling')
Batch_Labeling = Transition(label='Batch Labeling')
Sustainable_Pack = Transition(label='Sustainable Pack')
Order_Scheduling = Transition(label='Order Scheduling')
Local_Shipping = Transition(label='Local Shipping')
Retail_Liaison = Transition(label='Retail Liaison')
Feedback_Review = Transition(label='Feedback Review')

# Construct the fermentation and aging partial order with intermittent taste sampling
# Sequence: Milk Sourcing -> Starter Prep -> Curd Cutting -> Whey Draining -> Mold Inoculation -> Pressing Cheese -> Salt Brining 
# -> Fermentation (with looping control by Aging Control and Taste Sampling)
pre_fermentation_nodes = [
    Milk_Sourcing,
    Starter_Prep,
    Curd_Cutting,
    Whey_Draining,
    Mold_Inoculation,
    Pressing_Cheese,
    Salt_Brining
]

# Fermentation and aging loop:
# Loop (Fermentation, XOR(Taste Sampling, Aging Control))
# The aging control leads to the choice of exiting or looping again (taste sampling triggers another aging cycle)
aging_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[Taste_Sampling, Aging_Control])
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Fermentation, aging_loop_choice])

# Sequencing pre-fermentation activities to fermentation loop
fermentation_segment = StrictPartialOrder(nodes=pre_fermentation_nodes + [fermentation_loop])
for i in range(len(pre_fermentation_nodes) - 1):
    fermentation_segment.order.add_edge(pre_fermentation_nodes[i], pre_fermentation_nodes[i + 1])
fermentation_segment.order.add_edge(pre_fermentation_nodes[-1], fermentation_loop)

# After fermentation loop: Batch Labeling
# Then sustainable packing and order scheduling can be concurrent with local shipping
# Retail liaison after local shipping
batch_pack_schedule = StrictPartialOrder(nodes=[Batch_Labeling, Sustainable_Pack, Order_Scheduling])
batch_pack_schedule.order.add_edge(Batch_Labeling, Sustainable_Pack)
batch_pack_schedule.order.add_edge(Batch_Labeling, Order_Scheduling)

# Local shipping after packing and scheduling
shipping_segment = StrictPartialOrder(nodes=[batch_pack_schedule, Local_Shipping])
shipping_segment.order.add_edge(batch_pack_schedule, Local_Shipping)

# Retail liaison after local shipping
retail_segment = StrictPartialOrder(nodes=[Local_Shipping, Retail_Liaison])
retail_segment.order.add_edge(Local_Shipping, Retail_Liaison)

# Quality testing can be done after Milk Sourcing and intermittently before fermentation begins
# It happens right after Milk Sourcing and before Starter Prep (strict order Milk Sourcing->Quality Testing->Starter Prep)
quality_segment = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Prep])
quality_segment.order.add_edge(Milk_Sourcing, Quality_Testing)
quality_segment.order.add_edge(Quality_Testing, Starter_Prep)

# Replace the pre_fermentation_nodes start with quality segment start (Milk Sourcing -> Quality Testing -> Starter Prep)
# So the pre_fermentation_nodes except Milk_Sourcing are replaced by quality_segment nodes from Milk_Sourcing onward
# We'll reconstruct fermentation_segment accordingly:

# New fermentation_segment:
# Nodes: all without Milk_Sourcing + quality_segment + fermentation_loop
# Wait, to keep unique references for edges, we'll have:
# quality_segment nodes: Milk_Sourcing, Quality_Testing, Starter_Prep
# then Curd Cutting -> Whey Draining -> ... as before

post_starter_nodes = [
    Curd_Cutting,
    Whey_Draining,
    Mold_Inoculation,
    Pressing_Cheese,
    Salt_Brining
]

fermentation_segment = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Prep] + post_starter_nodes + [fermentation_loop])

# Edges for quality segment
fermentation_segment.order.add_edge(Milk_Sourcing, Quality_Testing)
fermentation_segment.order.add_edge(Quality_Testing, Starter_Prep)

# Edges from Starter_Prep to post_starter_nodes
fermentation_segment.order.add_edge(Starter_Prep, Curd_Cutting)
for i in range(len(post_starter_nodes) - 1):
    fermentation_segment.order.add_edge(post_starter_nodes[i], post_starter_nodes[i + 1])

# Last post_starter node to fermentation loop
fermentation_segment.order.add_edge(post_starter_nodes[-1], fermentation_loop)

# Feedback Review loops back to Batch Labeling, representing consumer feedback for refining batches
# Model feedback loop: loop(Batch_Labeling, Feedback_Review)
batch_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Batch_Labeling, Feedback_Review])

# Now, Sustainable Pack, Order Scheduling proceed after the feedback loop exits
post_feedback_segment = StrictPartialOrder(nodes=[batch_feedback_loop, Sustainable_Pack, Order_Scheduling])
post_feedback_segment.order.add_edge(batch_feedback_loop, Sustainable_Pack)
post_feedback_segment.order.add_edge(batch_feedback_loop, Order_Scheduling)

# Local Shipping after those
shipping_segment = StrictPartialOrder(nodes=[post_feedback_segment, Local_Shipping])
shipping_segment.order.add_edge(post_feedback_segment, Local_Shipping)

# Retail Liaison after shipping
retail_segment = StrictPartialOrder(nodes=[Local_Shipping, Retail_Liaison])
retail_segment.order.add_edge(Local_Shipping, Retail_Liaison)

# Compose the full order: fermentation_segment --> post_feedback_segment --> local shipping --> retail
root = StrictPartialOrder(nodes=[
    fermentation_segment,
    post_feedback_segment,
    Local_Shipping,
    Retail_Liaison
])
root.order.add_edge(fermentation_segment, post_feedback_segment)
root.order.add_edge(post_feedback_segment, Local_Shipping)
root.order.add_edge(Local_Shipping, Retail_Liaison)