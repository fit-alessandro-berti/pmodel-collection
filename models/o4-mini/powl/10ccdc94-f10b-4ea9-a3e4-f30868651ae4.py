# Generated from: 10ccdc94-f10b-4ea9-a3e4-f30868651ae4.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It begins with structural assessment and legal compliance checks, followed by soil and water testing. Selection of plant varieties suitable for rooftop conditions is critical, alongside the installation of irrigation and drainage systems. The process also includes microclimate monitoring, pest control strategies tailored to urban environments, and community engagement for educational programs. Finally, ongoing maintenance schedules and yield optimization through data analytics complete the setup, ensuring a sustainable and productive rooftop farm in a dense cityscape.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sc   = Transition(label='Structure Check')
lr   = Transition(label='Legal Review')
st   = Transition(label='Soil Testing')
wa   = Transition(label='Water Analysis')
ps   = Transition(label='Plant Selection')
iset = Transition(label='Irrigation Setup')
di   = Transition(label='Drainage Install')
cm   = Transition(label='Climate Monitor')
pc   = Transition(label='Pest Control')
ce   = Transition(label='Community Engage')
ep   = Transition(label='Education Plan')
mp   = Transition(label='Maintenance Plan')
yt   = Transition(label='Yield Tracking')
da   = Transition(label='Data Analytics')
hs   = Transition(label='Harvest Schedule')
wm   = Transition(label='Waste Manage')

# Build the loop body for ongoing operations: Yield -> Data -> Harvest -> Waste
body = StrictPartialOrder(nodes=[yt, da, hs, wm])
body.order.add_edge(yt, da)
body.order.add_edge(da, hs)
body.order.add_edge(hs, wm)

# Loop: do Maintenance Plan, then optionally do body and again Maintenance Plan, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[mp, body])

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    sc, lr,             # initial checks
    st, wa,             # testing
    ps,                 # selection
    iset, di,           # installation
    cm, pc, ce, ep,     # monitoring & community/education
    loop                # ongoing operations
])

# Dependencies: initial checks -> testing
root.order.add_edge(sc, st)
root.order.add_edge(sc, wa)
root.order.add_edge(lr, st)
root.order.add_edge(lr, wa)

# testing -> plant selection
root.order.add_edge(st, ps)
root.order.add_edge(wa, ps)

# selection -> installation
root.order.add_edge(ps, iset)
root.order.add_edge(ps, di)

# installation -> monitoring & engagement
for prev in (iset, di):
    root.order.add_edge(prev, cm)
    root.order.add_edge(prev, pc)
    root.order.add_edge(prev, ce)
    root.order.add_edge(prev, ep)

# monitoring & engagement -> loop
for prev in (cm, pc, ce, ep):
    root.order.add_edge(prev, loop)