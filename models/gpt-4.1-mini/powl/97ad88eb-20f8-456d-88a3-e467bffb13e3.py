# Generated from: 97ad88eb-20f8-456d-88a3-e467bffb13e3.json
# Description: This process details the end-to-end supply chain of artisan cheese production, starting from raw milk sourcing from local farms, through specialized fermentation and aging stages in climate-controlled environments. It includes quality inspections, packaging with eco-friendly materials, and coordinating limited batch logistics to boutique retailers and gourmet restaurants. The process also involves seasonal recipe adjustments based on milk composition, direct customer feedback integration for flavor profiling, and regulatory compliance checks to ensure product safety and authenticity. This atypical process highlights the delicate balance between traditional craftsmanship and modern supply chain management in a niche food sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Starter_Culture = Transition(label='Starter Culture')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Press_Mold = Transition(label='Press Mold')
Brine_Soak = Transition(label='Brine Soak')
Aging_Control = Transition(label='Aging Control')
Flavor_Check = Transition(label='Flavor Check')
Recipe_Adjust = Transition(label='Recipe Adjust')
Eco_Packaging = Transition(label='Eco Packaging')
Batch_Label = Transition(label='Batch Label')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Review = Transition(label='Customer Review')
Compliance_Audit = Transition(label='Compliance Audit')

# Model explanation & structuring:
# - Start: Milk Sourcing --> Quality Testing --> Milk Pasteurize
# - Then Starter Culture --> Curd Cutting --> Whey Drain --> Press Mold --> Brine Soak
# - Aging Control and Flavor Check run concurrently after Brine Soak
# - Loop for seasonal recipe adjustments: Recipe_Adjust followed by Aging Control and Flavor Check again
# - After aging and flavor checks done/finalized -> Packaging sequence: Eco Packaging -> Batch Label
# - Then logistics planning and delivery: Logistics Plan -> Retail Delivery
# - After delivery, Customer Review and Compliance Audit run concurrently
# - The Recipe_Adjust loop models repeated improvements based on feedback and milk composition

# Define the loop on recipe adjustment and aging/flavor control
aging_flavor_po = StrictPartialOrder(nodes=[Aging_Control, Flavor_Check])
# no order edges: concurrent activities

# Loop: * (Recipe_Adjust, aging_flavor_po)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Recipe_Adjust, aging_flavor_po])

# Packaging partial order: Eco Packaging then Batch Label
packaging_po = StrictPartialOrder(nodes=[Eco_Packaging, Batch_Label])
packaging_po.order.add_edge(Eco_Packaging, Batch_Label)

# Logistics partial order: Logistics Plan then Retail Delivery
logistics_po = StrictPartialOrder(nodes=[Logistics_Plan, Retail_Delivery])
logistics_po.order.add_edge(Logistics_Plan, Retail_Delivery)

# Post delivery concurrent activities: Customer Review and Compliance Audit
post_delivery_po = StrictPartialOrder(nodes=[Customer_Review, Compliance_Audit])
# no edges - concurrent

# Upstream process sequence partial order for initial cheese making steps
initial_po = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Milk_Pasteurize,
    Starter_Culture, Curd_Cutting, Whey_Drain, Press_Mold, Brine_Soak])
# Add edges to model sequence:
initial_po.order.add_edge(Milk_Sourcing, Quality_Testing)
initial_po.order.add_edge(Quality_Testing, Milk_Pasteurize)
initial_po.order.add_edge(Milk_Pasteurize, Starter_Culture)
initial_po.order.add_edge(Starter_Culture, Curd_Cutting)
initial_po.order.add_edge(Curd_Cutting, Whey_Drain)
initial_po.order.add_edge(Whey_Drain, Press_Mold)
initial_po.order.add_edge(Press_Mold, Brine_Soak)

# After brine soak, aging and flavor check concurrent
# So create partial order that continues: brine soak --> loop (recipe_adjust and aging/flavor)
# and initial_po --> loop
# then loop --> packaging_po --> logistics_po --> post_delivery_po

root = StrictPartialOrder(nodes=[initial_po, loop, packaging_po, logistics_po, post_delivery_po])
root.order.add_edge(initial_po, loop)
root.order.add_edge(loop, packaging_po)
root.order.add_edge(packaging_po, logistics_po)
root.order.add_edge(logistics_po, post_delivery_po)