# Generated from: 103a0ed3-b61f-442b-b086-aed6044f0a8a.json
# Description: This process involves the intricate steps of crafting bespoke perfumes using rare and natural ingredients sourced globally. It begins with ingredient selection and testing, followed by precise blending and maturation phases. The process includes sensory evaluations, iterative reformulations based on feedback, and finally, bespoke packaging tailored to client preferences. This atypical process blends art, chemistry, and logistics, requiring coordination between botanists, chemists, and designers to ensure each perfume is unique and meets high-quality standards. The entire workflow emphasizes sustainability and exclusivity, making it suitable for luxury niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Sample_Testing = Transition(label='Sample Testing')
Blend_Creation = Transition(label='Blend Creation')
Initial_Maturation = Transition(label='Initial Maturation')
Sensory_Review = Transition(label='Sensory Review')
Formula_Adjust = Transition(label='Formula Adjust')
Secondary_Maturation = Transition(label='Secondary Maturation')
Quality_Check = Transition(label='Quality Check')
Client_Feedback = Transition(label='Client Feedback')
Final_Adjust = Transition(label='Final Adjust')
Bottle_Design = Transition(label='Bottle Design')
Label_Printing = Transition(label='Label Printing')
Packaging_Prep = Transition(label='Packaging Prep')
Custom_Assembly = Transition(label='Custom Assembly')
Dispatch_Arrange = Transition(label='Dispatch Arrange')

# Loop to model iterative reformulations based on sensory review and client feedback
# Loop body:
# A = Sensory Review + Formula Adjust + Secondary Maturation + Quality Check + Client Feedback + Final Adjust (sequence)
# B = tau (silent transition) to represent option to exit or repeat
# Actually, the LOOP in pm4py is (A,B): execute A once, then either exit or do B then A again.
# To model the iterative cycle: sens review -> formula adjust -> secondary maturation -> quality check -> client feedback -> final adjust
iterative_cycle = StrictPartialOrder(nodes=[
    Sensory_Review,
    Formula_Adjust,
    Secondary_Maturation,
    Quality_Check,
    Client_Feedback,
    Final_Adjust
])
iterative_cycle.order.add_edge(Sensory_Review, Formula_Adjust)
iterative_cycle.order.add_edge(Formula_Adjust, Secondary_Maturation)
iterative_cycle.order.add_edge(Secondary_Maturation, Quality_Check)
iterative_cycle.order.add_edge(Quality_Check, Client_Feedback)
iterative_cycle.order.add_edge(Client_Feedback, Final_Adjust)

# B branch of loop is a silent transition (exit condition)
skip = SilentTransition()

loop_iteration = OperatorPOWL(operator=Operator.LOOP, children=[iterative_cycle, skip])

# Partial order for the initial sequence before the loop: Ingredient Sourcing -> Sample Testing -> Blend Creation -> Initial Maturation
initial_seq = StrictPartialOrder(nodes=[
    Ingredient_Sourcing,
    Sample_Testing,
    Blend_Creation,
    Initial_Maturation
])
initial_seq.order.add_edge(Ingredient_Sourcing, Sample_Testing)
initial_seq.order.add_edge(Sample_Testing, Blend_Creation)
initial_seq.order.add_edge(Blend_Creation, Initial_Maturation)

# Connecting Initial Maturation to loop iteration (Sensory Review starts the loop)
# We can model a partial order connecting the initial sequence to the loop
# But since the loop node (loop_iteration) contains Sensory Review as entry, we add edge from Initial Maturation to loop_iteration
# In POWL model, edges refer to nodes, here loop_iteration is a node.

# After loop ends (exits), continue with packaging and dispatch sequence:
# Bottle Design -> Label Printing -> Packaging Prep -> Custom Assembly -> Dispatch Arrange
packaging_seq = StrictPartialOrder(nodes=[
    Bottle_Design,
    Label_Printing,
    Packaging_Prep,
    Custom_Assembly,
    Dispatch_Arrange
])
packaging_seq.order.add_edge(Bottle_Design, Label_Printing)
packaging_seq.order.add_edge(Label_Printing, Packaging_Prep)
packaging_seq.order.add_edge(Packaging_Prep, Custom_Assembly)
packaging_seq.order.add_edge(Custom_Assembly, Dispatch_Arrange)

# Compose partial order of the entire process:
# nodes = initial_seq, loop_iteration, packaging_seq
# edges: initial_seq -> loop_iteration; loop_iteration -> packaging_seq

root = StrictPartialOrder(nodes=[initial_seq, loop_iteration, packaging_seq])
root.order.add_edge(initial_seq, loop_iteration)
root.order.add_edge(loop_iteration, packaging_seq)