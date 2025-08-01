# Generated from: 2f2342d8-a1fa-4ce0-b668-45db052aa093.json
# Description: This process involves the coordinated collaboration of multiple industry sectors to develop breakthrough products by integrating disparate technologies, market insights, and regulatory frameworks. Starting with trend identification, the process advances through joint ideation workshops, prototype co-creation, inter-sector testing, and compliance harmonization. Activities include iterative feedback loops from diverse stakeholder groups, adaptive resource allocation, and continuous risk assessment to ensure viability. The cycle culminates in synchronized market launch strategies and post-launch impact evaluation, fostering sustainable innovation across traditionally siloed domains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
trend_scan       = Transition(label='Trend Scan')
idea_sync        = Transition(label='Idea Sync')
tech_merge       = Transition(label='Tech Merge')
concept_map      = Transition(label='Concept Map')
prototype_build  = Transition(label='Prototype Build')
cross_test       = Transition(label='Cross-Test')
stakeholder_poll = Transition(label='Stakeholder Poll')
feedback_loop    = Transition(label='Feedback Loop')
resource_shift   = Transition(label='Resource Shift')
risk_assess      = Transition(label='Risk Assess')
reg_review       = Transition(label='Reg Review')
compliance_check = Transition(label='Compliance Check')
launch_plan      = Transition(label='Launch Plan')
market_sync      = Transition(label='Market Sync')
impact_audit     = Transition(label='Impact Audit')

# Build the iterative feedback loop: poll → feedback → resource shift → risk assess
A_loop = StrictPartialOrder(nodes=[stakeholder_poll, feedback_loop, resource_shift, risk_assess])
A_loop.order.add_edge(stakeholder_poll, feedback_loop)
A_loop.order.add_edge(feedback_loop, resource_shift)
A_loop.order.add_edge(resource_shift, risk_assess)

# Build the compliance harmonization part: regulatory review → compliance check
B_loop = StrictPartialOrder(nodes=[reg_review, compliance_check])
B_loop.order.add_edge(reg_review, compliance_check)

# Loop operator combining the two parts
loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    trend_scan, idea_sync, tech_merge, concept_map, prototype_build,
    cross_test, loop, launch_plan, market_sync, impact_audit
])
root.order.add_edge(trend_scan, idea_sync)
root.order.add_edge(idea_sync, tech_merge)
root.order.add_edge(tech_merge, concept_map)
root.order.add_edge(concept_map, prototype_build)
root.order.add_edge(prototype_build, cross_test)
root.order.add_edge(cross_test, loop)
root.order.add_edge(loop, launch_plan)
root.order.add_edge(launch_plan, market_sync)
root.order.add_edge(market_sync, impact_audit)