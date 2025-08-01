# Generated from: c5ee20a6-c73f-40c8-a93c-7403f387b081.json
# Description: This process outlines the detailed workflow for restoring antique items, combining delicate physical restoration techniques with historical research and provenance verification. It involves initial assessment, condition documentation, material analysis, sourcing authentic replacement parts, gentle cleaning, stabilization, repair, and finishing. The process integrates expert consultations, archival referencing, and conservation ethics to ensure the item's historical integrity is maintained. Post-restoration, the item undergoes quality inspection, photographic documentation, and packaging for safe delivery, accompanied by a detailed restoration report and provenance certification to enhance value and authenticity verification.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
initial_assess     = Transition(label='Initial Assess')
condition_scan     = Transition(label='Condition Scan')
material_test      = Transition(label='Material Test')
historical_check   = Transition(label='Historical Check')
provenance_verify  = Transition(label='Provenance Verify')
expert_consult     = Transition(label='Expert Consult')
archival_review    = Transition(label='Archival Review')
ethics_audit       = Transition(label='Ethics Audit')
parts_sourcing     = Transition(label='Parts Sourcing')
gentle_clean       = Transition(label='Gentle Clean')
stabilize_item     = Transition(label='Stabilize Item')
structural_repair  = Transition(label='Structural Repair')
surface_finish     = Transition(label='Surface Finish')
quality_inspect    = Transition(label='Quality Inspect')
photo_document     = Transition(label='Photo Document')
packaging_prep     = Transition(label='Packaging Prep')
report_generate    = Transition(label='Report Generate')
certify_provenance = Transition(label='Certify Provenance')

# Assemble all nodes
nodes = [
    initial_assess, condition_scan, material_test,
    historical_check, provenance_verify,
    expert_consult, archival_review, ethics_audit,
    parts_sourcing, gentle_clean, stabilize_item,
    structural_repair, surface_finish,
    quality_inspect, photo_document,
    packaging_prep, report_generate, certify_provenance
]

# Create the partial‐order workflow
root = StrictPartialOrder(nodes=nodes)

# 1. Initial linear chain: Initial Assess -> Condition Scan -> Material Test
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(condition_scan, material_test)

# 2. After Material Test, fork into Historical Check and Provenance Verify
root.order.add_edge(material_test, historical_check)
root.order.add_edge(material_test, provenance_verify)

# 3. Both research branches feed into Expert Consult, Archival Review, Ethics Audit
for predecessor in [historical_check, provenance_verify]:
    root.order.add_edge(predecessor, expert_consult)
    root.order.add_edge(predecessor, archival_review)
    root.order.add_edge(predecessor, ethics_audit)

# 4. After those three, continue with Parts Sourcing
for predecessor in [expert_consult, archival_review, ethics_audit]:
    root.order.add_edge(predecessor, parts_sourcing)

# 5. Then the main restoration and finishing chain
chain = [
    parts_sourcing, gentle_clean, stabilize_item, structural_repair,
    surface_finish, quality_inspect, photo_document,
    packaging_prep, report_generate, certify_provenance
]
for src, tgt in zip(chain, chain[1:]):
    root.order.add_edge(src, tgt)