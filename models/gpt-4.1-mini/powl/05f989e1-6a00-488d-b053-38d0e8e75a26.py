# Generated from: 05f989e1-6a00-488d-b053-38d0e8e75a26.json
# Description: This process involves a cyclical approach to innovation that integrates insights from multiple unrelated industries to generate breakthrough products or services. It begins with trend spotting across diverse sectors, followed by cross-pollination workshops where teams share unconventional ideas. Next, rapid prototyping combines disparate technologies, which undergo iterative testing in simulated environments. Feedback loops incorporate external expert reviews and customer co-creation sessions to refine concepts. Concurrently, strategic alignment ensures business objectives are met while managing intellectual property risks. The cycle concludes with a staged launch plan involving phased market entry and continuous monitoring of competitive responses, enabling adaptive scaling and sustained innovation momentum.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Trend_Spotting = Transition(label='Trend Spotting')

# Cross-pollination workshops phase
Idea_Sharing = Transition(label='Idea Sharing')
Cross_Workshops = Transition(label='Cross Workshops')
cross_pollination = StrictPartialOrder(nodes=[Idea_Sharing, Cross_Workshops])
# Idea Sharing and Cross Workshops concurrent (no edges means concurrent)

# Rapid prototyping and iterative testing (loop)
Tech_Fusion = Transition(label='Tech Fusion')
Proto_Building = Transition(label='Proto Building')
Sim_Test = Transition(label='Sim Test')

proto_loop_body = StrictPartialOrder(nodes=[Proto_Building, Sim_Test])
proto_loop_body.order.add_edge(Proto_Building, Sim_Test)

proto_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Tech_Fusion, proto_loop_body]
)

# Feedback loops phase (loop): external expert reviews and customer co-creation lead to refine concept
Expert_Review = Transition(label='Expert Review')
Customer_Input = Transition(label='Customer Input')
Concept_Refine = Transition(label='Concept Refine')

feedback_concurrent = StrictPartialOrder(nodes=[Expert_Review, Customer_Input])
# Expert Review and Customer Input concurrent

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_concurrent, Concept_Refine]
)

# Concurrent strategic alignment phase
IP_Assessment = Transition(label='IP Assessment')
Strategy_Align = Transition(label='Strategy Align')
Risk_Manage = Transition(label='Risk Manage')
strategic_align = StrictPartialOrder(nodes=[IP_Assessment, Strategy_Align, Risk_Manage])
# All three concurrent, no order edges

# Launch plan sequence with concurrent monitoring and adaptive scaling
Launch_Plan = Transition(label='Launch Plan')
Market_Entry = Transition(label='Market Entry')
Response_Track = Transition(label='Response Track')
Scale_Adjust = Transition(label='Scale Adjust')

monitoring = StrictPartialOrder(nodes=[Response_Track, Scale_Adjust])
# Response Track and Scale Adjust concurrent

launch_seq = StrictPartialOrder(nodes=[Launch_Plan, Market_Entry, monitoring])
launch_seq.order.add_edge(Launch_Plan, Market_Entry)
launch_seq.order.add_edge(Market_Entry, monitoring)

# Assemble all major phases in order:
# Trend Spotting -->
# cross_pollination -->
# proto_loop -->
# feedback_loop -->
# strategic_align (concurrent with feedback loops? The description says concurrently with feedback loops)
# The description says "Feedback loops incorporate... Concurrently, strategic alignment ensures..."
# So feedback_loop and strategic_align concurrent
# Then the cycle concludes with launch_seq

feedback_and_strategic = StrictPartialOrder(nodes=[feedback_loop, strategic_align])
# concurrent: no edges between feedback_loop and strategic_align to allow concurrency

# Build full process order
root = StrictPartialOrder(nodes=[Trend_Spotting, cross_pollination, proto_loop, feedback_and_strategic, launch_seq])

root.order.add_edge(Trend_Spotting, cross_pollination)
root.order.add_edge(cross_pollination, proto_loop)
root.order.add_edge(proto_loop, feedback_and_strategic)
root.order.add_edge(feedback_and_strategic, launch_seq)