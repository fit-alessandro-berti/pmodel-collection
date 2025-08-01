# Generated from: 913237f6-b457-440c-a46a-7ac0d6702457.json
# Description: This process involves sourcing innovative ideas from a global crowd through a digital platform, followed by multi-phase validation including community voting, expert evaluation, and prototype development. The process incorporates iterative feedback loops from contributors and stakeholders to refine ideas before final selection. Legal and IP reviews are conducted to secure intellectual property rights. Selected innovations proceed to pilot testing with real users, gathering data to assess viability. Upon successful pilots, the process transitions to scaling strategies involving marketing and production planning, ensuring alignment with organizational goals and market demands. Continuous post-launch monitoring and community engagement maintain innovation momentum and foster ongoing improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Idea_Sourcing = Transition(label='Idea Sourcing')
Community_Vote = Transition(label='Community Vote')
Expert_Review = Transition(label='Expert Review')
IP_Clearance = Transition(label='IP Clearance')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Stakeholder_Align = Transition(label='Stakeholder Align')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Viability_Assess = Transition(label='Viability Assess')
Scale_Planning = Transition(label='Scale Planning')
Market_Prep = Transition(label='Market Prep')
Production_Setup = Transition(label='Production Setup')
Post_Launch = Transition(label='Post Launch')
Engagement_Boost = Transition(label='Engagement Boost')

skip = SilentTransition()

# Iterative multi-phase validation loop:
# (Community Vote -> Expert Review)
# then choice: either do Feedback Loop + Stakeholder Align and repeat validation, or exit loop
validation_phases = StrictPartialOrder(nodes=[Community_Vote, Expert_Review])
validation_phases.order.add_edge(Community_Vote, Expert_Review)

feedback_sequence = StrictPartialOrder(nodes=[Feedback_Loop, Stakeholder_Align])
feedback_sequence.order.add_edge(Feedback_Loop, Stakeholder_Align)

# LOOP node: A=validation_phases, B=feedback_sequence
# meaning: run validation phases; after that choose either exit or run feedback_sequence then repeat validation again
validation_loop = OperatorPOWL(operator=Operator.LOOP, children=[validation_phases, feedback_sequence])

# After validation loop, do IP Clearance and then Prototype Build (concurrent communities and feedback done -> IP clearance -> prototype)
ip_and_prototype = StrictPartialOrder(nodes=[IP_Clearance, Prototype_Build])
ip_and_prototype.order.add_edge(IP_Clearance, Prototype_Build)

# Pilot testing sequence: Pilot Launch -> Data Capture -> Viability Assess
pilot_sequence = StrictPartialOrder(nodes=[Pilot_Launch, Data_Capture, Viability_Assess])
pilot_sequence.order.add_edge(Pilot_Launch, Data_Capture)
pilot_sequence.order.add_edge(Data_Capture, Viability_Assess)

# Scaling sequence: Scale Planning -> Market Prep -> Production Setup
scaling_sequence = StrictPartialOrder(nodes=[Scale_Planning, Market_Prep, Production_Setup])
scaling_sequence.order.add_edge(Scale_Planning, Market_Prep)
scaling_sequence.order.add_edge(Market_Prep, Production_Setup)

# Post launch sequence: Post Launch -> Engagement Boost
post_launch_sequence = StrictPartialOrder(nodes=[Post_Launch, Engagement_Boost])
post_launch_sequence.order.add_edge(Post_Launch, Engagement_Boost)

# Top-level strict partial order:
# Idea Sourcing -> validation_loop -> ip_and_prototype -> pilot_sequence -> scaling_sequence -> post_launch_sequence
root = StrictPartialOrder(nodes=[
    Idea_Sourcing,
    validation_loop,
    ip_and_prototype,
    pilot_sequence,
    scaling_sequence,
    post_launch_sequence
])
root.order.add_edge(Idea_Sourcing, validation_loop)
root.order.add_edge(validation_loop, ip_and_prototype)
root.order.add_edge(ip_and_prototype, pilot_sequence)
root.order.add_edge(pilot_sequence, scaling_sequence)
root.order.add_edge(scaling_sequence, post_launch_sequence)