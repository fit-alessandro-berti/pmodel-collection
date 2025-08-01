# Generated from: 3e65fd9a-7e5e-4ed7-9edf-8c903c5b6b48.json
# Description: This process encompasses the intricate steps of producing and distributing artisanal cheese, starting from selecting rare milk varieties, through specialized fermentation and aging techniques unique to small-scale producers. It involves precise quality checks, custom packaging, and coordinating with niche retailers and gourmet markets. The process also includes managing seasonal variations in milk supply, maintaining traditional methods while ensuring compliance with modern food safety regulations, and handling direct-to-consumer logistics with careful temperature control to preserve cheese integrity during shipment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Testing')
culture = Transition(label='Culture Prep')
pasteurize = Transition(label='Milk Pasteurize')
coagulation = Transition(label='Coagulation')
curd = Transition(label='Curd Cutting')
whey = Transition(label='Whey Draining')
molding = Transition(label='Molding')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
aging_setup = Transition(label='Aging Setup')
temp_mon = Transition(label='Temperature Monitor')
flavor = Transition(label='Flavor Check')
packaging = Transition(label='Packaging')
order_proc = Transition(label='Order Processing')
dispatch = Transition(label='Dispatch')
retail = Transition(label='Retail Coordination')
skip = SilentTransition()

# Define the aging cycle as a partial order: Temperature Monitor --> Flavor Check
cycle = StrictPartialOrder(nodes=[temp_mon, flavor])
cycle.order.add_edge(temp_mon, flavor)

# Loop over the cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    milk, quality, culture, pasteurize, coagulation, curd, whey,
    molding, pressing, salting, aging_setup, loop,
    packaging, order_proc, dispatch, retail
])

# Add sequencing and partial order edges
root.order.add_edge(milk, quality)
root.order.add_edge(quality, culture)
root.order.add_edge(quality, pasteurize)
root.order.add_edge(culture, coagulation)
root.order.add_edge(pasteurize, coagulation)
root.order.add_edge(coagulation, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, molding)
root.order.add_edge(molding, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, aging_setup)
root.order.add_edge(aging_setup, loop)
root.order.add_edge(loop, packaging)
root.order.add_edge(packaging, order_proc)
root.order.add_edge(order_proc, dispatch)
root.order.add_edge(order_proc, retail)