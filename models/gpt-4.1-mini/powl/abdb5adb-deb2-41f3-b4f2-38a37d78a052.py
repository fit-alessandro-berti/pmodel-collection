# Generated from: abdb5adb-deb2-41f3-b4f2-38a37d78a052.json
# Description: This process governs the cyclical collaboration between multiple departments to foster continuous innovation within an organization. It begins with idea solicitation from all teams, followed by cross-functional brainstorming sessions. Selected concepts undergo rapid prototyping, internal testing, and iterative feedback collection. Simultaneously, risk assessments and market feasibility studies are conducted to ensure viability. Upon refinement, resource allocation and budget approval are secured before pilot deployment. Post-deployment analytics and stakeholder evaluations inform final adjustments. The cycle concludes with knowledge sharing and documentation to embed learnings into organizational best practices, thus promoting sustainable innovation across departments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Idea_Gathering = Transition(label='Idea Gathering')
Cross_Brainstorm = Transition(label='Cross Brainstorm')
Concept_Screening = Transition(label='Concept Screening')
Prototype_Build = Transition(label='Prototype Build')
Internal_Testing = Transition(label='Internal Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Review = Transition(label='Risk Review')
Market_Study = Transition(label='Market Study')
Resource_Plan = Transition(label='Resource Plan')
Budget_Approval = Transition(label='Budget Approval')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Analysis = Transition(label='Data Analysis')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Final_Adjust = Transition(label='Final Adjust')
Knowledge_Share = Transition(label='Knowledge Share')

# Partial order for concurrent Risk Review and Market Study
risk_market = StrictPartialOrder(nodes=[Risk_Review, Market_Study])  # concurrent, no edge

# Partial order for concurrent Data Analysis and Stakeholder Meet
analysis_stakeholder = StrictPartialOrder(nodes=[Data_Analysis, Stakeholder_Meet])  # concurrent, no edge

# Partial order: Data Analysis and Stakeholder Meet --> Final Adjust
post_deploy = StrictPartialOrder(
    nodes=[analysis_stakeholder, Final_Adjust]
)
post_deploy.order.add_edge(analysis_stakeholder, Final_Adjust)

# Partial order: Resource Plan --> Budget Approval --> Pilot Launch --> post_deploy
res_part = StrictPartialOrder(
    nodes=[Resource_Plan, Budget_Approval, Pilot_Launch, post_deploy]
)
res_part.order.add_edge(Resource_Plan, Budget_Approval)
res_part.order.add_edge(Budget_Approval, Pilot_Launch)
res_part.order.add_edge(Pilot_Launch, post_deploy)

# Partial order: Prototype Build --> Internal Testing --> Feedback Loop
proto_test_feedback = StrictPartialOrder(
    nodes=[Prototype_Build, Internal_Testing, Feedback_Loop]
)
proto_test_feedback.order.add_edge(Prototype_Build, Internal_Testing)
proto_test_feedback.order.add_edge(Internal_Testing, Feedback_Loop)

# The refinement phase includes prototype/testing/feedback and concurrent risk_market, both must finish before Resource Plan etc.
refinement = StrictPartialOrder(
    nodes=[proto_test_feedback, risk_market]
)  # concurrent: no edge

# Now refinement is followed by Resource Plan and onward
refine_to_res = StrictPartialOrder(
    nodes=[refinement, res_part]
)
refine_to_res.order.add_edge(refinement, res_part)

# Cycle body: Cross Brainstorm --> Concept Screening --> (refine_to_res) --> Knowledge Share
cycle_body_nodes = [Cross_Brainstorm, Concept_Screening, refine_to_res, Knowledge_Share]
cycle_body = StrictPartialOrder(nodes=cycle_body_nodes)
cycle_body.order.add_edge(Cross_Brainstorm, Concept_Screening)
cycle_body.order.add_edge(Concept_Screening, refine_to_res)
cycle_body.order.add_edge(refine_to_res, Knowledge_Share)

# Loop: first execute Idea Gathering, then the cycle_body repeatedly until exit.
# Loop operator: *(A, B) = execute A, then repeat (choose exit or B then A again)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Idea_Gathering, cycle_body])

root = loop