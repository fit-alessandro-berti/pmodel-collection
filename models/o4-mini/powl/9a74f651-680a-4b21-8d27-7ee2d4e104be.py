# Generated from: 9a74f651-680a-4b21-8d27-7ee2d4e104be.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from small-scale farms to boutique retailers. It begins with selective milk sourcing, followed by controlled fermentation, aging under precise environmental conditions, quality inspections, and customized packaging. The chain further includes dynamic inventory adjustments based on seasonal demand, specialized cold-chain logistics, and direct marketing efforts to niche customer segments. Each stage requires meticulous coordination between farmers, master cheesemakers, logistics partners, and sales teams to maintain product integrity and brand authenticity while navigating regulatory compliance and fluctuating raw material availability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_milk           = Transition(label='Milk Sourcing')
t_pasteurize     = Transition(label='Milk Pasteurize')
t_starter        = Transition(label='Starter Culture')
t_curd           = Transition(label='Curd Formation')
t_whey           = Transition(label='Whey Separation')
t_press          = Transition(label='Pressing Cheese')
t_aging          = Transition(label='Aging Control')
t_flavor         = Transition(label='Flavor Monitoring')
t_inspect        = Transition(label='Quality Inspect')
t_quality_test   = Transition(label='Quality Testing')
t_pack           = Transition(label='Custom Packaging')
t_inventory      = Transition(label='Inventory Update')
t_cold           = Transition(label='Cold Transport')
t_delivery       = Transition(label='Retail Delivery')
t_feedback       = Transition(label='Customer Feedback')
tau              = SilentTransition()

# 1) Pre‐cheese sequence: Milk sourcing through pressing
pre_cheese = StrictPartialOrder(nodes=[
    t_milk, t_pasteurize, t_starter, t_curd, t_whey, t_press
])
pre_cheese.order.add_edge(t_milk,       t_pasteurize)
pre_cheese.order.add_edge(t_pasteurize, t_starter)
pre_cheese.order.add_edge(t_starter,    t_curd)
pre_cheese.order.add_edge(t_curd,       t_whey)
pre_cheese.order.add_edge(t_whey,       t_press)

# 2) Aging loop: control aging, monitor flavor, inspect; repeat monitoring+inspect as needed
aging_cycle = StrictPartialOrder(nodes=[t_aging, t_flavor, t_inspect])
aging_cycle.order.add_edge(t_aging,  t_flavor)
aging_cycle.order.add_edge(t_flavor, t_inspect)

monitor_cycle = StrictPartialOrder(nodes=[t_flavor, t_inspect])
monitor_cycle.order.add_edge(t_flavor, t_inspect)

loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_cycle, monitor_cycle]
)

# 3) Inventory update loop (dynamic seasonal adjustments)
#    first child = skip one round, second child = do an inventory update
inventory_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[tau, t_inventory]
)

# 4) Final linear flow: quality test → packaging → inventory_loop → cold chain → delivery → feedback
root = StrictPartialOrder(nodes=[
    pre_cheese,
    loop_aging,
    t_quality_test,
    t_pack,
    inventory_loop,
    t_cold,
    t_delivery,
    t_feedback
])

# Hook up the partial‐order edges between the major blocks
root.order.add_edge(pre_cheese,     loop_aging)
root.order.add_edge(loop_aging,     t_quality_test)
root.order.add_edge(t_quality_test, t_pack)
root.order.add_edge(t_pack,         inventory_loop)
root.order.add_edge(inventory_loop, t_cold)
root.order.add_edge(t_cold,         t_delivery)
root.order.add_edge(t_delivery,     t_feedback)