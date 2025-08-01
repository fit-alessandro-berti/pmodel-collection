# Generated from: d8bab320-d1e5-4f58-a81d-c22093886a1a.json
# Description: This process manages the end-to-end supply chain for artisan cheese production, incorporating unique steps like raw milk sourcing from small farms, microbial culture selection, controlled aging environments, and bespoke packaging. It involves quality assurance through sensory analysis, regulatory compliance checks, seasonal demand forecasting, and custom order fulfillment for niche markets. The process also integrates sustainability tracking, waste byproduct recycling, and collaborative innovation with local cheesemakers to continuously improve flavor profiles and production efficiency, ensuring a premium product reaches specialized retailers and consumers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
order_forecast    = Transition(label='Order Forecast')
regulation_audit  = Transition(label='Regulation Audit')
milk_sourcing     = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize   = Transition(label='Milk Pasteurize')
curd_formation    = Transition(label='Curd Formation')
whey_separation   = Transition(label='Whey Separation')
waste_recycling   = Transition(label='Waste Recycling')
mold_inoculate    = Transition(label='Mold Inoculate')
cheese_pressing   = Transition(label='Cheese Pressing')
aging_setup       = Transition(label='Aging Setup')
humidity_control  = Transition(label='Humidity Control')
flavor_testing    = Transition(label='Flavor Testing')
packaging_design  = Transition(label='Packaging Design')
label_approval    = Transition(label='Label Approval')
market_delivery   = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Loop for controlled aging (setup then humidity control, repeat until exit)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])

# Build the partial order
root = StrictPartialOrder(nodes=[
    order_forecast, regulation_audit,
    milk_sourcing, culture_selection,
    milk_pasteurize, curd_formation,
    whey_separation, waste_recycling,
    mold_inoculate, cheese_pressing,
    aging_loop, flavor_testing,
    packaging_design, label_approval,
    market_delivery, customer_feedback
])

# Define ordering relations
root.order.add_edge(order_forecast,    regulation_audit)
root.order.add_edge(order_forecast,    milk_sourcing)
root.order.add_edge(order_forecast,    culture_selection)

root.order.add_edge(milk_sourcing,     milk_pasteurize)
root.order.add_edge(culture_selection, milk_pasteurize)
root.order.add_edge(milk_pasteurize,   curd_formation)
root.order.add_edge(curd_formation,    whey_separation)
root.order.add_edge(whey_separation,   waste_recycling)
root.order.add_edge(whey_separation,   mold_inoculate)

root.order.add_edge(mold_inoculate,    cheese_pressing)
root.order.add_edge(cheese_pressing,   aging_loop)
root.order.add_edge(aging_loop,        flavor_testing)

root.order.add_edge(flavor_testing,    packaging_design)
root.order.add_edge(regulation_audit,  label_approval)
root.order.add_edge(packaging_design,  label_approval)

root.order.add_edge(label_approval,    market_delivery)
root.order.add_edge(market_delivery,   customer_feedback)