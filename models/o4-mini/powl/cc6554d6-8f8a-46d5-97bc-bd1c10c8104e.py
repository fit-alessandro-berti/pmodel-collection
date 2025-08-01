# Generated from: cc6554d6-8f8a-46d5-97bc-bd1c10c8104e.json
# Description: This process involves dynamically adjusting the supply chain network in response to real-time disruptions such as supplier failures, transportation delays, or sudden demand fluctuations. It integrates predictive analytics with automated decision-making to reroute shipments, reallocate inventory, and engage alternative suppliers. The process ensures continuity by balancing cost, speed, and risk while maintaining compliance with regulatory constraints. Continuous feedback loops enable learning and refinement of strategies to improve resilience and agility over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
df = Transition(label='Demand Forecast')
ra = Transition(label='Risk Assess')
sa = Transition(label='Supplier Audit')
iscan = Transition(label='Inventory Scan')
ropt = Transition(label='Route Optimize')
op = Transition(label='Order Prioritize')
cc = Transition(label='Compliance Check')
cr = Transition(label='Contract Review')
dmon = Transition(label='Delay Monitor')
sr = Transition(label='Shipment Reroute')
ire = Transition(label='Inventory Reallocate')
ae = Transition(label='Alternative Engage')
ca = Transition(label='Cost Analyze')
pt = Transition(label='Performance Track')
fl = Transition(label='Feedback Loop')
su = Transition(label='Strategy Update')

# Silent skip for the XOR in the loop
skip = SilentTransition()

# Define the repair sub‐process as a partial order: 
# Shipment Reroute -> Inventory Reallocate -> Alternative Engage
repair_po = StrictPartialOrder(nodes=[sr, ire, ae])
repair_po.order.add_edge(sr, ire)
repair_po.order.add_edge(ire, ae)

# XOR between doing nothing (skip) or the repair subprocess
repair_choice = OperatorPOWL(operator=Operator.XOR, children=[skip, repair_po])

# Loop: monitor delay, then optionally repair, repeat until exit
delay_loop = OperatorPOWL(operator=Operator.LOOP, children=[dmon, repair_choice])

# Continuous feedback loop: track performance then update strategy
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, su])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    df, ra, sa, iscan,
    ropt, op,
    cc, cr,
    delay_loop,
    ca, pt,
    feedback_loop
])

# Define the sequencing and concurrency via edges
root.order.add_edge(df, ra)
root.order.add_edge(ra, sa)
root.order.add_edge(ra, iscan)
root.order.add_edge(sa, ropt)
root.order.add_edge(iscan, ropt)
root.order.add_edge(ropt, op)
root.order.add_edge(op, cc)
root.order.add_edge(cc, cr)
root.order.add_edge(cr, delay_loop)
root.order.add_edge(delay_loop, ca)
root.order.add_edge(ca, pt)
root.order.add_edge(pt, feedback_loop)