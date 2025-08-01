# Generated from: 30403100-c1f8-4d43-9b0b-47f49f085b27.json
# Description: This process outlines the intricate steps involved in producing, aging, and distributing artisan cheeses from small-scale farms to niche gourmet shops. It begins with milk sourcing and quality testing, followed by curdling and molding. The cheese then undergoes controlled aging with regular monitoring of humidity and temperature. Packaging requires specialized materials to maintain freshness, and logistics include refrigerated transport with real-time tracking. Finally, marketing involves targeted outreach to culinary experts and hosting tasting events to build brand recognition. Each stage requires close coordination to ensure product authenticity and compliance with food safety standards, making the process both complex and highly specialized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Testing')
pasteurize = Transition(label='Milk Pasteurize')
curd = Transition(label='Curd Formation')
mold = Transition(label='Mold Pressing')
salting = Transition(label='Salting Stage')
aging_setup = Transition(label='Aging Setup')
packaging_prep = Transition(label='Packaging Prep')
seal_inspection = Transition(label='Seal Inspection')
cold_storage = Transition(label='Cold Storage')
transport_route = Transition(label='Transport Route')
delivery_confirm = Transition(label='Delivery Confirm')
marketing_push = Transition(label='Marketing Push')
event_hosting = Transition(label='Event Hosting')

# Define monitoring checks (they may be repeated)
humidity = Transition(label='Humidity Check')
temperature = Transition(label='Temperature Log')
flavor = Transition(label='Flavor Sampling')

# Build the "checks" partial order: humidity & temperature can run in any order, both must precede flavor sampling
checks = StrictPartialOrder(nodes=[humidity, temperature, flavor])
checks.order.add_edge(humidity, flavor)
checks.order.add_edge(temperature, flavor)

# A silent transition for loop initialization/termination
skip = SilentTransition()

# Loop: zero or more iterations of the checks block
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, checks])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        milk,
        quality,
        pasteurize,
        curd,
        mold,
        salting,
        aging_setup,
        monitor_loop,
        packaging_prep,
        seal_inspection,
        cold_storage,
        transport_route,
        delivery_confirm,
        marketing_push,
        event_hosting
    ]
)

# Define the sequential/control-flow edges
root.order.add_edge(milk, quality)
root.order.add_edge(quality, pasteurize)
root.order.add_edge(pasteurize, curd)
root.order.add_edge(curd, mold)
root.order.add_edge(mold, salting)
root.order.add_edge(salting, aging_setup)
root.order.add_edge(aging_setup, monitor_loop)
root.order.add_edge(monitor_loop, packaging_prep)
root.order.add_edge(packaging_prep, seal_inspection)
root.order.add_edge(seal_inspection, cold_storage)
root.order.add_edge(cold_storage, transport_route)
root.order.add_edge(transport_route, delivery_confirm)

# After delivery, marketing activities can proceed in parallel
root.order.add_edge(delivery_confirm, marketing_push)
root.order.add_edge(delivery_confirm, event_hosting)