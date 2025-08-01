# Generated from: 178dddf8-63a2-4464-ac6e-cf3bf8e64c11.json
# Description: This process involves the meticulous authentication and provenance verification of rare artifacts within a decentralized consortium of museums and private collectors. It begins with initial artifact intake and preliminary inspection, followed by multi-source historical data aggregation including archival documents, expert opinions, and scientific testing results. The process includes blockchain registration for immutable provenance records, advanced material composition analysis using spectrometry, and AI-driven stylistic comparison against established artifact databases. Discrepancies trigger a collaborative review session among curators and historians before final certification. Post-authentication, the artifact’s digital twin is created and integrated into a virtual exhibit platform, enabling real-time condition monitoring and public accessibility while ensuring ongoing provenance validation through periodic re-assessment cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake   = Transition(label="Artifact Intake")
prelim_inspect    = Transition(label="Prelim Inspect")
data_agg          = Transition(label="Data Aggregation")
archive_review    = Transition(label="Archive Review")
expert_consult    = Transition(label="Expert Consult")
material_test     = Transition(label="Material Test")
blockchain_entry  = Transition(label="Blockchain Entry")
spectrometry      = Transition(label="Spectrometry Scan")
style_compare     = Transition(label="Style Compare")
discrepancy_flag  = Transition(label="Discrepancy Flag")
review_session    = Transition(label="Review Session")
final_certify     = Transition(label="Final Certify")
digital_twin      = Transition(label="Digital Twin")
exhibit_upload    = Transition(label="Exhibit Upload")
condition_monitor = Transition(label="Condition Monitor")
periodic_audit    = Transition(label="Periodic Audit")

# Define silent transition for the "no discrepancy" branch
skip = SilentTransition()

# Concurrency of archival, expert and material testing
agg_conc = StrictPartialOrder(nodes=[archive_review, expert_consult, material_test])

# Concurrency of blockchain entry, spectrometry and style comparison
par3 = StrictPartialOrder(nodes=[blockchain_entry, spectrometry, style_compare])

# XOR between no-discrepancy and discrepancy-review paths
discrep_proc = StrictPartialOrder(nodes=[discrepancy_flag, review_session])
discrep_proc.order.add_edge(discrepancy_flag, review_session)
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, discrep_proc])

# Loop for condition monitoring + periodic audit
loop_oper = OperatorPOWL(operator=Operator.LOOP, children=[condition_monitor, periodic_audit])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        prelim_inspect,
        data_agg,
        agg_conc,
        par3,
        xor,
        final_certify,
        digital_twin,
        exhibit_upload,
        loop_oper
    ]
)

# Sequence edges
root.order.add_edge(artifact_intake, prelim_inspect)
root.order.add_edge(prelim_inspect, data_agg)

# Data aggregation --> concurrent sub-processes
root.order.add_edge(data_agg, agg_conc)

# After aggregation --> blockchain/spectrometry/style concurrently
root.order.add_edge(agg_conc, par3)

# After checking tasks --> discrepancy choice
root.order.add_edge(par3, xor)

# After resolution --> final certification
root.order.add_edge(xor, final_certify)

# Post-certification: digital twin and exhibit upload
root.order.add_edge(final_certify, digital_twin)
root.order.add_edge(digital_twin, exhibit_upload)

# Exhibit upload --> ongoing monitoring loop
root.order.add_edge(exhibit_upload, loop_oper)