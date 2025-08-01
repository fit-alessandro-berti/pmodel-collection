# Generated from: 0352a4e8-91a1-4107-a8a2-4c0681356a07.json
# Description: This process outlines the creation and deployment of a custom urban farming system tailored for small rooftop spaces. It involves site analysis, environmental data collection, modular design planning, resource procurement, automated irrigation setup, sensor integration for real-time monitoring, community stakeholder engagement, pilot testing, iterative adjustments based on collected data, compliance verification with local regulations, training sessions for end-users, and final deployment with ongoing remote support to ensure sustainable urban agriculture in constrained environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ss = Transition(label='Site Survey')
dc = Transition(label='Data Capture')
dl = Transition(label='Design Layout')
mo = Transition(label='Material Order')
mb = Transition(label='Module Build')
ir = Transition(label='Irrigation Setup')
si = Transition(label='Sensor Install')
sc = Transition(label='Software Config')
sm = Transition(label='Stakeholder Meet')
pd = Transition(label='Pilot Deploy')
fg = Transition(label='Feedback Gather')
ad = Transition(label='Adjust Design')
cc = Transition(label='Compliance Check')
ut = Transition(label='User Training')
fl = Transition(label='Final Launch')
rs = Transition(label='Remote Support')

# Build the loop for iterative adjustments: deploy & gather feedback, then optionally adjust and repeat
A_sub = StrictPartialOrder(nodes=[pd, fg])
A_sub.order.add_edge(pd, fg)
loop_adjust = OperatorPOWL(operator=Operator.LOOP, children=[A_sub, ad])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    ss, dc, dl, mo, mb, ir, si, sc, sm,
    loop_adjust, cc, ut, fl, rs
])

# Add sequence edges
root.order.add_edge(ss, dc)
root.order.add_edge(dc, dl)
root.order.add_edge(dl, mo)
root.order.add_edge(mo, mb)
root.order.add_edge(mb, ir)
root.order.add_edge(ir, si)
root.order.add_edge(si, sc)
root.order.add_edge(sc, sm)
root.order.add_edge(sm, loop_adjust)
root.order.add_edge(loop_adjust, cc)
root.order.add_edge(cc, ut)
root.order.add_edge(ut, fl)
root.order.add_edge(fl, rs)