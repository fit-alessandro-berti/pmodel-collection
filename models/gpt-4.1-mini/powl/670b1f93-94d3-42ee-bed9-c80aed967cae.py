# Generated from: 670b1f93-94d3-42ee-bed9-c80aed967cae.json
# Description: This process orchestrates the systematic fusion of ideas from disparate industries to generate breakthrough products. It begins with trend spotting across unrelated sectors, followed by interdisciplinary brainstorming sessions. Concepts are prototyped using agile sprints, then undergo cross-functional peer reviews to identify unforeseen synergies. After iterative refinements, pilot launches are conducted in niche markets to collect diverse user feedback. The insights gained inform strategic pivots and scaling decisions. Throughout, knowledge management ensures lessons learned are archived for future cycles, fostering continuous evolution and competitive advantage in rapidly shifting markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Trend_Spotting = Transition(label='Trend Spotting')
Idea_Mining = Transition(label='Idea Mining')
Brainstorming = Transition(label='Brainstorming')
Concept_Sketch = Transition(label='Concept Sketch')
Prototype_Build = Transition(label='Prototype Build')
Sprint_Review = Transition(label='Sprint Review')
Peer_Feedback = Transition(label='Peer Feedback')
Iterate_Design = Transition(label='Iterate Design')
Pilot_Launch = Transition(label='Pilot Launch')
User_Survey = Transition(label='User Survey')
Data_Analysis = Transition(label='Data Analysis')
Market_Pivot = Transition(label='Market Pivot')
Scale_Planning = Transition(label='Scale Planning')
Knowledge_Archive = Transition(label='Knowledge Archive')
Cycle_Review = Transition(label='Cycle Review')

# Knowledge management (Knowledge_Archive) is continuous, 
# so we add it concurrently with the main process.

# Main process partial order:

# Step 1: Trend Spotting
# Step 2: Idea Mining and Brainstorming are concurrent after Trend Spotting
# - From description, "trend spotting" then "interdisciplinary brainstorming sessions"
#   but "Idea Mining" is part of mining ideas across industries, 
#   so logically we include Idea Mining here in parallel to Brainstorming.

# Step 3: Concept Sketch after Idea Mining and Brainstorming complete
# Step 4: Prototype Build after Concept Sketch
# Step 5: Sprint Review after Prototype Build
# Step 6: Peer Feedback after Sprint Review
# Step 7: Iterate Design after Peer Feedback (could loop with Sprint Review and Peer Feedback iterations)
# Step 8: Pilot Launch after iteration finishes
# Step 9: User Survey after Pilot Launch
# Step 10: Data Analysis after User Survey
# Step 11: Market Pivot and Scale Planning after Data Analysis (choice to pivot or scale)
# Step 12: Cycle Review after Market Pivot and Scale Planning
# Throughout process Knowledge Archive runs concurrently

# Build iteration loop between (Sprint Review & Peer Feedback & Iterate Design)
# We'll model iteration as:
# body = Sprint Review + Peer Feedback + Iterate Design partial order
# redo = body
# loop structure: first execute body once, then 
# choose to either exit or execute redo then body again repeatedly

# Define partial orders for iteration body:
iteration_body = StrictPartialOrder(nodes=[Sprint_Review, Peer_Feedback, Iterate_Design])
iteration_body.order.add_edge(Sprint_Review, Peer_Feedback)
iteration_body.order.add_edge(Peer_Feedback, Iterate_Design)

# Loop: * (body, body)
iteration_loop = OperatorPOWL(operator=Operator.LOOP, children=[iteration_body, iteration_body])

# Choice after Data Analysis: Market Pivot XOR Scale Planning
pivot_scale_choice = OperatorPOWL(operator=Operator.XOR, children=[Market_Pivot, Scale_Planning])

# Build main partial order
nodes_main = [
    Trend_Spotting,
    Idea_Mining,
    Brainstorming,
    Concept_Sketch,
    Prototype_Build,
    iteration_loop,
    Pilot_Launch,
    User_Survey,
    Data_Analysis,
    pivot_scale_choice,
    Cycle_Review,
    Knowledge_Archive
]

root = StrictPartialOrder(nodes=nodes_main)

# Add order edges according to process logic

# Trend Spotting --> Idea Mining & Brainstorming (concurrent)
root.order.add_edge(Trend_Spotting, Idea_Mining)
root.order.add_edge(Trend_Spotting, Brainstorming)

# Idea Mining & Brainstorming --> Concept Sketch
root.order.add_edge(Idea_Mining, Concept_Sketch)
root.order.add_edge(Brainstorming, Concept_Sketch)

# Concept Sketch --> Prototype Build
root.order.add_edge(Concept_Sketch, Prototype_Build)

# Prototype Build --> iteration_loop
root.order.add_edge(Prototype_Build, iteration_loop)

# iteration_loop --> Pilot Launch
root.order.add_edge(iteration_loop, Pilot_Launch)

# Pilot Launch --> User Survey
root.order.add_edge(Pilot_Launch, User_Survey)

# User Survey --> Data Analysis
root.order.add_edge(User_Survey, Data_Analysis)

# Data Analysis --> pivot_scale_choice
root.order.add_edge(Data_Analysis, pivot_scale_choice)

# pivot_scale_choice --> Cycle Review
root.order.add_edge(pivot_scale_choice, Cycle_Review)

# Knowledge Archive runs concurrently so no ordering edges needed (can start at any time)
