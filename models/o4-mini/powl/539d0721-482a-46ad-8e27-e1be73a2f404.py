# Generated from: 539d0721-482a-46ad-8e27-e1be73a2f404.json
# Description: This process outlines a quantum-enhanced supply chain system where quantum computing optimizes inventory forecasting and logistics in real-time. It begins with demand sensing through quantum sensors, followed by entangled data verification and quantum encryption for secure transactions. The process integrates quantum machine learning to predict disruptions, dynamically re-routing shipments using quantum algorithms. Supplier contracts are negotiated using quantum secure channels, while quantum simulators test production scenarios. The process concludes with a quantum audit ensuring transparency and compliance, enabling ultra-efficient and resilient supply chain management beyond classical capabilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ds = Transition(label='Demand Sensing')
dv = Transition(label='Data Verification')
qe = Transition(label='Quantum Encrypt')

rp = Transition(label='Risk Predict')
ro = Transition(label='Route Optimize')
st = Transition(label='Shipment Track')
isync = Transition(label='Inventory Sync')
fl = Transition(label='Feedback Loop')

cr = Transition(label='Contract Review')
ss = Transition(label='Scenario Sim')
sa = Transition(label='Supplier Audit')

oc = Transition(label='Order Confirm')
pp = Transition(label='Payment Process')
cc = Transition(label='Compliance Check')
qa = Transition(label='Quantum Audit')

# Build the repeating cycle: Risk Predict -> Route Optimize -> Shipment Track -> Inventory Sync
cycle = StrictPartialOrder(nodes=[rp, ro, st, isync])
cycle.order.add_edge(rp, ro)
cycle.order.add_edge(ro, st)
cycle.order.add_edge(st, isync)

# Loop: do 'cycle', then either exit or perform 'Feedback Loop' and repeat
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[cycle, fl])

# Root partial order: sequences and concurrent branches
root = StrictPartialOrder(
    nodes=[ds, dv, qe,
           loop_node,
           cr, ss, sa,
           oc, pp, cc, qa]
)

# Main control-flow edges
root.order.add_edge(ds, dv)
root.order.add_edge(dv, qe)
root.order.add_edge(qe, loop_node)

root.order.add_edge(loop_node, cr)
# After contract review, scenario simulation and supplier audit run in parallel
root.order.add_edge(cr, ss)
root.order.add_edge(cr, sa)
# They synchronize at order confirmation
root.order.add_edge(ss, oc)
root.order.add_edge(sa, oc)

root.order.add_edge(oc, pp)
root.order.add_edge(pp, cc)
root.order.add_edge(cc, qa)