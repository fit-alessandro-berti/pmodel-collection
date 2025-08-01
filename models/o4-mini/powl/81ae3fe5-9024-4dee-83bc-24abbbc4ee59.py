# Generated from: 81ae3fe5-9024-4dee-83bc-24abbbc4ee59.json
# Description: This process involves identifying emerging technologies across unrelated industries, synthesizing insights through collaborative workshops, rapid prototyping of hybrid solutions, and iterative feedback cycles with multi-disciplinary teams. The aim is to generate breakthrough products by leveraging unconventional technology pairings, validating feasibility through pilot deployments, and scaling solutions via strategic partnerships while continuously adapting to market shifts and regulatory changes. The loop closes with knowledge codification and dissemination to foster organizational learning and sustained innovation capacity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
tech_scouting       = Transition(label='Tech Scouting')
insight_gathering   = Transition(label='Insight Gathering')
idea_workshop       = Transition(label='Idea Workshop')
concept_drafting_0  = Transition(label='Concept Drafting')  # initial drafting
concept_drafting_1  = Transition(label='Concept Drafting')  # for the loop
prototype_build     = Transition(label='Prototype Build')
user_testing        = Transition(label='User Testing')
feedback_analyze    = Transition(label='Feedback Analyze')
pilot_deploy        = Transition(label='Pilot Deploy')
market_scan         = Transition(label='Market Scan')
regulation_check    = Transition(label='Regulation Check')
partner_align       = Transition(label='Partner Align')
scale_planning      = Transition(label='Scale Planning')
launch_prep         = Transition(label='Launch Prep')
knowledge_codify    = Transition(label='Knowledge Codify')
innovation_review   = Transition(label='Innovation Review')
adapt_strategy      = Transition(label='Adapt Strategy')

# Build the inner prototyping‐feedback loop body: 
# User Testing → Feedback Analyze → Concept Drafting → Prototype Build
body_loop = StrictPartialOrder(nodes=[
    user_testing,
    feedback_analyze,
    concept_drafting_1,
    prototype_build
])
body_loop.order.add_edge(user_testing,      feedback_analyze)
body_loop.order.add_edge(feedback_analyze,  concept_drafting_1)
body_loop.order.add_edge(concept_drafting_1, prototype_build)

# Create the LOOP operator: 
# execute Prototype Build, then either exit or run the body and repeat
loop_proto = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prototype_build, body_loop]
)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    tech_scouting,
    insight_gathering,
    idea_workshop,
    concept_drafting_0,
    loop_proto,
    pilot_deploy,
    market_scan,
    regulation_check,
    partner_align,
    scale_planning,
    launch_prep,
    knowledge_codify,
    innovation_review,
    adapt_strategy
])

# Define the control‐flow dependencies
o = root.order
o.add_edge(tech_scouting,      insight_gathering)
o.add_edge(insight_gathering,  idea_workshop)
o.add_edge(idea_workshop,      concept_drafting_0)
o.add_edge(concept_drafting_0, loop_proto)
o.add_edge(loop_proto,         pilot_deploy)
o.add_edge(pilot_deploy,       market_scan)
o.add_edge(pilot_deploy,       regulation_check)
o.add_edge(market_scan,        partner_align)
o.add_edge(regulation_check,   partner_align)
o.add_edge(partner_align,      scale_planning)
o.add_edge(scale_planning,     launch_prep)
o.add_edge(launch_prep,        knowledge_codify)
o.add_edge(knowledge_codify,   innovation_review)
o.add_edge(innovation_review,  adapt_strategy)