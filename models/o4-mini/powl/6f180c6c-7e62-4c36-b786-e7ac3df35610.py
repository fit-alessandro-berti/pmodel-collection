# Generated from: 6f180c6c-7e62-4c36-b786-e7ac3df35610.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It includes initial site assessment considering structural integrity and sunlight exposure, securing permits from local authorities, sourcing sustainable soil and seeds, installing efficient irrigation systems, and integrating automated climate controls. Additionally, it involves community engagement for education and volunteer programs, ongoing pest management with eco-friendly methods, crop rotation planning to maintain soil health, and establishing partnerships with local markets for produce distribution. Finally, the process covers regular yield monitoring, data collection for optimization, and scaling strategies for expansion to additional rooftops in urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
sa = Transition(label='Site Assess')
pa = Transition(label='Permit Acquire')
soil = Transition(label='Soil Source')
seed = Transition(label='Seed Select')
irr = Transition(label='Irrigation Install')
climate = Transition(label='Climate Setup')
vol = Transition(label='Volunteer Recruit')
comm = Transition(label='Community Meet')
pc = Transition(label='Pest Control')
crop = Transition(label='Crop Rotate')
market = Transition(label='Market Partner')
yield_mon = Transition(label='Yield Monitor')
data = Transition(label='Data Collect')
opt = Transition(label='Optimize Plan')
scale = Transition(label='Scale Expand')

# Loop for ongoing pest control and crop rotation
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[pc, crop])

# Sequence Data Collect -> Optimize Plan as the body of the second loop
po_data_opt = StrictPartialOrder(nodes=[data, opt])
po_data_opt.order.add_edge(data, opt)

# Loop for yield monitoring and optimization
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[yield_mon, po_data_opt])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    sa, pa,
    soil, seed,
    irr, climate,
    vol, comm,
    loop1,
    market,
    loop2,
    scale
])
# Define the control‐flow edges
root.order.add_edge(sa, pa)
root.order.add_edge(pa, soil)
root.order.add_edge(pa, seed)
root.order.add_edge(soil, irr)
root.order.add_edge(seed, irr)
root.order.add_edge(irr, climate)
root.order.add_edge(climate, vol)
root.order.add_edge(climate, comm)
root.order.add_edge(vol, loop1)
root.order.add_edge(comm, loop1)
root.order.add_edge(loop1, market)
root.order.add_edge(market, loop2)
root.order.add_edge(loop2, scale)