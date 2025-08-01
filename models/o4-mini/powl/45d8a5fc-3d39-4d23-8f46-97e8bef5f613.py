# Generated from: 45d8a5fc-3d39-4d23-8f46-97e8bef5f613.json
# Description: This process outlines the complex and multidisciplinary approach required to establish a sustainable urban rooftop farm in a densely populated city. It begins with site assessment and structural evaluation, followed by obtaining permits and integrating smart irrigation systems. The workflow includes soil testing, modular bed installation, seed selection, and pest management planning. Additionally, the process incorporates community engagement initiatives, renewable energy integration, crop monitoring through IoT devices, and waste composting strategies. Finally, it concludes with harvest scheduling and urban market distribution logistics, ensuring environmental compliance and maximizing yield within limited rooftop spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
sa = Transition(label='Site Assess')
st = Transition(label='Structure Test')
pa = Transition(label='Permit Acquire')
ir = Transition(label='Irrigation Plan')
so = Transition(label='Soil Analyze')
bi = Transition(label='Bed Install')
sc = Transition(label='Seed Choose')
pc = Transition(label='Pest Control')
cm = Transition(label='Community Meet')
es = Transition(label='Energy Setup')
cr = Transition(label='Crop Monitor')
wc = Transition(label='Waste Compost')
hp = Transition(label='Harvest Plan')
ms = Transition(label='Market Ship')
cc = Transition(label='Compliance Check')

# Build the partial order
root = StrictPartialOrder(nodes=[sa, st, pa, ir,
                                 so, bi, sc, pc,
                                 cm, es, cr, wc,
                                 hp, cc, ms])

# Phase 1 -> Phase 2
root.order.add_edge(sa, pa)
root.order.add_edge(sa, ir)
root.order.add_edge(st, pa)
root.order.add_edge(st, ir)

# Phase 2 -> Phase 3
for prev in [pa, ir]:
    for nxt in [so, bi, sc, pc]:
        root.order.add_edge(prev, nxt)

# Phase 3 -> Phase 4
for prev in [so, bi, sc, pc]:
    for nxt in [cm, es, cr, wc]:
        root.order.add_edge(prev, nxt)

# Phase 4 -> Phase 5 (harvest planning and compliance)
for prev in [cm, es, cr, wc]:
    root.order.add_edge(prev, hp)
    root.order.add_edge(prev, cc)

# Phase 5 -> Final shipping
root.order.add_edge(hp, ms)
root.order.add_edge(cc, ms)