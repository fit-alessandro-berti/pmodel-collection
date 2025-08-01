# Generated from: 84bb4476-6a44-4f48-8858-38c49da0501c.json
# Description: This process orchestrates the convergence of disparate industry insights to foster breakthrough innovations. It begins with trend spotting across multiple sectors, followed by cross-functional ideation sessions where specialists from unrelated fields collaborate. Prototypes are developed using hybrid technologies, then subjected to multi-domain feasibility and impact assessments. Stakeholder engagement spans beyond traditional partners to include community feedback and regulatory foresight. Iterative refinement incorporates lessons from pilot deployments in diverse market conditions, ensuring adaptability and scalability before final rollout. Continuous knowledge sharing and post-launch analytics close the loop, enabling sustained innovation in a complex, interconnected ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define Activities
Trend_Spotting = Transition(label='Trend Spotting')
Idea_Mining = Transition(label='Idea Mining')
Cross_Pollinate = Transition(label='Cross Pollinate')
Concept_Sketch = Transition(label='Concept Sketch')
Tech_Fusion = Transition(label='Tech Fusion')
Proto_Build = Transition(label='Proto Build')
Feasibility_Test = Transition(label='Feasibility Test')
Impact_Review = Transition(label='Impact Review')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Community_Input = Transition(label='Community Input')
Regulatory_Scan = Transition(label='Regulatory Scan')
Pilot_Deploy = Transition(label='Pilot Deploy')
Data_Capture = Transition(label='Data Capture')
Iterate_Design = Transition(label='Iterate Design')
Scale_Plan = Transition(label='Scale Plan')
Knowledge_Share = Transition(label='Knowledge Share')
Launch_Review = Transition(label='Launch Review')

# Cross-functional ideation session as a partial order of Idea Mining and Cross Pollinate (concurrent)
Ideation_PO = StrictPartialOrder(nodes=[Idea_Mining, Cross_Pollinate]) 
# No edges to allow concurrency between Idea Mining and Cross Pollinate

# Assessment phase: Feasibility Test and Impact Review concurrent
Assessment_PO = StrictPartialOrder(nodes=[Feasibility_Test, Impact_Review])

# Stakeholder engagement: Stakeholder Sync, Community Input, Regulatory Scan concurrent
Stakeholder_PO = StrictPartialOrder(nodes=[Stakeholder_Sync, Community_Input, Regulatory_Scan])

# Pilot deployment with data capture concurrent
Pilot_PO = StrictPartialOrder(nodes=[Pilot_Deploy, Data_Capture])

# Iterative refinement loop: loop over (Iterate Design) and (Pilot_PO and Stakeholder_PO and Assessment_PO and Proto Build)
# We define the body (B) as the combination of Pilot_PO, Stakeholder_PO, Assessment_PO, and Proto_Build + Tech Fusion + Concept Sketch
# From hierarchy in description:
# Concept sketch + Tech Fusion -> Proto Build 
# Then testing (Feasibility & Impact) and stakeholder engagement and pilot deployment
# Iterate Design is the looping activity to refine based on lessons

# Compose prototyping phase as partial order:
# Concept Sketch and Tech Fusion concurrent, both precede Proto Build

Proto_phase = StrictPartialOrder(
    nodes=[Concept_Sketch, Tech_Fusion, Proto_Build]
)
Proto_phase.order.add_edge(Concept_Sketch, Proto_Build)
Proto_phase.order.add_edge(Tech_Fusion, Proto_Build)

# Compose all testing and stakeholder and pilot deployment as one PO concurrency (Assessment_PO, Stakeholder_PO, Pilot_PO)
Test_Stakeholder_Pilot = StrictPartialOrder(
    nodes=[Assessment_PO, Stakeholder_PO, Pilot_PO]
)
# No edges => all concurrent

# The loop body is:
# First execute Proto_phase
# Then Test_Stakeholder_Pilot
# Then Iterate_Design
# We compose: Proto_phase --> Test_Stakeholder_Pilot --> Iterate_Design
Body_PO = StrictPartialOrder(
    nodes=[Proto_phase, Test_Stakeholder_Pilot, Iterate_Design]
)
Body_PO.order.add_edge(Proto_phase, Test_Stakeholder_Pilot)
Body_PO.order.add_edge(Test_Stakeholder_Pilot, Iterate_Design)

# Loop: execute body repeatedly until exit (iterate design THEN exit or repeat)
Loop_node = OperatorPOWL(operator=Operator.LOOP, children=[Iterate_Design, Body_PO])

# Scale Plan and Knowledge Share concurrent after loop
Scale_Knowledge_PO = StrictPartialOrder(nodes=[Scale_Plan, Knowledge_Share])

# Final rollout phase: Scale Plan, Knowledge Share, then Launch Review
Final_PO = StrictPartialOrder(nodes=[Scale_Knowledge_PO, Launch_Review])
Final_PO.order.add_edge(Scale_Knowledge_PO, Launch_Review)

# Build full process PO:
# Trend Spotting --> Ideation_PO --> Loop_node --> Final_PO

root = StrictPartialOrder(
    nodes=[Trend_Spotting, Ideation_PO, Loop_node, Final_PO]
)
root.order.add_edge(Trend_Spotting, Ideation_PO)
root.order.add_edge(Ideation_PO, Loop_node)
root.order.add_edge(Loop_node, Final_PO)