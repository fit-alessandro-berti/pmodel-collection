# Generated from: 30403100-c1f8-4d43-9b0b-47f49f085b27.json
# Description: This process outlines the intricate steps involved in producing, aging, and distributing artisan cheeses from small-scale farms to niche gourmet shops. It begins with milk sourcing and quality testing, followed by curdling and molding. The cheese then undergoes controlled aging with regular monitoring of humidity and temperature. Packaging requires specialized materials to maintain freshness, and logistics include refrigerated transport with real-time tracking. Finally, marketing involves targeted outreach to culinary experts and hosting tasting events to build brand recognition. Each stage requires close coordination to ensure product authenticity and compliance with food safety standards, making the process both complex and highly specialized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

MS = Transition(label='Milk Sourcing')
QT = Transition(label='Quality Testing')
MP = Transition(label='Milk Pasteurize')
CF = Transition(label='Curd Formation')
MPres = Transition(label='Mold Pressing')
SS = Transition(label='Salting Stage')
AS = Transition(label='Aging Setup')
HC = Transition(label='Humidity Check')
TL = Transition(label='Temperature Log')
FS = Transition(label='Flavor Sampling')
PP = Transition(label='Packaging Prep')
SI = Transition(label='Seal Inspection')
CS = Transition(label='Cold Storage')
TR = Transition(label='Transport Route')
DC = Transition(label='Delivery Confirm')
MPush = Transition(label='Marketing Push')
EH = Transition(label='Event Hosting')

# Aging monitoring partial order: Humidity Check, Temperature Log, Flavor Sampling concurrent
aging_monitoring = StrictPartialOrder(nodes=[HC, TL, FS])

# Define packaging partial order
packaging = StrictPartialOrder(nodes=[PP, SI])
packaging.order.add_edge(PP, SI)

# Define logistics partial order
logistics = StrictPartialOrder(nodes=[CS, TR, DC])
logistics.order.add_edge(CS, TR)
logistics.order.add_edge(TR, DC)

# Define marketing partial order
marketing = StrictPartialOrder(nodes=[MPush, EH])
marketing.order.add_edge(MPush, EH)

# Aging stage as partial order: Aging Setup then concurrent aging monitoring
aging_stage = StrictPartialOrder(nodes=[AS, aging_monitoring])
aging_stage.order.add_edge(AS, aging_monitoring)

# Produce partial order: Milk Sourcing -> Quality Testing -> Milk Pasteurize -> Curd Formation -> Mold Pressing -> Salting Stage -> aging_stage
produce = StrictPartialOrder(nodes=[MS, QT, MP, CF, MPres, SS, aging_stage])
produce.order.add_edge(MS, QT)
produce.order.add_edge(QT, MP)
produce.order.add_edge(MP, CF)
produce.order.add_edge(CF, MPres)
produce.order.add_edge(MPres, SS)
produce.order.add_edge(SS, aging_stage)

# Final full partial order including packaging, logistics, marketing all in sequence
root = StrictPartialOrder(
    nodes=[produce, packaging, logistics, marketing]
)
root.order.add_edge(produce, packaging)
root.order.add_edge(packaging, logistics)
root.order.add_edge(logistics, marketing)