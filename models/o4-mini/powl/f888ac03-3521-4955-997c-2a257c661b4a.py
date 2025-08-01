# Generated from: f888ac03-3521-4955-997c-2a257c661b4a.json
# Description: This process manages the end-to-end operation of urban drone deliveries for perishable goods. It includes initial order validation, dynamic route optimization considering real-time air traffic and weather conditions, automated drone dispatch, continuous in-flight monitoring with obstacle avoidance, secure parcel handoff using biometric verification, and post-delivery data analytics to improve future efficiency. The workflow integrates cross-functional teams and advanced AI algorithms to ensure timely, safe, and compliant deliveries within congested city environments, adapting dynamically to unexpected disruptions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
OV    = Transition(label='Order Validate')
RO    = Transition(label='Route Optimize')
DA    = Transition(label='Drone Assign')
PC    = Transition(label='Preflight Check')
LP    = Transition(label='Load Package')
FL    = Transition(label='Flight Launch')
TM    = Transition(label='Traffic Monitor')
WA    = Transition(label='Weather Assess')
OA    = Transition(label='Obstacle Avoid')
BC    = Transition(label='Battery Check')
DV    = Transition(label='Delivery Verify')
BS    = Transition(label='Biometric Scan')
PR    = Transition(label='Package Release')
RF    = Transition(label='Return Flight')
PF    = Transition(label='Post Flight')
DAna  = Transition(label='Data Analyze')
FC    = Transition(label='Feedback Collect')

# Silent transition for loop exit
skip = SilentTransition()

# In‐flight monitoring: traffic, weather, obstacle, battery concurrently, looped
monitorPO   = StrictPartialOrder(nodes=[TM, WA, OA, BC])
monitorLoop = OperatorPOWL(operator=Operator.LOOP, children=[monitorPO, skip])

# Secure handoff sequence: verify → biometric scan → release
handoffPO = StrictPartialOrder(nodes=[DV, BS, PR])
handoffPO.order.add_edge(DV, BS)
handoffPO.order.add_edge(BS, PR)

# Return flight sequence: return → post‐flight
returnPO = StrictPartialOrder(nodes=[RF, PF])
returnPO.order.add_edge(RF, PF)

# Post‐delivery analytics and feedback loop
postPO   = StrictPartialOrder(nodes=[DAna, FC])
postPO.order.add_edge(DAna, FC)
postLoop = OperatorPOWL(operator=Operator.LOOP, children=[postPO, skip])

# Assemble the root partial order
root = StrictPartialOrder(
    nodes=[OV, RO, DA, PC, LP, FL, monitorLoop, handoffPO, returnPO, postLoop]
)
root.order.add_edge(OV,    RO)
root.order.add_edge(RO,    DA)
root.order.add_edge(DA,    PC)
root.order.add_edge(PC,    LP)
root.order.add_edge(LP,    FL)
root.order.add_edge(FL,    monitorLoop)
root.order.add_edge(monitorLoop, handoffPO)
root.order.add_edge(handoffPO,   returnPO)
root.order.add_edge(returnPO,     postLoop)