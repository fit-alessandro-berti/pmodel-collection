# Generated from: 96f43016-51c9-4278-9060-d7317a4843fb.json
# Description: This process involves the careful examination and verification of antique artifacts to determine their authenticity and provenance. It includes initial condition assessment, detailed material analysis, historical research, expert consultations, and cross-referencing with known databases. The procedure must account for potential forgeries, restoration history, and legal ownership verification. Final reporting includes certification and recommendations for preservation or sale, ensuring all findings are meticulously documented for collectors, museums, or auction houses.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all labeled transitions
intake    = Transition(label='Artifact Intake')
cond      = Transition(label='Condition Check')
ms        = Transition(label='Material Scan')
sc        = Transition(label='Style Compare')
pt        = Transition(label='Provenance Trace')
ds        = Transition(label='Database Search')
er        = Transition(label='Expert Review')
fd        = Transition(label='Forgery Detect')
rc        = Transition(label='Restoration Check')
lv        = Transition(label='Legal Verify')
ma        = Transition(label='Market Analysis')
ra        = Transition(label='Risk Assess')
rd        = Transition(label='Report Draft')
ci        = Transition(label='Certification Issue')
pa        = Transition(label='Preservation Advise')
cb        = Transition(label='Client Brief')

# Phase 1: concurrent deep research activities
research = StrictPartialOrder(nodes=[ms, sc, pt, ds])
# no edges => all four run in parallel

# Phase 2: concurrent validation (forgery detection and restoration history)
validation = StrictPartialOrder(nodes=[fd, rc])

# Phase 3: concurrent checks (legal, market, risk)
post_checks = StrictPartialOrder(nodes=[lv, ma, ra])

# Final choice: either preservation advice or a client brief
final_choice = OperatorPOWL(operator=Operator.XOR, children=[pa, cb])

# Final phase: issue certification in parallel with the chosen recommendation
final_phase = StrictPartialOrder(nodes=[ci, final_choice])
# no edges => certification and chosen advice run in parallel

# Build the overall workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[intake, cond, research, er, validation, post_checks, rd, final_phase]
)

# Define the sequential dependencies
root.order.add_edge(intake, cond)
root.order.add_edge(cond, research)
root.order.add_edge(research, er)
root.order.add_edge(er, validation)
root.order.add_edge(validation, post_checks)
root.order.add_edge(post_checks, rd)
root.order.add_edge(rd, final_phase)