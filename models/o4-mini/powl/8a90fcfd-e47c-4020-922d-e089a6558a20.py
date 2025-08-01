# Generated from: 8a90fcfd-e47c-4020-922d-e089a6558a20.json
# Description: This process outlines the setup of an urban vertical farming system within a constrained city environment. It involves selecting suitable building structures, integrating hydroponic and aeroponic technologies, optimizing energy consumption with renewable sources, and establishing automated monitoring for nutrient delivery and climate control. The process also includes compliance with local zoning laws, community engagement for sustainable practices, and iterative testing of crop yields under varying light and humidity conditions to maximize productivity while minimizing ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
t1  = Transition(label='Site Survey')
t2  = Transition(label='Structure Assess')
t3  = Transition(label='Tech Select')
t4  = Transition(label='Energy Plan')
t5  = Transition(label='Legal Review')
t6  = Transition(label='Permit Acquire')
t7  = Transition(label='System Design')
t8  = Transition(label='Material Order')
t9  = Transition(label='Install Framework')
t10 = Transition(label='Irrigation Setup')
t11 = Transition(label='Climate Configure')
t12 = Transition(label='Sensor Deploy')
t13 = Transition(label='Software Integrate')
t14 = Transition(label='Community Meet')

# Loop body A: Trial Cultivation -> Yield Monitor
t15 = Transition(label='Trial Cultivation')
t16 = Transition(label='Yield Monitor')
loop_A = StrictPartialOrder(nodes=[t15, t16])
loop_A.order.add_edge(t15, t16)

# Loop redo B: Data Analyze -> Process Adjust
t17 = Transition(label='Data Analyze')
t18 = Transition(label='Process Adjust')
loop_B = StrictPartialOrder(nodes=[t17, t18])
loop_B.order.add_edge(t17, t18)

# Loop operator: repeat Trial/Yield with Data Analyze/Process Adjust
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_A, loop_B])

# Root partial order
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, t5, t6,
    t7, t8, t9, t10, t11, t12, t13, t14,
    loop
])

# Define the control-flow order
root.order.add_edge(t1,  t2)
root.order.add_edge(t2,  t3)
# After Tech Select, two concurrent branches: energy & system build-out
root.order.add_edge(t3,  t4)
root.order.add_edge(t3,  t7)

# Energy branch
root.order.add_edge(t4,  t5)
root.order.add_edge(t5,  t6)
# System design/build branch
root.order.add_edge(t7,  t8)
root.order.add_edge(t8,  t9)
root.order.add_edge(t9,  t10)
root.order.add_edge(t10, t11)
root.order.add_edge(t11, t12)
root.order.add_edge(t12, t13)
root.order.add_edge(t13, t14)

# Both branches must complete before starting iterative trials
root.order.add_edge(t6,  loop)
root.order.add_edge(t14, loop)