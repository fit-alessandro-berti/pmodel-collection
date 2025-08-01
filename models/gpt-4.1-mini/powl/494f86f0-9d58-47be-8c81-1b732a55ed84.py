# Generated from: 494f86f0-9d58-47be-8c81-1b732a55ed84.json
# Description: This process involves integrating unconventional insights from multiple industries to generate breakthrough products or services. It starts by scouting emerging trends across unrelated sectors, followed by collaborative ideation sessions where cross-functional teams reinterpret these insights. Rapid prototyping and iterative testing occur in simulated environments, incorporating real-time data from pilot markets. Feedback loops include external expert evaluations and adaptive refinement of concepts. Final steps encompass strategic alignment with corporate goals and phased market introduction, ensuring scalability and cross-sector adaptability while managing regulatory and cultural nuances effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Trend_Scouting = Transition(label='Trend Scouting')
Insight_Mapping = Transition(label='Insight Mapping')
Idea_Workshops = Transition(label='Idea Workshops')
Concept_Selection = Transition(label='Concept Selection')
Prototype_Build = Transition(label='Prototype Build')
Simulate_Testing = Transition(label='Simulate Testing')
Data_Integration = Transition(label='Data Integration')
Expert_Review = Transition(label='Expert Review')
Feedback_Loop = Transition(label='Feedback Loop')
Design_Revision = Transition(label='Design Revision')
Strategy_Align = Transition(label='Strategy Align')
Market_Pilot = Transition(label='Market Pilot')
Scale_Planning = Transition(label='Scale Planning')
Regulatory_Check = Transition(label='Regulatory Check')
Cultural_Audit = Transition(label='Cultural Audit')
Launch_Prep = Transition(label='Launch Prep')

# Loop body: Feedback loop involving Expert Review, Feedback Loop, Design Revision,
# then back to Expert Review or exit - looping structure of (Expert Review + Feedback Loop + Design Revision)
# We'll model this as: loop(ExpertReview sequence, FeedbackLoop sequence)
# Inner sequence of the loop is: Expert_Review --> Feedback_Loop --> Design_Revision
# Loop operator format: *(A, B), execute A then either exit or execute B then A again repeatedly
# Here, define the body A as the first activity in loop, B as the repeating part
# We'll consider A = Expert Review, B= sequence Feedback_Loop --> Design_Revision

# Create the repeating part B of the loop: Feedback_Loop --> Design_Revision
feedback_revision = StrictPartialOrder(nodes=[Feedback_Loop, Design_Revision])
feedback_revision.order.add_edge(Feedback_Loop, Design_Revision)

loop_node = OperatorPOWL(operator=Operator.LOOP, children=[Expert_Review, feedback_revision])

# Assemble the main process partial order
nodes = [
    Trend_Scouting,
    Insight_Mapping,
    Idea_Workshops,
    Concept_Selection,
    Prototype_Build,
    Simulate_Testing,
    Data_Integration,
    loop_node,
    Strategy_Align,
    Market_Pilot,
    Scale_Planning,
    Regulatory_Check,
    Cultural_Audit,
    Launch_Prep
]

root = StrictPartialOrder(nodes=nodes)

# Add control flow edges reflecting process description

# Initial phase
root.order.add_edge(Trend_Scouting, Insight_Mapping)  # Scout -> Map
root.order.add_edge(Insight_Mapping, Idea_Workshops) # Map -> Workshops
root.order.add_edge(Idea_Workshops, Concept_Selection) # Workshops -> Selection

# Prototype and testing preparation
root.order.add_edge(Concept_Selection, Prototype_Build) # Selection -> Build
root.order.add_edge(Prototype_Build, Simulate_Testing) # Build -> Test
root.order.add_edge(Simulate_Testing, Data_Integration) # Test -> Data

# Feedback loop integration
root.order.add_edge(Data_Integration, loop_node) # Data in -> loop with expert review and feedback

# After exiting the feedback loop, continue process
root.order.add_edge(loop_node, Strategy_Align)   # After feedback, align strategy
root.order.add_edge(Strategy_Align, Market_Pilot) # Align -> pilot

# Final scaling and checks before launch
root.order.add_edge(Market_Pilot, Scale_Planning)  # Pilot -> scale
root.order.add_edge(Scale_Planning, Regulatory_Check) # Scale -> regulatory
root.order.add_edge(Regulatory_Check, Cultural_Audit)  # Regulatory -> cultural
root.order.add_edge(Cultural_Audit, Launch_Prep)       # Cultural check -> launch prep

# No explicit concurrency edges needed, all flows are sequential except inside the loop node
