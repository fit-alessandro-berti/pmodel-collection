# Generated from: e307a4e0-16b7-4ac0-b3db-6db1b2536966.json
# Description: This process involves the careful restoration and preservation of antique artifacts, ensuring historical accuracy while enhancing structural integrity. It starts with initial assessment and documentation, followed by controlled cleaning and material analysis. Conservation techniques are applied selectively to preserve originality, including stabilization, repair, and protective coating. Throughout the process, ethical considerations and provenance validation are maintained. Final steps include detailed reporting, client review, and archival storage, ensuring the artifact's longevity and historical value for future generations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities and a silent skip
init_assess      = Transition(label='Initial Assess')
scan             = Transition(label='Artifact Scan')
cond_map         = Transition(label='Condition Map')
mat_test         = Transition(label='Material Test')
clean_phase      = Transition(label='Cleaning Phase')
stability        = Transition(label='Stability Check')
minor_repair     = Transition(label='Minor Repair')
struct_reinf     = Transition(label='Structural Reinforce')
surface_restore  = Transition(label='Surface Restore')
coating          = Transition(label='Coating Apply')
ethics           = Transition(label='Ethics Review')
provenance       = Transition(label='Provenance Verify')
client_update    = Transition(label='Client Update')
final_report     = Transition(label='Final Report')
archive          = Transition(label='Archive Store')
skip             = SilentTransition()

# Optional repair and reinforcement via XOR
xor_repair = OperatorPOWL(operator=Operator.XOR, children=[minor_repair, skip])
xor_reinf  = OperatorPOWL(operator=Operator.XOR, children=[struct_reinf, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    init_assess, scan, cond_map, mat_test, clean_phase,
    stability, xor_repair, xor_reinf, surface_restore,
    coating, ethics, provenance, client_update,
    final_report, archive
])

# Sequencing and concurrency
root.order.add_edge(init_assess, scan)
root.order.add_edge(scan, cond_map)

# Material analysis and cleaning can run in parallel
root.order.add_edge(cond_map, mat_test)
root.order.add_edge(cond_map, clean_phase)

# Both analysis and cleaning must finish before stabilization
root.order.add_edge(mat_test, stability)
root.order.add_edge(clean_phase, stability)

# Conservation techniques
root.order.add_edge(stability, xor_repair)
root.order.add_edge(xor_repair, xor_reinf)
root.order.add_edge(xor_reinf, surface_restore)
root.order.add_edge(surface_restore, coating)

# Ethical and provenance checks can run in parallel after coating
root.order.add_edge(coating, ethics)
root.order.add_edge(coating, provenance)

# Both checks complete before client update
root.order.add_edge(ethics, client_update)
root.order.add_edge(provenance, client_update)

# Final reporting and archival
root.order.add_edge(client_update, final_report)
root.order.add_edge(final_report, archive)