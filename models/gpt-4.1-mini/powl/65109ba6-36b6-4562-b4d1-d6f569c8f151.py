# Generated from: 65109ba6-36b6-4562-b4d1-d6f569c8f151.json
# Description: This process involves leveraging a global community to generate, evaluate, and refine innovative ideas for new product development. It starts by broadcasting challenge themes to a diverse participant base, encouraging submission of novel concepts. These ideas undergo automated and peer review stages to filter feasible proposals. Selected ideas enter prototyping, where rapid virtual models are created and tested using simulation tools. Feedback loops from community experts and end-users drive iterative improvements. Concurrently, intellectual property assessments and market viability analyses are conducted to ensure alignment with strategic goals. Final concepts proceed to a pilot launch phase, coupled with targeted marketing experiments and data collection to validate user engagement and scalability before full-scale production is authorized.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Theme_Launch = Transition(label='Theme Launch')
Idea_Submit = Transition(label='Idea Submit')
Auto_Filter = Transition(label='Auto Filter')
Peer_Review = Transition(label='Peer Review')
Feasibility_Check = Transition(label='Feasibility Check')
Prototype_Build = Transition(label='Prototype Build')
Simulate_Test = Transition(label='Simulate Test')
Expert_Feedback = Transition(label='Expert Feedback')
User_Review = Transition(label='User Review')
IP_Audit = Transition(label='IP Audit')
Market_Scan = Transition(label='Market Scan')
Iterate_Design = Transition(label='Iterate Design')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Collect = Transition(label='Data Collect')
Scale_Approve = Transition(label='Scale Approve')

# Build peer review partial order: (Auto Filter --> Peer Review --> Feasibility Check)
peer_review = StrictPartialOrder(nodes=[Auto_Filter, Peer_Review, Feasibility_Check])
peer_review.order.add_edge(Auto_Filter, Peer_Review)
peer_review.order.add_edge(Peer_Review, Feasibility_Check)

# Build prototyping partial order:
# (Prototype Build --> Simulate Test --> {Expert Feedback, User Review, Iterate Design} in loop)
# with loop: after Expert Feedback, User Review, Iterate Design, go back to Prototype Build
# Represent feedback loop as a loop: body=Prototype_Build + Simulate_Test,
# redo = a XOR of feedback activities in partial order: Expert Feedback --> User Review --> Iterate Design
feedback_seq = StrictPartialOrder(nodes=[Expert_Feedback, User_Review, Iterate_Design])
feedback_seq.order.add_edge(Expert_Feedback, User_Review)
feedback_seq.order.add_edge(User_Review, Iterate_Design)
feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_seq, SilentTransition()])  # choice: stop loop or redo

# Loop: execute (Prototype Build --> Simulate Test), then choose to exit or feedback_xor then repeat
prototyping_body = StrictPartialOrder(nodes=[Prototype_Build, Simulate_Test])
prototyping_body.order.add_edge(Prototype_Build, Simulate_Test)

prototyping_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototyping_body, feedback_xor])

# IP Audit and Market Scan can be concurrent and before Pilot Launch
ip_market = StrictPartialOrder(nodes=[IP_Audit, Market_Scan])
# No order edge: they are concurrent

# Post-prototyping: after Feasibility Check, and prototyping_loop and the concurrent ip_market, move to Pilot Launch
# But Feasibility_Check, Prototyping_loop, IP_Audit, Market_Scan can run concurrently after peer review + feasibility check in sequence?
# According to description, intellectual property and market scan run concurrently to feedback loops,
# But feedback loops are in prototyping_loop; Prototyping_loop should start after Feasibility_Check
# So Feasibility_Check --> prototyping_loop
# Feasibility_Check --> ip_market
# Then prototyping_loop and ip_market run concurrently, both must finish before Pilot Launch
post_review_PO = StrictPartialOrder(nodes=[Feasibility_Check, prototyping_loop, IP_Audit, Market_Scan])
post_review_PO.order.add_edge(Feasibility_Check, prototyping_loop)
post_review_PO.order.add_edge(Feasibility_Check, IP_Audit)
post_review_PO.order.add_edge(Feasibility_Check, Market_Scan)

# The final Pilot Launch phase waits for prototyping_loop, ip_market (IP_Audit & Market_Scan)
# So pilot_launch after prototyping_loop and ip_market concurrent group
pilot_dependencies = StrictPartialOrder(nodes=[prototyping_loop, IP_Audit, Market_Scan, Pilot_Launch])
pilot_dependencies.order.add_edge(prototyping_loop, Pilot_Launch)
pilot_dependencies.order.add_edge(IP_Audit, Pilot_Launch)
pilot_dependencies.order.add_edge(Market_Scan, Pilot_Launch)

# After Pilot Launch, Marketing Experiment and Data Collection concurrent
marketing_exp = Transition(label='Data Collect')  # Data Collect activity (label as given)
post_pilot = StrictPartialOrder(nodes=[Pilot_Launch, Data_Collect, Scale_Approve])
# Pilot_Launch --> Data_Collect --> Scale_Approve
post_pilot.order.add_edge(Pilot_Launch, Data_Collect)
post_pilot.order.add_edge(Data_Collect, Scale_Approve)

# Assemble the whole workflow partial order:
# Theme Launch --> Idea Submit --> peer_review --> post_review_PO --> pilot_dependencies --> post_pilot
root = StrictPartialOrder(nodes=[
    Theme_Launch,
    Idea_Submit,
    peer_review,
    post_review_PO,
    pilot_dependencies,
    post_pilot
])

# Add edges accordingly:
root.order.add_edge(Theme_Launch, Idea_Submit)
root.order.add_edge(Idea_Submit, peer_review)
root.order.add_edge(peer_review, post_review_PO)
root.order.add_edge(post_review_PO, pilot_dependencies)
root.order.add_edge(pilot_dependencies, post_pilot)