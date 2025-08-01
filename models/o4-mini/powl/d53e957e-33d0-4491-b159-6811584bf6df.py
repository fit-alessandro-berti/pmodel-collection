# Generated from: d53e957e-33d0-4491-b159-6811584bf6df.json
# Description: This process outlines a complex cycle where a company integrates insights from multiple unrelated industries to innovate new products or services. It involves systematically gathering cross-sector data, conducting comparative trend analysis, ideating disruptive concepts, prototyping with multi-disciplinary teams, validating through external expert panels, and iterating designs based on feedback. The process includes navigating regulatory landscapes across sectors, aligning intellectual property strategies, coordinating supply chain adaptations, and preparing go-to-market strategies customized for hybrid markets. Continuous monitoring of impact metrics and adaptive learning loops ensure sustained competitive advantage and long-term growth through unconventional innovation pathways.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
data_capture    = Transition(label='Data Capture')
trend_scan      = Transition(label='Trend Scan')
idea_workshop   = Transition(label='Idea Workshop')
concept_draft   = Transition(label='Concept Draft')
prototype_build = Transition(label='Prototype Build')
expert_review   = Transition(label='Expert Review')
regulation_check= Transition(label='Regulation Check')
ip_alignment    = Transition(label='IP Alignment')
supply_sync     = Transition(label='Supply Sync')
market_mapping  = Transition(label='Market Mapping')
pilot_launch    = Transition(label='Pilot Launch')
impact_measure  = Transition(label='Impact Measure')
strategy_adapt  = Transition(label='Strategy Adapt')
feedback_loop   = Transition(label='Feedback Loop')
design_iterate  = Transition(label='Design Iterate')

# Build the main (body) partial order of one iteration
body = StrictPartialOrder(nodes=[
    data_capture, trend_scan, idea_workshop, concept_draft,
    prototype_build, expert_review,
    regulation_check, ip_alignment, supply_sync, market_mapping,
    pilot_launch, impact_measure, strategy_adapt
])
# Sequential flow
body.order.add_edge(data_capture,    trend_scan)
body.order.add_edge(trend_scan,      idea_workshop)
body.order.add_edge(idea_workshop,   concept_draft)
body.order.add_edge(concept_draft,   prototype_build)
body.order.add_edge(prototype_build, expert_review)
# Parallel regulatory/IP/supply/market checks after expert review
for chk in [regulation_check, ip_alignment, supply_sync, market_mapping]:
    body.order.add_edge(expert_review, chk)
    body.order.add_edge(chk,            pilot_launch)
# Continue after pilot launch
body.order.add_edge(pilot_launch,    impact_measure)
body.order.add_edge(impact_measure,  strategy_adapt)

# Build the redo-partial order (feedback & redesign)
redo = StrictPartialOrder(nodes=[feedback_loop, design_iterate])
redo.order.add_edge(feedback_loop, design_iterate)

# Wrap into a LOOP: execute `body` once, then choose to exit or do `redo` + body again
root = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])