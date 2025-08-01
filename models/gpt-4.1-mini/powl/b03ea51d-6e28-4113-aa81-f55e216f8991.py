# Generated from: b03ea51d-6e28-4113-aa81-f55e216f8991.json
# Description: This process involves systematically integrating emerging technologies from unrelated industries to create breakthrough products. It starts with environmental scanning followed by hypothesis formulation and rapid prototyping. Cross-functional teams iterate through user feedback loops, intellectual property assessment, and scalability testing. The cycle includes compliance verification and strategic partnership alignment before final commercialization. Continuous knowledge transfer and post-launch analysis ensure sustained innovation and market relevance, making the process highly adaptive and multidisciplinary.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Scan_Trends = Transition(label='Scan Trends')
Form_Hypothesis = Transition(label='Form Hypothesis')
Build_Prototype = Transition(label='Build Prototype')

User_Testing = Transition(label='User Testing')
Gather_Feedback = Transition(label='Gather Feedback')
IP_Review = Transition(label='IP Review')
Scale_Testing = Transition(label='Scale Testing')
Compliance_Check = Transition(label='Compliance Check')
Partner_Align = Transition(label='Partner Align')

Market_Analysis = Transition(label='Market Analysis')
Knowledge_Share = Transition(label='Knowledge Share')
Iterate_Design = Transition(label='Iterate Design')
Risk_Assess = Transition(label='Risk Assess')
Launch_Plan = Transition(label='Launch Plan')
Post_Launch = Transition(label='Post Launch')

# Define the core loop of the cross-functional teams iterating:
# The iteration cycle includes:
# User Testing, Gather Feedback, IP Review, Scale Testing,
# Compliance Check, Partner Align, Iterate Design, Risk Assess
# This is followed by building prototype again (B), creating the loop

# Inner loop body:
inner_loop_body = StrictPartialOrder(nodes=[
    User_Testing,
    Gather_Feedback,
    IP_Review,
    Scale_Testing,
    Compliance_Check,
    Partner_Align,
    Iterate_Design,
    Risk_Assess
])
# Partial order for the inner loop body can be concurrency for the tests/checks if no explicit order:
# But User Testing -> Gather Feedback is likely sequential,
# Let's order two sequences, then concurrent checks

# Order: User Testing --> Gather Feedback --> (IP Review, Scale Testing, Compliance Check, Partner Align) concurrent --> Iterate Design --> Risk Assess
inner_loop_body.order.add_edge(User_Testing, Gather_Feedback)

inner_loop_body.order.add_edge(Gather_Feedback, IP_Review)
inner_loop_body.order.add_edge(Gather_Feedback, Scale_Testing)
inner_loop_body.order.add_edge(Gather_Feedback, Compliance_Check)
inner_loop_body.order.add_edge(Gather_Feedback, Partner_Align)

inner_loop_body.order.add_edge(IP_Review, Iterate_Design)
inner_loop_body.order.add_edge(Scale_Testing, Iterate_Design)
inner_loop_body.order.add_edge(Compliance_Check, Iterate_Design)
inner_loop_body.order.add_edge(Partner_Align, Iterate_Design)

inner_loop_body.order.add_edge(Iterate_Design, Risk_Assess)

# The loop is: Build_Prototype (A), then choose exit or inner_loop_body (B) + build again
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Build_Prototype, inner_loop_body]
)

# Before the loop:
# Scan Trends --> Form Hypothesis --> loop
pre_loop = StrictPartialOrder(nodes=[Scan_Trends, Form_Hypothesis, loop])
pre_loop.order.add_edge(Scan_Trends, Form_Hypothesis)
pre_loop.order.add_edge(Form_Hypothesis, loop)

# After the loop finishes, continue with:
# Market Analysis, Knowledge Share, Launch Plan, Post Launch
post_loop = StrictPartialOrder(
    nodes=[Market_Analysis, Knowledge_Share, Launch_Plan, Post_Launch]
)
# Order them sequentially
post_loop.order.add_edge(Market_Analysis, Knowledge_Share)
post_loop.order.add_edge(Knowledge_Share, Launch_Plan)
post_loop.order.add_edge(Launch_Plan, Post_Launch)

# Combine pre_loop and post_loop with partial order: pre_loop --> post_loop
root = StrictPartialOrder(nodes=[pre_loop, post_loop])
root.order.add_edge(pre_loop, post_loop)