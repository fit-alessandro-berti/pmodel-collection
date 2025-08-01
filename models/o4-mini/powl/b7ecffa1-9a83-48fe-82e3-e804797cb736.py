# Generated from: b7ecffa1-9a83-48fe-82e3-e804797cb736.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for museum acquisition. It includes initial artifact reception, condition assessment, provenance verification through archival research, scientific material analysis using spectroscopy, expert consultation for stylistic evaluation, and risk assessment of forgery. The workflow further involves documentation preparation, cross-referencing with international databases, legal clearance for export-import, insurance valuation, and final approval by the acquisition committee. Post-approval, artifacts are cataloged, conserved, and displayed with detailed authentication reports to ensure transparency and maintain cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
receive_artifact    = Transition(label="Receive Artifact")
condition_check     = Transition(label="Condition Check")
provenance_research = Transition(label="Provenance Research")
material_analysis   = Transition(label="Material Analysis")
stylistic_review    = Transition(label="Stylistic Review")
forgery_risk        = Transition(label="Forgery Risk")
expert_consult      = Transition(label="Expert Consult")
document_prep       = Transition(label="Document Prep")
database_cross      = Transition(label="Database Cross")
legal_clearance     = Transition(label="Legal Clearance")
insurance_quote     = Transition(label="Insurance Quote")
committee_review    = Transition(label="Committee Review")
approval_grant      = Transition(label="Approval Grant")
catalog_entry       = Transition(label="Catalog Entry")
conservation        = Transition(label="Conservation")
display_setup       = Transition(label="Display Setup")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    receive_artifact, condition_check, provenance_research, material_analysis,
    stylistic_review, forgery_risk, expert_consult, document_prep,
    database_cross, legal_clearance, insurance_quote, committee_review,
    approval_grant, catalog_entry, conservation, display_setup
])

# Add control‐flow edges
root.order.add_edge(receive_artifact, condition_check)
root.order.add_edge(condition_check, provenance_research)
root.order.add_edge(provenance_research, material_analysis)

# After material analysis, run stylistic review, expert consult, and forgery risk in parallel
root.order.add_edge(material_analysis, stylistic_review)
root.order.add_edge(material_analysis, expert_consult)
root.order.add_edge(material_analysis, forgery_risk)

# All three feed into document preparation
root.order.add_edge(stylistic_review, document_prep)
root.order.add_edge(expert_consult, document_prep)
root.order.add_edge(forgery_risk, document_prep)

# Continue sequentially to final approval
root.order.add_edge(document_prep, database_cross)
root.order.add_edge(database_cross, legal_clearance)
root.order.add_edge(legal_clearance, insurance_quote)
root.order.add_edge(insurance_quote, committee_review)
root.order.add_edge(committee_review, approval_grant)

# Post‐approval steps (catalog, conservation, display) can proceed in parallel
root.order.add_edge(approval_grant, catalog_entry)
root.order.add_edge(approval_grant, conservation)
root.order.add_edge(approval_grant, display_setup)