# Generated from: 30af60e5-47bb-44ce-a02c-5adb25413d02.json
# Description: This process involves the systematic identification, adaptation, and implementation of innovations from unrelated industries to solve unique organizational challenges. It begins with cross-sector trend scanning, followed by feasibility evaluation and rapid prototyping adapted to the company's context. Stakeholder feedback is continuously integrated to refine solutions, while strategic partnerships are formed to access external expertise. The process concludes with scaling successful innovations through tailored training programs and performance tracking to ensure sustained impact and competitive advantage across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_trend       = Transition(label='Trend Scan')
t_idea        = Transition(label='Idea Harvest')
t_feasibility = Transition(label='Feasibility Check')
t_concept     = Transition(label='Concept Design')
t_proto       = Transition(label='Prototype Build')
t_pilot       = Transition(label='Pilot Launch')
t_stake       = Transition(label='Stakeholder Input')
t_feedback    = Transition(label='Feedback Loop')
t_iterate     = Transition(label='Iterate Model')
t_partner     = Transition(label='Partner Align')
t_training    = Transition(label='Training Deploy')
t_scale       = Transition(label='Scale Rollout')
t_review      = Transition(label='Impact Review')
t_share       = Transition(label='Knowledge Share')
t_adapt       = Transition(label='Market Adapt')

# Build the prototyping loop:
#  A = Prototype Build -> Pilot Launch
poA = StrictPartialOrder(nodes=[t_proto, t_pilot])
poA.order.add_edge(t_proto, t_pilot)

#  B = Stakeholder Input -> Feedback Loop -> Iterate Model
poB = StrictPartialOrder(nodes=[t_stake, t_feedback, t_iterate])
poB.order.add_edge(t_stake, t_feedback)
poB.order.add_edge(t_feedback, t_iterate)

loop_proto = OperatorPOWL(operator=Operator.LOOP, children=[poA, poB])

# Root partial order assembling the entire process
root = StrictPartialOrder(nodes=[
    t_trend,
    t_idea,
    t_feasibility,
    t_concept,
    t_partner,
    loop_proto,
    t_training,
    t_scale,
    t_review,
    t_share,
    t_adapt
])

# Sequence: Trend Scan -> Idea Harvest -> Feasibility Check -> Concept Design
root.order.add_edge(t_trend,       t_idea)
root.order.add_edge(t_idea,        t_feasibility)
root.order.add_edge(t_feasibility, t_concept)

# After Concept Design: in parallel Partner Align and the prototyping loop
root.order.add_edge(t_concept, loop_proto)
root.order.add_edge(t_concept, t_partner)

# After both Partner Align and loop finish, deploy training
root.order.add_edge(loop_proto, t_training)
root.order.add_edge(t_partner,  t_training)

# Then scale, review
root.order.add_edge(t_training, t_scale)
root.order.add_edge(t_scale,    t_review)

# Final concurrent branches: Knowledge Share and Market Adapt after review
root.order.add_edge(t_review, t_share)
root.order.add_edge(t_review, t_adapt)