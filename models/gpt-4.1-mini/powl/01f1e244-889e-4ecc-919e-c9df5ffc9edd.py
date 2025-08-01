# Generated from: 01f1e244-889e-4ecc-919e-c9df5ffc9edd.json
# Description: This process outlines the intricate journey of artisan cheese production and distribution, starting from raw milk sourcing on small farms, through traditional curdling and aging methods, quality assurance by expert tasters, custom packaging, and finally niche market delivery. The chain integrates seasonal milk variations, manual aging adjustments, artisan branding, compliance with food safety standards, and direct customer feedback loops to maintain product uniqueness and authenticity across diverse regional markets. Each step requires expert craftsmanship combined with logistical coordination to preserve the delicate flavor profiles and cultural heritage of the cheese varieties produced.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Curd_Preparation = Transition(label='Curd Preparation')
Whey_Separation = Transition(label='Whey Separation')
Press_Molding = Transition(label='Press Molding')
Salting_Process = Transition(label='Salting Process')
Aging_Control = Transition(label='Aging Control')
Flavor_Infusion = Transition(label='Flavor Infusion')
Texture_Assessment = Transition(label='Texture Assessment')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Batch_Tracking = Transition(label='Batch Tracking')
Regulatory_Check = Transition(label='Regulatory Check')
Market_Delivery = Transition(label='Market Delivery')
Customer_Review = Transition(label='Customer Review')

# Construct the partial orders and loops for the detailed process:

# Step 1: Milk Sourcing

# Step 2 & 3: Quality Testing and Curd Preparation proceed in order
quality_curd_po = StrictPartialOrder(nodes=[Quality_Testing, Curd_Preparation])
quality_curd_po.order.add_edge(Quality_Testing, Curd_Preparation)

# Step 4, 5 and 6: Whey Separation -> Press Molding -> Salting Process
whey_press_salt_po = StrictPartialOrder(nodes=[Whey_Separation, Press_Molding, Salting_Process])
whey_press_salt_po.order.add_edge(Whey_Separation, Press_Molding)
whey_press_salt_po.order.add_edge(Press_Molding, Salting_Process)

# Step 7-9: Aging Control, Flavor Infusion, Texture Assessment happen sequentially,
ag_texture_po = StrictPartialOrder(nodes=[Aging_Control, Flavor_Infusion, Texture_Assessment])
ag_texture_po.order.add_edge(Aging_Control, Flavor_Infusion)
ag_texture_po.order.add_edge(Flavor_Infusion, Texture_Assessment)

# Step 10-13: Packaging Design, Label Printing, Batch Tracking, Regulatory Check 
packaging_po = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing, Batch_Tracking, Regulatory_Check])
packaging_po.order.add_edge(Packaging_Design, Label_Printing)
packaging_po.order.add_edge(Label_Printing, Batch_Tracking)
packaging_po.order.add_edge(Batch_Tracking, Regulatory_Check)

# Step 14-15: Market Delivery then Customer Review in sequence,
delivery_review_po = StrictPartialOrder(nodes=[Market_Delivery, Customer_Review])
delivery_review_po.order.add_edge(Market_Delivery, Customer_Review)

# Loop for Aging Control adjustments (manual aging adjustments and feedback loop from Customer Review)
# Loop body: (Aging_Control) then choice to exit or Customer_Review then back to Aging_Control

loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Aging_Control, Customer_Review]
)

# Integration of Quality Testing branching due to seasonal milk variation - model as choice between
# continuing with Quality_Testing or skipping Quality_Testing (silent skip) to represent seasonal variations
skip = SilentTransition()
quality_choice = OperatorPOWL(operator=Operator.XOR, children=[Quality_Testing, skip])

# Build the large partial order
# Nodes: Milk_Sourcing -> quality_choice -> Curd_Preparation -> Whey_Separation .. etc
# Replace Quality_Testing with quality_choice

nodes = [
    Milk_Sourcing,
    quality_choice,
    Curd_Preparation,
    Whey_Separation,
    Press_Molding,
    Salting_Process,
    loop_aging,  # loop replaces Aging_Control node, combined with Customer_Review
    Flavor_Infusion,
    Texture_Assessment,
    Packaging_Design,
    Label_Printing,
    Batch_Tracking,
    Regulatory_Check,
    Market_Delivery,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for sequence
root.order.add_edge(Milk_Sourcing, quality_choice)
root.order.add_edge(quality_choice, Curd_Preparation)
root.order.add_edge(Curd_Preparation, Whey_Separation)
root.order.add_edge(Whey_Separation, Press_Molding)
root.order.add_edge(Press_Molding, Salting_Process)
root.order.add_edge(Salting_Process, loop_aging)  # loop includes Aging_Control part
root.order.add_edge(loop_aging, Flavor_Infusion)
root.order.add_edge(Flavor_Infusion, Texture_Assessment)
root.order.add_edge(Texture_Assessment, Packaging_Design)
root.order.add_edge(Packaging_Design, Label_Printing)
root.order.add_edge(Label_Printing, Batch_Tracking)
root.order.add_edge(Batch_Tracking, Regulatory_Check)
root.order.add_edge(Regulatory_Check, Market_Delivery)

# Market_Delivery and Customer_Review inside the loop, so no direct edges outside

# We do not add Customer_Review as separate node outside loop since it is inside loop_aging

# This models the sequential flow, with a loop for aging control adjustments based on customer reviews,
# and a choice simulating seasonal variability in quality testing
