# Generated from: 01b845f5-6467-4a65-833e-a9e45912565a.json
# Description: This process involves the bespoke design and manufacturing of high-frequency antennas tailored for specialized aerospace and defense applications. It starts with client requirement analysis, followed by electromagnetic simulation and material selection. The process continues with precision machining, micro-assembly, and multi-layer coating to optimize signal integrity and durability. Quality assurance is performed through advanced spectral testing and environmental stress screening. Final packaging includes custom shielding and documentation before dispatch to ensure performance under extreme conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ra = Transition(label='Requirement Analysis')
sm = Transition(label='Signal Modeling')
ms = Transition(label='Material Selection')
pe = Transition(label='Pattern Etching')
sc = Transition(label='Substrate Cutting')
ma = Transition(label='Micro Assembly')
ll = Transition(label='Layer Lamination')
ca = Transition(label='Coating Application')
st = Transition(label='Spectral Testing')
ss = Transition(label='Stress Screening')
tc = Transition(label='Thermal Cycling')
fi = Transition(label='Final Inspection')
sh = Transition(label='Shielding Setup')
doc = Transition(label='Documentation')
cp = Transition(label='Custom Packaging')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ra, sm, ms,
    pe, sc,
    ma, ll, ca,
    st, ss, tc,
    fi,
    sh, doc, cp
])

# 1) After requirement analysis -> simulation & material selection
root.order.add_edge(ra, sm)
root.order.add_edge(ra, ms)

# 2) After both simulation & material selection -> precision machining (parallel etching & cutting)
root.order.add_edge(sm, pe)
root.order.add_edge(sm, sc)
root.order.add_edge(ms, pe)
root.order.add_edge(ms, sc)

# 3) Machine outputs -> micro‐assembly -> layer lamination -> coating application
root.order.add_edge(pe, ma)
root.order.add_edge(sc, ma)
root.order.add_edge(ma, ll)
root.order.add_edge(ll, ca)

# 4) After coating -> QA: spectral testing and stress screening
root.order.add_edge(ca, st)
root.order.add_edge(ca, ss)
# stress screening includes thermal cycling
root.order.add_edge(ss, tc)

# 5) QA results -> final inspection
root.order.add_edge(st, fi)
root.order.add_edge(tc, fi)

# 6) After inspection -> packaging prep (shielding & documentation in parallel)
root.order.add_edge(fi, sh)
root.order.add_edge(fi, doc)

# 7) Shielding & documentation -> custom packaging
root.order.add_edge(sh, cp)
root.order.add_edge(doc, cp)