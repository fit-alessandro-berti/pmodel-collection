# Generated from: 48d26c37-a630-47cf-8e08-02e96fd96c3c.json
# Description: This process outlines the end-to-end flow for producing and distributing artisanal cheese from small-scale farms. It begins with raw milk sourcing from select local farms, followed by quality testing and fermentation initiation under controlled conditions. The curdling phase involves precise temperature and humidity adjustments, then aging in specialized environments with regular monitoring. Packaging is done using eco-friendly materials, then the product undergoes certification for organic and regional authenticity. Distribution channels include farmer’s markets, boutique stores, and direct online sales, supported by customer feedback loops and inventory management to ensure freshness and demand alignment. Finally, waste materials are composted or repurposed, closing the sustainable cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define atomic activities
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Test')
ferm = Transition(label='Fermentation Start')
curdling = Transition(label='Curdling Phase')
temp = Transition(label='Temperature Control')
humidity = Transition(label='Humidity Adjust')
aging = Transition(label='Aging Monitor')
packaging = Transition(label='Eco Packaging')
cert = Transition(label='Certification Check')
market = Transition(label='Market Distribution')
store = Transition(label='Store Delivery')
online = Transition(label='Online Sales')
feedback = Transition(label='Feedback Loop')
inventory = Transition(label='Inventory Audit')
waste = Transition(label='Waste Compost')

# Sub-model for the Curdling Phase with parallel temperature & humidity adjustments
curdling_sub = StrictPartialOrder(nodes=[curdling, temp, humidity])
curdling_sub.order.add_edge(curdling, temp)
curdling_sub.order.add_edge(curdling, humidity)

# Sub-model for Distribution & Support Activities (all concurrent)
distribution_sub = StrictPartialOrder(nodes=[market, store, online, feedback, inventory])
# No edges => all five activities may proceed in parallel

# Root partial order
root = StrictPartialOrder(nodes=[
    milk, quality, ferm, curdling_sub,
    aging, packaging, cert,
    distribution_sub, waste
])

# Add the global ordering
root.order.add_edge(milk, quality)
root.order.add_edge(quality, ferm)
root.order.add_edge(ferm, curdling_sub)
root.order.add_edge(curdling_sub, aging)
root.order.add_edge(aging, packaging)
root.order.add_edge(packaging, cert)
root.order.add_edge(cert, distribution_sub)
# Ensure the cycle closes only after all distribution/support activities finish
root.order.add_edge(distribution_sub, waste)