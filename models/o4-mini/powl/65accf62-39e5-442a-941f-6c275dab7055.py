# Generated from: 65accf62-39e5-442a-941f-6c275dab7055.json
# Description: This process outlines a complex, atypical approach to fostering innovation by integrating expertise and resources across multiple unrelated industries. It begins with opportunity scanning across sectors, followed by cross-functional ideation workshops designed to blend diverse perspectives. Subsequently, hybrid prototyping leverages materials and technologies from different fields. The next phase includes iterative testing in parallel market environments to gather multifaceted feedback. Stakeholder alignment sessions ensure continuous buy-in from diverse partners, while adaptive strategy reviews recalibrate objectives based on emerging insights. Legal cross-compliance checks mitigate risks stemming from regulatory differences. Finally, the process culminates in joint commercialization planning and synchronized product launches targeting hybrid customer segments, fostering sustainable competitive advantages through unconventional collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
op_scan = Transition(label='Opportunity Scan')
cross_ideation = Transition(label='Cross Ideation')
resource_merge = Transition(label='Resource Merge')
tech_transfer = Transition(label='Tech Transfer')
hybrid_prototype = Transition(label='Hybrid Prototype')
parallel_testing = Transition(label='Parallel Testing')
feedback_loop = Transition(label='Feedback Loop')
strategic_pivot = Transition(label='Strategic Pivot')
stakeholder_align = Transition(label='Stakeholder Align')
adaptive_review = Transition(label='Adaptive Review')
compliance_check = Transition(label='Compliance Check')
risk_assessment = Transition(label='Risk Assessment')
market_sync = Transition(label='Market Sync')
joint_launch = Transition(label='Joint Launch')
performance_audit = Transition(label='Performance Audit')

# Build the iterative prototyping loop:
# First do Hybrid Prototype, then zero-or-more cycles of [Parallel Testing -> Feedback Loop -> Strategic Pivot]
loop_body = StrictPartialOrder(nodes=[parallel_testing, feedback_loop, strategic_pivot])
loop_body.order.add_edge(parallel_testing, feedback_loop)
loop_body.order.add_edge(feedback_loop, strategic_pivot)

prototyping_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[hybrid_prototype, loop_body]
)

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    op_scan,
    cross_ideation,
    resource_merge,
    tech_transfer,
    prototyping_loop,
    stakeholder_align,
    adaptive_review,
    compliance_check,
    risk_assessment,
    market_sync,
    joint_launch,
    performance_audit
])

# Define control-flow edges
root.order.add_edge(op_scan, cross_ideation)
root.order.add_edge(cross_ideation, resource_merge)
root.order.add_edge(resource_merge, tech_transfer)
root.order.add_edge(tech_transfer, prototyping_loop)

# After prototyping, run stakeholder alignment, adaptive review, and compliance checks in parallel
root.order.add_edge(prototyping_loop, stakeholder_align)
root.order.add_edge(prototyping_loop, adaptive_review)
root.order.add_edge(prototyping_loop, compliance_check)

# Compliance check must precede risk assessment
root.order.add_edge(compliance_check, risk_assessment)

# All three branches converge before market synchronization
root.order.add_edge(stakeholder_align, market_sync)
root.order.add_edge(adaptive_review, market_sync)
root.order.add_edge(risk_assessment, market_sync)

# Final commercialization steps
root.order.add_edge(market_sync, joint_launch)
root.order.add_edge(joint_launch, performance_audit)