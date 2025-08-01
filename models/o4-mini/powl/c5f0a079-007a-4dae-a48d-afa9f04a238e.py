# Generated from: c5f0a079-007a-4dae-a48d-afa9f04a238e.json
# Description: This process involves the intricate steps required to authenticate rare historical artifacts. It begins with initial provenance research followed by material composition analysis using advanced spectrometry. Specialists then conduct microscopic wear pattern examination to identify inconsistencies. Concurrently, digital imaging captures high-resolution details for pattern matching against known databases. Legal verification ensures ownership legitimacy, while ethical committees assess cultural sensitivity. The artifact undergoes carbon dating to confirm age, and restoration experts evaluate preservation needs. Finally, a comprehensive report is compiled, reviewed by multiple stakeholders, and archived securely for future reference and public exhibition approval.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
pc  = Transition(label="Provenance Check")
ms  = Transition(label="Material Scan")
wa  = Transition(label="Wear Analysis")
ic  = Transition(label="Image Capture")
pm_ = Transition(label="Pattern Match")
ov  = Transition(label="Ownership Verify")
er  = Transition(label="Ethics Review")
cd  = Transition(label="Carbon Dating")
re_ = Transition(label="Restoration Eval")
rd  = Transition(label="Report Draft")
sr  = Transition(label="Stakeholder Review")
ad  = Transition(label="Archive Data")
ea  = Transition(label="Exhibit Approve")
fc  = Transition(label="Final Certification")

# Build a loop for continuous condition monitoring
skip = SilentTransition()
cm   = Transition(label="Condition Monitor")
loop_cm = OperatorPOWL(operator=Operator.LOOP, children=[skip, cm])

# Assemble the POWL model as a partial order
root = StrictPartialOrder(nodes=[
    pc, ms, wa,
    ic, pm_,
    ov, er,
    cd, re_,
    rd, sr,
    ad, ea,
    loop_cm,
    fc
])

# Define the control-flow (order) dependencies
root.order.add_edge(pc,  ms)
root.order.add_edge(ms,  wa)

# Two branches concurrently after wear analysis:
root.order.add_edge(wa,  ic)
root.order.add_edge(wa,  ov)

# Branch 1: imaging -> pattern matching
root.order.add_edge(ic,  pm_)

# Branch 2: legal -> ethics
root.order.add_edge(ov,  er)

# Join both branches into carbon dating
root.order.add_edge(pm_, cd)
root.order.add_edge(er,  cd)

# Continue sequentially
root.order.add_edge(cd,  re_)
root.order.add_edge(re_, rd)
root.order.add_edge(rd,  sr)
root.order.add_edge(sr,  ad)
root.order.add_edge(ad,  ea)

# After exhibit approval, do continuous condition monitoring, then final certification
root.order.add_edge(ea,       loop_cm)
root.order.add_edge(loop_cm,  fc)