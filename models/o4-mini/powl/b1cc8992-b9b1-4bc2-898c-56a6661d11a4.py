# Generated from: b1cc8992-b9b1-4bc2-898c-56a6661d11a4.json
# Description: This process involves establishing an urban vertical farm in a dense metropolitan area, integrating sustainable agriculture with advanced technology. It includes site analysis, modular system design, climate control calibration, nutrient cycling optimization, and IoT sensor deployment. The process ensures efficient use of limited space by stacking growing layers, automating plant care, and minimizing resource consumption. It also incorporates community engagement, compliance with urban regulations, and a phased production rollout to guarantee consistent crop yield and quality throughout varying seasonal conditions in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ss = Transition(label="Site Survey")
rc = Transition(label="Regulation Check")
sd = Transition(label="System Design")
mb = Transition(label="Modular Build")
cs = Transition(label="Climate Setup")
si = Transition(label="Sensor Install")
nm = Transition(label="Nutrient Mix")
wc = Transition(label="Water Cycle")
lc = Transition(label="Light Calibration")
ps = Transition(label="Plant Selection")
au = Transition(label="Automation Setup")
di = Transition(label="Data Integration")
tg = Transition(label="Trial Growth")
qt = Transition(label="Quality Test")
co = Transition(label="Community Outreach")
ya = Transition(label="Yield Analysis")
mp = Transition(label="Maintenance Plan")

# Silent transition for the LOOP operator
skip = SilentTransition()

# Build the loop for repeated trial‐&‐test cycles:
#   body A = Trial Growth -> Quality Test
#   redo  B = silent (skip) so we can iterate or exit
po_tq = StrictPartialOrder(nodes=[tg, qt])
po_tq.order.add_edge(tg, qt)
loop = OperatorPOWL(operator=Operator.LOOP, children=[po_tq, skip])

# Build the overall partial‐order workflow
root = StrictPartialOrder(
    nodes=[ss, rc, sd, mb, cs, si, au, nm, wc, lc, di, ps, co, loop, ya, mp]
)

# 1) Site Survey -> Regulation Check -> System Design
root.order.add_edge(ss, rc)
root.order.add_edge(rc, sd)
# 2) After design, do Modular Build and start Community Outreach in parallel
root.order.add_edge(sd, mb)
root.order.add_edge(sd, co)
# 3) From Modular Build, spin up infrastructure in parallel
root.order.add_edge(mb, cs)   # climate
root.order.add_edge(mb, si)   # sensors
root.order.add_edge(mb, au)   # automation
root.order.add_edge(mb, nm)   # nutrient system
# 4) Climate -> Light Calibration
root.order.add_edge(cs, lc)
# 5) Nutrient Mix -> Water Cycle
root.order.add_edge(nm, wc)
# 6) Sensors & Automation feed into Data Integration
root.order.add_edge(si, di)
root.order.add_edge(au, di)
# 7) Calibration / setup complete before Plant Selection
root.order.add_edge(lc, ps)
root.order.add_edge(wc, ps)
root.order.add_edge(di, ps)
# 8) Plant Selection -> Trial‐&‐Test loop
root.order.add_edge(ps, loop)
# 9) After loop exit, yield analysis (also waits for community outreach to finish)
root.order.add_edge(loop, ya)
root.order.add_edge(co, ya)
# 10) Finally proceed to Maintenance Plan
root.order.add_edge(ya, mp)