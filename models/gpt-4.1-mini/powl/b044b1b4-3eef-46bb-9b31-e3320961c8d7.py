# Generated from: b044b1b4-3eef-46bb-9b31-e3320961c8d7.json
# Description: This process involves the authentication and validation of rare artifacts for a specialized auction house. It begins with initial artifact intake, followed by detailed provenance research, material composition analysis using advanced spectroscopy, expert stylistic comparison, and historical context verification. Each artifact undergoes multi-disciplinary review sessions, condition assessment, and restoration feasibility studies. Legal ownership checks and export compliance reviews are conducted before final valuation and cataloging. The process concludes with secure storage preparation and digital archiving of all findings to ensure transparency and traceability for high-value sales.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
artifact_intake = Transition(label='Artifact Intake')

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_review = Transition(label='Style Review')
context_verify = Transition(label='Context Verify')

expert_panel = Transition(label='Expert Panel')

condition_report = Transition(label='Condition Report')
restoration_plan = Transition(label='Restoration Plan')

ownership_audit = Transition(label='Ownership Audit')
export_review = Transition(label='Export Review')

final_valuation = Transition(label='Final Valuation')
catalog_entry = Transition(label='Catalog Entry')

storage_prep = Transition(label='Storage Prep')
digital_archive = Transition(label='Digital Archive')

sales_approval = Transition(label='Sales Approval')

# Provenance Check, Material Scan, Style Review, Context Verify are concurrent after intake
provenance_po = StrictPartialOrder(nodes=[provenance_check, material_scan, style_review, context_verify])
# No order edges => fully concurrent

# Multi-disciplinary review sessions: expert panel after all provenance activities
# So provenance_check, material_scan, style_review, context_verify --> expert_panel
# We create a partial order with nodes provenance activities + expert_panel and edges from each provenance activity to expert_panel

expert_panel_po = StrictPartialOrder(nodes=[provenance_check, material_scan, style_review, context_verify, expert_panel])
expert_panel_po.order.add_edge(provenance_check, expert_panel)
expert_panel_po.order.add_edge(material_scan, expert_panel)
expert_panel_po.order.add_edge(style_review, expert_panel)
expert_panel_po.order.add_edge(context_verify, expert_panel)

# Condition assessment and restoration feasibility studies are concurrent after expert panel
condition_restoration_po = StrictPartialOrder(nodes=[condition_report, restoration_plan])
# concurrent, no edges

# Legal ownership checks and export compliance reviews concurrent after condition/restoration
legal_export_po = StrictPartialOrder(nodes=[ownership_audit, export_review])
# concurrent, no edges

# Final valuation and cataloging sequential (valuation -> catalog)
valuation_catalog_po = StrictPartialOrder(nodes=[final_valuation, catalog_entry])
valuation_catalog_po.order.add_edge(final_valuation, catalog_entry)

# Storage preparation and digital archiving are concurrent after cataloging
storage_digital_po = StrictPartialOrder(nodes=[storage_prep, digital_archive])
# concurrent, no edges

# Connect all steps in proper order:

# From artifact intake -> expert_panel_po (which includes provenance checks etc)
# But the raw provenance activities are nodes inside expert_panel_po
# Instead, we have to chain intake -> provenance activities (provenance_check, material_scan, style_review, context_verify)
# but we have expert_panel_po as a subgraph including these and expert_panel node.

# Thus for clarity, we will use expert_panel_po as the sole model substituting the provenance activities & expert panel.

# After artifact intake --> expert_panel_po
# Then expert_panel -> concurrent condition/restoration po
# Then condition/restoration po -> legal/export po
# Then legal/export po -> valuation_catalog_po
# Then valuation_catalog_po -> storage_digital_po
# Then storage_digital_po -> sales_approval

# Build StrictPartialOrder for the whole process

nodes = [
    artifact_intake,
    expert_panel_po,
    condition_report,
    restoration_plan,
    ownership_audit,
    export_review,
    final_valuation,
    catalog_entry,
    storage_prep,
    digital_archive,
    sales_approval,
]

root = StrictPartialOrder(nodes=nodes)

# artifact intake before all provenance checks in expert_panel_po, but expert_panel_po is a node here
# So artifact intake -> expert_panel_po
root.order.add_edge(artifact_intake, expert_panel_po)

# expert_panel_po before condition_report and restoration_plan
root.order.add_edge(expert_panel_po, condition_report)
root.order.add_edge(expert_panel_po, restoration_plan)

# condition_report and restoration_plan before ownership_audit and export_review
root.order.add_edge(condition_report, ownership_audit)
root.order.add_edge(condition_report, export_review)
root.order.add_edge(restoration_plan, ownership_audit)
root.order.add_edge(restoration_plan, export_review)

# ownership_audit and export_review before final_valuation
root.order.add_edge(ownership_audit, final_valuation)
root.order.add_edge(export_review, final_valuation)

# final_valuation before catalog_entry
root.order.add_edge(final_valuation, catalog_entry)

# catalog_entry before storage_prep and digital_archive
root.order.add_edge(catalog_entry, storage_prep)
root.order.add_edge(catalog_entry, digital_archive)

# storage_prep and digital_archive before sales_approval
root.order.add_edge(storage_prep, sales_approval)
root.order.add_edge(digital_archive, sales_approval)