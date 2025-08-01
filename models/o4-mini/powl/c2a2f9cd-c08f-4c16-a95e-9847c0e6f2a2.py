# Generated from: c2a2f9cd-c08f-4c16-a95e-9847c0e6f2a2.json
# Description: This process manages the end-to-end operations for sourcing rare artisan cheeses from remote farms, ensuring quality compliance, managing cold chain logistics, coordinating with local distributors, handling export regulations, and delivering to high-end retailers. It involves multiple stakeholders including farmers, quality inspectors, transporters, customs agents, and marketing teams to maintain product integrity through each step. The process also integrates seasonal variations, demand forecasting, and sustainable packaging solutions to meet eco-friendly standards while optimizing costs and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
farm_sourcing     = Transition(label='Farm Sourcing')
quality_check     = Transition(label='Quality Check')
sample_testing    = Transition(label='Sample Testing')
cold_storage      = Transition(label='Cold Storage')
order_planning    = Transition(label='Order Planning')
packaging_prep    = Transition(label='Packaging Prep')
transport_booking = Transition(label='Transport Booking')
customs_filing    = Transition(label='Customs Filing')
export_clearance  = Transition(label='Export Clearance')
distributor_contact   = Transition(label='Distributor Contact')
retail_scheduling     = Transition(label='Retail Scheduling')
demand_forecast       = Transition(label='Demand Forecast')
sustainability_audit  = Transition(label='Sustainability Audit')
customer_feedback     = Transition(label='Customer Feedback')
inventory_refill      = Transition(label='Inventory Refill')

# Silent skip for optional branches
skip = SilentTransition()

# Loop for periodic demand forecasting and inventory refill
loop_forecast = OperatorPOWL(
    operator=Operator.LOOP, 
    children=[demand_forecast, inventory_refill]
)

# Exclusive choice: perform sustainability audit or skip
xor_sustain = OperatorPOWL(
    operator=Operator.XOR, 
    children=[sustainability_audit, skip]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    quality_check,
    sample_testing,
    cold_storage,
    loop_forecast,
    order_planning,
    packaging_prep,
    transport_booking,
    customs_filing,
    export_clearance,
    distributor_contact,
    retail_scheduling,
    customer_feedback,
    xor_sustain
])

# Define the control-flow edges (--> means precedes)
root.order.add_edge(farm_sourcing,     quality_check)
root.order.add_edge(quality_check,     sample_testing)
root.order.add_edge(sample_testing,    cold_storage)
root.order.add_edge(cold_storage,      loop_forecast)
root.order.add_edge(loop_forecast,     order_planning)
root.order.add_edge(order_planning,    packaging_prep)
root.order.add_edge(packaging_prep,    transport_booking)
root.order.add_edge(transport_booking, customs_filing)
root.order.add_edge(customs_filing,    export_clearance)
root.order.add_edge(export_clearance,  distributor_contact)
root.order.add_edge(distributor_contact, retail_scheduling)
root.order.add_edge(retail_scheduling,   customer_feedback)
root.order.add_edge(customer_feedback,   xor_sustain)