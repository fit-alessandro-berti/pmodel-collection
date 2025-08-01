# Generated from: 21651cc1-1e0f-4113-9d07-1f700033ec50.json
# Description: This process outlines the intricate supply chain of artisan cheese production, starting from raw milk sourcing from select farms with specific breed cows to quality testing and aging in controlled environments. It includes steps like microbial culture preparation, curd cutting, whey drainage, pressing, salting, and maturation under precise humidity and temperature settings. The process also involves packaging with eco-friendly materials, batch traceability tagging, and coordinating delivery logistics to specialty retailers, ensuring freshness and compliance with food safety standards. Customer feedback is integrated for continuous improvement, and seasonal variations in milk quality are accounted for by adjusting fermentation parameters accordingly.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drainage = Transition(label='Whey Drainage')
Curd_Pressing = Transition(label='Curd Pressing')
Salt_Application = Transition(label='Salt Application')
Cheese_Aging = Transition(label='Cheese Aging')
Humidity_Control = Transition(label='Humidity Control')
Temp_Monitoring = Transition(label='Temp Monitoring')
Packaging_Eco = Transition(label='Packaging Eco')
Batch_Tagging = Transition(label='Batch Tagging')
Delivery_Plan = Transition(label='Delivery Plan')
Retail_Coordination = Transition(label='Retail Coordination')
Feedback_Review = Transition(label='Feedback Review')
Parameter_Adjust = Transition(label='Parameter Adjust')

# Define partial order for the initial preparation
prep_PO = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Culture_Prep, Milk_Pasteurize, 
    Curd_Cutting, Whey_Drainage, Curd_Pressing, Salt_Application
])
prep_PO.order.add_edge(Milk_Sourcing, Quality_Testing)
prep_PO.order.add_edge(Quality_Testing, Culture_Prep)
prep_PO.order.add_edge(Culture_Prep, Milk_Pasteurize)
prep_PO.order.add_edge(Milk_Pasteurize, Curd_Cutting)
prep_PO.order.add_edge(Curd_Cutting, Whey_Drainage)
prep_PO.order.add_edge(Whey_Drainage, Curd_Pressing)
prep_PO.order.add_edge(Curd_Pressing, Salt_Application)

# Define partial order for aging including controlling humidity and temperature (concurrent)
aging_PO = StrictPartialOrder(nodes=[
    Cheese_Aging, Humidity_Control, Temp_Monitoring
])
aging_PO.order.add_edge(Humidity_Control, Cheese_Aging)
aging_PO.order.add_edge(Temp_Monitoring, Cheese_Aging)
# Humidity_Control and Temp_Monitoring are concurrent - no order between them

# Packaging and delivery steps
packaging_PO = StrictPartialOrder(nodes=[
    Packaging_Eco, Batch_Tagging, Delivery_Plan, Retail_Coordination
])
packaging_PO.order.add_edge(Packaging_Eco, Batch_Tagging)
packaging_PO.order.add_edge(Batch_Tagging, Delivery_Plan)
packaging_PO.order.add_edge(Delivery_Plan, Retail_Coordination)

# Loop for seasonal variations: adjust fermentation parameters based on feedback
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Parameter_Adjust, Feedback_Review]
)
# This means:
#  - Execute Parameter_Adjust,
#  - loop body is Feedback_Review then back to Parameter_Adjust,
#  - loop can exit after Parameter_Adjust without entering Feedback_Review

# Assemble the main process partial order
root = StrictPartialOrder(nodes=[prep_PO, aging_PO, packaging_PO, seasonal_loop])

# Define order between phases:
# preparation -> aging -> packaging -> seasonal adjustments

root.order.add_edge(prep_PO, aging_PO)
root.order.add_edge(aging_PO, packaging_PO)
root.order.add_edge(packaging_PO, seasonal_loop)