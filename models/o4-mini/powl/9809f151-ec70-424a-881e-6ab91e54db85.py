# Generated from: 9809f151-ec70-424a-881e-6ab91e54db85.json
# Description: This process facilitates the systematic transfer and adaptation of innovative ideas and technologies between unrelated industries to foster breakthrough advancements. It involves identifying emerging trends, scouting potential partners from diverse sectors, conducting feasibility analyses, adapting concepts to new contexts, prototyping, iterative testing, regulatory alignment, intellectual property management, and finally, scaling through joint ventures or licensing agreements. The complexity lies in navigating unfamiliar domain constraints, aligning disparate stakeholder incentives, and ensuring the innovation remains viable and competitive across different market landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
ts = Transition(label="Trend Scan")
ps = Transition(label="Partner Scout")
fc = Transition(label="Feasibility Check")
ca = Transition(label="Concept Adapt")
pb = Transition(label="Prototype Build")
it = Transition(label="Iterate Test")
comp = Transition(label="Compliance Align")
ip = Transition(label="IP Secure")
mm = Transition(label="Market Map")
ss = Transition(label="Stakeholder Sync")
ra = Transition(label="Resource Allocate")
risk = Transition(label="Risk Assess")
jv = Transition(label="Joint Venture")
lic = Transition(label="License Setup")
sl = Transition(label="Scale Launch")

# Loop for prototyping & iterative testing
proto_loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, it])

# Choice between joint venture or licensing for scaling
scale_choice = OperatorPOWL(operator=Operator.XOR, children=[jv, lic])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        ts, ps, fc, ca,
        proto_loop,
        comp, ip,
        mm, ss, ra, risk,
        scale_choice,
        sl
    ]
)

# Sequential ordering
root.order.add_edge(ts, ps)
root.order.add_edge(ps, fc)
root.order.add_edge(fc, ca)
root.order.add_edge(ca, proto_loop)
root.order.add_edge(proto_loop, comp)
root.order.add_edge(comp, ip)

# After IP Secure, four activities can proceed in parallel, all feeding into the scaling choice
for n in [mm, ss, ra, risk]:
    root.order.add_edge(ip, n)
    root.order.add_edge(n, scale_choice)

# After the XOR choice, finally scale launch
root.order.add_edge(scale_choice, sl)