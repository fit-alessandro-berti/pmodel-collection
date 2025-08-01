# Generated from: 3a218297-cb5d-44bb-b1c6-8b131795ef69.json
# Description: This process involves meticulously tracing the origin, ownership, and transformation history of unique cultural artifacts as they move through various custodians, restoration phases, and exhibition venues. It includes authentication, condition assessment, multi-party negotiations, legal verifications, and secure transportation planning to ensure the artifact's integrity and provenance remain uncompromised while satisfying collectors, museums, and regulatory bodies. The process requires collaboration between historians, legal experts, conservators, and logistics teams to maintain a transparent, documented chain of custody over extended periods, often spanning multiple countries and jurisdictions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Ai = Transition(label='Artifact Intake')
CC = Transition(label='Condition Check')
OR = Transition(label='Origin Research')
OV = Transition(label='Ownership Verify')
LR = Transition(label='Legal Review')
RP = Transition(label='Restoration Plan')
EC = Transition(label='Expert Consult')
PL = Transition(label='Provenance Log')
CT = Transition(label='Custody Transfer')
TA = Transition(label='Transport Arrange')
SB = Transition(label='Security Brief')
ES = Transition(label='Exhibit Setup')
IU = Transition(label='Insurance Update')
DOC = Transition(label='Documentation')
SN = Transition(label='Stakeholder Notify')
FA = Transition(label='Final Audit')

# Parallel branch: origin research and ownership verification
origin_ownership = StrictPartialOrder(nodes=[OR, OV])
# No order edges → OR and OV are concurrent

# Sequence for restoration redo
redo_seq = StrictPartialOrder(nodes=[RP, EC])
redo_seq.order.add_edge(RP, EC)

# Loop: do a condition check, then optionally perform restoration & consult and re-check
restoration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[CC, redo_seq]
)

# Parallel branch: insurance update and documentation
iu_doc = StrictPartialOrder(nodes=[IU, DOC])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    Ai,
    origin_ownership,
    LR,
    restoration_loop,
    PL,
    CT,
    TA,
    SB,
    ES,
    iu_doc,
    SN,
    FA
])

# Define the control‐flow relations
root.order.add_edge(Ai, origin_ownership)
root.order.add_edge(origin_ownership, LR)
root.order.add_edge(LR, restoration_loop)
root.order.add_edge(restoration_loop, PL)
root.order.add_edge(PL, CT)
root.order.add_edge(CT, TA)
root.order.add_edge(TA, SB)
root.order.add_edge(SB, ES)
root.order.add_edge(ES, iu_doc)
root.order.add_edge(iu_doc, SN)
root.order.add_edge(SN, FA)