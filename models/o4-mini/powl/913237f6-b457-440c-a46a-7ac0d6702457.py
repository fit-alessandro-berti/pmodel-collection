# Generated from: 913237f6-b457-440c-a46a-7ac0d6702457.json
# Description: This process involves sourcing innovative ideas from a global crowd through a digital platform, followed by multi-phase validation including community voting, expert evaluation, and prototype development. The process incorporates iterative feedback loops from contributors and stakeholders to refine ideas before final selection. Legal and IP reviews are conducted to secure intellectual property rights. Selected innovations proceed to pilot testing with real users, gathering data to assess viability. Upon successful pilots, the process transitions to scaling strategies involving marketing and production planning, ensuring alignment with organizational goals and market demands. Continuous post-launch monitoring and community engagement maintain innovation momentum and foster ongoing improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
idea_sourcing   = Transition(label='Idea Sourcing')
community_vote  = Transition(label='Community Vote')
expert_review   = Transition(label='Expert Review')
ip_clearance    = Transition(label='IP Clearance')
prototype_build = Transition(label='Prototype Build')
feedback_loop   = Transition(label='Feedback Loop')
stakeholder_align = Transition(label='Stakeholder Align')
pilot_launch    = Transition(label='Pilot Launch')
data_capture    = Transition(label='Data Capture')
viability_assess = Transition(label='Viability Assess')
market_prep     = Transition(label='Market Prep')
production_setup = Transition(label='Production Setup')
scale_planning  = Transition(label='Scale Planning')
post_launch     = Transition(label='Post Launch')
engagement_boost = Transition(label='Engagement Boost')

# Loop body: stakeholder alignment → feedback loop
loop_body = StrictPartialOrder(nodes=[stakeholder_align, feedback_loop])
loop_body.order.add_edge(stakeholder_align, feedback_loop)

# Iterative prototype refinement: build → (align+feedback) → build …
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, loop_body])

# Root partial order connecting all phases
root = StrictPartialOrder(nodes=[
    idea_sourcing, community_vote, expert_review,
    refinement_loop, ip_clearance,
    pilot_launch, data_capture, viability_assess,
    market_prep, production_setup, scale_planning,
    post_launch, engagement_boost
])

# Sequencing edges
root.order.add_edge(idea_sourcing, community_vote)
root.order.add_edge(community_vote, expert_review)
root.order.add_edge(expert_review, refinement_loop)
root.order.add_edge(refinement_loop, ip_clearance)
root.order.add_edge(ip_clearance, pilot_launch)
root.order.add_edge(pilot_launch, data_capture)
root.order.add_edge(data_capture, viability_assess)
root.order.add_edge(viability_assess, market_prep)
root.order.add_edge(market_prep, production_setup)
root.order.add_edge(production_setup, scale_planning)

# After scaling, run post‐launch monitoring and engagement in parallel
root.order.add_edge(scale_planning, post_launch)
root.order.add_edge(scale_planning, engagement_boost)