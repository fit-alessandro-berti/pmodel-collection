# Generated from: 4a162be1-371b-413d-9c59-4dab451d92b1.json
# Description: This process involves identifying emerging technologies from unrelated industries and systematically adapting them for novel applications within a company's core sector. It starts with cross-sector research, followed by ideation workshops that blend diverse perspectives. Prototyping leverages rapid iteration and external collaborations. Validation includes multi-disciplinary testing and market simulations. Implementation requires customized integration planning and change management. Finally, continuous feedback loops ensure scalability and sustained innovation, fostering a culture that embraces unconventional problem-solving and leverages external knowledge ecosystems to maintain competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ts = Transition(label='Trend Scan')
th = Transition(label='Tech Harvest')
im = Transition(label='Idea Merge')
cs = Transition(label='Concept Sketch')
rp = Transition(label='Rapid Prototype')
er = Transition(label='Expert Review')
ct = Transition(label='Cross-Test')
ms = Transition(label='Market Simulate')
ip = Transition(label='Integration Plan')
ca = Transition(label='Change Align')
pd = Transition(label='Pilot Deploy')
fl = Transition(label='Feedback Loop')
su = Transition(label='Scale Up')
ks = Transition(label='Knowledge Share')
ce = Transition(label='Culture Embed')

# Silent transitions for loop exits
skip_proto = SilentTransition()
skip_cont = SilentTransition()

# Stage 1: Cross‐sector research
stage1 = StrictPartialOrder(nodes=[ts, th])
stage1.order.add_edge(ts, th)

# Stage 2: Ideation workshops
stage2 = StrictPartialOrder(nodes=[im, cs])
stage2.order.add_edge(im, cs)

# Stage 3: Prototyping loop (rapid iteration + external review)
proto_seq = StrictPartialOrder(nodes=[rp, er])
proto_seq.order.add_edge(rp, er)
proto_loop = OperatorPOWL(operator=Operator.LOOP, children=[proto_seq, skip_proto])

# Stage 4: Validation
validation = StrictPartialOrder(nodes=[ct, ms])
validation.order.add_edge(ct, ms)

# Stage 5: Implementation planning & change management
implementation = StrictPartialOrder(nodes=[ip, ca, pd])
implementation.order.add_edge(ip, ca)
implementation.order.add_edge(ca, pd)

# Stage 6: Continuous feedback & scaling loop
feedback_seq = StrictPartialOrder(nodes=[fl, su, ks, ce])
feedback_seq.order.add_edge(fl, su)
feedback_seq.order.add_edge(su, ks)
feedback_seq.order.add_edge(ks, ce)
cont_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_seq, skip_cont])

# Assemble the overall process
root = StrictPartialOrder(
    nodes=[stage1, stage2, proto_loop, validation, implementation, cont_loop]
)
root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, proto_loop)
root.order.add_edge(proto_loop, validation)
root.order.add_edge(validation, implementation)
root.order.add_edge(implementation, cont_loop)