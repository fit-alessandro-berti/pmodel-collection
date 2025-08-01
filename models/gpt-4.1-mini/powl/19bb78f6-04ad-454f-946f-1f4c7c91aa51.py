# Generated from: 19bb78f6-04ad-454f-946f-1f4c7c91aa51.json
# Description: This process outlines the unique and intricate supply chain for artisanal cheese production, involving sourcing rare milk types, carefully timed fermentation, handcrafted molding, aging under controlled humidity, and specialized packaging. The process requires coordination between small-scale farmers, fermentation experts, quality inspectors, and boutique distributors to ensure the final product maintains its distinct flavor profile and meets niche market demands while complying with strict food safety regulations and seasonal variations in milk availability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Pressing = Transition(label='Mold Pressing')
Salt_Brining = Transition(label='Salt Brining')
Fermentation_Check = Transition(label='Fermentation Check')
Humidity_Aging = Transition(label='Humidity Aging')
Flavor_Infuse = Transition(label='Flavor Infuse')
Rind_Treatment = Transition(label='Rind Treatment')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Design = Transition(label='Packaging Design')
Boutique_Shipping = Transition(label='Boutique Shipping')
Market_Feedback = Transition(label='Market Feedback')

# Initial partial order: Milk sourcing -> Quality testing -> Starter culture
# and pasteurization depends on quality testing,
# followed by curd cutting --> whey draining --> mold pressing --> salt brining
# fermentation check happens after salt brining
# humidity aging and flavor infuse are concurrent after fermentation check
# rind treatment after flavor infuse
# quality inspect after rind treatment and humidity aging complete
# packaging design after quality inspect
# boutique shipping after packaging design
# market feedback after boutique shipping

# Build partial orders stepwise to keep structure clear

# First segment: milk sourcing -> quality testing -> (starter culture and pasteurize)
segment1 = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Culture, Milk_Pasteurize])
segment1.order.add_edge(Milk_Sourcing, Quality_Testing)
segment1.order.add_edge(Quality_Testing, Starter_Culture)
segment1.order.add_edge(Quality_Testing, Milk_Pasteurize)

# Second segment: after both starter culture and pasteurize finish, curd cutting and whey draining sequentially
segment2 = StrictPartialOrder(nodes=[Curd_Cutting, Whey_Draining, Mold_Pressing, Salt_Brining, Fermentation_Check])
segment2.order.add_edge(Curd_Cutting, Whey_Draining)
segment2.order.add_edge(Whey_Draining, Mold_Pressing)
segment2.order.add_edge(Mold_Pressing, Salt_Brining)
segment2.order.add_edge(Salt_Brining, Fermentation_Check)
# curd cutting depends on both starter culture and pasteurize, so this partial order will be connected accordingly

# Third segment: humidity aging and flavor infuse concurrent after fermentation check
# then rind treatment after flavor infuse
segment3 = StrictPartialOrder(nodes=[Humidity_Aging, Flavor_Infuse, Rind_Treatment])
segment3.order.add_edge(Flavor_Infuse, Rind_Treatment)

# Fourth segment: quality inspect after rind treatment and humidity aging finished
segment4 = StrictPartialOrder(nodes=[Quality_Inspect])
# connections added later to link segment3 nodes to quality inspect

# Fifth segment: packaging design -> boutique shipping -> market feedback
segment5 = StrictPartialOrder(nodes=[Packaging_Design, Boutique_Shipping, Market_Feedback])
segment5.order.add_edge(Packaging_Design, Boutique_Shipping)
segment5.order.add_edge(Boutique_Shipping, Market_Feedback)

# Now combine all segments into a root partial order
# Nodes are all segments' nodes plus the partial orders themselves where relevant
# PM4PY expects a single PO with nodes and order edges; but nodes are transitions or operator POWL
# So we embed segment2 inside segment1 by creating a PO with nodes=[segment1, segment2, segment3, segment4, segment5]
# and add edges among these high-level POs as needed.
# However, since PM4PY POWL StrictPartialOrder nodes must be nodes (Transitions or Operators), 
# we embed segment2,3,4,5 as sets of transitions into one big StrictPartialOrder (root)

all_nodes = [
    Milk_Sourcing, Quality_Testing, Starter_Culture, Milk_Pasteurize,
    Curd_Cutting, Whey_Draining, Mold_Pressing, Salt_Brining, Fermentation_Check,
    Humidity_Aging, Flavor_Infuse, Rind_Treatment,
    Quality_Inspect, Packaging_Design, Boutique_Shipping, Market_Feedback
]

root = StrictPartialOrder(nodes=all_nodes)

# Define all edges following the process description:

# segment1 edges
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Culture)
root.order.add_edge(Quality_Testing, Milk_Pasteurize)

# segment2 edges and dependency from segment1 finishes (Starter Culture and Milk Pasteurize) to Curd Cutting
root.order.add_edge(Starter_Culture, Curd_Cutting)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Mold_Pressing)
root.order.add_edge(Mold_Pressing, Salt_Brining)
root.order.add_edge(Salt_Brining, Fermentation_Check)

# segment3 edges, concurrent after fermentation check
root.order.add_edge(Fermentation_Check, Humidity_Aging)
root.order.add_edge(Fermentation_Check, Flavor_Infuse)
root.order.add_edge(Flavor_Infuse, Rind_Treatment)

# segment4 Quality Inspect after both Humidity Aging and Rind Treatment
root.order.add_edge(Humidity_Aging, Quality_Inspect)
root.order.add_edge(Rind_Treatment, Quality_Inspect)

# segment5 final packaging and shipping
root.order.add_edge(Quality_Inspect, Packaging_Design)
root.order.add_edge(Packaging_Design, Boutique_Shipping)
root.order.add_edge(Boutique_Shipping, Market_Feedback)