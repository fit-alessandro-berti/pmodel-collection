# Generated from: aff6549e-675f-4ff7-b6cb-9fdbf9bb0a70.json
# Description: This process involves the multi-layered authentication of rare historical artifacts for museums and private collectors. It begins with initial provenance verification and scientific material analysis, followed by expert stylistic evaluation and forensic imaging. Subsequent steps include cross-referencing with global databases, consulting cultural heritage specialists, and conducting environmental aging simulations. The process further incorporates stakeholder interviews, legal ownership verification, and risk assessment for potential forgery. Final activities encompass preparation of detailed certification reports, digital archiving of findings, and secure artifact handover with traceability protocols to ensure authenticity and legal compliance throughout the artifact's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
pc = Transition(label="Provenance Check")
ms = Transition(label="Material Scan")
se = Transition(label="Stylistic Eval")
fi = Transition(label="Forensic Image")
dm = Transition(label="Database Match")
hc = Transition(label="Heritage Consult")
asim = Transition(label="Age Simulation")
st = Transition(label="Stakeholder Talk")
ov = Transition(label="Ownership Verify")
fr = Transition(label="Forgery Risk")
cr = Transition(label="Certify Report")
da = Transition(label="Data Archive")
sh = Transition(label="Secure Handover")
tp = Transition(label="Trace Protocol")
lr = Transition(label="Legal Review")

# Build a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    pc, ms,
    se, fi,
    dm, hc, asim,
    st, ov, fr,
    cr, da, sh, tp, lr
])

# 1) Initial provenance check and material scan are concurrent;
#    both must complete before stylistic eval and forensic imaging.
root.order.add_edge(pc, se)
root.order.add_edge(pc, fi)
root.order.add_edge(ms, se)
root.order.add_edge(ms, fi)

# 2) After stylistic eval & forensic imaging, do database match,
#    heritage consult, and age simulation (they can run in parallel).
for src in (se, fi):
    for tgt in (dm, hc, asim):
        root.order.add_edge(src, tgt)

# 3) Once the three analyses finish, conduct stakeholder talk,
#    ownership verification, and forgery risk assessment (parallel).
for src in (dm, hc, asim):
    for tgt in (st, ov, fr):
        root.order.add_edge(src, tgt)

# 4) After interviews/verification/risk assessment, prepare final activities.
#    All these depend on completion of st, ov, fr.
for src in (st, ov, fr):
    for tgt in (cr, da, sh, lr):
        root.order.add_edge(src, tgt)

# 5) Order among final steps:
#    certify report before legal review, then secure handover, then trace protocol.
root.order.add_edge(cr, lr)
root.order.add_edge(lr, sh)
root.order.add_edge(sh, tp)