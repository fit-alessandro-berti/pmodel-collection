# Generated from: 5aff6ae7-ff82-4e43-9ac2-d84e8e8aa349.json
# Description: This process involves sourcing rare milk varieties from remote farms, followed by a detailed fermentation and aging procedure under controlled environmental conditions. Quality inspectors assess texture and flavor profiles periodically. Packaging requires specialized breathable materials to maintain cheese integrity during long overseas transit. Customs documentation and international compliance checks are handled before shipment. Upon arrival, distribution partners coordinate cold storage and retail placement, ensuring freshness and optimal shelf life. Customer feedback loops influence future batch adjustments, integrating artisanal craft with global supply chain complexities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
fs = Transition(label='Fermentation Start')
am = Transition(label='Age Monitoring')
tc = Transition(label='Texture Check')
fp = Transition(label='Flavor Profiling')
pp = Transition(label='Packaging Prep')
bw = Transition(label='Breathable Wrap')
cf = Transition(label='Customs Filing')
ca = Transition(label='Compliance Audit')
es = Transition(label='Export Scheduling')
cs = Transition(label='Cold Storage')
rp = Transition(label='Retail Placement')
fr = Transition(label='Feedback Review')
ba = Transition(label='Batch Adjust')

# Define the main production partial order (A)
A = StrictPartialOrder(nodes=[
    ms, qt, fs,
    am, tc, fp,
    pp, bw,
    cf, ca,
    es,
    cs,
    rp
])
# Sequencing edges for A
A.order.add_edge(ms, qt)
A.order.add_edge(qt, fs)
A.order.add_edge(fs, am)
A.order.add_edge(am, tc)
A.order.add_edge(tc, fp)
A.order.add_edge(fp, pp)
A.order.add_edge(pp, bw)
A.order.add_edge(bw, cf)
A.order.add_edge(cf, ca)
A.order.add_edge(ca, es)
A.order.add_edge(es, cs)
A.order.add_edge(cs, rp)

# Define the feedback adjustment partial order (B)
B = StrictPartialOrder(nodes=[fr, ba])
B.order.add_edge(fr, ba)

# Wrap the entire process in a loop: run A, then optionally perform feedback B and A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])