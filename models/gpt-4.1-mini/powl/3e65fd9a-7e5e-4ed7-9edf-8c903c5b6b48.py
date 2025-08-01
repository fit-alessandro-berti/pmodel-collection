# Generated from: 3e65fd9a-7e5e-4ed7-9edf-8c903c5b6b48.json
# Description: This process encompasses the intricate steps of producing and distributing artisanal cheese, starting from selecting rare milk varieties, through specialized fermentation and aging techniques unique to small-scale producers. It involves precise quality checks, custom packaging, and coordinating with niche retailers and gourmet markets. The process also includes managing seasonal variations in milk supply, maintaining traditional methods while ensuring compliance with modern food safety regulations, and handling direct-to-consumer logistics with careful temperature control to preserve cheese integrity during shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding = Transition(label='Molding')
Pressing = Transition(label='Pressing')
Salting = Transition(label='Salting')
Aging_Setup = Transition(label='Aging Setup')
Temperature_Monitor = Transition(label='Temperature Monitor')
Flavor_Check = Transition(label='Flavor Check')
Packaging = Transition(label='Packaging')
Order_Processing = Transition(label='Order Processing')
Dispatch = Transition(label='Dispatch')
Retail_Coordination = Transition(label='Retail Coordination')

# Partial order representing cheese production steps
# Milk sourcing -> Quality Testing -> Culture Prep -> Milk Pasteurize -> Coagulation -> Curd Cutting
# -> Whey Draining -> Molding -> Pressing -> Salting -> Aging Setup
prod_nodes = [
    Milk_Sourcing,
    Quality_Testing,
    Culture_Prep,
    Milk_Pasteurize,
    Coagulation,
    Curd_Cutting,
    Whey_Draining,
    Molding,
    Pressing,
    Salting,
    Aging_Setup,
]
prod_order = [
    (Milk_Sourcing, Quality_Testing),
    (Quality_Testing, Culture_Prep),
    (Culture_Prep, Milk_Pasteurize),
    (Milk_Pasteurize, Coagulation),
    (Coagulation, Curd_Cutting),
    (Curd_Cutting, Whey_Draining),
    (Whey_Draining, Molding),
    (Molding, Pressing),
    (Pressing, Salting),
    (Salting, Aging_Setup),
]

prod_po = StrictPartialOrder(nodes=prod_nodes)
for src, tgt in prod_order:
    prod_po.order.add_edge(src, tgt)

# Loop for monitoring and flavor checking during aging process
# Loop: Execute Temperature Monitor, then either exit or Flavor Check then repeat Temperature Monitor
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Temperature_Monitor, Flavor_Check])

# After aging setup, do the monitoring loop
aging_and_monitor = StrictPartialOrder(nodes=[prod_po, monitor_loop])
aging_and_monitor.order.add_edge(prod_po, monitor_loop)

# Packaging and subsequent distribution activities in partial order
distr_nodes = [
    Packaging,
    Order_Processing,
    Dispatch,
    Retail_Coordination,
]
distr_order = [
    (Packaging, Order_Processing),
    (Order_Processing, Dispatch),
    (Dispatch, Retail_Coordination),
]
distribution_po = StrictPartialOrder(nodes=distr_nodes)
for src, tgt in distr_order:
    distribution_po.order.add_edge(src, tgt)

# Final root partial order composing production -> aging/monitor loop -> distribution
root = StrictPartialOrder(nodes=[aging_and_monitor, distribution_po])
root.order.add_edge(aging_and_monitor, distribution_po)