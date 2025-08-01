# Generated from: eceb2fab-1690-40f3-8ace-ff7a5cbeee79.json
# Description: This process involves the identification, evaluation, and meticulous restoration of antique assets for resale or exhibition. It begins with provenance research and condition assessment, followed by careful dismantling, cleaning, and material analysis to determine appropriate restoration techniques. Specialists perform stabilization, reconstruction, and aesthetic enhancement while preserving originality. Each restoration phase is documented for authenticity and compliance. Finally, the asset undergoes quality validation, market valuation, and targeted marketing before delivery to collectors or museums, ensuring historical value and investment potential are maintained throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
cs = Transition(label='Condition Scan')
dis = Transition(label='Disassembly')
sc = Transition(label='Surface Clean')
mt = Transition(label='Material Test')
stb = Transition(label='Stabilize Parts')
sr = Transition(label='Structural Repair')
rc = Transition(label='Reconstruction')
fm = Transition(label='Finish Match')
doc = Transition(label='Documentation')
qa = Transition(label='Quality Audit')
val = Transition(label='Valuation')
ma = Transition(label='Market Analysis')
to = Transition(label='Target Outreach')
dp = Transition(label='Delivery Prep')
cf = Transition(label='Client Feedback')

# Build the overall strict partial order
root = StrictPartialOrder(nodes=[
    pc, cs, dis, sc, mt,
    stb, sr, rc, fm, doc,
    qa, val, ma, to, dp, cf
])

# Establish the sequence of dependencies
root.order.add_edge(pc, cs)
root.order.add_edge(cs, dis)
root.order.add_edge(dis, sc)
root.order.add_edge(sc, mt)

root.order.add_edge(mt, stb)
root.order.add_edge(stb, sr)
root.order.add_edge(sr, rc)
root.order.add_edge(rc, fm)

root.order.add_edge(fm, doc)
root.order.add_edge(doc, qa)
root.order.add_edge(qa, val)
root.order.add_edge(val, ma)

root.order.add_edge(ma, to)
root.order.add_edge(to, dp)
root.order.add_edge(dp, cf)