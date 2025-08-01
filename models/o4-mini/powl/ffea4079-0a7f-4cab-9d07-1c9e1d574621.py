# Generated from: ffea4079-0a7f-4cab-9d07-1c9e1d574621.json
# Description: This process involves designing, deploying, and managing a large-scale crisis simulation for emergency response teams across multiple agencies. It includes scenario creation, resource allocation, real-time monitoring, dynamic adjustment of variables, inter-agency communication protocols, and post-simulation analysis and reporting. The process requires coordination between technology teams, field operatives, and decision-makers to ensure realistic conditions and effective training outcomes. Feedback loops and iterative refinement are essential to improve future simulations and validate response strategies under evolving threat landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ss   = Transition(label='Scenario Setup')
rm   = Transition(label='Resource Mapping')
tb   = Transition(label='Team Briefing')
td   = Transition(label='Tech Deployment')
ds   = Transition(label='Data Sync')
cs   = Transition(label='Comm Setup')
ii   = Transition(label='Incident Injection')
lm   = Transition(label='Live Monitoring')
rt   = Transition(label='Response Tracking')
ic   = Transition(label='Interlock Check')
rf   = Transition(label='Real-time Feedback')
va   = Transition(label='Variable Adjust')
debr = Transition(label='Debrief Session')
oa   = Transition(label='Outcome Analysis')
rg   = Transition(label='Report Generation')
impr = Transition(label='Improvement Plan')

# Small loop: run the simulation steps, then optionally adjust variables and repeat
A_small = StrictPartialOrder(nodes=[ii, lm, rt, ic, rf])
A_small.order.add_edge(ii, lm)
A_small.order.add_edge(lm, rt)
A_small.order.add_edge(rt, ic)
A_small.order.add_edge(ic, rf)
small_loop = OperatorPOWL(operator=Operator.LOOP, children=[A_small, va])

# Main sequence (one simulation run)
A_big = StrictPartialOrder(
    nodes=[ss, rm, tb, td, ds, cs, small_loop, debr, oa, rg]
)
# setup ordering
A_big.order.add_edge(ss,   rm)
A_big.order.add_edge(rm,   tb)
# after briefing, tech & data & comm can run in parallel
A_big.order.add_edge(tb,   td)
A_big.order.add_edge(tb,   ds)
A_big.order.add_edge(tb,   cs)
# all three must complete before the simulation loop starts
A_big.order.add_edge(td,       small_loop)
A_big.order.add_edge(ds,       small_loop)
A_big.order.add_edge(cs,       small_loop)
# after simulation loop, do debrief, analysis, report
A_big.order.add_edge(small_loop, debr)
A_big.order.add_edge(debr,      oa)
A_big.order.add_edge(oa,        rg)

# Top‐level loop: after report generation, create improvement plan and iterate
root = OperatorPOWL(operator=Operator.LOOP, children=[A_big, impr])