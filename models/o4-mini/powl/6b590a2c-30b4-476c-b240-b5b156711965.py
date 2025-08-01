# Generated from: 6b590a2c-30b4-476c-b240-b5b156711965.json
# Description: This process outlines the systematic approach to identifying, evaluating, and integrating breakthrough technologies from unrelated industries into existing business models. It begins with external trend scouting and unconventional partnership building, followed by rapid prototyping and cross-functional validation. The process emphasizes iterative feedback loops involving diverse teams to adapt innovations for unique market needs, culminating in staged commercialization and performance monitoring to ensure sustainable competitive advantage. This atypical approach encourages out-of-the-box thinking, risk tolerance, and continuous learning to drive transformative growth beyond traditional sector boundaries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts  = Transition(label='Trend Scouting')
pr  = Transition(label='Partner Outreach')
ih  = Transition(label='Idea Harvesting')
tsc = Transition(label='Tech Screening')
fc  = Transition(label='Feasibility Check')
rp  = Transition(label='Rapid Prototyping')
cv  = Transition(label='Cross-Validate')
ut  = Transition(label='User Testing')
itd = Transition(label='Iterate Design')
ra  = Transition(label='Risk Assessment')
ss  = Transition(label='Stakeholder Sync')
pl  = Transition(label='Pilot Launch')
pt  = Transition(label='Performance Track')
ma  = Transition(label='Market Adapt')
sd  = Transition(label='Scale Deployment')

# Build the iterative feedback loop: after initial prototyping (rp), do validate–test–iterate–assess–sync
loop_body = StrictPartialOrder(nodes=[cv, ut, itd, ra, ss])
loop_body.order.add_edge(cv, ut)
loop_body.order.add_edge(ut, itd)
loop_body.order.add_edge(itd, ra)
loop_body.order.add_edge(ra, ss)
loop = OperatorPOWL(operator=Operator.LOOP, children=[rp, loop_body])

# Assemble the full process
root = StrictPartialOrder(nodes=[ts, pr, ih, tsc, fc, loop, pl, pt, ma, sd])
# Phase 1 → idea harvesting
root.order.add_edge(ts,  ih)
root.order.add_edge(pr,  ih)
# Idea harvesting → screening & feasibility (concurrent)
root.order.add_edge(ih,  tsc)
root.order.add_edge(ih,  fc)
# Evaluation → prototyping loop
root.order.add_edge(tsc, loop)
root.order.add_edge(fc,  loop)
# After loop → pilot launch
root.order.add_edge(loop, pl)
# Pilot → performance tracking & market adaptation (concurrent)
root.order.add_edge(pl,  pt)
root.order.add_edge(pl,  ma)
# Both → final scale deployment
root.order.add_edge(pt, sd)
root.order.add_edge(ma, sd)