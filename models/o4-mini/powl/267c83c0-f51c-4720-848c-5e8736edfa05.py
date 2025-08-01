# Generated from: 267c83c0-f51c-4720-848c-5e8736edfa05.json
# Description: This process orchestrates the seamless collaboration of diverse industry sectors to foster breakthrough innovations that leverage unique domain expertise and emerging technologies. Starting from opportunity scouting across unrelated fields, it integrates multidisciplinary ideation sessions followed by rapid prototyping using hybrid resource pools. The process includes iterative feedback loops involving external stakeholders, advanced risk evaluation tailored to unconventional markets, and adaptive regulatory alignment. It culminates in scalable pilot launches and knowledge dissemination to accelerate future innovation cycles, ensuring sustained competitive advantage in volatile environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
op_scan        = Transition(label='Opportunity Scan')
stake_map      = Transition(label='Stakeholder Map')
idea_sprint    = Transition(label='Idea Sprint')
concept_merge  = Transition(label='Concept Merge')
resource_align = Transition(label='Resource Align')
prototype_build= Transition(label='Prototype Build')
hybrid_testing = Transition(label='Hybrid Testing')
feedback       = Transition(label='Feedback Loop')
risk_assess    = Transition(label='Risk Assess')
compliance     = Transition(label='Compliance Check')
pilot_launch   = Transition(label='Pilot Launch')
data_capture   = Transition(label='Data Capture')
impact_review  = Transition(label='Impact Review')
scaling_plan   = Transition(label='Scaling Plan')
knowledge_share= Transition(label='Knowledge Share')
market_adapt   = Transition(label='Market Adapt')

# Define the build-test cycle as a partial order
cycle = StrictPartialOrder(nodes=[prototype_build, hybrid_testing])
cycle.order.add_edge(prototype_build, hybrid_testing)

# Wrap the cycle in a feedback loop: do build→test, then either exit or do Feedback Loop then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, feedback])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    op_scan, stake_map, idea_sprint, concept_merge, resource_align,
    loop, risk_assess, compliance, pilot_launch, data_capture,
    impact_review, scaling_plan, knowledge_share, market_adapt
])

# Define the control-flow (partial order) edges
root.order.add_edge(op_scan,        stake_map)
root.order.add_edge(stake_map,      idea_sprint)
root.order.add_edge(idea_sprint,    concept_merge)
root.order.add_edge(concept_merge,  resource_align)
root.order.add_edge(resource_align, loop)
root.order.add_edge(loop,           risk_assess)
root.order.add_edge(risk_assess,    compliance)
root.order.add_edge(compliance,     pilot_launch)
root.order.add_edge(pilot_launch,   data_capture)
root.order.add_edge(data_capture,   impact_review)

# After reviewing impact, scale, share knowledge, and adapt to market concurrently
root.order.add_edge(impact_review,  scaling_plan)
root.order.add_edge(impact_review,  knowledge_share)
root.order.add_edge(impact_review,  market_adapt)