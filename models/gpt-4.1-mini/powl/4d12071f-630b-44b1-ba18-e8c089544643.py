# Generated from: 4d12071f-630b-44b1-ba18-e8c089544643.json
# Description: This process describes a cyclical approach to fostering innovation by integrating insights from multiple unrelated industries. It starts by identifying emerging trends in diverse sectors, followed by collaborative ideation sessions involving cross-disciplinary teams. The ideas are then prototyped using rapid development methods and tested within controlled environments. Feedback loops are established through user interaction data and expert reviews, which inform iterative refinements. The process also includes strategic partnership formation with external entities to leverage unique capabilities. Finally, successful innovations undergo market adaptation and scaling strategies, while lessons learned feed back into the trend identification phase, ensuring continuous evolution and relevance in a rapidly changing business landscape.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions corresponding to activities
trend_scan = Transition(label='Trend Scan')
team_assemble = Transition(label='Team Assemble')
idea_workshop = Transition(label='Idea Workshop')
concept_sketch = Transition(label='Concept Sketch')
rapid_build = Transition(label='Rapid Build')
test_deploy = Transition(label='Test Deploy')
data_capture = Transition(label='Data Capture')
expert_review = Transition(label='Expert Review')
iterate_design = Transition(label='Iterate Design')
partner_align = Transition(label='Partner Align')
market_adapt = Transition(label='Market Adapt')
scale_plan = Transition(label='Scale Plan')
user_engage = Transition(label='User Engage')
risk_assess = Transition(label='Risk Assess')
feedback_loop = Transition(label='Feedback Loop')

skip = SilentTransition()

# Feedback loop modeled as a loop:
#  - Body: Iterate Design (refinements)
#  - Loop portion: (User Engage & Risk Assess & Feedback Loop + Expert Review + Data Capture)
#    --> Then goes back to Iterate Design or exit loop
# We model the feedback analysis as a partial order of User Engage, Risk Assess, Feedback Loop, Expert Review, Data Capture concurrent or partially ordered.
# The description says feedback loops established through user interaction data and expert reviews, which inform iterative refinements.

# Feedback analysis nodes
feedback_activities = [user_engage, risk_assess, feedback_loop, expert_review, data_capture]
feedback_po = StrictPartialOrder(nodes=feedback_activities)
# We can say Data Capture --> Feedback Loop (Data feeds feedback loop),
# User Engage and Risk Assess and Expert Review are concurrent to Data Capture (no specific order given)
# However, Feedback Loop synthesizes user data, so:
feedback_po.order.add_edge(data_capture, feedback_loop)
# Rest concurrent (no edges)

# Create loop: iterate_design followed by feedback_po then back or exit:
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[iterate_design, feedback_po])

# Now model main process partial order
# 1) Trend Scan
# 2) Team Assemble
# 3) Idea Workshop
# 4) Concept Sketch
# 5) Rapid Build
# 6) Test Deploy
# 7) loop_feedback (Iterate Design + feedback loop)

# Additionally,
# Strategic partnership formation with external entities - Partner Align - can be concurrent or after loop?
# Description: "The process also includes strategic partnership formation ..."
# This suggests Partner Align can happen concurrently with feedback loop or iteration or parallel branch before market adaptation.

# Final step: Market Adapt and Scale Plan in sequence
# Lessons learned feed back into Trend Scan - this is global cycle -> modeled by the feedback loop and iterative cycle only,
# or we can model explicit order from Scale Plan back to Trend Scan via silent transition.

# Proposal:
# After loop_feedback and partner_align complete, move to Market Adapt and Scale Plan

# Model partner_align to be concurrent with loop_feedback
# Final PO: Trend Scan --> Team Assemble --> Idea Workshop --> Concept Sketch --> Rapid Build --> Test Deploy --> (parallel: loop_feedback and partner_align) --> Market Adapt --> Scale Plan

# Then add loop back (silent) from Scale Plan to Trend Scan for continuous evolution

# Silent transition for loop back
loop_back = SilentTransition()

# Build main sequence nodes
main_sequence = [
    trend_scan,
    team_assemble,
    idea_workshop,
    concept_sketch,
    rapid_build,
    test_deploy,
]

# Partial order nodes: all above + loop_feedback + partner_align + market_adapt + scale_plan + loop_back
nodes = main_sequence + [loop_feedback, partner_align, market_adapt, scale_plan, loop_back]

root = StrictPartialOrder(nodes=nodes)

# Add main sequential edges
root.order.add_edge(trend_scan, team_assemble)
root.order.add_edge(team_assemble, idea_workshop)
root.order.add_edge(idea_workshop, concept_sketch)
root.order.add_edge(concept_sketch, rapid_build)
root.order.add_edge(rapid_build, test_deploy)

# After test_deploy --> loop_feedback and partner_align concurrently
root.order.add_edge(test_deploy, loop_feedback)
root.order.add_edge(test_deploy, partner_align)

# After both loop_feedback and partner_align we proceed to market_adapt
# So from loop_feedback --> market_adapt and partner_align --> market_adapt
root.order.add_edge(loop_feedback, market_adapt)
root.order.add_edge(partner_align, market_adapt)

# Then market_adapt --> scale_plan
root.order.add_edge(market_adapt, scale_plan)

# Loop back from scale_plan --> trend_scan to model continuous evolution
root.order.add_edge(scale_plan, loop_back)
root.order.add_edge(loop_back, trend_scan)