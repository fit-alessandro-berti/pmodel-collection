# Generated from: b5b8e9b0-07bd-496d-a68e-fa019089f01b.json
# Description: This process outlines the end-to-end supply chain management of a small-scale artisan microbrewery that specializes in rare hop varieties and seasonal brews. It involves sourcing unique ingredients from remote farms, custom fermentation monitoring, small-batch quality control, adaptive packaging design, and direct-to-consumer distribution through niche channels. The process integrates traditional brewing techniques with modern IoT sensors for environment regulation, includes community feedback loops for recipe refinement, and leverages sustainable logistics practices to minimize carbon footprint while maintaining artisanal quality and exclusivity in the craft beer market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
hop_sourcing = Transition(label='Hop Sourcing')
malt_selection = Transition(label='Malt Selection')
water_testing = Transition(label='Water Testing')
yeast_culturing = Transition(label='Yeast Culturing')
batch_planning = Transition(label='Batch Planning')

fermentation_start = Transition(label='Fermentation Start')
sensor_setup = Transition(label='Sensor Setup')

quality_sampling = Transition(label='Quality Sampling')
recipe_adjust = Transition(label='Recipe Adjust')

packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
bottling_run = Transition(label='Bottling Run')
cold_storage = Transition(label='Cold Storage')

order_processing = Transition(label='Order Processing')
direct_shipping = Transition(label='Direct Shipping')

customer_feedback = Transition(label='Customer Feedback')

waste_recycling = Transition(label='Waste Recycling')
inventory_audit = Transition(label='Inventory Audit')

skip = SilentTransition()

# Community feedback loop: After Quality Sampling, optionally Adjust Recipe and repeat Quality Sampling
# loop = *(Quality Sampling, Recipe Adjust)
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_sampling, recipe_adjust]
)

# Brewing preparation partial order with concurrency of sourcing ingredients
brewing_prep_nodes = [
    hop_sourcing,
    malt_selection,
    water_testing,
    yeast_culturing,
    batch_planning
]
brewing_prep = StrictPartialOrder(nodes=brewing_prep_nodes)
# No order edges here means these activities can be done in parallel

# After preparation -> start fermentation and sensor setup (concurrent)
fermentation_setup = StrictPartialOrder(nodes=[fermentation_start, sensor_setup])

# After fermentation start and sensor setup -> Quality Sampling with feedback loop
# Model feedback loop including Quality Sampling - Recipe Adjust loop above
quality_control = StrictPartialOrder(nodes=[feedback_loop])

# Packaging partial order (design, print label, bottling, cold storage) in sequence
packaging = StrictPartialOrder(
    nodes=[packaging_design, label_printing, bottling_run, cold_storage]
)
packaging.order.add_edge(packaging_design, label_printing)
packaging.order.add_edge(label_printing, bottling_run)
packaging.order.add_edge(bottling_run, cold_storage)

# Distribution partial order (order processing then direct shipping)
distribution = StrictPartialOrder(nodes=[order_processing, direct_shipping])
distribution.order.add_edge(order_processing, direct_shipping)

# Sustainability partial order: Waste Recycling and Inventory Audit concurrently
sustainability = StrictPartialOrder(nodes=[waste_recycling, inventory_audit])

# Assemble main partial order with dependency edges
# brewing_prep -> fermentation_setup
# fermentation_setup -> quality_control
# quality_control -> packaging
# packaging -> distribution
# distribution -> customer feedback
# branching final sustainability (concurrent with or after customer feedback) - model after customer feedback

root = StrictPartialOrder(nodes=[
    brewing_prep, 
    fermentation_setup, 
    quality_control, 
    packaging, 
    distribution, 
    customer_feedback, 
    sustainability
])

# Add ordering dependencies
root.order.add_edge(brewing_prep, fermentation_setup)
root.order.add_edge(fermentation_setup, quality_control)
root.order.add_edge(quality_control, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, customer_feedback)
# customer_feedback and sustainability are concurrent