# Generated from: de616bbd-3f19-4b25-8646-c6568d584849.json
# Description: This process involves establishing a fully automated urban vertical farm within a repurposed warehouse. It begins with site analysis and structural assessment, followed by environmental system design including hydroponics and LED lighting setup. Next, sensor installations for climate control and nutrient monitoring are integrated. Seed selection and germination protocols are developed alongside automated planting routines. Crop growth is continuously monitored using AI-driven analytics to optimize yield and resource usage. Harvesting is performed by robotic arms, and produce is packaged on-site with traceability labeling. Finally, logistics coordination ensures timely delivery to local markets, completing a sustainable urban agriculture cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
sa = Transition(label='Site Analysis')
sc = Transition(label='Structural Check')
sd = Transition(label='System Design')
hs = Transition(label='Hydroponics Setup')
li = Transition(label='Lighting Install')
si = Transition(label='Sensor Install')
cc = Transition(label='Climate Control')
nm = Transition(label='Nutrient Monitor')
ss = Transition(label='Seed Selection')
gs = Transition(label='Germination Start')
ap = Transition(label='Auto Planting')
gm = Transition(label='Growth Monitoring')
ai = Transition(label='AI Analytics')
rh = Transition(label='Robotic Harvest')
pkg = Transition(label='Packaging')
tl = Transition(label='Trace Labeling')
lp = Transition(label='Logistics Plan')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    sa, sc, sd, hs, li, si, cc, nm,
    ss, gs, ap, gm, ai, rh, pkg, tl, lp
])

# Initial assessment feeds into system design
root.order.add_edge(sa, sd)
root.order.add_edge(sc, sd)

# System design leads to hydroponics and lighting setup (concurrent)
root.order.add_edge(sd, hs)
root.order.add_edge(sd, li)

# Both setups precede sensor installation
root.order.add_edge(hs, si)
root.order.add_edge(li, si)

# Sensor install leads to climate control and nutrient monitoring (concurrent)
root.order.add_edge(si, cc)
root.order.add_edge(si, nm)

# Climate control and nutrient monitoring feed into seed selection, germination, and auto planting (all concurrent)
for pre in (cc, nm):
    root.order.add_edge(pre, ss)
    root.order.add_edge(pre, gs)
    root.order.add_edge(pre, ap)

# Those three feed into growth monitoring
root.order.add_edge(ss, gm)
root.order.add_edge(gs, gm)
root.order.add_edge(ap, gm)

# Continuous monitoring then AI analytics
root.order.add_edge(gm, ai)

# Analytics drives robotic harvest, packaging, trace labeling, and logistics in sequence
root.order.add_edge(ai, rh)
root.order.add_edge(rh, pkg)
root.order.add_edge(pkg, tl)
root.order.add_edge(tl, lp)