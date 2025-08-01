# Generated from: 05f989e1-6a00-488d-b053-38d0e8e75a26.json
# Description: This process involves a cyclical approach to innovation that integrates insights from multiple unrelated industries to generate breakthrough products or services. It begins with trend spotting across diverse sectors, followed by cross-pollination workshops where teams share unconventional ideas. Next, rapid prototyping combines disparate technologies, which undergo iterative testing in simulated environments. Feedback loops incorporate external expert reviews and customer co-creation sessions to refine concepts. Concurrently, strategic alignment ensures business objectives are met while managing intellectual property risks. The cycle concludes with a staged launch plan involving phased market entry and continuous monitoring of competitive responses, enabling adaptive scaling and sustained innovation momentum.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
trend = Transition(label='Trend Spotting')
idea = Transition(label='Idea Sharing')
cross = Transition(label='Cross Workshops')
fusion = Transition(label='Tech Fusion')
proto = Transition(label='Proto Building')
sim = Transition(label='Sim Test')
expert = Transition(label='Expert Review')
customer = Transition(label='Customer Input')
refine = Transition(label='Concept Refine')
strategy = Transition(label='Strategy Align')
ip = Transition(label='IP Assessment')
risk = Transition(label='Risk Manage')
launch = Transition(label='Launch Plan')
entry = Transition(label='Market Entry')
response = Transition(label='Response Track')
scale = Transition(label='Scale Adjust')

# A: the core sequence of spotting, sharing, workshops, fusion, prototyping, testing
A = StrictPartialOrder(nodes=[trend, idea, cross, fusion, proto, sim])
A.order.add_edge(trend, idea)
A.order.add_edge(idea, cross)
A.order.add_edge(cross, fusion)
A.order.add_edge(fusion, proto)
A.order.add_edge(proto, sim)

# B: the feedback sub‐process (expert review & customer input in parallel, then concept refine)
B = StrictPartialOrder(nodes=[expert, customer, refine])
B.order.add_edge(expert, refine)
B.order.add_edge(customer, refine)

# Loop: repeat A, then optionally do B and loop again, or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Root partial order: loop runs concurrent with strategic/IP tasks, then final launch sequence
root = StrictPartialOrder(
    nodes=[loop, strategy, ip, risk, launch, entry, response, scale]
)
# Internal ordering for strategy → IP assessment → risk management
root.order.add_edge(strategy, ip)
root.order.add_edge(ip, risk)
# After the innovation loop completes, do launch plan and downstream steps
root.order.add_edge(loop, launch)
root.order.add_edge(launch, entry)
root.order.add_edge(entry, response)
root.order.add_edge(response, scale)