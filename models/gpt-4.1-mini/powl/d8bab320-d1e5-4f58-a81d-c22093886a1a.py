# Generated from: d8bab320-d1e5-4f58-a81d-c22093886a1a.json
# Description: This process manages the end-to-end supply chain for artisan cheese production, incorporating unique steps like raw milk sourcing from small farms, microbial culture selection, controlled aging environments, and bespoke packaging. It involves quality assurance through sensory analysis, regulatory compliance checks, seasonal demand forecasting, and custom order fulfillment for niche markets. The process also integrates sustainability tracking, waste byproduct recycling, and collaborative innovation with local cheesemakers to continuously improve flavor profiles and production efficiency, ensuring a premium product reaches specialized retailers and consumers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_forecast = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Build the aging environment sub-process as a PO with aging, humidity control and flavor testing possibly parallel order but aging_setup before humidity_control,
# flavor_testing after aging & humidity.
aging_po = StrictPartialOrder(
    nodes=[aging_setup, humidity_control, flavor_testing]
)
aging_po.order.add_edge(aging_setup, humidity_control)
aging_po.order.add_edge(humidity_control, flavor_testing)

# Quality assurance: packaging_design and label_approval in sequence
quality_po = StrictPartialOrder(
    nodes=[packaging_design, label_approval]
)
quality_po.order.add_edge(packaging_design, label_approval)

# Market and feedback in parallel (market_delivery, customer_feedback)
market_po = StrictPartialOrder(
    nodes=[market_delivery, customer_feedback],
    # no edges: concurrent
)

# Sustainability tracking: waste_recycling and regulation_audit can be in parallel but
# regulation_audit after order_forecast (regulatory compliance after forecasting)
sustainability_po = StrictPartialOrder(
    nodes=[order_forecast, regulation_audit, waste_recycling]
)
sustainability_po.order.add_edge(order_forecast, regulation_audit)
# waste_recycling independent (concurrent)

# Core cheese production steps sequential partial order
core_po = StrictPartialOrder(
    nodes=[milk_sourcing, culture_selection, milk_pasteurize,
           curd_formation, whey_separation, mold_inoculate,
           cheese_pressing]
)
core_po.order.add_edge(milk_sourcing, culture_selection)
core_po.order.add_edge(culture_selection, milk_pasteurize)
core_po.order.add_edge(milk_pasteurize, curd_formation)
core_po.order.add_edge(curd_formation, whey_separation)
core_po.order.add_edge(whey_separation, mold_inoculate)
core_po.order.add_edge(mold_inoculate, cheese_pressing)

# Compose main production: core -> aging -> quality
production_po = StrictPartialOrder(
    nodes=[core_po, aging_po, quality_po]
)
production_po.order.add_edge(core_po, aging_po)
production_po.order.add_edge(aging_po, quality_po)

# Compose final entire process:
# production_po before sustainability_po and market_po
root = StrictPartialOrder(
    nodes=[production_po, sustainability_po, market_po]
)
root.order.add_edge(production_po, sustainability_po)
root.order.add_edge(production_po, market_po)