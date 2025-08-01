# Generated from: 05332ff8-4cf2-481c-8a8b-8175180b81db.json
# Description: This process involves integrating disparate industry insights to generate breakthrough innovations. It begins with cross-sector trend scanning, followed by ideation workshops leveraging diverse experts. Concepts undergo rapid prototyping paired with real-time user feedback loops. Concurrently, risk assessments and regulatory reviews ensure viability. Iterative refinement cycles incorporate market simulation data. Final outputs include scalable business models and tailored go-to-market strategies, all orchestrated through agile governance and continuous knowledge sharing across departments to accelerate adoption and impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activity transitions
ts = Transition(label='Trend Scan')
es = Transition(label='Expert Sync')
ispr = Transition(label='Idea Sprint')
pb = Transition(label='Proto Build')
ut = Transition(label='User Test')
rr = Transition(label='Risk Review')
rgr = Transition(label='Reg Review')
ms = Transition(label='Market Sim')
fl = Transition(label='Feedback Loop')
md = Transition(label='Model Design')
sp = Transition(label='Strategy Plan')
aa = Transition(label='Agile Align')
ds = Transition(label='Data Share')
ia = Transition(label='Impact Assess')
lp = Transition(label='Launch Prep')

# Define the iterative refinement loop: execute Market Sim, 
# then either exit or do Feedback Loop + Market Sim again
loop = OperatorPOWL(operator=Operator.LOOP, children=[ms, fl])

# Build the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    ts, es, ispr, pb, ut, rr, rgr, loop,
    md, sp, aa, ds, ia, lp
])

# Sequence: Trend Scan → Expert Sync → Idea Sprint → Proto Build → User Test
root.order.add_edge(ts, es)
root.order.add_edge(es, ispr)
root.order.add_edge(ispr, pb)
root.order.add_edge(pb, ut)

# After User Test, do Risk Review and Reg Review in parallel
root.order.add_edge(ut, rr)
root.order.add_edge(ut, rgr)

# After both reviews, enter the refinement loop
root.order.add_edge(rr, loop)
root.order.add_edge(rgr, loop)

# After finishing the loop, concurrently design model and strategy
root.order.add_edge(loop, md)
root.order.add_edge(loop, sp)

# Then align agile governance and share data in parallel
root.order.add_edge(md, aa)
root.order.add_edge(sp, aa)
root.order.add_edge(md, ds)
root.order.add_edge(sp, ds)

# Finally assess impact and prepare for launch
root.order.add_edge(aa, ia)
root.order.add_edge(ds, ia)
root.order.add_edge(ia, lp)