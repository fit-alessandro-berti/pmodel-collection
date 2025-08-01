# Generated from: df605e32-635d-4d25-b47f-6aa20cfc8cd8.json
# Description: This process governs the identification, authentication, and retrieval of lost or stolen corporate artifacts that hold significant historical or intellectual value. It involves cross-departmental coordination, legal compliance verification, covert negotiation with third parties, and secure logistics to ensure the artifact's safe return while preserving its confidentiality and integrity. Each step requires meticulous documentation, risk assessment, and contingency planning to mitigate potential reputational and financial damages associated with artifact loss. The process concludes with restoration and archival procedures to reintegrate the artifact within corporate heritage assets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
t1  = Transition(label='Artifact Scan')
t2  = Transition(label='Ownership Verify')
t3  = Transition(label='Risk Assess')
t4  = Transition(label='Legal Review')
t5  = Transition(label='Stakeholder Notify')
t6  = Transition(label='Recovery Plan')
t7  = Transition(label='Third-Party Contact')
t8  = Transition(label='Negotiation Setup')
t9  = Transition(label='Secure Transport')
t10 = Transition(label='Condition Inspect')
t11 = Transition(label='Restoration Begin')
t12 = Transition(label='Documentation Log')
t13 = Transition(label='Heritage Archive')
t14 = Transition(label='Final Audit')
t15 = Transition(label='Process Close')

# Model the negotiation cycle as a LOOP: 
#   execute Third-Party Contact, then either exit or do Negotiation Setup + loop again
negotiation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t7, t8]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, t5, t6,
    negotiation_loop,
    t9, t10, t11, t12, t13, t14, t15
])

# Sequential dependencies
root.order.add_edge(t1,  t2)
root.order.add_edge(t2,  t3)
root.order.add_edge(t3,  t4)
root.order.add_edge(t4,  t5)
root.order.add_edge(t5,  t6)
root.order.add_edge(t6,  negotiation_loop)
root.order.add_edge(negotiation_loop, t9)
root.order.add_edge(t9,  t10)
root.order.add_edge(t10, t11)
root.order.add_edge(t11, t12)
root.order.add_edge(t12, t13)
root.order.add_edge(t13, t14)
root.order.add_edge(t14, t15)