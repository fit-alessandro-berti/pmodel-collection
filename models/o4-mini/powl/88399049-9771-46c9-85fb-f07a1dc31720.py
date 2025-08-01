# Generated from: 88399049-9771-46c9-85fb-f07a1dc31720.json
# Description: This process involves the intricate creation of bespoke artisan perfumes, starting from sourcing rare natural ingredients globally to blending unique scent profiles tailored for individual clients. It includes rigorous quality testing, aging phases, and custom packaging design. The process requires coordination between botanists, chemists, and designers to ensure a harmonious final product that meets personalized fragrance desires while maintaining sustainable and ethical standards throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ing = Transition(label='Ingredient Sourcing')
test = Transition(label='Sample Testing')
interview = Transition(label='Client Interview')
blend = Transition(label='Scent Blending')
stability = Transition(label='Stability Check')
aging = Transition(label='Aging Monitor')
quality = Transition(label='Quality Review')
pack = Transition(label='Packaging Design')
label = Transition(label='Label Printing')
approval = Transition(label='Client Approval')
batch = Transition(label='Batch Mixing')
audit = Transition(label='Compliance Audit')
fulfill = Transition(label='Order Fulfillment')
ship = Transition(label='Shipping Arrange')
inventory = Transition(label='Inventory Update')
feedback = Transition(label='Feedback Collection')

# Loop for iterative stability check and aging monitoring
stability_loop = OperatorPOWL(operator=Operator.LOOP, children=[stability, aging])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    ing, test, interview, blend,
    stability_loop, quality,
    pack, label, approval,
    batch, audit, fulfill,
    ship, inventory, feedback
])

# Define the control‐flow dependencies
root.order.add_edge(ing, test)
root.order.add_edge(test, interview)
root.order.add_edge(interview, blend)
root.order.add_edge(blend, stability_loop)
root.order.add_edge(stability_loop, quality)

# Parallel packaging/design tasks
root.order.add_edge(quality, pack)
root.order.add_edge(quality, label)

# Synchronize before approval
root.order.add_edge(pack, approval)
root.order.add_edge(label, approval)

# Remaining sequential steps
root.order.add_edge(approval, batch)
root.order.add_edge(batch, audit)
root.order.add_edge(audit, fulfill)
root.order.add_edge(fulfill, ship)
root.order.add_edge(ship, inventory)
root.order.add_edge(inventory, feedback)