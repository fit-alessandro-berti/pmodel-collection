# Generated from: d53e957e-33d0-4491-b159-6811584bf6df.json
# Description: This process outlines a complex cycle where a company integrates insights from multiple unrelated industries to innovate new products or services. It involves systematically gathering cross-sector data, conducting comparative trend analysis, ideating disruptive concepts, prototyping with multi-disciplinary teams, validating through external expert panels, and iterating designs based on feedback. The process includes navigating regulatory landscapes across sectors, aligning intellectual property strategies, coordinating supply chain adaptations, and preparing go-to-market strategies customized for hybrid markets. Continuous monitoring of impact metrics and adaptive learning loops ensure sustained competitive advantage and long-term growth through unconventional innovation pathways.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Data_Capture = Transition(label='Data Capture')
Trend_Scan = Transition(label='Trend Scan')
Idea_Workshop = Transition(label='Idea Workshop')
Concept_Draft = Transition(label='Concept Draft')
Expert_Review = Transition(label='Expert Review')
Prototype_Build = Transition(label='Prototype Build')
Regulation_Check = Transition(label='Regulation Check')
IP_Alignment = Transition(label='IP Alignment')
Supply_Sync = Transition(label='Supply Sync')
Market_Mapping = Transition(label='Market Mapping')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Loop = Transition(label='Feedback Loop')
Design_Iterate = Transition(label='Design Iterate')
Impact_Measure = Transition(label='Impact Measure')
Strategy_Adapt = Transition(label='Strategy Adapt')

# Define the innovation cycle loop
# loop node: * (Data Capture and following steps, Feedback Loop and Design Iterate as body loop)

# First, a strict partial order of initial activities before Feedback Loop
# Data Capture -> Trend Scan -> Idea Workshop -> Concept Draft -> Expert Review -> Prototype Build
seq_main_innov = StrictPartialOrder(nodes=[
    Data_Capture, Trend_Scan, Idea_Workshop, Concept_Draft, Expert_Review, Prototype_Build
])
seq_main_innov.order.add_edge(Data_Capture, Trend_Scan)
seq_main_innov.order.add_edge(Trend_Scan, Idea_Workshop)
seq_main_innov.order.add_edge(Idea_Workshop, Concept_Draft)
seq_main_innov.order.add_edge(Concept_Draft, Expert_Review)
seq_main_innov.order.add_edge(Expert_Review, Prototype_Build)

# Regulatory, IP, Supply chain parallel activities before Market Mapping
# These are concurrent and all must complete before Market Mapping
pre_market_nodes = [Regulation_Check, IP_Alignment, Supply_Sync]
pre_market = StrictPartialOrder(nodes=pre_market_nodes)
# no order edges => concurrent

# Market Mapping after regulatory/IP/supply sync
market_mapping_order = StrictPartialOrder(nodes=pre_market_nodes + [Market_Mapping])
for node in pre_market_nodes:
    market_mapping_order.order.add_edge(node, Market_Mapping)

# Pilot Launch follows Market Mapping
pilot_seq = StrictPartialOrder(nodes=[Market_Mapping, Pilot_Launch])
pilot_seq.order.add_edge(Market_Mapping, Pilot_Launch)

# Feedback loop: Feedback Loop and Design Iterate form the looping body
body_loop = StrictPartialOrder(nodes=[Feedback_Loop, Design_Iterate])
body_loop.order.add_edge(Feedback_Loop, Design_Iterate)

# Impact Measure and Strategy Adapt follow the loop (exit branch)
exit_branch = StrictPartialOrder(nodes=[Impact_Measure, Strategy_Adapt])
exit_branch.order.add_edge(Impact_Measure, Strategy_Adapt)

# Combine the loop node * (main_innov, body_loop) representing:
# Execute main innovation sequence, then choose:
# - exit (go to Impact Measure and Strategy Adapt)
# - or do Feedback Loop and Design Iterate, then main innovation sequence again
main_and_feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seq_main_innov, body_loop]
)

# After loop finishes, proceed to exit branch Impact Measure -> Strategy Adapt
after_loop = StrictPartialOrder(nodes=[main_and_feedback_loop, exit_branch])
after_loop.order.add_edge(main_and_feedback_loop, exit_branch)

# Add Pilot Launch and Market Mapping coordination before loop ends:
# Put pilot sequence concurrently with after_loop (to model coordination)
# But pilot launch logically after market mapping,
# and both sequences should come after the regulatory/IP/supply sync concurrency.

# Combine regulatory/IP/supply -> market mapping -> pilot launch partial order
pre_market_to_pilot = StrictPartialOrder(nodes=[Regulation_Check, IP_Alignment, Supply_Sync, Market_Mapping, Pilot_Launch])
for node in pre_market_nodes:
    pre_market_to_pilot.order.add_edge(node, Market_Mapping)
pre_market_to_pilot.order.add_edge(Market_Mapping, Pilot_Launch)

# Now, combine all:
# pre_market_to_pilot --> main_and_feedback_loop --> exit_branch (Impact Measure, Strategy Adapt)

# So we set a strict partial order over the nodes:
root = StrictPartialOrder(
    nodes=[pre_market_to_pilot, main_and_feedback_loop, exit_branch]
)
root.order.add_edge(pre_market_to_pilot, main_and_feedback_loop)
root.order.add_edge(main_and_feedback_loop, exit_branch)