# Generated from: 613a6e3d-3e88-4750-a7ac-eee645e486fd.json
# Description: This process details the complex cycle of managing an urban vertical farm that integrates hydroponics and AI-driven environmental controls to optimize crop yield in limited city spaces. The process includes seed selection based on market demand, automated nutrient mixing, real-time climate adjustments, pest detection through machine vision, and dynamic harvesting schedules. It also incorporates waste recycling from plant residue into biofertilizers, energy management through solar and battery systems, and data analysis for continuous improvement. The cycle ends with distribution logistics tailored for last-mile urban delivery, ensuring freshness and minimal carbon footprint while maintaining regulatory compliance and consumer feedback integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Transitions for each activity
ss = Transition(label='Seed Select')
nm = Transition(label='Nutrient Mix')
pset = Transition(label='Plant Setup')
ct = Transition(label='Climate Tune')
ws = Transition(label='Water Supply')
la = Transition(label='Light Adjust')
gm = Transition(label='Growth Monitor')
ps = Transition(label='Pest Scan')
bw = Transition(label='Bio Waste')
em = Transition(label='Energy Manage')
hp = Transition(label='Harvest Plan')
cp = Transition(label='Crop Pick')
po = Transition(label='Pack Order')
dr = Transition(label='Delivery Route')
fl = Transition(label='Feedback Log')
da = Transition(label='Data Analyze')

# Loop: repeatedly monitor growth and then optionally re‐apply adjustments
# Body of the loop (always executed): Growth Monitor
body = gm
# Redo part (applied before next iteration): Pest Scan, Climate Tune, Water Supply, Light Adjust, Nutrient Mix (all concurrent)
redo = StrictPartialOrder(nodes=[ps, ct, ws, la, nm])
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# Concurrent end‐of‐cycle tasks: Bio Waste recycling and Energy Management
end_conc = StrictPartialOrder(nodes=[bw, em])

# Main workflow partial order
root = StrictPartialOrder(
    nodes=[ss, nm, pset, ct, ws, la, loop, hp, cp, po, dr, end_conc, fl, da]
)

# Define the control‐flow (partial order edges)
root.order.add_edge(ss, nm)
root.order.add_edge(nm, pset)
root.order.add_edge(pset, ct)
root.order.add_edge(ct, ws)
root.order.add_edge(ws, la)
root.order.add_edge(la, loop)
root.order.add_edge(loop, hp)
root.order.add_edge(hp, cp)
root.order.add_edge(cp, po)
root.order.add_edge(po, dr)
root.order.add_edge(dr, end_conc)
root.order.add_edge(end_conc, fl)
root.order.add_edge(fl, da)