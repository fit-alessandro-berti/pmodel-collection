# Generated from: 731f410f-02c2-4c09-bf6e-621f7155f97d.json
# Description: This process involves leveraging a global community to generate, evaluate, and implement innovative ideas for product development. It starts with idea crowdsourcing, followed by filtering through AI-assisted evaluation, community voting, expert refinement, and prototype creation. After field testing with select users, feedback is collected and analyzed to iterate on designs. The process incorporates rapid pivoting based on real-time data, intellectual property assessment, and strategic partnerships to scale successful innovations. Continuous monitoring and knowledge sharing ensure sustained innovation beyond the initial cycle, fostering an adaptive and collaborative environment uncommon in traditional R&D workflows.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
t1  = Transition(label='Idea Sourcing')
t2  = Transition(label='AI Filtering')
t3  = Transition(label='Community Vote')
t4  = Transition(label='Expert Review')
t5  = Transition(label='Concept Refining')
t6  = Transition(label='Prototype Build')
t7  = Transition(label='Field Testing')
t8  = Transition(label='Feedback Collect')
t9  = Transition(label='Data Analyze')
t10 = Transition(label='Design Iterate')
t11 = Transition(label='Pivot Decision')
t12 = Transition(label='IP Assessment')
t13 = Transition(label='Partner Align')
t14 = Transition(label='Scale Launch')
t15 = Transition(label='Knowledge Share')
t16 = Transition(label='Monitor Trends')

# Build the main sequential process as a strict partial order
po = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, t5, t6, t7, t8,
    t9, t10, t11, t12, t13, t14, t15, t16
])
edges = [
    (t1,  t2),  (t2,  t3),  (t3,  t4),  (t4,  t5),
    (t5,  t6),  (t6,  t7),  (t7,  t8),  (t8,  t9),
    (t9,  t10), (t10, t11), (t11, t12), (t12, t13),
    (t13, t14), (t14, t15), (t15, t16)
]
for src, tgt in edges:
    po.order.add_edge(src, tgt)

# Silent transition for loop back
skip = SilentTransition()

# Loop the entire innovation cycle indefinitely
root = OperatorPOWL(operator=Operator.LOOP, children=[po, skip])