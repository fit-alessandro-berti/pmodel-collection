# Generated from: 706c8dbd-7a52-4e40-ad66-45d1ea0ee995.json
# Description: This process involves the intricate steps required to authenticate historical artifacts for museum acquisition or private collection. It begins with preliminary visual inspection followed by material composition analysis using non-invasive techniques. Provenance research is conducted through archival record comparison and expert interviews. Scientific dating methods such as radiocarbon or thermoluminescence are applied to determine age. Microbial and residue analysis identify environmental exposure and usage patterns. A risk assessment for forgery indicators is completed, including stylistic evaluation by art historians. Legal clearance ensures compliance with cultural heritage laws. Finally, a comprehensive authenticity report is compiled and peer-reviewed before final approval and acquisition decision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
vc = Transition(label='Visual Check')
ms = Transition(label='Material Scan')
as_ = Transition(label='Archival Search')
ei = Transition(label='Expert Interview')
rc = Transition(label='Radiocarbon Test')
tl = Transition(label='Thermoluminescence')
ra = Transition(label='Residue Analysis')
mt = Transition(label='Microbial Test')
sr = Transition(label='Style Review')
fr = Transition(label='Forgery Risk')
lr = Transition(label='Legal Review')
cc = Transition(label='Compliance Check')
rd = Transition(label='Report Draft')
pr = Transition(label='Peer Review')
fa = Transition(label='Final Approval')

# XOR choice between Radiocarbon Test and Thermoluminescence
dating_choice = OperatorPOWL(operator=Operator.XOR, children=[rc, tl])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    vc, ms,
    as_, ei,
    dating_choice,
    ra, mt,
    sr, fr,
    lr, cc,
    rd, pr, fa
])

# Add the ordering constraints
# 1. Visual Check → Material Scan
root.order.add_edge(vc, ms)
# 2. Material Scan → {Archival Search, Expert Interview}
root.order.add_edge(ms, as_)
root.order.add_edge(ms, ei)
# 3. Both provenance tasks → dating choice
root.order.add_edge(as_, dating_choice)
root.order.add_edge(ei, dating_choice)
# 4. Dating choice → {Residue Analysis, Microbial Test}
root.order.add_edge(dating_choice, ra)
root.order.add_edge(dating_choice, mt)
# 5. Both analyses → {Style Review, Forgery Risk}
root.order.add_edge(ra, sr)
root.order.add_edge(ra, fr)
root.order.add_edge(mt, sr)
root.order.add_edge(mt, fr)
# 6. Both risk tasks → Legal Review
root.order.add_edge(sr, lr)
root.order.add_edge(fr, lr)
# 7. Legal Review → Compliance Check → Report Draft → Peer Review → Final Approval
root.order.add_edge(lr, cc)
root.order.add_edge(cc, rd)
root.order.add_edge(rd, pr)
root.order.add_edge(pr, fa)