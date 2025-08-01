# Generated from: 0dddba58-ee44-4fb2-bd74-d1f00dbc87fc.json
# Description: This process outlines the multi-step procedure for authenticating rare historical artifacts before acquisition by a museum. It involves initial appraisal, scientific testing including spectroscopy and radiocarbon dating, provenance verification through archival research, consultation with external experts, risk assessment for forgery, legal ownership checks, and final approval by the curatorial board. The process ensures comprehensive validation to prevent acquisition of counterfeit or illegally acquired items, balancing scholarly integrity with institutional acquisition goals. Documentation and digital archiving of each step are mandatory for transparency and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ia   = Transition(label="Initial Appraisal")
vi   = Transition(label="Visual Inspection")
ms   = Transition(label="Material Sampling")
st   = Transition(label="Spectroscopy Test")
rd   = Transition(label="Radiocarbon Date")
pc   = Transition(label="Provenance Check")
as_  = Transition(label="Archive Search")
ec   = Transition(label="Expert Consult")
fa   = Transition(label="Forgery Analysis")
risk = Transition(label="Risk Assessment")
lr   = Transition(label="Legal Review")
ov   = Transition(label="Ownership Verify")
cm   = Transition(label="Curator Meeting")
fapp = Transition(label="Final Approval")
rec  = Transition(label="Record Archive")
du   = Transition(label="Digital Upload")

# Build the partial order
root = StrictPartialOrder(nodes=[
    ia, vi, ms, st, rd, pc, as_, ec, fa, risk,
    lr, ov, cm, fapp, rec, du
])

# Sequence of appraisal
root.order.add_edge(ia, vi)
root.order.add_edge(vi, ms)

# Parallel branches after inspection
root.order.add_edge(vi, pc)
root.order.add_edge(ms, st)
root.order.add_edge(ms, rd)
root.order.add_edge(pc, as_)

# Analysis branches
root.order.add_edge(st, fa)
root.order.add_edge(rd, fa)
root.order.add_edge(as_, ec)

# Consolidation into risk assessment
root.order.add_edge(fa, risk)
root.order.add_edge(ec, risk)

# Legal and ownership checks
root.order.add_edge(risk, lr)
root.order.add_edge(lr, ov)

# Final approval path
root.order.add_edge(ov, cm)
root.order.add_edge(cm, fapp)

# Documentation and archiving at the end (concurrent)
root.order.add_edge(fapp, rec)
root.order.add_edge(fapp, du)