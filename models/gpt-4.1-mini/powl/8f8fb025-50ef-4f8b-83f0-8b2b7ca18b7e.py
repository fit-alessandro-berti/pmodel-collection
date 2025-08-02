# Generated from: 8f8fb025-50ef-4f8b-83f0-8b2b7ca18b7e.json
# Description: This process manages the end-to-end supply chain of artisanal cheese, beginning with sourcing rare milk varieties from local farms, followed by specialized fermentation and aging phases conducted in controlled environments. Quality inspections occur at multiple stages, including raw material intake, mid-fermentation checks, and pre-shipment assessment. Unique packaging is designed to preserve flavor and freshness, incorporating biodegradable materials. Distribution involves coordinating with niche gourmet retailers and direct-to-consumer channels, ensuring traceability and adherence to organic certifications throughout. Seasonal demand fluctuations require dynamic inventory adjustment and flexible logistics planning. Customer feedback loops influence future batch recipes and supply decisions, creating a continuous improvement cycle for this specialized product line.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_check = Transition(label='Quality Check')
fermentation_start = Transition(label='Fermentation Start')
mid_check = Transition(label='Mid-Check')
aging_control = Transition(label='Aging Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
eco_packaging = Transition(label='Eco Packaging')
inventory_update = Transition(label='Inventory Update')
order_processing = Transition(label='Order Processing')
logistics_plan = Transition(label='Logistics Plan')
retail_coordination = Transition(label='Retail Coordination')
direct_shipping = Transition(label='Direct Shipping')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjust = Transition(label='Recipe Adjust')

# Quality inspections partial order (quality_check after milk_sourcing, and mid_check after fermentation_start)
quality_inspections = StrictPartialOrder(nodes=[quality_check, mid_check])
quality_inspections.order.add_edge(quality_check, mid_check)

# Fermentation and aging partial order: fermentation_start --> mid_check --> aging_control --> flavor_testing
fermentation_aging = StrictPartialOrder(nodes=[fermentation_start, mid_check, aging_control, flavor_testing])
fermentation_aging.order.add_edge(fermentation_start, mid_check)
fermentation_aging.order.add_edge(mid_check, aging_control)
fermentation_aging.order.add_edge(aging_control, flavor_testing)

# Packaging partial order: packaging_design --> eco_packaging
packaging = StrictPartialOrder(nodes=[packaging_design, eco_packaging])
packaging.order.add_edge(packaging_design, eco_packaging)

# Distribution partial order: logistics_plan --> (retail_coordination XOR direct_shipping)
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, direct_shipping])
distribution = StrictPartialOrder(nodes=[logistics_plan, distribution_choice])
distribution.order.add_edge(logistics_plan, distribution_choice)

# Inventory update and logistics planning may be done sequentially after packaging
inventory_and_logistics = StrictPartialOrder(nodes=[inventory_update, distribution])
inventory_and_logistics.order.add_edge(inventory_update, distribution)

# Customer feedback loop modeled as LOOP: 
# loop = *(customer_feedback, recipe_adjust)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, recipe_adjust])

# Overall process partial order:
# Start with milk_sourcing
# Then quality_check and fermentation_aging run with dependency (enforce order via quality_check and fermentation chain)
# Then packaging after flavor_testing
# Then inventory update and distribution
# Then customer feedback loop
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_check,
    fermentation_start,
    mid_check,
    aging_control,
    flavor_testing,
    packaging_design,
    eco_packaging,
    inventory_update,
    order_processing,
    logistics_plan,
    retail_coordination,
    direct_shipping,
    customer_feedback,
    recipe_adjust,
    feedback_loop
])

# Define order relations:
root.order.add_edge(milk_sourcing, quality_check)
root.order.add_edge(milk_sourcing, fermentation_start)

root.order.add_edge(quality_check, mid_check)
root.order.add_edge(fermentation_start, mid_check)
root.order.add_edge(mid_check, aging_control)
root.order.add_edge(aging_control, flavor_testing)

root.order.add_edge(flavor_testing, packaging_design)
root.order.add_edge(packaging_design, eco_packaging)

root.order.add_edge(eco_packaging, inventory_update)

root.order.add_edge(inventory_update, order_processing)
root.order.add_edge(order_processing, logistics_plan)

root.order.add_edge(logistics_plan, retail_coordination)
root.order.add_edge(logistics_plan, direct_shipping)

root.order.add_edge(feedback_loop, recipe_adjust)
# To close feedback loop: recipe_adjust enables next feedback iteration (loop operator handles repetition)
# The feedback loop is attached after distribution and order_processing to reflect continuous improvement cycle

root.order.add_edge(direct_shipping, feedback_loop)
root.order.add_edge(retail_coordination, feedback_loop)
root.order.add_edge(order_processing, feedback_loop)