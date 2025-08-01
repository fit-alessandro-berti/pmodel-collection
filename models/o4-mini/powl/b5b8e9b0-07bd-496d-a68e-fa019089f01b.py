# Generated from: b5b8e9b0-07bd-496d-a68e-fa019089f01b.json
# Description: This process outlines the end-to-end supply chain management of a small-scale artisan microbrewery that specializes in rare hop varieties and seasonal brews. It involves sourcing unique ingredients from remote farms, custom fermentation monitoring, small-batch quality control, adaptive packaging design, and direct-to-consumer distribution through niche channels. The process integrates traditional brewing techniques with modern IoT sensors for environment regulation, includes community feedback loops for recipe refinement, and leverages sustainable logistics practices to minimize carbon footprint while maintaining artisanal quality and exclusivity in the craft beer market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
hop_sourcing      = Transition(label='Hop Sourcing')
malt_selection    = Transition(label='Malt Selection')
water_testing     = Transition(label='Water Testing')
yeast_culturing   = Transition(label='Yeast Culturing')
batch_planning    = Transition(label='Batch Planning')
sensor_setup      = Transition(label='Sensor Setup')
fermentation_start= Transition(label='Fermentation Start')
quality_sampling  = Transition(label='Quality Sampling')
recipe_adjust     = Transition(label='Recipe Adjust')
packaging_design  = Transition(label='Packaging Design')
label_printing    = Transition(label='Label Printing')
bottling_run      = Transition(label='Bottling Run')
cold_storage      = Transition(label='Cold Storage')
order_processing  = Transition(label='Order Processing')
direct_shipping   = Transition(label='Direct Shipping')
customer_feedback = Transition(label='Customer Feedback')
waste_recycling   = Transition(label='Waste Recycling')
inventory_audit   = Transition(label='Inventory Audit')

# Define loops
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_sampling, recipe_adjust])
feedback_loop   = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, recipe_adjust])

# Build the partial order
root = StrictPartialOrder(nodes=[
    hop_sourcing, malt_selection, water_testing, yeast_culturing,
    batch_planning,
    sensor_setup,
    fermentation_start,
    monitoring_loop,
    packaging_design, label_printing, bottling_run, cold_storage,
    order_processing, direct_shipping,
    feedback_loop,
    waste_recycling, inventory_audit
])

# Constrain sourcing and prep to come before planning
for prep in [hop_sourcing, malt_selection, water_testing, yeast_culturing]:
    root.order.add_edge(prep, batch_planning)

# Sequence of brewing
root.order.add_edge(batch_planning, sensor_setup)
root.order.add_edge(sensor_setup, fermentation_start)
root.order.add_edge(fermentation_start, monitoring_loop)
root.order.add_edge(monitoring_loop, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, bottling_run)
root.order.add_edge(bottling_run, cold_storage)

# Distribution and feedback
root.order.add_edge(cold_storage, order_processing)
root.order.add_edge(order_processing, direct_shipping)
root.order.add_edge(direct_shipping, feedback_loop)

# Sustainable logistics in parallel after storage
root.order.add_edge(cold_storage, waste_recycling)
root.order.add_edge(cold_storage, inventory_audit)