# Generated from: 57ba80f3-2505-469c-9b71-ed3891a0af79.json
# Description: This process orchestrates the ideation and development of innovative solutions by integrating inputs from multiple departments including R&D, marketing, finance, and operations. It begins with opportunity scanning and proceeds through collaborative brainstorming sessions, rapid prototyping, cross-functional reviews, and iterative feedback loops. The process incorporates external stakeholder engagement, regulatory compliance checks, and risk assessment to ensure feasibility. Final stages involve pilot testing, resource allocation for scaling, performance monitoring, and continuous improvement measures to embed innovation sustainably within the organization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define basic activities
Opportunity_Scan = Transition(label='Opportunity Scan')
Idea_Collection = Transition(label='Idea Collection')
Brainstorming = Transition(label='Brainstorming')
Prototype_Build = Transition(label='Prototype Build')
Cross_Review = Transition(label='Cross-Review')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Compliance_Check = Transition(label='Compliance Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Loop = Transition(label='Feedback Loop')
Resource_Plan = Transition(label='Resource Plan')
Scaling_Prep = Transition(label='Scaling Prep')
Performance_Track = Transition(label='Performance Track')
Improvement_Plan = Transition(label='Improvement Plan')
Final_Approval = Transition(label='Final Approval')

# iterative feedback loop: loop with body=Feedback_Loop (B) and core=Cross_Review (A)
# * (Cross_Review, Feedback_Loop) represents: execute Cross_Review, choose to exit or Feedback_Loop then Cross_Review again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Cross_Review, Feedback_Loop])

# combine Stakeholder_Meet, Compliance_Check, Risk_Assess in parallel after Prototype_Build, before feedback_loop
external_checks = StrictPartialOrder(
    nodes=[Stakeholder_Meet, Compliance_Check, Risk_Assess]
)  # no order, fully concurrent

# combine Resource_Plan, Scaling_Prep, Performance_Track, Improvement_Plan in partial order with Improvement_Plan last
scaling_and_monitoring = StrictPartialOrder(
    nodes=[Resource_Plan, Scaling_Prep, Performance_Track, Improvement_Plan]
)
scaling_and_monitoring.order.add_edge(Resource_Plan, Scaling_Prep)
scaling_and_monitoring.order.add_edge(Scaling_Prep, Performance_Track)
scaling_and_monitoring.order.add_edge(Performance_Track, Improvement_Plan)

# Main sequence partial order (strict linear order except where concurrency):
# 1. Opportunity Scan --> Idea Collection --> Brainstorming --> Prototype Build
# 2. Prototype Build --> external_checks (Stakeholder_Meet || Compliance_Check || Risk_Assess)
# 3. external_checks --> feedback_loop (* (Cross_Review, Feedback_Loop))
# 4. feedback_loop --> Pilot_Launch --> scaling_and_monitoring --> Final_Approval

root = StrictPartialOrder(
    nodes=[
        Opportunity_Scan,
        Idea_Collection,
        Brainstorming,
        Prototype_Build,
        external_checks,
        feedback_loop,
        Pilot_Launch,
        scaling_and_monitoring,
        Final_Approval
    ]
)

# impose order for main sequence
root.order.add_edge(Opportunity_Scan, Idea_Collection)
root.order.add_edge(Idea_Collection, Brainstorming)
root.order.add_edge(Brainstorming, Prototype_Build)
root.order.add_edge(Prototype_Build, external_checks)
root.order.add_edge(external_checks, feedback_loop)
root.order.add_edge(feedback_loop, Pilot_Launch)
root.order.add_edge(Pilot_Launch, scaling_and_monitoring)
root.order.add_edge(scaling_and_monitoring, Final_Approval)