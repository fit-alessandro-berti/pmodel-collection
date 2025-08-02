# Generated from: c121363a-d3d8-4399-92fc-785a72441319.json
# Description: This process manages the intricate supply chain for artisan cheese production, involving unique steps like milk sourcing from specific heritage breeds, microbial culture selection based on regional terroir, precise aging environment control, and customized packaging for niche markets. It also includes artisanal quality inspections, seasonal recipe adjustments, and direct collaboration with boutique retailers and specialty food events to ensure authenticity and premium customer experience throughout the product lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions for activities
breed_selection = Transition(label='Breed Selection')
milk_harvest = Transition(label='Milk Harvest')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
salt_rub = Transition(label='Salt Rub')
aging_monitor = Transition(label='Aging Monitor')
humidity_check = Transition(label='Humidity Check')
flavor_test = Transition(label='Flavor Test')
packaging_design = Transition(label='Packaging Design')
retail_partner = Transition(label='Retail Partner')
event_setup = Transition(label='Event Setup')
customer_feedback = Transition(label='Customer Feedback')

# Build partial orders for upstream milk processing chain:
# Breed Selection --> Milk Harvest --> Culture Prep --> Milk Pasteurize
milk_processing = StrictPartialOrder(
    nodes=[breed_selection, milk_harvest, culture_prep, milk_pasteurize]
)
milk_processing.order.add_edge(breed_selection, milk_harvest)
milk_processing.order.add_edge(milk_harvest, culture_prep)
milk_processing.order.add_edge(culture_prep, milk_pasteurize)

# Cheese formation steps sequence:
# Milk Pasteurize --> Curd Formation --> Whey Drain --> Mold Inoculate --> Press Cheese --> Salt Rub
cheese_formation = StrictPartialOrder(
    nodes=[milk_pasteurize, curd_formation, whey_drain, mold_inoculate, press_cheese, salt_rub]
)
cheese_formation.order.add_edge(milk_pasteurize, curd_formation)
cheese_formation.order.add_edge(curd_formation, whey_drain)
cheese_formation.order.add_edge(whey_drain, mold_inoculate)
cheese_formation.order.add_edge(mold_inoculate, press_cheese)
cheese_formation.order.add_edge(press_cheese, salt_rub)

# Aging environment control (monitoring in parallel with humidity check):
# Loop for continuous monitoring: Aging Monitor and Humidity Check repeated until exit
# This models ongoing aging control where flavor test is done after exiting loop

monitoring_body = StrictPartialOrder(
    nodes=[aging_monitor, humidity_check]
)
# No order edges = concurrent monitoring of aging and humidity

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_monitor, humidity_check])

# Actually, LOOP operator usually takes two children: A is the body, B is the redo behavior
# We'll model the loop as: (A = monitoring_body), (B = monitoring_body)
# But pm4py example uses nodes inside LOOP directly - to follow example:

# Construct a loop of:
# Execute monitoring concurrently (aging_monitor, humidity_check)
# then choose to do another monitoring iteration or exit

# Let's create a PO for the concurrent monitoring activities as a subgraph to use as loop body.

monitoring_body = StrictPartialOrder(nodes=[aging_monitor, humidity_check])

loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[
    monitoring_body,  # do monitoring
    SilentTransition() # silent transition to represent exit or redo (re-execute monitoring)
])

# Quality checks after aging:
# After exiting the monitoring loop, do Flavor Test
quality_checks = StrictPartialOrder(nodes=[flavor_test])
# packaging design follows quality checks
packaging_and_marketing = StrictPartialOrder(
    nodes=[packaging_design, retail_partner, event_setup, customer_feedback]
)
# Retail partner, event setup, and customer feedback can be partially concurrent after packaging design

packaging_and_marketing.order.add_edge(packaging_design, retail_partner)
packaging_and_marketing.order.add_edge(packaging_design, event_setup)
packaging_and_marketing.order.add_edge(retail_partner, customer_feedback)
packaging_and_marketing.order.add_edge(event_setup, customer_feedback)

# Combine steps into a global partial order:
# milk_processing --> cheese_formation --> loop_monitoring --> quality_checks --> packaging_and_marketing

root = StrictPartialOrder(
    nodes=[milk_processing, cheese_formation, loop_monitoring, quality_checks, packaging_and_marketing]
)
root.order.add_edge(milk_processing, cheese_formation)
root.order.add_edge(cheese_formation, loop_monitoring)
root.order.add_edge(loop_monitoring, quality_checks)
root.order.add_edge(quality_checks, packaging_and_marketing)