# Generated from: 98025af4-a756-49c6-b8d0-f2c8727aabc1.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense metropolitan area. It involves initial feasibility studies including structural integrity assessments, microclimate analysis, and community engagement. Following approvals, the process continues with soil-less media selection, irrigation system design, and seed sourcing tailored to urban conditions. Subsequent activities address installation of modular planters, integration of renewable energy sources, pest management using biological controls, and continuous monitoring via IoT sensors. The process concludes with crop harvesting, distribution logistics optimized for local markets, and iterative feedback collection to improve future cycles. This atypical yet practical approach merges urban planning, agriculture, and technology to enhance food security and urban greening.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
fs   = Transition(label='Feasibility Study')
sc   = Transition(label='Structure Check')
cl   = Transition(label='Climate Survey')
cm   = Transition(label='Community Meet')
pr   = Transition(label='Permit Request')
ms   = Transition(label='Media Select')
ip   = Transition(label='Irrigation Plan')
ss   = Transition(label='Seed Sourcing')
ps   = Transition(label='Planter Setup')
ei   = Transition(label='Energy Install')
pc   = Transition(label='Pest Control')
sd   = Transition(label='Sensor Deploy')
crop = Transition(label='Crop Monitor')
hp   = Transition(label='Harvest Plan')
mr   = Transition(label='Market Route')
fb   = Transition(label='Feedback Loop')

# 1) Initial feasibility branch: do a Feasibility Study, then in parallel
#    Structure Check, Climate Survey, Community Meet
initialPO = StrictPartialOrder(nodes=[fs, sc, cl, cm])
initialPO.order.add_edge(fs, sc)
initialPO.order.add_edge(fs, cl)
initialPO.order.add_edge(fs, cm)

# 2) Soil‐less media selection → Irrigation plan → Seed sourcing
seq_media = StrictPartialOrder(nodes=[ms, ip, ss])
seq_media.order.add_edge(ms, ip)
seq_media.order.add_edge(ip, ss)

# 3) Parallel installation & setup tasks
po3 = StrictPartialOrder(nodes=[ps, ei, pc, sd, crop])
#    (no explicit ordering among these tasks, they run concurrently)

# 4) Harvest & distribution as a sequence, with an iterative feedback loop
seq_harvest = StrictPartialOrder(nodes=[hp, mr])
seq_harvest.order.add_edge(hp, mr)

loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seq_harvest, fb]
)

# 5) Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[initialPO, pr, seq_media, po3, loop_feedback])
root.order.add_edge(initialPO, pr)
root.order.add_edge(pr, seq_media)
root.order.add_edge(seq_media, po3)
root.order.add_edge(po3, loop_feedback)