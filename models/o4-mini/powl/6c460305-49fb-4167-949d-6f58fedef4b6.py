# Generated from: 6c460305-49fb-4167-949d-6f58fedef4b6.json
# Description: This process involves the intricate verification and authentication of rare historical artifacts for high-profile clients. It starts with initial provenance research, followed by multi-layered physical examinations including spectroscopy and carbon dating. Expert consultations are organized to validate findings, and legal compliance with international trade laws is ensured. Digital fingerprinting and blockchain registration provide immutable tracking, while insurance valuation and client briefing close the cycle. This atypical process demands coordination between archaeologists, legal experts, technologists, and insurers to guarantee authenticity and secure ownership transfer in a highly specialized market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
pc = Transition(label="Provenance Check")
ms = Transition(label="Material Scan")
cd = Transition(label="Carbon Date")
st = Transition(label="Spectral Test")
er = Transition(label="Expert Review")
la = Transition(label="Legal Audit")
tv = Transition(label="Trade Verify")
fp = Transition(label="Fingerprinting")
bc = Transition(label="Blockchain Reg")
va = Transition(label="Valuation Assess")
iq = Transition(label="Insurance Quote")
cb = Transition(label="Client Brief")
ol = Transition(label="Ownership Log")
ta = Transition(label="Transfer Approve")
fa = Transition(label="Final Archive")

# Define concurrent subprocesses
scanning = StrictPartialOrder(nodes=[ms, cd, st])
legal_checks = StrictPartialOrder(nodes=[la, tv])
digital_reg = StrictPartialOrder(nodes=[fp, bc])
valuation = StrictPartialOrder(nodes=[va, iq])
transfer = StrictPartialOrder(nodes=[ol, ta])

# Compose the overall process as a partial order
root = StrictPartialOrder(
    nodes=[
        pc,
        scanning,
        er,
        legal_checks,
        digital_reg,
        valuation,
        cb,
        transfer,
        fa
    ]
)

# Define the control-flow (partial order) edges
root.order.add_edge(pc, scanning)
root.order.add_edge(scanning, er)
root.order.add_edge(er, legal_checks)
root.order.add_edge(legal_checks, digital_reg)
root.order.add_edge(digital_reg, valuation)
root.order.add_edge(valuation, cb)
root.order.add_edge(cb, transfer)
root.order.add_edge(transfer, fa)