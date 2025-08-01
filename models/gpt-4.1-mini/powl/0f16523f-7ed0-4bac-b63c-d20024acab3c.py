# Generated from: 0f16523f-7ed0-4bac-b63c-d20024acab3c.json
# Description: This process involves leveraging a global crowd to generate, refine, and implement innovative solutions for complex business challenges. It starts with problem framing and crowdsourcing ideas through an open platform, followed by multi-stage evaluation, collaborative prototyping, and iterative testing. The process incorporates community voting, expert moderation, and real-time feedback loops to ensure quality and relevance. Successful prototypes undergo pilot deployment with select users, data-driven performance analysis, and scaling strategies. It closes with knowledge capture and incentivization to sustain continual engagement and innovation momentum within diverse stakeholder ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Problem_Frame = Transition(label='Problem Frame')
Idea_Gather = Transition(label='Idea Gather')

Community_Vote = Transition(label='Community Vote')
Expert_Review = Transition(label='Expert Review')

Concept_Filter = Transition(label='Concept Filter')

Prototype_Build = Transition(label='Prototype Build')
User_Testing = Transition(label='User Testing')

Feedback_Loop = Transition(label='Feedback Loop')
Iterate_Design = Transition(label='Iterate Design')

Pilot_Deploy = Transition(label='Pilot Deploy')

Data_Analyze = Transition(label='Data Analyze')

Scale_Plan = Transition(label='Scale Plan')

Knowledge_Capture = Transition(label='Knowledge Capture')

Reward_Allocate = Transition(label='Reward Allocate')

Engagement_Boost = Transition(label='Engagement Boost')

Innovation_Audit = Transition(label='Innovation Audit')

# Define the iterative testing loop: Execute Feedback Loop followed by Iterate Design repeatedly or exit after Prototype Build & User Testing
# loop = *(A,B) where A=Feedback Loop, B=Iterate Design
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Iterate_Design])

# Multi-stage evaluation is modeled as choice between Community Vote or Expert Review before Concept Filter
eval_choice = OperatorPOWL(operator=Operator.XOR, children=[Community_Vote, Expert_Review])

# Construct partial orders step-by-step

# Step 1: Problem Frame --> Idea Gather
po1 = StrictPartialOrder(nodes=[Problem_Frame, Idea_Gather])
po1.order.add_edge(Problem_Frame, Idea_Gather)

# Step 2: Idea Gather --> (Community Vote XOR Expert Review) --> Concept Filter
po2 = StrictPartialOrder(nodes=[eval_choice, Concept_Filter])
po2.order.add_edge(eval_choice, Concept_Filter)

# Step 3: Concept Filter --> Prototype Build --> User Testing --> (Feedback Loop * Iterate Design)
po3 = StrictPartialOrder(nodes=[Concept_Filter, Prototype_Build, User_Testing, loop_testing])
po3.order.add_edge(Concept_Filter, Prototype_Build)
po3.order.add_edge(Prototype_Build, User_Testing)
po3.order.add_edge(User_Testing, loop_testing)

# Step 4: After iterative testing loop done --> Pilot Deploy --> Data Analyze --> Scale Plan
po4 = StrictPartialOrder(nodes=[Pilot_Deploy, Data_Analyze, Scale_Plan])
po4.order.add_edge(Pilot_Deploy, Data_Analyze)
po4.order.add_edge(Data_Analyze, Scale_Plan)

# Step 5: Scale Plan --> Knowledge Capture --> Reward Allocate --> Engagement Boost --> Innovation Audit
po5 = StrictPartialOrder(nodes=[Knowledge_Capture, Reward_Allocate, Engagement_Boost, Innovation_Audit])
po5.order.add_edge(Knowledge_Capture, Reward_Allocate)
po5.order.add_edge(Reward_Allocate, Engagement_Boost)
po5.order.add_edge(Engagement_Boost, Innovation_Audit)

# Now build a top-level POWL combining all partial orders and links between them
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5]
)

# Connect the partial orders in sequence:
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, po4)
root.order.add_edge(po4, po5)