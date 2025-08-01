# Generated from: 0f16523f-7ed0-4bac-b63c-d20024acab3c.json
# Description: This process involves leveraging a global crowd to generate, refine, and implement innovative solutions for complex business challenges. It starts with problem framing and crowdsourcing ideas through an open platform, followed by multi-stage evaluation, collaborative prototyping, and iterative testing. The process incorporates community voting, expert moderation, and real-time feedback loops to ensure quality and relevance. Successful prototypes undergo pilot deployment with select users, data-driven performance analysis, and scaling strategies. It closes with knowledge capture and incentivization to sustain continual engagement and innovation momentum within diverse stakeholder ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
pf = Transition(label='Problem Frame')
ig = Transition(label='Idea Gather')
cv = Transition(label='Community Vote')
er = Transition(label='Expert Review')
cf = Transition(label='Concept Filter')
pb = Transition(label='Prototype Build')
ut = Transition(label='User Testing')
fl = Transition(label='Feedback Loop')
idg = Transition(label='Iterate Design')
pd = Transition(label='Pilot Deploy')
da = Transition(label='Data Analyze')
sp = Transition(label='Scale Plan')
kc = Transition(label='Knowledge Capture')
ra = Transition(label='Reward Allocate')
eb = Transition(label='Engagement Boost')
ia = Transition(label='Innovation Audit')

# Define the iterative testing loop: build prototype, then test-feedback-iterate until exit
body_loop = StrictPartialOrder(nodes=[ut, fl, idg])
body_loop.order.add_edge(ut, fl)
body_loop.order.add_edge(fl, idg)

loop_proto = OperatorPOWL(operator=Operator.LOOP, children=[pb, body_loop])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    pf, ig, cv, er, cf,
    loop_proto,
    pd, da, sp,
    kc, ra, eb,
    ia
])

# Add the control-flow dependencies
root.order.add_edge(pf, ig)
root.order.add_edge(ig, cv)
root.order.add_edge(cv, er)
root.order.add_edge(er, cf)
root.order.add_edge(cf, loop_proto)
root.order.add_edge(loop_proto, pd)
root.order.add_edge(pd, da)
root.order.add_edge(da, sp)
root.order.add_edge(sp, kc)
root.order.add_edge(kc, ra)
root.order.add_edge(kc, eb)
root.order.add_edge(ra, ia)
root.order.add_edge(eb, ia)