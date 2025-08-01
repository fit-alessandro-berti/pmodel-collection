# Generated from: 8cf01db4-b1eb-47cb-9fbe-fa99d06fa21d.json
# Description: This process manages the intricate supply chain of artisan cheese production, starting from raw milk sourcing from local farms to aging in specialized cellars. It involves quality testing, custom flavor blending, packaging in eco-friendly materials, coordinating seasonal demand fluctuations, compliance with food safety regulations, and direct-to-consumer delivery logistics. Each step ensures traceability and maintains product authenticity while optimizing for shelf life and market responsiveness. The process also incorporates feedback loops from retailers and consumers to refine production batches and flavor profiles, balancing artisanal craftsmanship with efficient distribution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
curd_formation     = Transition(label='Curd Formation')
pressing_cheese    = Transition(label='Pressing Cheese')
batch_blending     = Transition(label='Batch Blending')
flavor_profiling   = Transition(label='Flavor Profiling')
aging_control      = Transition(label='Aging Control')
packaging_prep     = Transition(label='Packaging Prep')
eco_packaging      = Transition(label='Eco Packaging')
label_printing     = Transition(label='Label Printing')
inventory_audit    = Transition(label='Inventory Audit')
regulatory_check   = Transition(label='Regulatory Check')
demand_forecast    = Transition(label='Demand Forecast')
order_processing   = Transition(label='Order Processing')
shipping_setup     = Transition(label='Shipping Setup')
customer_feedback  = Transition(label='Customer Feedback')
batch_refinement   = Transition(label='Batch Refinement')

# Normal (production & distribution) partial order
normal_flow = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, curd_formation, pressing_cheese,
    batch_blending, flavor_profiling, aging_control,
    packaging_prep, eco_packaging, label_printing,
    inventory_audit, regulatory_check,
    demand_forecast, order_processing, shipping_setup
])

# Define the sequencing and dependencies
nf = normal_flow.order
nf.add_edge(milk_sourcing, quality_testing)
nf.add_edge(quality_testing, curd_formation)
nf.add_edge(curd_formation, pressing_cheese)
nf.add_edge(pressing_cheese, batch_blending)
nf.add_edge(batch_blending, flavor_profiling)
nf.add_edge(flavor_profiling, aging_control)
nf.add_edge(aging_control, packaging_prep)
nf.add_edge(packaging_prep, eco_packaging)
nf.add_edge(packaging_prep, label_printing)
nf.add_edge(eco_packaging, inventory_audit)
nf.add_edge(eco_packaging, regulatory_check)
nf.add_edge(label_printing, inventory_audit)
nf.add_edge(label_printing, regulatory_check)
nf.add_edge(inventory_audit, demand_forecast)
nf.add_edge(regulatory_check, demand_forecast)
nf.add_edge(demand_forecast, order_processing)
nf.add_edge(order_processing, shipping_setup)

# Feedback loop partial order
feedback_flow = StrictPartialOrder(nodes=[customer_feedback, batch_refinement])
ff = feedback_flow.order
ff.add_edge(customer_feedback, batch_refinement)

# Build the loop: run normal_flow, then optionally do feedback_flow and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[normal_flow, feedback_flow]
)