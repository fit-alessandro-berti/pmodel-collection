# Generated from: ca7654e3-92a8-4190-8cda-fca1c95e0cd7.json
# Description: This process covers the end-to-end supply chain for artisan cheese production, blending traditional methods with modern logistics. It begins with sourcing rare milk varieties from specialized farms, followed by precise curdling and aging techniques governed by seasonal conditions. Quality inspections and microbial testing are conducted repeatedly to ensure product integrity. Packaging involves eco-friendly materials tailored to preserve flavor and texture. Distribution requires coordination with boutique retailers and direct-to-consumer channels, including subscription services. The process integrates feedback loops from tastings and market trends to continuously refine recipes and supply strategies, balancing artisanal quality with scalable delivery demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Preparation = Transition(label='Curd Preparation')
Starter_Culture = Transition(label='starter Culture')
Temperature_Control = Transition(label='Temperature Control')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Process = Transition(label='Aging Process')
Microbial_Test = Transition(label='Microbial Test')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Processing = Transition(label='Order Processing')
Retail_Shipping = Transition(label='Retail Shipping')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Update = Transition(label='Recipe Update')
Market_Analysis = Transition(label='Market Analysis')

# Loop for Quality inspections and microbial testing (repeat: Microbial Test then Quality Check)
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Quality_Check,
    Microbial_Test
])

# Loop for feedback and continuous improvement:
# execute Customer Feedback, then choose exit or execute (Recipe Update + Market Analysis) then feedback again
improvement_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Customer_Feedback,
    StrictPartialOrder(nodes=[Recipe_Update, Market_Analysis])
])

# Packaging process as partial order (Eco Packaging and Label Printing can be concurrent)
packaging = StrictPartialOrder(nodes=[Eco_Packaging, Label_Printing])

# Distribution split into two concurrent channels
# Channel 1: Inventory Audit -> Order Processing -> Retail Shipping
channel1 = StrictPartialOrder(nodes=[Inventory_Audit, Order_Processing, Retail_Shipping])
channel1.order.add_edge(Inventory_Audit, Order_Processing)
channel1.order.add_edge(Order_Processing, Retail_Shipping)

# Channel 2: Customer Feedback with improvement loop is separate, run concurrently
# so distribution is a partial order with the 2 channels and feedback loop concurrently
distribution = StrictPartialOrder(nodes=[channel1, improvement_loop])

# Aging process includes Temperature Control and Starter Culture as concurrent prerequisites
aging_pre = StrictPartialOrder(nodes=[Starter_Culture, Temperature_Control])
# After aging prerequisites, Aging Process itself
aging = StrictPartialOrder(nodes=[aging_pre, Aging_Process])
aging.order.add_edge(aging_pre, Aging_Process)

# Cheese processing linear sequence after curd preparation
processing_seq = StrictPartialOrder(nodes=[
    Pressing_Cheese,
    Salting_Stage
])
processing_seq.order.add_edge(Pressing_Cheese, Salting_Stage)

# Full production flow partial order nodes:
# Start -> Milk Sourcing -> Curd Preparation -> parallel (Starter Culture & Temp Control) -> Aging -> processing_seq -> inspection_loop -> packaging -> distribution

production_nodes = [
    Milk_Sourcing,
    Curd_Preparation,
    aging,
    processing_seq,
    inspection_loop,
    packaging,
    distribution
]

root = StrictPartialOrder(nodes=production_nodes)

# Add edges for main flow
root.order.add_edge(Milk_Sourcing, Curd_Preparation)
root.order.add_edge(Curd_Preparation, aging)
root.order.add_edge(aging, processing_seq)
root.order.add_edge(processing_seq, inspection_loop)
root.order.add_edge(inspection_loop, packaging)
root.order.add_edge(packaging, distribution)