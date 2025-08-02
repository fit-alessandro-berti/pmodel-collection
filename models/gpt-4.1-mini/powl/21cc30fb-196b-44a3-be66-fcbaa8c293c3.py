# Generated from: 21cc30fb-196b-44a3-be66-fcbaa8c293c3.json
# Description: This process orchestrates the identification, evaluation, and integration of breakthrough innovations sourced from diverse industries into a company's existing product or service lines. It involves systematic scouting of emerging technologies, cross-disciplinary ideation workshops, feasibility assessments combining technical and market insights, pilot prototyping with rapid iteration, stakeholder alignment across departments, regulatory compliance checks adapted for unconventional applications, and finally scaled deployment with continuous feedback loops. The process emphasizes agility, knowledge transfer, and risk management to harness unconventional ideas while ensuring alignment with strategic goals and operational capabilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition nodes
tech_scouting = Transition(label='Tech Scouting')
idea_harvest = Transition(label='Idea Harvest')
feasibility_check = Transition(label='Feasibility Check')
market_scan = Transition(label='Market Scan')
concept_workshop = Transition(label='Concept Workshop')
risk_review = Transition(label='Risk Review')
prototype_build = Transition(label='Prototype Build')
pilot_launch = Transition(label='Pilot Launch')
stakeholder_sync = Transition(label='Stakeholder Sync')
compliance_audit = Transition(label='Compliance Audit')
feedback_loop = Transition(label='Feedback Loop')
iteration_sprint = Transition(label='Iteration Sprint')
scale_planning = Transition(label='Scale Planning')
knowledge_transfer = Transition(label='Knowledge Transfer')
launch_review = Transition(label='Launch Review')
post_launch = Transition(label='Post Launch')

# 1) Scouting and ideation (Tech Scouting -> Idea Harvest)
scout_idea = StrictPartialOrder(nodes=[tech_scouting, idea_harvest])
scout_idea.order.add_edge(tech_scouting, idea_harvest)

# 2) Feasibility assessment combining technical and market:
# Feasibility Check and Market Scan concurrent, both after Idea Harvest
feasibility = StrictPartialOrder(nodes=[feasibility_check, market_scan, idea_harvest])
feasibility.order.add_edge(idea_harvest, feasibility_check)
feasibility.order.add_edge(idea_harvest, market_scan)

# 3) Concept Workshop depends on both feasibility check and market scan
concept_wshop = StrictPartialOrder(nodes=[feasibility_check, market_scan, concept_workshop])
concept_wshop.order.add_edge(feasibility_check, concept_workshop)
concept_wshop.order.add_edge(market_scan, concept_workshop)

# 4) Risk Review after Concept Workshop
risk = StrictPartialOrder(nodes=[concept_workshop, risk_review])
risk.order.add_edge(concept_workshop, risk_review)

# 5) Prototype Build after Risk Review
prototype = StrictPartialOrder(nodes=[risk_review, prototype_build])
prototype.order.add_edge(risk_review, prototype_build)

# 6) Pilot Launch after Prototype Build
pilot = StrictPartialOrder(nodes=[prototype_build, pilot_launch])
pilot.order.add_edge(prototype_build, pilot_launch)

# 7) Stakeholder Sync and Compliance Audit concurrent, both after Pilot Launch
stakeholder_compliance = StrictPartialOrder(nodes=[pilot_launch, stakeholder_sync, compliance_audit])
stakeholder_compliance.order.add_edge(pilot_launch, stakeholder_sync)
stakeholder_compliance.order.add_edge(pilot_launch, compliance_audit)

# 8) Loop: Iteration Sprint and Feedback Loop
# After Stakeholder Sync and Compliance Audit, loop over (Iteration Sprint + Feedback Loop)
# with knowledge transfer after each iteration sprint and before next iteration or exit
# Loop structure: LOOP(body=A, redo=B)
# Here, B will be the Feedback + Iteration sprint + Knowledge Transfer partial order

feedback = feedback_loop
iteration = iteration_sprint
knowledge = knowledge_transfer

feedback_iteration_knowledge = StrictPartialOrder(nodes=[feedback, iteration, knowledge])
feedback_iteration_knowledge.order.add_edge(feedback, iteration)
feedback_iteration_knowledge.order.add_edge(iteration, knowledge)

loop = OperatorPOWL(operator=Operator.LOOP, children=[knowledge, feedback_iteration_knowledge])

# 9) Scale Planning after loop exits
# Loop outputs to Scale Planning
scale = scale_planning

# 10) Launch Review after Scale Planning, then Post Launch
launch_and_post = StrictPartialOrder(nodes=[scale, launch_review, post_launch])
launch_and_post.order.add_edge(scale, launch_review)
launch_and_post.order.add_edge(launch_review, post_launch)

# Now combine the top-level flow:
# tech_scouting->idea_harvest->feasibility check + market scan concurrent->concept workshop->risk review->prototype build->pilot launch->stakeholder sync + compliance audit concurrent->loop->scale planning->launch review->post launch

# Combine scout_idea (tech scouting->idea harvest) + feasibility (idea harvest->feasibility and market scan)
first_block = StrictPartialOrder(nodes=[scout_idea, feasibility])
first_block.order.add_edge(scout_idea, feasibility)

# Replace nodes in feasibility to be the actual activities for ordering, so edges link properly
# Actually add edges between idea_harvest (in scout_idea) and feasibility's feasibility_check and market_scan nodes.
# But since scout_idea and feasibility are composite PO, they cannot be inner nodes. 
# Instead, rewrite as strict partial order of all these activities for accurate sequencing.

# To create a correct strict partial order for the whole process, list all nodes and add edges based on dependencies:

all_nodes = [
    tech_scouting, idea_harvest,
    feasibility_check, market_scan,
    concept_workshop, risk_review,
    prototype_build, pilot_launch,
    stakeholder_sync, compliance_audit,
    loop,
    scale, launch_review, post_launch
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges reflecting ordering dependencies:

# Scouting to idea harvest
root.order.add_edge(tech_scouting, idea_harvest)

# Idea harvest to feasibility and market scan (they can run concurrently)
root.order.add_edge(idea_harvest, feasibility_check)
root.order.add_edge(idea_harvest, market_scan)

# Feasibility check and market scan to concept workshop
root.order.add_edge(feasibility_check, concept_workshop)
root.order.add_edge(market_scan, concept_workshop)

# Concept workshop to risk review
root.order.add_edge(concept_workshop, risk_review)

# Risk review to prototype build
root.order.add_edge(risk_review, prototype_build)

# Prototype build to pilot launch
root.order.add_edge(prototype_build, pilot_launch)

# Pilot launch to stakeholder sync and compliance audit (concurrent)
root.order.add_edge(pilot_launch, stakeholder_sync)
root.order.add_edge(pilot_launch, compliance_audit)

# Stakeholder sync and compliance audit to loop
root.order.add_edge(stakeholder_sync, loop)
root.order.add_edge(compliance_audit, loop)

# Loop children: knowledge transfer (A), feedback_iteration_knowledge (B with feedback->iteration->knowledge)
# loop node already created above

# Loop to scale planning
root.order.add_edge(loop, scale)

# Scale planning to launch review to post launch
root.order.add_edge(scale, launch_review)
root.order.add_edge(launch_review, post_launch)