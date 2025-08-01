# Generated from: f60ac12f-82be-4c56-800f-8ab484788887.json
# Description: This process describes the end-to-end supply chain for artisan cheese production and distribution, starting from raw milk sourcing to aging, quality testing, packaging, and delivery. It includes unique steps like microbial culture blending, environmental condition monitoring, and niche market allocation. The process ensures traceability, maintains artisanal quality standards, and incorporates customer feedback loops for continuous improvement while coordinating with local farms, specialty retailers, and export partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Blending = Transition(label='Culture Blending')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Salt_Brine = Transition(label='Salt Brine')
Age_Monitor = Transition(label='Age Monitor')
Quality_Test = Transition(label='Quality Test')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Design = Transition(label='Label Design')
Order_Allocation = Transition(label='Order Allocation')
Transport_Arrange = Transition(label='Transport Arrange')
Retail_Sync = Transition(label='Retail Sync')
Customer_Review = Transition(label='Customer Review')
Feedback_Analyze = Transition(label='Feedback Analyze')

# Define partial order for the initial milk processing chain
milk_processing = StrictPartialOrder(
    nodes=[Milk_Sourcing, Culture_Blending, Milk_Pasteurize, 
           Curd_Cutting, Whey_Drain, Mold_Inoculate, Press_Cheese, Salt_Brine]
)
milk_processing.order.add_edge(Milk_Sourcing, Culture_Blending)
milk_processing.order.add_edge(Culture_Blending, Milk_Pasteurize)
milk_processing.order.add_edge(Milk_Pasteurize, Curd_Cutting)
milk_processing.order.add_edge(Curd_Cutting, Whey_Drain)
milk_processing.order.add_edge(Whey_Drain, Mold_Inoculate)
milk_processing.order.add_edge(Mold_Inoculate, Press_Cheese)
milk_processing.order.add_edge(Press_Cheese, Salt_Brine)

# Partial order for aging and monitoring (concurrent with next stage)
aging_and_quality = StrictPartialOrder(
    nodes=[Age_Monitor, Quality_Test]
)
aging_and_quality.order.add_edge(Age_Monitor, Quality_Test)

# Packaging and labeling partial order
packaging = StrictPartialOrder(
    nodes=[Packaging_Prep, Label_Design]
)
packaging.order.add_edge(Packaging_Prep, Label_Design)

# Order allocation with synchronizations with partners (choice to reorder retail sync or export handled by concurrency)
order_distribution = StrictPartialOrder(
    nodes=[Order_Allocation, Transport_Arrange, Retail_Sync]
)
order_distribution.order.add_edge(Order_Allocation, Transport_Arrange)
order_distribution.order.add_edge(Order_Allocation, Retail_Sync)

# Customer feedback loop as a loop operator:
# Loop: (Customer_Review, Feedback_Analyze)
# meaning: do Customer_Review, then either exit or Feedback_Analyze and repeat the review
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Customer_Review, Feedback_Analyze]
)

# Compose the final model as partial orders with ordering:
# milk_processing --> aging_and_quality --> packaging --> order_distribution --> feedback_loop

root = StrictPartialOrder(
    nodes=[milk_processing, aging_and_quality, packaging, order_distribution, feedback_loop]
)
root.order.add_edge(milk_processing, aging_and_quality)
root.order.add_edge(aging_and_quality, packaging)
root.order.add_edge(packaging, order_distribution)
root.order.add_edge(order_distribution, feedback_loop)