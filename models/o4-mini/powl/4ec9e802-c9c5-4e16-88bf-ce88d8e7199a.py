# Generated from: 4ec9e802-c9c5-4e16-88bf-ce88d8e7199a.json
# Description: This process outlines a highly adaptive urban farming cycle designed to optimize crop yields in micro-environments within cityscapes. It begins with microclimate scanning to assess localized conditions, followed by dynamic soil profiling to tailor nutrient delivery. The system employs modular planting strategies which adapt based on real-time sensor data, enabling selective germination and staggered growth phases. Automated pest detection and biological control deployment ensure sustainable protection without chemicals. Concurrently, vertical irrigation management adjusts water flow based on evapotranspiration rates. Harvesting is synchronized with market demand analytics to minimize waste and maximize freshness. Post-harvest sorting integrates AI-driven quality assessment, while urban composting loops recycle organic waste into nutrient-rich substrates. Finally, community feedback and data-driven analytics refine future cycles, creating a continuous improvement loop tailored for dense urban agricultural ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define all activities
ms  = Transition(label='Microclimate Scan')
sp  = Transition(label='Soil Profiling')
nm  = Transition(label='Nutrient Mapping')
mp  = Transition(label='Modular Planting')
sc  = Transition(label='Sensor Calibration')
gc  = Transition(label='Germination Check')
gs  = Transition(label='Growth Staggering')
pd  = Transition(label='Pest Detection')
bc  = Transition(label='Biocontrol Deploy')
ia  = Transition(label='Irrigation Adjust')
msy = Transition(label='Market Sync')
ht  = Transition(label='Harvest Timing')
qs  = Transition(label='Quality Sorting')
cp  = Transition(label='Compost Processing')
fa  = Transition(label='Feedback Analyze')
cr  = Transition(label='Cycle Refinement')

# Body of one farming cycle
A = StrictPartialOrder(nodes=[ms, sp, nm, mp, sc, gc, gs, pd, bc, ia, msy, ht, qs, cp])
A.order.add_edge(ms,  sp)
A.order.add_edge(sp,  nm)
A.order.add_edge(nm,  mp)
A.order.add_edge(mp,  sc)
A.order.add_edge(sc,  gc)
A.order.add_edge(gc,  gs)
A.order.add_edge(gs,  pd)
A.order.add_edge(gs,  ia)
A.order.add_edge(pd,  bc)
A.order.add_edge(bc,  msy)
A.order.add_edge(ia,  msy)
A.order.add_edge(msy, ht)
A.order.add_edge(ht,  qs)
A.order.add_edge(qs,  cp)

# Feedback-and-refinement part
B = StrictPartialOrder(nodes=[fa, cr])
B.order.add_edge(fa, cr)

# Loop over cycles: execute A, then either exit or do B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])