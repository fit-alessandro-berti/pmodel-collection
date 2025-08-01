# Generated from: f131da4d-47d1-41ec-811f-b92c38a83a07.json
# Description: This process entails the end-to-end creation and distribution of artisan cheese, starting from specialized milk sourcing through unique fermentation techniques, quality assurance, packaging, and finally niche market delivery. It integrates seasonal milk variations, custom aging environments, microbial culture selection, and direct-to-consumer logistics, ensuring product distinctiveness and traceability in a highly regulated food sector. Each step involves collaboration between farmers, microbiologists, quality inspectors, and boutique retailers, all coordinated to maintain authenticity and meet regulatory standards while optimizing freshness and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing       = Transition(label="Milk Sourcing")
culture_selection   = Transition(label="Culture Selection")
milk_testing        = Transition(label="Milk Testing")
fermentation_start  = Transition(label="Fermentation Start")
temperature_control = Transition(label="Temperature Control")
ph_monitoring       = Transition(label="pH Monitoring")
curd_cutting        = Transition(label="Curd Cutting")
whey_draining       = Transition(label="Whey Draining")
molding_cheese      = Transition(label="Molding Cheese")
salting_process     = Transition(label="Salting Process")
aging_setup         = Transition(label="Aging Setup")
quality_check       = Transition(label="Quality Check")
packaging_prep      = Transition(label="Packaging Prep")
label_design        = Transition(label="Label Design")
distribution_plan   = Transition(label="Distribution Plan")
retail_delivery     = Transition(label="Retail Delivery")
customer_feedback   = Transition(label="Customer Feedback")

# Loop for aging + repeated quality checks
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_setup, quality_check]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_selection, milk_testing,
    fermentation_start, temperature_control, ph_monitoring,
    curd_cutting, whey_draining, molding_cheese, salting_process,
    aging_loop,
    packaging_prep, label_design,
    distribution_plan, retail_delivery, customer_feedback
])

# Define ordering edges
o = root.order
o.add_edge(milk_sourcing,      culture_selection)
o.add_edge(culture_selection,  milk_testing)
o.add_edge(milk_testing,       fermentation_start)
o.add_edge(fermentation_start, temperature_control)
o.add_edge(fermentation_start, ph_monitoring)
o.add_edge(temperature_control, curd_cutting)
o.add_edge(ph_monitoring,       curd_cutting)
o.add_edge(curd_cutting,        whey_draining)
o.add_edge(whey_draining,       molding_cheese)
o.add_edge(molding_cheese,      salting_process)
o.add_edge(salting_process,     aging_loop)
o.add_edge(aging_loop,          packaging_prep)
o.add_edge(aging_loop,          label_design)
o.add_edge(packaging_prep,      distribution_plan)
o.add_edge(label_design,        distribution_plan)
o.add_edge(distribution_plan,   retail_delivery)
o.add_edge(retail_delivery,     customer_feedback)