# Generated from: 50cd576d-d3fa-4938-a50a-903ca2c2f1c5.json
# Description: This process involves the systematic integration of emerging technologies from diverse industries to foster breakthrough product development. It begins with trend scouting across sectors, followed by multi-disciplinary brainstorming sessions to ideate novel applications. Prototyping includes rapid iteration with cross-functional teams, incorporating feedback from external experts and end-users. Subsequent steps focus on regulatory alignment, intellectual property mapping, and pilot testing in controlled environments. The cycle concludes with strategic scaling and continuous post-launch innovation monitoring, ensuring sustained competitive advantage in rapidly evolving markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ts = Transition(label='Trend Scouting')
ih = Transition(label='Idea Harvest')
cs = Transition(label='Concept Screening')
tm = Transition(label='Tech Mapping')
ct = Transition(label='Cross Teams')
pb = Transition(label='Prototype Build')
er = Transition(label='Expert Review')
ut = Transition(label='User Testing')
rc = Transition(label='Regulatory Check')
ipa = Transition(label='IP Analysis')
pl = Transition(label='Pilot Launch')
dc = Transition(label='Data Capture')
sp = Transition(label='Scale Planning')
mr = Transition(label='Market Rollout')
ia = Transition(label='Innovation Audit')

# Prototyping loop: Prototype Build -> (Expert Review -> User Testing) -> Prototype Build -> …
proto_review_test = StrictPartialOrder(nodes=[er, ut])
proto_review_test.order.add_edge(er, ut)
proto_loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, proto_review_test])

# Post‐launch monitoring loop: Data Capture -> (Scale Planning -> Market Rollout -> Innovation Audit) -> Data Capture -> …
monitor_seq = StrictPartialOrder(nodes=[sp, mr, ia])
monitor_seq.order.add_edge(sp, mr)
monitor_seq.order.add_edge(mr, ia)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[dc, monitor_seq])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[ts, ih, cs, tm, ct, proto_loop, rc, ipa, pl, monitor_loop]
)
root.order.add_edge(ts, ih)
root.order.add_edge(ih, cs)
root.order.add_edge(cs, tm)
root.order.add_edge(tm, ct)
root.order.add_edge(ct, proto_loop)
root.order.add_edge(proto_loop, rc)
root.order.add_edge(rc, ipa)
root.order.add_edge(ipa, pl)
root.order.add_edge(pl, monitor_loop)