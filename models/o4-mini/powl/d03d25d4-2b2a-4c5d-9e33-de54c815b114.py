# Generated from: d03d25d4-2b2a-4c5d-9e33-de54c815b114.json
# Description: This process ensures complete traceability and quality control in the artisanal coffee supply chain, from farm to cup. It involves unique steps like micro-lot identification, sensory profiling, blockchain recording, and dynamic pricing based on real-time market demand and quality metrics. The process also integrates direct farmer feedback, environmental impact assessment, and adaptive roasting schedules to optimize flavor profiles while maintaining sustainability and ethical sourcing. Each batch undergoes rigorous testing and certification before distribution, enabling transparency and consumer trust in a highly competitive specialty coffee market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
fr = Transition(label="Farm Registration")
lt = Transition(label="Lot Tagging")
st = Transition(label="Soil Testing")
hl = Transition(label="Harvest Logging")
cs = Transition(label="Coffee Sorting")
sp = Transition(label="Sensory Profiling")
qs = Transition(label="Quality Scoring")
be = Transition(label="Blockchain Entry")
ea = Transition(label="Environmental Audit")
ff = Transition(label="Farmer Feedback")
dp = Transition(label="Dynamic Pricing")
rs = Transition(label="Roast Scheduling")
bt = Transition(label="Batch Testing")
cr = Transition(label="Certification Review")
dist = Transition(label="Distribution Prep")
cf = Transition(label="Consumer Feedback")

# Model the dynamic pricing + farmer feedback as a loop:
#   execute Dynamic Pricing, then either exit or do Farmer Feedback and then repeat
loop_pricing = OperatorPOWL(operator=Operator.LOOP, children=[dp, ff])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    fr, lt, st, hl, cs, sp, qs, be, ea,
    loop_pricing,
    rs, bt, cr, dist, cf
])

# Add the sequencing dependencies
root.order.add_edge(fr, lt)
root.order.add_edge(lt, st)
root.order.add_edge(st, hl)
root.order.add_edge(hl, cs)
root.order.add_edge(cs, sp)
root.order.add_edge(sp, qs)
root.order.add_edge(qs, be)
root.order.add_edge(be, ea)
root.order.add_edge(ea, loop_pricing)
root.order.add_edge(loop_pricing, rs)
root.order.add_edge(rs, bt)
root.order.add_edge(bt, cr)
root.order.add_edge(cr, dist)
root.order.add_edge(dist, cf)