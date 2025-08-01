# Generated from: 7b1a9edd-8c90-4d84-8749-609e2667fee5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, focusing on integrating advanced hydroponic systems, renewable energy sources, and AI-driven crop management. It begins with site analysis and urban zoning compliance, followed by modular structure assembly and environmental control installation. Crop selection is tailored for urban consumer demand, optimizing yield and nutrient density. The process includes water recycling system setup and renewable energy integration to minimize environmental impact. Continuous AI monitoring adjusts lighting, nutrients, and climate to maximize growth efficiency. Finally, harvested produce undergoes quality assessment before packaging and distribution to local markets, ensuring freshness and sustainability throughout the urban supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label="Site Analysis")
zr = Transition(label="Zoning Review")
mb = Transition(label="Modular Build")
hs = Transition(label="Hydroponic Setup")
ei = Transition(label="Energy Install")
wr = Transition(label="Water Recycling")
ec_setup = Transition(label="Climate Control")
cs = Transition(label="Crop Select")
ai = Transition(label="AI Calibration")
nm = Transition(label="Nutrient Mix")
ec_loop = Transition(label="Climate Control")
gc = Transition(label="Growth Monitor")
qc = Transition(label="Quality Check")
pp = Transition(label="Packaging Prep")
md = Transition(label="Market Dispatch")
wm = Transition(label="Waste Manage")

# Monitoring sequence that will be looped
monitor_seq = StrictPartialOrder(nodes=[ai, nm, ec_loop, gc])
monitor_seq.order.add_edge(ai, nm)
monitor_seq.order.add_edge(nm, ec_loop)
monitor_seq.order.add_edge(ec_loop, gc)

# Loop over the monitoring sequence
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_seq, monitor_seq])

# Root partial order
root = StrictPartialOrder(nodes=[
    sa, zr, mb, hs,
    ei, wr, ec_setup,
    cs, monitor_loop,
    qc, pp, md, wm
])

# Sequence: Site Analysis -> Zoning Review -> Modular Build -> Hydroponic Setup
root.order.add_edge(sa, zr)
root.order.add_edge(zr, mb)
root.order.add_edge(mb, hs)

# After Hydroponic Setup: Energy Install, Water Recycling, Climate Control concurrently
root.order.add_edge(hs, ei)
root.order.add_edge(hs, wr)
root.order.add_edge(hs, ec_setup)

# All three precede Crop Select
root.order.add_edge(ei, cs)
root.order.add_edge(wr, cs)
root.order.add_edge(ec_setup, cs)

# Crop Select -> Monitoring Loop -> Quality Check -> Packaging Prep
root.order.add_edge(cs, monitor_loop)
root.order.add_edge(monitor_loop, qc)
root.order.add_edge(qc, pp)

# Packaging Prep -> Market Dispatch and Waste Manage (concurrent)
root.order.add_edge(pp, md)
root.order.add_edge(pp, wm)