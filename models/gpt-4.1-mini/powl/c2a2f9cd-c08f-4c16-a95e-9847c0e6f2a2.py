# Generated from: c2a2f9cd-c08f-4c16-a95e-9847c0e6f2a2.json
# Description: This process manages the end-to-end operations for sourcing rare artisan cheeses from remote farms, ensuring quality compliance, managing cold chain logistics, coordinating with local distributors, handling export regulations, and delivering to high-end retailers. It involves multiple stakeholders including farmers, quality inspectors, transporters, customs agents, and marketing teams to maintain product integrity through each step. The process also integrates seasonal variations, demand forecasting, and sustainable packaging solutions to meet eco-friendly standards while optimizing costs and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
farm_sourcing = Transition(label='Farm Sourcing')
quality_check = Transition(label='Quality Check')
sample_testing = Transition(label='Sample Testing')
cold_storage = Transition(label='Cold Storage')
order_planning = Transition(label='Order Planning')
packaging_prep = Transition(label='Packaging Prep')
transport_booking = Transition(label='Transport Booking')
customs_filing = Transition(label='Customs Filing')
export_clearance = Transition(label='Export Clearance')
distributor_contact = Transition(label='Distributor Contact')
retail_scheduling = Transition(label='Retail Scheduling')
demand_forecast = Transition(label='Demand Forecast')
sustainability_audit = Transition(label='Sustainability Audit')
customer_feedback = Transition(label='Customer Feedback')
inventory_refill = Transition(label='Inventory Refill')

# Partial order nodes representing main sequential and concurrent phases with some loops and choices

# Quality assurance subprocess as a loop:
# Execute Quality Check -> Sample Testing, then optionally repeat Sample Testing before continuing
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, sample_testing])

# Export and Customs subprocess (linear)
export_process = StrictPartialOrder(nodes=[customs_filing, export_clearance])
export_process.order.add_edge(customs_filing, export_clearance)

# Logistics subprocess with concurrent booking and cold storage
logistics = StrictPartialOrder(nodes=[cold_storage, transport_booking])
# no ordering between cold_storage and transport_booking => concurrent

# Distribution subprocess linearly
distribution = StrictPartialOrder(nodes=[distributor_contact, retail_scheduling])
distribution.order.add_edge(distributor_contact, retail_scheduling)

# Demand forecasting and sustainability audit can be done in parallel before order planning
forecast_and_sustain = StrictPartialOrder(nodes=[demand_forecast, sustainability_audit])
# no ordering => concurrent

# Packaging and order planning must follow forecast & sustainability audit
packaging_order = StrictPartialOrder(nodes=[order_planning, packaging_prep])
packaging_order.order.add_edge(order_planning, packaging_prep)

# Customer feedback and inventory refill can run concurrently after distribution
feedback_inventory = StrictPartialOrder(nodes=[customer_feedback, inventory_refill])
# no ordering => concurrent

# Main strict partial order combining all phases
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    quality_loop,
    forecast_and_sustain,
    packaging_order,
    logistics,
    export_process,
    distribution,
    feedback_inventory
])

# Define order edges to reflect process flow:
root.order.add_edge(farm_sourcing, quality_loop)  # after sourcing, do quality loop
root.order.add_edge(quality_loop, forecast_and_sustain)  # after quality, parallel forecast & sustain
root.order.add_edge(forecast_and_sustain, packaging_order)  # after forecast & sustain, do packaging & order planning
root.order.add_edge(packaging_order, logistics)  # after packaging/order, logistics starts
root.order.add_edge(logistics, export_process)  # after logistics, proceed with export
root.order.add_edge(export_process, distribution)  # after export, contact distributors and schedule retail
root.order.add_edge(distribution, feedback_inventory)  # after distribution, collect feedback and refill inventory