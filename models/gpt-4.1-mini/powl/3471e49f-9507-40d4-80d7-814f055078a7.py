# Generated from: 3471e49f-9507-40d4-80d7-814f055078a7.json
# Description: This process outlines the intricate supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise fermentation and aging under controlled conditions. It includes quality assessments at multiple stages, packaging with eco-friendly materials, and coordinating niche market distribution. The process also involves compliance checks with food safety regulations, demand forecasting for seasonal variations, and handling customer feedback to continuously improve product quality and supply efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurization = Transition(label='Milk Pasteurization')
starter_culture = Transition(label='Starter Culture')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
pressing_cheese = Transition(label='Pressing Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_sampling = Transition(label='Flavor Sampling')
packaging_prep = Transition(label='Packaging Prep')
eco_packaging = Transition(label='Eco Packaging')
regulatory_audit = Transition(label='Regulatory Audit')
market_forecast = Transition(label='Market Forecast')
order_fulfillment = Transition(label='Order Fulfillment')
customer_review = Transition(label='Customer Review')

# Model key sequences and concurrency according to the description

# Initial sourcing and testing sequence
initial_seq = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurization])
initial_seq.order.add_edge(milk_sourcing, quality_testing)
initial_seq.order.add_edge(quality_testing, milk_pasteurization)

# Starter culture, curd formation, whey separation, pressing sequence
cheese_making_seq = StrictPartialOrder(nodes=[starter_culture, curd_formation, whey_separation, pressing_cheese])
cheese_making_seq.order.add_edge(starter_culture, curd_formation)
cheese_making_seq.order.add_edge(curd_formation, whey_separation)
cheese_making_seq.order.add_edge(whey_separation, pressing_cheese)

# Aging with control and flavor sampling in partial order (humidity control concurrent with aging setup and flavor sampling )
aging_nodes = [aging_setup, humidity_control, flavor_sampling]
aging_po = StrictPartialOrder(nodes=aging_nodes)
aging_po.order.add_edge(aging_setup, flavor_sampling)
# humidity_control is parallel (no edges to/from humidity_control, so concurrent)
# Thus aging_setup->flavor_sampling, humidity_control concurrent to both

# Packaging preparation followed by eco packaging
packaging_seq = StrictPartialOrder(nodes=[packaging_prep, eco_packaging])
packaging_seq.order.add_edge(packaging_prep, eco_packaging)

# Regulatory audit, market forecast and order fulfillment have no strict order, but must happen after packaging
# Customer review happens at the end, dependent on order fulfillment

# Combine regulatory audit, market forecast and order fulfillment in partial order with packaging_seq
post_packaging_nodes = [regulatory_audit, market_forecast, order_fulfillment]
post_packaging_po = StrictPartialOrder(nodes=post_packaging_nodes)
# Order fulfillment depends on packaging and regulatory + forecast can be concurrent
# So only order_fulfillment depends on packaging_seq AND possibly regulatory_audit and market_forecast can be concurrent or before order_fulfillment
# We add order_fulfillment dependent on packaging completion

# We'll model regulatory_audit and market_forecast concurrent with packaging:
# to achieve that, create partial order of packaging and these, and then order fulfillment after all

pre_order_nodes = [packaging_seq, regulatory_audit, market_forecast]

# Create a PO with nodes = packaging_seq, regulatory_audit, market_forecast (packaging_seq treated as single node)
pre_order = StrictPartialOrder(nodes=pre_order_nodes)
# No order edges among packaging_seq, regulatory_audit, market_forecast (concurrent)

# order_fulfillment depends on all three
post_order = StrictPartialOrder(nodes=[pre_order, order_fulfillment])
post_order.order.add_edge(pre_order, order_fulfillment)

# Final customer review depends on order fulfillment
final_seq = StrictPartialOrder(nodes=[post_order, customer_review])
final_seq.order.add_edge(post_order, customer_review)

# Now combine all main parts respecting dependencies:

# initial_seq -> cheese_making_seq -> aging_po -> packaging_seq (but packaging_seq included in pre_order)
# So chain initial_seq -> cheese_making_seq -> aging_po -> pre_order -> order_fulfillment -> customer_review

# To put all together:
phase1 = StrictPartialOrder(nodes=[initial_seq, cheese_making_seq])
phase1.order.add_edge(initial_seq, cheese_making_seq)

phase2 = StrictPartialOrder(nodes=[phase1, aging_po])
phase2.order.add_edge(phase1, aging_po)

phase3 = StrictPartialOrder(nodes=[phase2, pre_order])
phase3.order.add_edge(phase2, pre_order)

phase4 = StrictPartialOrder(nodes=[phase3, order_fulfillment])
phase4.order.add_edge(phase3, order_fulfillment)

root = StrictPartialOrder(nodes=[phase4, customer_review])
root.order.add_edge(phase4, customer_review)