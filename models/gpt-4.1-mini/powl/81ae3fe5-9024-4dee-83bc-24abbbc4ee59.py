# Generated from: 81ae3fe5-9024-4dee-83bc-24abbbc4ee59.json
# Description: This process involves identifying emerging technologies across unrelated industries, synthesizing insights through collaborative workshops, rapid prototyping of hybrid solutions, and iterative feedback cycles with multi-disciplinary teams. The aim is to generate breakthrough products by leveraging unconventional technology pairings, validating feasibility through pilot deployments, and scaling solutions via strategic partnerships while continuously adapting to market shifts and regulatory changes. The loop closes with knowledge codification and dissemination to foster organizational learning and sustained innovation capacity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Tech_Scouting = Transition(label='Tech Scouting')
Insight_Gathering = Transition(label='Insight Gathering')
Idea_Workshop = Transition(label='Idea Workshop')
Concept_Drafting = Transition(label='Concept Drafting')
Prototype_Build = Transition(label='Prototype Build')
User_Testing = Transition(label='User Testing')
Feedback_Analyze = Transition(label='Feedback Analyze')
Pilot_Deploy = Transition(label='Pilot Deploy')
Market_Scan = Transition(label='Market Scan')
Regulation_Check = Transition(label='Regulation Check')
Partner_Align = Transition(label='Partner Align')
Scale_Planning = Transition(label='Scale Planning')
Launch_Prep = Transition(label='Launch Prep')
Knowledge_Codify = Transition(label='Knowledge Codify')
Innovation_Review = Transition(label='Innovation Review')
Adapt_Strategy = Transition(label='Adapt Strategy')

# Build subgraphs

# 1. Identify tech and gather insights before workshop:
# Tech Scouting --> Insight Gathering --> Idea Workshop
initial_PO = StrictPartialOrder(nodes=[Tech_Scouting, Insight_Gathering, Idea_Workshop])
initial_PO.order.add_edge(Tech_Scouting, Insight_Gathering)
initial_PO.order.add_edge(Insight_Gathering, Idea_Workshop)

# 2. Concept drafting after workshop
# Idea Workshop --> Concept Drafting
concept_PO = StrictPartialOrder(nodes=[Idea_Workshop, Concept_Drafting])
concept_PO.order.add_edge(Idea_Workshop, Concept_Drafting)

# 3. Prototype build after concept drafting
# Concept Drafting --> Prototype Build
prototype_PO = StrictPartialOrder(nodes=[Concept_Drafting, Prototype_Build])
prototype_PO.order.add_edge(Concept_Drafting, Prototype_Build)

# 4. User testing and feedback analysis after prototype build
# Prototype Build --> User Testing --> Feedback Analyze
testing_PO = StrictPartialOrder(nodes=[Prototype_Build, User_Testing, Feedback_Analyze])
testing_PO.order.add_edge(Prototype_Build, User_Testing)
testing_PO.order.add_edge(User_Testing, Feedback_Analyze)

# 5. Pilot deployment after feedback analyze
# Feedback Analyze --> Pilot Deploy
pilot_PO = StrictPartialOrder(nodes=[Feedback_Analyze, Pilot_Deploy])
pilot_PO.order.add_edge(Feedback_Analyze, Pilot_Deploy)

# 6. Market scan and regulation check before partner alignment (parallel)
# Market Scan and Regulation Check are concurrent, both before Partner Align
market_reg_PO = StrictPartialOrder(nodes=[Market_Scan, Regulation_Check])
# no edges between Market Scan and Regulation Check (concurrent)

# Partner Align after both Market Scan and Regulation Check
partner_PO = StrictPartialOrder(nodes=[Market_Scan, Regulation_Check, Partner_Align])
partner_PO.order.add_edge(Market_Scan, Partner_Align)
partner_PO.order.add_edge(Regulation_Check, Partner_Align)

# 7. Scale planning after partner align
scale_PO = StrictPartialOrder(nodes=[Partner_Align, Scale_Planning])
scale_PO.order.add_edge(Partner_Align, Scale_Planning)

# 8. Launch prep after scale planning
launch_PO = StrictPartialOrder(nodes=[Scale_Planning, Launch_Prep])
launch_PO.order.add_edge(Scale_Planning, Launch_Prep)

# 9. Innovation review and adapt strategy (review and adapt are parallel)
innovation_adapt_PO = StrictPartialOrder(nodes=[Innovation_Review, Adapt_Strategy])
# no edges => concurrent

# 10. Loop structure:
# Loop body: Innovation Review --> Adapt Strategy 
# Then Knowledge Codify (completes loop) and re-start without Innovation Review (we model LOOP as (* (Innovation Review + Adapt Strategy, Knowledge Codify)))
# But the description says:
# "loop closes with knowledge codification and dissemination"
# The loop is iterative feedback cycles with multi-disciplinary teams plus knowledge codify and dissemination

# So loop = LOOP with:
# A = Innovation_Review + Adapt_Strategy performed concurrently (concurrent partial order)
loop_body_A = StrictPartialOrder(nodes=[Innovation_Review, Adapt_Strategy])
# no edges between Innovation Review and Adapt Strategy (concurrent)

# B = Knowledge Codify (silent after doing A, then loops back to A or exits)
B = Knowledge_Codify

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_A, B])

# Now assemble the main linear flow:
# initial_PO --> concept_PO --> prototype_PO --> testing_PO --> pilot_PO --> partner_PO --> scale_PO --> launch_PO --> loop

# Create top-level PO with all major stages and the loop node
top_nodes = [initial_PO, concept_PO, prototype_PO, testing_PO, pilot_PO, partner_PO, scale_PO, launch_PO, loop]
root = StrictPartialOrder(nodes=top_nodes)

# Add edges to reflect the order
root.order.add_edge(initial_PO, concept_PO)
root.order.add_edge(concept_PO, prototype_PO)
root.order.add_edge(prototype_PO, testing_PO)
root.order.add_edge(testing_PO, pilot_PO)
root.order.add_edge(pilot_PO, partner_PO)
root.order.add_edge(partner_PO, scale_PO)
root.order.add_edge(scale_PO, launch_PO)
root.order.add_edge(launch_PO, loop)