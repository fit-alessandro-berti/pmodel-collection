# Generated from: 2153676c-d141-4308-8b3d-94ffafe1726e.json
# Description: This process manages the end-to-end flow of handcrafted materials from local artisan sourcing through quality verification, customized order assembly, and eco-friendly packaging to final distribution. It integrates traditional craftsmanship validation with modern logistics coordination, ensuring sustainable sourcing, traceability, and timely delivery while maintaining artisan uniqueness and regulatory compliance. The process includes dynamic inventory adjustments based on seasonal artisan availability and customer demand forecasting, alongside continuous feedback loops for artisan skill development and customer satisfaction enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t1  = Transition(label='Source Artisans')
t2  = Transition(label='Verify Quality')
t3  = Transition(label='Design Custom')
t4  = Transition(label='Material Sorting')
t5  = Transition(label='Demand Forecast')
t6  = Transition(label='Inventory Update')
t7  = Transition(label='Seasonal Adjust')
t8  = Transition(label='Order Assembly')
t9  = Transition(label='Compliance Check')
t10 = Transition(label='Package Eco')
t11 = Transition(label='Traceability Log')
t12 = Transition(label='Logistics Plan')
t13 = Transition(label='Dispatch Goods')
t14 = Transition(label='Customer Feedback')
t15 = Transition(label='Skill Training')
t16 = Transition(label='Skill Assessment')

# Main forward process
mainFlow = StrictPartialOrder(nodes=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13])
mainFlow.order.add_edge(t1,  t2)
# Parallel design, sorting, forecasting after quality check
mainFlow.order.add_edge(t2,  t3)
mainFlow.order.add_edge(t2,  t4)
mainFlow.order.add_edge(t2,  t5)
# Join and continue
mainFlow.order.add_edge(t3,  t6)
mainFlow.order.add_edge(t4,  t6)
mainFlow.order.add_edge(t5,  t6)
mainFlow.order.add_edge(t6,  t7)
mainFlow.order.add_edge(t7,  t8)
mainFlow.order.add_edge(t8,  t9)
mainFlow.order.add_edge(t9,  t10)
mainFlow.order.add_edge(t10, t11)
mainFlow.order.add_edge(t11, t12)
mainFlow.order.add_edge(t12, t13)

# Feedback loop: customer satisfaction & artisan skill development
feedbackFlow = StrictPartialOrder(nodes=[t14, t15, t16])
feedbackFlow.order.add_edge(t14, t15)
feedbackFlow.order.add_edge(t15, t16)

# Loop: run mainFlow, then either exit or perform feedbackFlow and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[mainFlow, feedbackFlow])