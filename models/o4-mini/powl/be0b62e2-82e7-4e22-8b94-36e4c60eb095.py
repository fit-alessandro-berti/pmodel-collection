# Generated from: be0b62e2-82e7-4e22-8b94-36e4c60eb095.json
# Description: This process describes a cyclical approach where multiple industries collaborate to innovate a shared technology platform. It begins with trend spotting in diverse sectors, followed by ideation sessions that mix domain experts. Prototypes are co-developed and tested in controlled pilot environments across industries. Feedback loops involve multi-disciplinary review boards, adapting the product for specific market needs. Parallel regulatory assessments ensure compliance across jurisdictions. After iterative refinement, a joint go-to-market strategy is launched, including synchronized branding and distribution channels. Post-launch monitoring collects cross-sector data to inform the next innovation cycle, fostering sustainable competitive advantage through continuous, collaborative evolution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Trend Spotting')
ih = Transition(label='Idea Harvest')
es = Transition(label='Expert Sync')
cs = Transition(label='Concept Sketch')
fc = Transition(label='Feasibility Check')
pb = Transition(label='Prototype Build')
pd = Transition(label='Pilot Deploy')
mt = Transition(label='Multisector Test')
rb = Transition(label='Review Board')
ma = Transition(label='Market Adapt')
cb = Transition(label='Compliance Audit')
sp = Transition(label='Strategy Plan')
ba = Transition(label='Brand Align')
ls = Transition(label='Launch Sync')
pt = Transition(label='Performance Track')
fl = Transition(label='Feedback Loop')
cr = Transition(label='Cycle Review')

# Build one iteration (A) of the innovation cycle as a partial order
A = StrictPartialOrder(nodes=[
    ts, ih, es, cs, fc, pb, pd, mt,
    rb, cb, ma,
    sp, ba, ls,
    pt, fl, cr
])

# Sequential flow up to prototype testing
A.order.add_edge(ts, ih)
A.order.add_edge(ih, es)
A.order.add_edge(es, cs)
A.order.add_edge(cs, fc)
A.order.add_edge(fc, pb)
A.order.add_edge(pb, pd)
A.order.add_edge(pd, mt)

# After testing: parallel branches to review & compliance
A.order.add_edge(mt, rb)
A.order.add_edge(mt, cb)

# Review branch adapts market needs
A.order.add_edge(rb, ma)

# Both Market Adapt and Compliance Audit must finish before strategy
A.order.add_edge(ma, sp)
A.order.add_edge(cb, sp)

# Go-to-market sequence
A.order.add_edge(sp, ba)
A.order.add_edge(ba, ls)

# Post-launch monitoring and feedback
A.order.add_edge(ls, pt)
A.order.add_edge(pt, fl)
A.order.add_edge(fl, cr)

# Loop control: after one cycle (A), either exit or silently continue
skip = SilentTransition()
root = OperatorPOWL(operator=Operator.LOOP, children=[A, skip])