# Generated from: a0ec933c-a3a3-4191-b732-c18bc858d9ff.json
# Description: This process describes the end-to-end supply chain for artisanal cheese production, focusing on unique challenges such as seasonal milk sourcing, traditional fermentation monitoring, and small-batch aging. It involves coordination between local dairy farms, quality inspections of raw milk, controlled fermentation environments, handcrafting by cheesemakers, detailed aging schedules, and niche market distribution including direct-to-consumer and boutique retailers. Each step requires specialized skills to maintain authenticity and product integrity, while adapting to fluctuating supply and demand. The process also includes feedback loops for sensory evaluation and recipe adjustments to preserve traditional flavors and textures, ensuring customer satisfaction in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Check = Transition(label='Quality Check')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Fermentation_Start = Transition(label='Fermentation Start')
pH_Monitoring = Transition(label='pH Monitoring')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Molding_Press = Transition(label='Molding Press')
Salting_Stage = Transition(label='Salting Stage')
Initial_Aging = Transition(label='Initial Aging')
Flip_Schedule = Transition(label='Flip Schedule')
Humidity_Control = Transition(label='Humidity Control')
Sensory_Test = Transition(label='Sensory Test')
Packaging_Prep = Transition(label='Packaging Prep')
Order_Fulfill = Transition(label='Order Fulfill')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Adjust = Transition(label='Recipe Adjust')

# Define aging partial order:
# Initial Aging followed by Flip Schedule and Humidity Control concurrent in any order (partial order with edges Initial_Aging -> Flip_Schedule and Initial_Aging -> Humidity_Control)
# Flip Schedule and Humidity Control concurrent (no edge between them)
aging = StrictPartialOrder(nodes=[Initial_Aging, Flip_Schedule, Humidity_Control])
aging.order.add_edge(Initial_Aging, Flip_Schedule)
aging.order.add_edge(Initial_Aging, Humidity_Control)

# Sensory Test after aging
# Followed by a loop for feedback & recipe adjust: loop(
#     do Sensory_Test
#     then choice(exit or do Recipe_Adjust then loop again)
# )
sensory_test = Sensory_Test

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        sensory_test,
        Recipe_Adjust
    ])

# Packaging and order fulfillment partial order (Packaging_Prep --> Order_Fulfill)
packaging_order = StrictPartialOrder(nodes=[Packaging_Prep, Order_Fulfill])
packaging_order.order.add_edge(Packaging_Prep, Order_Fulfill)

# The main linear partial order from milk sourcing to aging then sensory test & feedback loop then packaging and order fulfill
# Structure:
# Milk_Sourcing --> Quality_Check --> Milk_Pasteurize --> Fermentation_Start --> pH_Monitoring --> Curd_Cutting --> Whey_Drain --> Molding_Press --> Salting_Stage --> aging --> feedback_loop --> packaging_order --> Customer_Feedback

# We see that Customer_Feedback logically follows Order_Fulfill
# So add Customer_Feedback as final activity after Order_Fulfill

# Build the full partial order:

nodes_main = [
    Milk_Sourcing, Quality_Check, Milk_Pasteurize, Fermentation_Start, pH_Monitoring,
    Curd_Cutting, Whey_Drain, Molding_Press, Salting_Stage,
    aging,
    feedback_loop,
    packaging_order,
    Customer_Feedback
]

root = StrictPartialOrder(nodes=nodes_main)

# Add edges for main linear flow
root.order.add_edge(Milk_Sourcing, Quality_Check)
root.order.add_edge(Quality_Check, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Fermentation_Start)
root.order.add_edge(Fermentation_Start, pH_Monitoring)
root.order.add_edge(pH_Monitoring, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Drain)
root.order.add_edge(Whey_Drain, Molding_Press)
root.order.add_edge(Molding_Press, Salting_Stage)
root.order.add_edge(Salting_Stage, aging)
root.order.add_edge(aging, feedback_loop)
root.order.add_edge(feedback_loop, packaging_order)
root.order.add_edge(packaging_order, Customer_Feedback)