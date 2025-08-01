# Generated from: 8b74b1cf-06c9-4b88-9f6d-2d6510f3e481.json
# Description: This process outlines the complex and atypical supply chain of artisan cheese production and distribution. It begins with raw milk sourcing from niche farms focusing on unique breeds, followed by milk quality testing and specialized fermentation. The aging environment is carefully controlled, requiring regular monitoring and adjustments based on sensory evaluations. Packaging involves customized biodegradable materials to preserve flavor and texture. The distribution network integrates small-scale retailers and direct-to-consumer subscriptions, necessitating dynamic logistics planning to maintain freshness. Marketing leverages storytelling around origin and craft, supported by seasonal event coordination and customer feedback loops to refine product offerings and ensure sustainable practices throughout the chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qc = Transition(label='Quality Check')
mp = Transition(label='Milk Pasteurize')
ca = Transition(label='Culture Add')
coag = Transition(label='Coagulate Milk')
cut = Transition(label='Cut Curds')
drain = Transition(label='Drain Whey')
mold = Transition(label='Mold Press')
salt = Transition(label='Salting Step')
cave = Transition(label='Cave Aging')
sensory = Transition(label='Sensory Test')
package_cheese = Transition(label='Package Cheese')
label_design = Transition(label='Label Design')
customer_survey = Transition(label='Customer Survey')
event_manage = Transition(label='Event Manage')
supply_audit = Transition(label='Supply Audit')

# Loop for aging with sensory checks
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cave, sensory]
)

# Distribution: two exclusive paths (small‐scale retailers vs direct subscriptions)
# Path 1: Retail
rp1 = Transition(label='Route Planning')
of1 = Transition(label='Order Fulfill')
retail_po = StrictPartialOrder(nodes=[rp1, of1])
retail_po.order.add_edge(rp1, of1)

# Path 2: Subscription
rp2 = Transition(label='Route Planning')
of2 = Transition(label='Order Fulfill')
subscription_po = StrictPartialOrder(nodes=[rp2, of2])
subscription_po.order.add_edge(rp2, of2)

dist_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[retail_po, subscription_po]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    ms, qc, mp, ca, coag, cut, drain, mold, salt,
    aging_loop, package_cheese,
    dist_choice,
    label_design, event_manage, customer_survey, supply_audit
])

# Add the sequential/control dependencies
root.order.add_edge(ms, qc)
root.order.add_edge(qc, mp)
root.order.add_edge(mp, ca)
root.order.add_edge(ca, coag)
root.order.add_edge(coag, cut)
root.order.add_edge(cut, drain)
root.order.add_edge(drain, mold)
root.order.add_edge(mold, salt)
root.order.add_edge(salt, aging_loop)
root.order.add_edge(aging_loop, package_cheese)
root.order.add_edge(package_cheese, dist_choice)

# Marketing & feedback activities run after distribution, concurrently
root.order.add_edge(dist_choice, label_design)
root.order.add_edge(dist_choice, event_manage)
root.order.add_edge(dist_choice, customer_survey)
root.order.add_edge(dist_choice, supply_audit)