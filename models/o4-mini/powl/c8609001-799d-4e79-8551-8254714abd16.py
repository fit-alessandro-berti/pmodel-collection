# Generated from: c8609001-799d-4e79-8551-8254714abd16.json
# Description: This process involves the detailed authentication and verification of antique assets before acquisition or sale. It includes provenance research, material analysis, expert consultations, and risk assessment to ensure the asset's legitimacy and value. The process incorporates cross-referencing historical databases, coordinating with multiple stakeholders, and finalizing legal documentation to mitigate fraud and optimize investment decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
t1  = Transition(label='Initial Review')
t2  = Transition(label='Provenance Check')
t3  = Transition(label='Material Test')
t4  = Transition(label='Database Search')
t5  = Transition(label='Expert Consult')
t6  = Transition(label='Condition Report')
t7  = Transition(label='Risk Assess')
t8  = Transition(label='Market Analysis')
t9  = Transition(label='Stakeholder Meet')
t10 = Transition(label='Insurance Quote')
t11 = Transition(label='Legal Review')
t12 = Transition(label='Price Negotiation')
t13 = Transition(label='Contract Draft')
t14 = Transition(label='Final Approval')
t15 = Transition(label='Asset Registration')

# Silent transition for optional paths and loop decision
tau = SilentTransition()

# Optional expert consultation: either do it or skip
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[t5, tau])

# Optional insurance quote: either do it or skip
xor_insurance = OperatorPOWL(operator=Operator.XOR, children=[t10, tau])

# Negotiation loop: perform price negotiation, then either exit or repeat
loop_neg = OperatorPOWL(operator=Operator.LOOP, children=[t12, tau])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4,
    xor_expert,
    t6, t7, t8, t9,
    xor_insurance,
    t11, t13,
    loop_neg,
    t14, t15
])

# Define the ordering/dependencies
# Initial review precedes provenance check, material test, database search
root.order.add_edge(t1, t2)
root.order.add_edge(t1, t3)
root.order.add_edge(t1, t4)

# Provenance check may trigger an expert consult (or skip)
root.order.add_edge(t2, xor_expert)

# Material test, database search, and optional expert consult all feed into the condition report
root.order.add_edge(t3, t6)
root.order.add_edge(t4, t6)
root.order.add_edge(xor_expert, t6)

# Condition report → risk assessment
root.order.add_edge(t6, t7)

# Risk assessment precedes market analysis, stakeholder meeting, and optional insurance quote
root.order.add_edge(t7, t8)
root.order.add_edge(t7, t9)
root.order.add_edge(t7, xor_insurance)

# Market analysis, stakeholder meeting, and insurance quote all precede legal review
root.order.add_edge(t8, t11)
root.order.add_edge(t9, t11)
root.order.add_edge(xor_insurance, t11)

# Legal review → contract drafting
root.order.add_edge(t11, t13)

# Contract draft → negotiation loop
root.order.add_edge(t13, loop_neg)

# After exiting the negotiation loop → final approval → asset registration
root.order.add_edge(loop_neg, t14)
root.order.add_edge(t14, t15)