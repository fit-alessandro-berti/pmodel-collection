# Generated from: 4bafa746-7cd3-40ad-b921-fe364b2331ed.json
# Description: This process involves the sourcing, aging, quality testing, and distribution of handcrafted artisan cheeses from small farms to specialty retailers and exclusive restaurants. It includes selecting raw milk suppliers based on seasonal yield, managing aging conditions with precise humidity and temperature controls, performing microbial assessments, coordinating packaging with unique branding, and arranging logistics that ensure freshness while complying with international food safety regulations. The process also incorporates feedback loops from retailers on flavor profiles and demand forecasting to adjust production volumes and diversify cheese varieties offered in the market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
milk_sourcing    = Transition(label='Milk Sourcing')
supplier_vetting = Transition(label='Supplier Vetting')
milk_testing     = Transition(label='Milk Testing')
curd_prep        = Transition(label='Curd Preparation')
pressing_cheese  = Transition(label='Pressing Cheese')
salt_application = Transition(label='Salt Application')
aging_setup      = Transition(label='Aging Setup')
humidity_ctrl    = Transition(label='Humidity Control')
microbial_test   = Transition(label='Microbial Testing')
flavor_sampling  = Transition(label='Flavor Sampling')
pack_design      = Transition(label='Packaging Design')
label_printing   = Transition(label='Label Printing')
order_processing = Transition(label='Order Processing')
transport_sched  = Transition(label='Transport Scheduling')
inventory_audit  = Transition(label='Inventory Audit')

retail_feedback  = Transition(label='Retail Feedback')
demand_forecast  = Transition(label='Demand Forecast')

# A silent transition to model optional vetting
skip_vetting = SilentTransition()

# Choice: either perform supplier vetting or skip
vet_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[supplier_vetting, skip_vetting]
)

# Define the main production pipeline as a partial order
prod_pipeline = StrictPartialOrder(nodes=[
    milk_sourcing,
    vet_choice,
    milk_testing,
    curd_prep,
    pressing_cheese,
    salt_application,
    aging_setup,
    humidity_ctrl,
    microbial_test,
    flavor_sampling,
    pack_design,
    label_printing,
    order_processing,
    transport_sched,
    inventory_audit
])
# Sequential dependencies
prod_pipeline.order.add_edge(milk_sourcing, vet_choice)
prod_pipeline.order.add_edge(vet_choice, milk_testing)
prod_pipeline.order.add_edge(milk_testing, curd_prep)
prod_pipeline.order.add_edge(curd_prep, pressing_cheese)
prod_pipeline.order.add_edge(pressing_cheese, salt_application)
prod_pipeline.order.add_edge(salt_application, aging_setup)

# Aging leads to three concurrent QC tasks
prod_pipeline.order.add_edge(aging_setup, humidity_ctrl)
prod_pipeline.order.add_edge(aging_setup, microbial_test)
prod_pipeline.order.add_edge(aging_setup, flavor_sampling)

# QC tasks must complete before packaging
prod_pipeline.order.add_edge(humidity_ctrl, pack_design)
prod_pipeline.order.add_edge(microbial_test, pack_design)
prod_pipeline.order.add_edge(flavor_sampling, pack_design)

# Finish the pipeline
prod_pipeline.order.add_edge(pack_design, label_printing)
prod_pipeline.order.add_edge(label_printing, order_processing)
prod_pipeline.order.add_edge(order_processing, transport_sched)
prod_pipeline.order.add_edge(transport_sched, inventory_audit)

# Define the feedback subprocess as a partial order
feedback_loop = StrictPartialOrder(nodes=[
    retail_feedback,
    demand_forecast
])
feedback_loop.order.add_edge(retail_feedback, demand_forecast)

# Wrap it all in a loop: do prod_pipeline, then optionally
# do feedback_loop and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prod_pipeline, feedback_loop]
)