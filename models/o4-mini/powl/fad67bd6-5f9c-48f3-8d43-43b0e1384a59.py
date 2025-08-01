# Generated from: fad67bd6-5f9c-48f3-8d43-43b0e1384a59.json
# Description: This process outlines the complex steps required to establish a fully operational urban drone delivery system. It includes obtaining regulatory approvals, designing drone flight paths that avoid restricted zones, integrating real-time weather data for flight safety, coordinating with local traffic control, setting up secure package handling protocols, and implementing customer notification systems. The process also covers periodic maintenance scheduling, emergency response planning, and data analytics to optimize delivery efficiency and reduce environmental impact, ensuring a sustainable and compliant urban delivery network.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
rc = Transition(label='Regulatory Check')
pd = Transition(label='Path Design')
ws = Transition(label='Weather Sync')
ta = Transition(label='Traffic Align')
ps = Transition(label='Package Secure')
ca = Transition(label='Customer Alert')
da = Transition(label='Drone Assemble')
ft = Transition(label='Flight Test')
dm = Transition(label='Data Monitor')
ru = Transition(label='Route Update')
sa = Transition(label='Safety Audit')
ep = Transition(label='Emergency Plan')
mp = Transition(label='Maintenance Plan')
bc = Transition(label='Battery Cycle')
pr = Transition(label='Performance Review')
is_ = Transition(label='Impact Study')
cr = Transition(label='Compliance Review')

# Concurrency of weather sync and traffic alignment
weather_traffic = StrictPartialOrder(nodes=[ws, ta])

# Loop for continuous data monitoring and route updating
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[dm, ru])

# Choice between performing a safety audit or executing an emergency plan
safety_or_emergency = OperatorPOWL(operator=Operator.XOR, children=[sa, ep])

# Loop for periodic maintenance (maintenance plan + battery cycle)
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[mp, bc])

# Assemble the overall partial order
root = StrictPartialOrder(
    nodes=[
        rc, pd, weather_traffic,
        ps, ca,
        da, ft,
        monitor_loop,
        safety_or_emergency,
        maintenance_loop,
        pr, is_, cr
    ]
)

# Define the control-flow dependencies
root.order.add_edge(rc, pd)
root.order.add_edge(pd, weather_traffic)
root.order.add_edge(weather_traffic, ps)
root.order.add_edge(ps, ca)
root.order.add_edge(ca, da)
root.order.add_edge(da, ft)
root.order.add_edge(ft, monitor_loop)
root.order.add_edge(monitor_loop, safety_or_emergency)
root.order.add_edge(safety_or_emergency, maintenance_loop)
root.order.add_edge(maintenance_loop, pr)
root.order.add_edge(pr, is_)
root.order.add_edge(is_, cr)