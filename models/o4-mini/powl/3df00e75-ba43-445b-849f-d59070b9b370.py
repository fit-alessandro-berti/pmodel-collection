# Generated from: 3df00e75-ba43-445b-849f-d59070b9b370.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil preparation, microclimate optimization, seed selection, irrigation system design, pest management planning, community engagement, regulatory compliance, crop rotation scheduling, harvest logistics, waste recycling, and market distribution. Each activity ensures environmental sustainability, economic viability, and social inclusiveness in the unique context of urban agriculture on rooftops, accounting for space constraints, weather variability, and local regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
ss = Transition(label="Site Survey")
la = Transition(label="Load Analysis")
st = Transition(label="Soil Testing")
cs = Transition(label="Climate Study")
se = Transition(label="Seed Selection")
ip = Transition(label="Irrigation Plan")
pc = Transition(label="Pest Control")
cm = Transition(label="Community Meet")
pf = Transition(label="Permit Filing")
cr = Transition(label="Crop Rotation")
ps = Transition(label="Planting Setup")
gm = Transition(label="Growth Monitoring")
hp = Transition(label="Harvest Prep")
ws = Transition(label="Waste Sorting")
md = Transition(label="Market Delivery")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ss, la, st, cs, se, ip, pc, cm, pf, cr, ps, gm, hp, ws, md
])

# Site Survey is the starting point
root.order.add_edge(ss, la)
root.order.add_edge(ss, st)
root.order.add_edge(ss, cs)
root.order.add_edge(ss, cm)
root.order.add_edge(ss, pf)

# Soil Testing & Climate Study drive planning of seeds, irrigation, pest control
root.order.add_edge(st, se)
root.order.add_edge(cs, se)
root.order.add_edge(st, ip)
root.order.add_edge(cs, ip)
root.order.add_edge(st, pc)
root.order.add_edge(cs, pc)

# Seed Selection leads to Crop Rotation scheduling
root.order.add_edge(se, cr)

# Planting Setup requires seed plan, irrigation plan, pest plan, permits, community engagement
root.order.add_edge(se, ps)
root.order.add_edge(ip, ps)
root.order.add_edge(pc, ps)
root.order.add_edge(pf, ps)
root.order.add_edge(cm, ps)

# Growth Monitoring depends on planting, crop rotation, and irrigation
root.order.add_edge(ps, gm)
root.order.add_edge(cr, gm)
root.order.add_edge(ip, gm)

# Harvest Prep follows growth monitoring
root.order.add_edge(gm, hp)

# Waste Sorting after harvest preparation
root.order.add_edge(hp, ws)

# Market Delivery is the final step
root.order.add_edge(ws, md)