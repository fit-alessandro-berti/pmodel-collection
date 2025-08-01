# Generated from: 2f2342d8-a1fa-4ce0-b668-45db052aa093.json
# Description: This process involves the coordinated collaboration of multiple industry sectors to develop breakthrough products by integrating disparate technologies, market insights, and regulatory frameworks. Starting with trend identification, the process advances through joint ideation workshops, prototype co-creation, inter-sector testing, and compliance harmonization. Activities include iterative feedback loops from diverse stakeholder groups, adaptive resource allocation, and continuous risk assessment to ensure viability. The cycle culminates in synchronized market launch strategies and post-launch impact evaluation, fostering sustainable innovation across traditionally siloed domains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Trend_Scan = Transition(label='Trend Scan')
Idea_Sync = Transition(label='Idea Sync')

# Concept development partial order: Tech Merge and Concept Map concurrent after Idea Sync
Tech_Merge = Transition(label='Tech Merge')
Concept_Map = Transition(label='Concept Map')

# Prototype and testing partial order + compliance
Prototype_Build = Transition(label='Prototype Build')
Cross_Test = Transition(label='Cross-Test')

# Compliance and risk
Reg_Review = Transition(label='Reg Review')
Risk_Assess = Transition(label='Risk Assess')

# Stakeholder polls, resource shift, feedback loop
Stakeholder_Poll = Transition(label='Stakeholder Poll')
Resource_Shift = Transition(label='Resource Shift')
Feedback_Loop = Transition(label='Feedback Loop')

# Compliance check after feedback loop
Compliance_Check = Transition(label='Compliance Check')

# Loop for iterative feedback and resource allocation + risk assess
loop_body = StrictPartialOrder(
    nodes=[Stakeholder_Poll, Resource_Shift, Feedback_Loop, Risk_Assess]
)
# These four run in parallel, no order edges for concurrency
# So no edges added, tasks are concurrent in loop body

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Compliance_Check,  # A: body part executed every loop iteration
    loop_body         # B: repeated part before Compliance_Check again (loop condition)
])

# Market launch and audit after loop
Launch_Plan = Transition(label='Launch Plan')
Impact_Audit = Transition(label='Impact Audit')
Market_Sync = Transition(label='Market Sync')

# Create partial order for Market launch phase: Launch Plan --> Impact Audit and Market Sync concurrent after Impact Audit
market_post = StrictPartialOrder(nodes=[Launch_Plan, Impact_Audit, Market_Sync])
market_post.order.add_edge(Launch_Plan, Impact_Audit)
# Impact Audit and Market Sync are concurrent (no edge between them)

# Prototype build forwards into Cross-Test, then regulatory review and risk assess concur with Stakeholder loops
proto_test = StrictPartialOrder(nodes=[Prototype_Build, Cross_Test, Reg_Review])
proto_test.order.add_edge(Prototype_Build, Cross_Test)

# Concept development partial order
concept_dev = StrictPartialOrder(nodes=[Tech_Merge, Concept_Map])
# Tech_Merge and Concept_Map concurrent

# Flow: Trend Scan -> Idea Sync -> concept_dev -> prototype/testing -> reg review and risk assess
front_phase = StrictPartialOrder(
    nodes=[Trend_Scan, Idea_Sync, concept_dev, proto_test]
)
front_phase.order.add_edge(Trend_Scan, Idea_Sync)
front_phase.order.add_edge(Idea_Sync, concept_dev)
front_phase.order.add_edge(concept_dev, proto_test)

# Combine reg_review inside proto_test -> reg_review is in proto_test nodes
# Risk assess inside loop body (Risk_Assess), notice two risk assess (one in loop body, one reg_review in proto_test)
# Different activities

# Link reg_review and loop (feedback/iteration)
reg_loop_post = StrictPartialOrder(
    nodes=[proto_test, loop]
)
reg_loop_post.order.add_edge(proto_test, loop)

# Main flow:
# front_phase --> proto_test and reg_review --> loop --> market_post

# Let's combine all in final PO:
root = StrictPartialOrder(
    nodes=[front_phase, reg_loop_post, market_post]
)
root.order.add_edge(front_phase, reg_loop_post)
root.order.add_edge(reg_loop_post, market_post)