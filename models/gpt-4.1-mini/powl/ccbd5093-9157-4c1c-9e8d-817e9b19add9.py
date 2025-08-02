# Generated from: ccbd5093-9157-4c1c-9e8d-817e9b19add9.json
# Description: This process involves a cyclical approach to fostering innovation by integrating insights and technologies from disparate industries. It begins with opportunity scanning across sectors, followed by ideation workshops combining cross-disciplinary teams. Prototypes are then rapidly developed and tested using augmented reality simulations. Feedback is collected from diverse user groups remotely via virtual platforms. Iterations incorporate regulatory and ethical reviews to ensure compliance. Parallel market analysis identifies niche gaps and partner ecosystems. Final concepts undergo strategic alignment sessions before pilot launches in limited markets. Post-launch, continuous monitoring leverages AI-driven analytics to detect emerging trends and pivot strategies accordingly, feeding back into the next cycle for sustained innovation momentum.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Scan_Markets = Transition(label='Scan Markets')
Host_Workshops = Transition(label='Host Workshops')
Form_Teams = Transition(label='Form Teams')
Develop_Prototypes = Transition(label='Develop Prototypes')
Simulate_Tests = Transition(label='Simulate Tests')
Collect_Feedback = Transition(label='Collect Feedback')
Review_Ethics = Transition(label='Review Ethics')
Conduct_Analysis = Transition(label='Conduct Analysis')
Identify_Partners = Transition(label='Identify Partners')
Align_Strategy = Transition(label='Align Strategy')
Launch_Pilots = Transition(label='Launch Pilots')
Monitor_Trends = Transition(label='Monitor Trends')
AI_Analytics = Transition(label='AI Analytics')
Pivot_Plans = Transition(label='Pivot Plans')
Cycle_Renewal = Transition(label='Cycle Renewal')  # Will use as silent for loop exit control

# Build the core cycle loop body

# Sequential preorder subsets within the cycle:
# 1) Scan Markets
# 2) Host Workshops and Form Teams (parallel)
# 3) Develop Prototypes --> Simulate Tests (sequence)
# 4) Collect Feedback
# 5) Review Ethics
# 6) Conduct Analysis and Identify Partners (parallel)
# 7) Align Strategy
# 8) Launch Pilots
# 9) Monitor Trends --> AI Analytics --> Pivot Plans (sequence)

# Build partial orders to express concurrency

# Host Workshops and Form Teams in parallel
hw_ft = StrictPartialOrder(nodes=[Host_Workshops, Form_Teams])

# Conduct Analysis and Identify Partners in parallel
ca_ip = StrictPartialOrder(nodes=[Conduct_Analysis, Identify_Partners])

# Monitor Trends --> AI Analytics --> Pivot Plans sequence
mt_aia_pp = StrictPartialOrder(nodes=[Monitor_Trends, AI_Analytics, Pivot_Plans])
mt_aia_pp.order.add_edge(Monitor_Trends, AI_Analytics)
mt_aia_pp.order.add_edge(AI_Analytics, Pivot_Plans)

# Develop Prototypes --> Simulate Tests sequence
dp_st = StrictPartialOrder(nodes=[Develop_Prototypes, Simulate_Tests])
dp_st.order.add_edge(Develop_Prototypes, Simulate_Tests)

# Build the full cycle body order
cycle_nodes = [Scan_Markets, hw_ft, dp_st, Collect_Feedback, Review_Ethics, ca_ip,
               Align_Strategy, Launch_Pilots, mt_aia_pp]

cycle_body = StrictPartialOrder(nodes=cycle_nodes)

# Add ordering between these major steps
# Scan Markets --> Host Workshops & Form Teams
cycle_body.order.add_edge(Scan_Markets, hw_ft)
# Host Workshops & Form Teams --> Develop Prototypes --> Simulate Tests
cycle_body.order.add_edge(hw_ft, dp_st)
# Develop Prototypes & Simulate Tests --> Collect Feedback
cycle_body.order.add_edge(dp_st, Collect_Feedback)
# Collect Feedback --> Review Ethics
cycle_body.order.add_edge(Collect_Feedback, Review_Ethics)
# Review Ethics --> Conduct Analysis & Identify Partners
cycle_body.order.add_edge(Review_Ethics, ca_ip)
# Conduct Analysis & Identify Partners --> Align Strategy
cycle_body.order.add_edge(ca_ip, Align_Strategy)
# Align Strategy --> Launch Pilots
cycle_body.order.add_edge(Align_Strategy, Launch_Pilots)
# Launch Pilots --> (Monitor Trends --> AI Analytics --> Pivot Plans)
cycle_body.order.add_edge(Launch_Pilots, mt_aia_pp)

# Build the loop

# LOOP(A = cycle_body, B = Cycle_Renewal (silent))
# According to definition * (A,B) means: execute A, then choose to exit or execute B then A again

loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, Cycle_Renewal])

# Define the root as the loop node
root = loop