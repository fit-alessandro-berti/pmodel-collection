# Generated from: c4d0932a-0550-47d9-bda9-d857c439a42a.json
# Description: This process details the end-to-end supply chain management of artisanal cheese production, starting from raw milk sourcing from small farms, through quality testing, fermentation monitoring, and aging in controlled environments. It includes packaging customization, seasonal demand forecasting, niche marketing strategies, distribution via boutique retailers, and feedback collection from connoisseurs to continuously refine the product. The process integrates traditional craftsmanship with modern traceability technology to ensure authenticity and compliance with food safety standards, while maintaining the unique characteristics that distinguish artisanal cheese in a competitive marketplace.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
starter_culture    = Transition(label='Starter Culture')
coagulation        = Transition(label='Coagulation')
curd_cutting       = Transition(label='Curd Cutting')
whey_draining      = Transition(label='Whey Draining')
molding_cheese     = Transition(label='Molding Cheese')
pressing_block     = Transition(label='Pressing Block')
brining_bath       = Transition(label='Brining Bath')
aging_control      = Transition(label='Aging Control')
flavor_profiling   = Transition(label='Flavor Profiling')
packaging_design   = Transition(label='Packaging Design')
demand_forecast    = Transition(label='Demand Forecast')
retail_outreach    = Transition(label='Retail Outreach')
customer_feedback  = Transition(label='Customer Feedback')

# Core production partial order (A)
A = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, starter_culture, coagulation,
    curd_cutting, whey_draining, molding_cheese, pressing_block,
    brining_bath, aging_control, flavor_profiling
])
A.order.add_edge(milk_sourcing,   quality_testing)
A.order.add_edge(quality_testing, starter_culture)
A.order.add_edge(starter_culture, coagulation)
A.order.add_edge(coagulation,     curd_cutting)
A.order.add_edge(curd_cutting,    whey_draining)
A.order.add_edge(whey_draining,   molding_cheese)
A.order.add_edge(molding_cheese,  pressing_block)
A.order.add_edge(pressing_block,  brining_bath)
A.order.add_edge(brining_bath,    aging_control)
A.order.add_edge(aging_control,   flavor_profiling)

# Packaging & distribution partial order (B)
B = StrictPartialOrder(nodes=[
    packaging_design, demand_forecast, retail_outreach, customer_feedback
])
B.order.add_edge(packaging_design,  demand_forecast)
B.order.add_edge(demand_forecast,   retail_outreach)
B.order.add_edge(retail_outreach,   customer_feedback)

# Loop: produce, then package & distribute & collect feedback, then repeat until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])