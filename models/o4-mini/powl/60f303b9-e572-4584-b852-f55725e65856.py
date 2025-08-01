# Generated from: 60f303b9-e572-4584-b852-f55725e65856.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban drone delivery network for perishable goods. It includes site assessment, regulatory compliance, drone fleet configuration, dynamic route planning, real-time weather monitoring, payload optimization, multi-agent coordination, emergency response setup, and continuous data analysis to ensure safe, efficient, and scalable delivery in dense metropolitan environments while minimizing environmental impact and adhering to privacy laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ss = Transition(label='Site Survey')
pc = Transition(label='Permit Check')
fc = Transition(label='Fleet Config')
pp = Transition(label='Payload Prep')
rd = Transition(label='Route Design')
wt = Transition(label='Weather Track')
ssig = Transition(label='Signal Setup')
ft = Transition(label='Flight Test')
lb = Transition(label='Load Balance')
ds = Transition(label='Data Sync')
ra = Transition(label='Risk Assess')
ed = Transition(label='Emergency Drill')
pa = Transition(label='Privacy Audit')
fd = Transition(label='Fleet Deploy')
dt = Transition(label='Delivery Track')
fb = Transition(label='Feedback Loop')
skip = SilentTransition()

# Optional emergency drill: either perform it or skip
emergency_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[ed, skip]
)

# Feedback loop on delivery: do Delivery Track, then choose exit or Feedback Loop then repeat
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[dt, fb]
)

# Parallel execution of load balancing and data synchronization
lb_ds_parallel = StrictPartialOrder(nodes=[lb, ds])

# Build the overall partially ordered workflow
root = StrictPartialOrder(
    nodes=[
        ss, pc, fc,
        pp, rd, wt, ssig,
        ft,
        lb_ds_parallel,
        ra, emergency_choice,
        pa, fd,
        feedback_loop
    ]
)

# Add the control-flow dependencies
o = root.order
o.add_edge(ss, pc)
o.add_edge(pc, fc)
# After fleet configuration, prepare payload, design routes, track weather, set up signals concurrently
o.add_edge(fc, pp)
o.add_edge(fc, rd)
o.add_edge(fc, wt)
o.add_edge(fc, ssig)
# Flight test after payload, routing and signal setup (and weather monitoring can overlap)
o.add_edge(pp, ft)
o.add_edge(rd, ft)
o.add_edge(ssig, ft)
o.add_edge(wt, ft)
# After flight test, do load balancing and data sync in parallel
o.add_edge(ft, lb_ds_parallel)
# Then risk assessment, optional emergency drill, privacy audit, fleet deployment
o.add_edge(lb_ds_parallel, ra)
o.add_edge(ra, emergency_choice)
o.add_edge(emergency_choice, pa)
o.add_edge(pa, fd)
# Finally deploy and enter the delivery/feedback loop
o.add_edge(fd, feedback_loop)