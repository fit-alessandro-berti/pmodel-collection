# Generated from: 57ba80f3-2505-469c-9b71-ed3891a0af79.json
# Description: This process orchestrates the ideation and development of innovative solutions by integrating inputs from multiple departments including R&D, marketing, finance, and operations. It begins with opportunity scanning and proceeds through collaborative brainstorming sessions, rapid prototyping, cross-functional reviews, and iterative feedback loops. The process incorporates external stakeholder engagement, regulatory compliance checks, and risk assessment to ensure feasibility. Final stages involve pilot testing, resource allocation for scaling, performance monitoring, and continuous improvement measures to embed innovation sustainably within the organization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
op_scan        = Transition(label='Opportunity Scan')
idea_coll      = Transition(label='Idea Collection')
brainstorming  = Transition(label='Brainstorming')
prototype      = Transition(label='Prototype Build')
cross_review   = Transition(label='Cross-Review')
stakeholder    = Transition(label='Stakeholder Meet')
compliance     = Transition(label='Compliance Check')
risk           = Transition(label='Risk Assess')
pilot          = Transition(label='Pilot Launch')
feedback       = Transition(label='Feedback Loop')
resource       = Transition(label='Resource Plan')
scaling        = Transition(label='Scaling Prep')
perf           = Transition(label='Performance Track')
improvement    = Transition(label='Improvement Plan')
final          = Transition(label='Final Approval')

# Loop for pilot and feedback iterations
loop_pilot = OperatorPOWL(operator=Operator.LOOP, children=[pilot, feedback])
# Loop for continuous performance tracking and improvement
loop_perf  = OperatorPOWL(operator=Operator.LOOP, children=[perf, improvement])

# Assemble the partial order
root = StrictPartialOrder(nodes=[
    op_scan, idea_coll, brainstorming, prototype, cross_review,
    stakeholder, compliance, risk,
    loop_pilot, resource, scaling,
    loop_perf, final
])

# Define the control-flow dependencies
root.order.add_edge(op_scan, idea_coll)
root.order.add_edge(idea_coll, brainstorming)
root.order.add_edge(brainstorming, prototype)
root.order.add_edge(prototype, cross_review)

# After cross-functional review, three concurrent checks
root.order.add_edge(cross_review, stakeholder)
root.order.add_edge(cross_review, compliance)
root.order.add_edge(cross_review, risk)

# All three must complete before pilot/feedback loop
root.order.add_edge(stakeholder, loop_pilot)
root.order.add_edge(compliance, loop_pilot)
root.order.add_edge(risk, loop_pilot)

# After iterative piloting, proceed to scaling
root.order.add_edge(loop_pilot, resource)
root.order.add_edge(resource, scaling)

# After scaling prep, enter continuous performance loop
root.order.add_edge(scaling, loop_perf)

# Finally, after improvement loop, seek final approval
root.order.add_edge(loop_perf, final)