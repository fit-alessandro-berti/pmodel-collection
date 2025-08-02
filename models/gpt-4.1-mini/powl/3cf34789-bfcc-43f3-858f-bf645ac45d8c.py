# Generated from: 3cf34789-bfcc-43f3-858f-bf645ac45d8c.json
# Description: This process manages the identification, evaluation, and integration of breakthrough technologies from unrelated industries into existing business models. It begins with cross-sector scouting to discover novel ideas outside the company’s domain, followed by multidisciplinary feasibility analysis involving experts from various fields. The process continues with iterative prototyping and pilot testing in controlled environments, ensuring adaptability and scalability. Strategic partnerships are established to leverage external capabilities and intellectual property. Market simulation and risk assessment are conducted concurrently to anticipate potential challenges. Finally, the process culminates in phased rollout plans and continuous feedback loops to refine the innovation and maximize impact across multiple business units, fostering sustained competitive advantage through unconventional innovation sources.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
idea_scouting = Transition(label='Idea Scouting')
tech_screening = Transition(label='Tech Screening')

feasibility_review = Transition(label='Feasibility Review')
expert_panel = Transition(label='Expert Panel')

concept_modeling = Transition(label='Concept Modeling')
risk_mapping = Transition(label='Risk Mapping')

partner_sourcing = Transition(label='Partner Sourcing')
ip_analysis = Transition(label='IP Analysis')

prototyping = Transition(label='Prototyping')
pilot_launch = Transition(label='Pilot Launch')

market_testing = Transition(label='Market Testing')
performance_tracking = Transition(label='Performance Tracking')

feedback_loop = Transition(label='Feedback Loop')
scale_planning = Transition(label='Scale Planning')

rollout_phase = Transition(label='Rollout Phase')
impact_review = Transition(label='Impact Review')

# Cross-sector scouting workflow: Idea Scouting --> Tech Screening
scouting_po = StrictPartialOrder(nodes=[idea_scouting, tech_screening])
scouting_po.order.add_edge(idea_scouting, tech_screening)

# Multidisciplinary feasibility analysis: Feasibility Review and Expert Panel concurrent
feasibility_po = StrictPartialOrder(nodes=[feasibility_review, expert_panel])

# Iterative prototyping and pilot testing loop:
# Loop body: Concept Modeling --> Prototyping --> Pilot Launch
# Loop condition: executed repeatedly until choosing to exit

concept_modeling_po = StrictPartialOrder(nodes=[concept_modeling])
prototyping_po = StrictPartialOrder(nodes=[prototyping])
pilot_launch_po = StrictPartialOrder(nodes=[pilot_launch])

cp_po = StrictPartialOrder(nodes=[concept_modeling, prototyping, pilot_launch])
cp_po.order.add_edge(concept_modeling, prototyping)
cp_po.order.add_edge(prototyping, pilot_launch)

# Loop with feedback loop inside after pilot launch, to model iterative refinement
# Add Feedback Loop activity after Pilot Launch inside the loop body before looping again.

loop_body_po = StrictPartialOrder(nodes=[concept_modeling, prototyping, pilot_launch, feedback_loop])
loop_body_po.order.add_edge(concept_modeling, prototyping)
loop_body_po.order.add_edge(prototyping, pilot_launch)
loop_body_po.order.add_edge(pilot_launch, feedback_loop)

# Loop: execute loop_body_po, then either exit or do loop again
# Using OperatorPOWL LOOP operator: children = [do_body, otherwise_body]
# where otherwise_body is often a silent transition representing exit

exit_silent = SilentTransition()
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_po, exit_silent])

# Strategic partnerships: Partner Sourcing and IP Analysis concurrent
partnership_po = StrictPartialOrder(nodes=[partner_sourcing, ip_analysis])

# Market simulation and risk assessment concurrent: Market Testing and Risk Mapping
market_risk_po = StrictPartialOrder(nodes=[market_testing, risk_mapping])

# Performance tracking runs concurrently with the above? Description: "conducted concurrently"
# So we can add performance_tracking concurrent with market_risk_po

market_risk_perf_po = StrictPartialOrder(nodes=[market_testing, risk_mapping, performance_tracking])

# Phased rollout plans and continuous feedback loops to refine and maximize impact
# Rollout Phase --> Scale Planning --> Impact Review --> Feedback Loop (already defined in loop? 
# But description says continuous feedback loops at the end too, so reuse the same feedback loop?)

rollout_po = StrictPartialOrder(nodes=[rollout_phase, scale_planning, impact_review, feedback_loop])
rollout_po.order.add_edge(rollout_phase, scale_planning)
rollout_po.order.add_edge(scale_planning, impact_review)
rollout_po.order.add_edge(impact_review, feedback_loop)

# Now assemble the whole process 
# Cross-sector scouting --> Multidisciplinary feasibility --> loop node (prototyping)
# Then strategic partnerships --> market_risk_perf_po
# Then rollout_po

# Feed flow:
# scouting_po --> feasibility_po --> loop_node --> partnership_po --> market_risk_perf_po --> rollout_po

# Create the root PO combining all nodes
root = StrictPartialOrder(nodes=[
    scouting_po,
    feasibility_po,
    loop_node,
    partnership_po,
    market_risk_perf_po,
    rollout_po
])

# Define the order edges between these sub-processes
root.order.add_edge(scouting_po, feasibility_po)
root.order.add_edge(feasibility_po, loop_node)
root.order.add_edge(loop_node, partnership_po)
root.order.add_edge(partnership_po, market_risk_perf_po)
root.order.add_edge(market_risk_perf_po, rollout_po)