# Generated from: 89ca1cb6-0c98-4160-b1fa-8b623c524694.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a dense city environment. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, and community integration strategies. The process requires coordinating multidisciplinary teams to address challenges such as limited space, energy efficiency, waste management, and crop selection tailored for vertical growth. Continuous monitoring and adaptive adjustments ensure sustainable yield and environmental compliance, ultimately fostering local food production in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
ts = Transition(label='Site Survey')
tl = Transition(label='Design Layout')
sb = Transition(label='System Build')
cs1 = Transition(label='Climate Setup')
lt1 = Transition(label='Lighting Tune')
nm1 = Transition(label='Nutrient Mix')
wc1 = Transition(label='Water Cycle')
ea = Transition(label='Energy Audit')
wp = Transition(label='Waste Plan')
rc = Transition(label='Regulation Check')
cr = Transition(label='Crop Select')
pa = Transition(label='Pollination Aid')
pc = Transition(label='Pest Control')
dm = Transition(label='Data Monitor')
yr = Transition(label='Yield Review')
cm = Transition(label='Community Meet')
sc = Transition(label='Supply Chain')

# For the adaptive‐adjustment loop, we need fresh Transition instances
cs2 = Transition(label='Climate Setup')
lt2 = Transition(label='Lighting Tune')
nm2 = Transition(label='Nutrient Mix')
wc2 = Transition(label='Water Cycle')

# Body of the loop: monitor data then review yield
body = StrictPartialOrder(nodes=[dm, yr])
body.order.add_edge(dm, yr)

# Redo‐branch of the loop: choose one adjustment to repeat
redo = OperatorPOWL(operator=Operator.XOR, children=[cs2, lt2, nm2, wc2])

# Loop operator: do (body), then either exit or do (redo) and repeat body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ts, tl, sb, cs1, lt1, nm1, wc1,   # initial setup path
    ea, wp, rc,                       # audits & checks (parallel)
    cr,                               # crop selection
    pa, pc,                           # pollination & pest control (parallel)
    loop,                             # monitoring & adaptive loop
    cm, sc                            # community integration and supply chain
])

# Sequential edges for the initial setup
root.order.add_edge(ts, tl)
root.order.add_edge(tl, sb)
root.order.add_edge(sb, cs1)
root.order.add_edge(cs1, lt1)
root.order.add_edge(lt1, nm1)
root.order.add_edge(nm1, wc1)

# After setup, trigger audits/checks in parallel
root.order.add_edge(wc1, ea)
root.order.add_edge(wc1, wp)
root.order.add_edge(wc1, rc)

# All audits must complete before crop selection
root.order.add_edge(ea, cr)
root.order.add_edge(wp, cr)
root.order.add_edge(rc, cr)

# After crop select, launch pollination and pest control in parallel
root.order.add_edge(cr, pa)
root.order.add_edge(cr, pc)

# Both pollination & pest control must finish before entering the loop
root.order.add_edge(pa, loop)
root.order.add_edge(pc, loop)

# After exiting the loop, proceed to community meeting then supply chain
root.order.add_edge(loop, cm)
root.order.add_edge(cm, sc)