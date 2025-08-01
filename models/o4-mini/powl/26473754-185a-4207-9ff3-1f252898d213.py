# Generated from: 26473754-185a-4207-9ff3-1f252898d213.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield in limited city spaces by dynamically integrating environmental data, community feedback, and resource constraints. It begins with microclimate analysis to assess localized conditions, followed by tailored seed selection that suits the urban microenvironment. Subsequent activities involve nutrient profiling and automated irrigation scheduling to maximize growth efficiency. The system incorporates pest monitoring using AI-powered sensors, triggering organic treatment protocols only when thresholds are exceeded. Community engagement is facilitated through real-time data sharing and volunteer coordination, ensuring social sustainability. Harvest timing is continuously adjusted based on predictive growth models, while post-harvest handling includes immediate quality grading and distribution planning to minimize waste. Finally, data from each cycle feeds into machine learning models to refine future operations, creating a resilient and self-improving urban agricultural ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ms   = Transition(label='Microclimate Scan')
ss   = Transition(label='Seed Selection')
soil = Transition(label='Soil Testing')
nut  = Transition(label='Nutrient Profile')
irr  = Transition(label='Irrigation Plan')
pest = Transition(label='Pest Monitoring')
ot   = Transition(label='Organic Treatment')
gr   = Transition(label='Growth Tracking')
hs   = Transition(label='Harvest Timing')
ds   = Transition(label='Data Sharing')
vs   = Transition(label='Volunteer Sync')
qg   = Transition(label='Quality Grading')
dp   = Transition(label='Distribution Plan')
wm   = Transition(label='Waste Minimization')
cf   = Transition(label='Cycle Feedback')
mt   = Transition(label='Model Training')

# Silent transition for skipping
skip = SilentTransition()

# XOR choice: only do Organic Treatment if threshold exceeded
xor_treatment = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip, ot]
)

# Community engagement (concurrent Data Sharing and Volunteer Sync)
community = StrictPartialOrder(nodes=[ds, vs])
# no ordering => concurrent

# Growth tracking and harvest timing in sequence
tracking = StrictPartialOrder(nodes=[gr, hs])
tracking.order.add_edge(gr, hs)

# Post-harvest handling in sequence
post_harvest = StrictPartialOrder(nodes=[qg, dp, wm])
post_harvest.order.add_edge(qg, dp)
post_harvest.order.add_edge(dp, wm)

# Cycle feedback feeding into model training
feedback = StrictPartialOrder(nodes=[cf, mt])
feedback.order.add_edge(cf, mt)

# Build the main body as a partial order
body = StrictPartialOrder(nodes=[
    ms, ss, soil, nut, irr, pest,
    xor_treatment, community,
    tracking, post_harvest, feedback
])
body.order.add_edge(ms, ss)
body.order.add_edge(ss, soil)
body.order.add_edge(soil, nut)
body.order.add_edge(nut, irr)
body.order.add_edge(irr, pest)
body.order.add_edge(pest, xor_treatment)
body.order.add_edge(xor_treatment, community)
body.order.add_edge(community, tracking)
body.order.add_edge(tracking, post_harvest)
body.order.add_edge(post_harvest, feedback)

# Wrap the entire cycle in a LOOP so it repeats,
# using 'skip' as the second child to signal loop-reentry
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body, skip]
)