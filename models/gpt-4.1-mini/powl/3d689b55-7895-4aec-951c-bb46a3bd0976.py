# Generated from: 3d689b55-7895-4aec-951c-bb46a3bd0976.json
# Description: This process outlines the complex, multi-stage supply chain for artisanal cheese production and distribution. It begins with sourcing rare milk varieties from niche farms, followed by precise curdling under controlled conditions. The cheese undergoes unique aging in microclimates, requiring regular quality inspections and environmental adjustments. Packaging involves sustainable, handcrafted materials to maintain freshness and brand ethos. Distribution channels include exclusive boutique stores and direct-to-consumer delivery with temperature monitoring. Throughout, traceability is ensured via blockchain logging to certify authenticity and origin, while customer feedback is gathered post-sale to refine future batches and marketing strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Formation = Transition(label='Curd Formation')
Temperature_Control = Transition(label='Temperature Control')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Check = Transition(label='Humidity Check')
Quality_Inspect = Transition(label='Quality Inspect')
Microclimate_Adjust = Transition(label='Microclimate Adjust')
Rind_Treatment = Transition(label='Rind Treatment')
Packaging_Prep = Transition(label='Packaging Prep')
Eco_Wrap = Transition(label='Eco Wrap')
Batch_Labeling = Transition(label='Batch Labeling')
Blockchain_Log = Transition(label='Blockchain Log')
Store_Delivery = Transition(label='Store Delivery')
Customer_Survey = Transition(label='Customer Survey')
Feedback_Review = Transition(label='Feedback Review')
Recipe_Update = Transition(label='Recipe Update')

# Group aging related activities into a partial order (can be concurrent or have order)
# From description, aging requires quality inspections and environmental adjustments regularly
# We can model: Aging_Setup -> (Humidity_Check and Quality_Inspect and Microclimate_Adjust in partial order)
aging_subpo = StrictPartialOrder(
    nodes=[Aging_Setup, Humidity_Check, Quality_Inspect, Microclimate_Adjust]
)
aging_subpo.order.add_edge(Aging_Setup, Humidity_Check)
aging_subpo.order.add_edge(Humidity_Check, Quality_Inspect)
aging_subpo.order.add_edge(Quality_Inspect, Microclimate_Adjust)

# Packaging steps, likely sequential
# Packaging Prep -> Eco Wrap -> Batch Labeling
packaging_po = StrictPartialOrder(
    nodes=[Packaging_Prep, Eco_Wrap, Batch_Labeling]
)
packaging_po.order.add_edge(Packaging_Prep, Eco_Wrap)
packaging_po.order.add_edge(Eco_Wrap, Batch_Labeling)

# Distribution channels: choice between Store Delivery and direct delivery (we can include blockchain logging before distribution)
distribution_channels = OperatorPOWL(
    operator=Operator.XOR,
    children=[Store_Delivery, Customer_Survey]  # Customer_Survey is post-sale feedback channel counted as distribution alternative here
)

# Feedback loop: Customer Survey -> Feedback Review -> Recipe Update
feedback_po = StrictPartialOrder(
    nodes=[Customer_Survey, Feedback_Review, Recipe_Update]
)
feedback_po.order.add_edge(Customer_Survey, Feedback_Review)
feedback_po.order.add_edge(Feedback_Review, Recipe_Update)

# Model distribution and feedback as partial order with Blockchain Log before distribution or feedback:
# Blockchain Log -> distribution_channels
# Blockchain Log -> feedback_po (for post-sale traceability and feedback)
distribution_feedback_po = StrictPartialOrder(
    nodes=[Blockchain_Log, distribution_channels, feedback_po]
)
distribution_feedback_po.order.add_edge(Blockchain_Log, distribution_channels)
distribution_feedback_po.order.add_edge(Blockchain_Log, feedback_po)

# Setup initial process steps order:
# Milk Sourcing -> Curd Formation -> Temperature Control -> aging_subpo -> Rind Treatment -> packaging_po -> distribution_feedback_po

root = StrictPartialOrder(
    nodes=[
        Milk_Sourcing,
        Curd_Formation,
        Temperature_Control,
        aging_subpo,
        Rind_Treatment,
        packaging_po,
        distribution_feedback_po,
    ]
)

root.order.add_edge(Milk_Sourcing, Curd_Formation)
root.order.add_edge(Curd_Formation, Temperature_Control)
root.order.add_edge(Temperature_Control, aging_subpo)
root.order.add_edge(aging_subpo, Rind_Treatment)
root.order.add_edge(Rind_Treatment, packaging_po)
root.order.add_edge(packaging_po, distribution_feedback_po)