# Generated from: ef1a0fbc-d3ef-4b0e-a3d3-13ea033dcc6c.json
# Description: This process details the intricate and highly specialized supply chain management for artisanal cheese production, starting from sourcing rare milk varieties from micro-farms, through controlled fermentation and aging in unique environmental conditions, to bespoke packaging and distribution to niche gourmet retailers worldwide. It involves coordination with local farmers, quality testing at multiple stages, compliance with food safety regulations, custom labeling, and handling of rare ingredient procurement. Additionally, the process integrates seasonal adjustments based on milk availability, real-time inventory tracking, and direct consumer feedback loops for continuous product refinement and artisan branding enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
milk_sourcing = Transition(label='Milk Sourcing')
farm_selection = Transition(label='Farm Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_fulfill = Transition(label='Order Fulfill')
retail_shipping = Transition(label='Retail Shipping')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for seasonal adjustment and milk availability feedback:
# Loop body:
#   milk_sourcing + farm_selection + quality_testing + milk_pasteurize + starter_culture + coagulation + curd_cutting + whey_draining + mold_inoculate + aging_control + flavor_tasting
# This part cycles until exit

# Construct partial order for milk processing sequence within loop
milk_processing = StrictPartialOrder(nodes=[
    milk_sourcing, farm_selection, quality_testing, milk_pasteurize,
    starter_culture, coagulation, curd_cutting, whey_draining,
    mold_inoculate, aging_control, flavor_tasting
])
milk_processing.order.add_edge(milk_sourcing, farm_selection)
milk_processing.order.add_edge(farm_selection, quality_testing)
milk_processing.order.add_edge(quality_testing, milk_pasteurize)
milk_processing.order.add_edge(milk_pasteurize, starter_culture)
milk_processing.order.add_edge(starter_culture, coagulation)
milk_processing.order.add_edge(coagulation, curd_cutting)
milk_processing.order.add_edge(curd_cutting, whey_draining)
milk_processing.order.add_edge(whey_draining, mold_inoculate)
milk_processing.order.add_edge(mold_inoculate, aging_control)
milk_processing.order.add_edge(aging_control, flavor_tasting)

# Loop node with milk_processing as A, and skip as B to allow exit
# Actually, LOOP(A,B) means: execute A, then choose to exit or execute B then A again
# For a typical loop with feedback, B is the body that runs before it loops back to A,
# but here it's natural to put A as milk_processing, and B as inventory audit and feedback cycle

# Define inventory and order fulfillment partial order (loop body B)
inventory_audit_node = inventory_audit
order_fulfill_node = order_fulfill
retail_shipping_node = retail_shipping

# Partial order for post-aging processing and distribution
post_processing = StrictPartialOrder(nodes=[
    packaging_design, label_approval, inventory_audit_node, order_fulfill_node, retail_shipping_node
])
# packaging_design and label_approval in sequence
post_processing.order.add_edge(packaging_design, label_approval)
# After label approval start inventory audit concurrently with order fulfillment process 
# Assume inventory audit happens before order fulfill, but order fulfill must precede retail shipping

post_processing.order.add_edge(label_approval, inventory_audit_node)
post_processing.order.add_edge(inventory_audit_node, order_fulfill_node)
post_processing.order.add_edge(order_fulfill_node, retail_shipping_node)

# The inventory feedback loop is integrated in the LOOP body as the repeated part
# The model: LOOP(A, B), where A = milk_processing, B = post_processing

loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_processing, post_processing])

root = loop