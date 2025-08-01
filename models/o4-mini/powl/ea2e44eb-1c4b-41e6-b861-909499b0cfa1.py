# Generated from: ea2e44eb-1c4b-41e6-b861-909499b0cfa1.json
# Description: This process outlines the complex steps involved in authenticating rare historical artifacts for a museum acquisition. It begins with initial artifact intake, followed by detailed provenance research including archival cross-referencing and expert consultations. Scientific analysis is conducted using non-invasive imaging techniques such as XRF and 3D scanning to determine material composition and manufacturing methods. Parallelly, stylistic comparisons with known artifact databases are performed. Results from all investigations are consolidated and reviewed in a multidisciplinary panel. Based on the consensus, a certification report is generated detailing authenticity, condition, and historical significance. Final steps include secure storage arrangement, digital cataloging, and preparation for public display or loan agreements with external institutions. Continuous monitoring protocols are established to ensure artifact preservation post-acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Artifact Intake')
prov_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_consult = Transition(label='Expert Consult')
material_scan = Transition(label='Material Scan')
imaging3d = Transition(label='3D Imaging')
db_query = Transition(label='Database Query')
stylistic_match = Transition(label='Stylistic Match')
panel_review = Transition(label='Panel Review')
certify_report = Transition(label='Certify Report')
condition_assess = Transition(label='Condition Assess')
storage_plan = Transition(label='Storage Plan')
catalog_entry = Transition(label='Catalog Entry')
display_prep = Transition(label='Display Prep')
loan_arrange = Transition(label='Loan Arrange')
monitor_setup = Transition(label='Monitor Setup')

# Provenance research: Archive Search and Expert Consult in parallel
prov_po = StrictPartialOrder(nodes=[archive_search, expert_consult])
# Scientific analysis: Material Scan and 3D Imaging in parallel
analysis_po = StrictPartialOrder(nodes=[material_scan, imaging3d])
# Stylistic comparison: Database Query then Stylistic Match
style_po = StrictPartialOrder(nodes=[db_query, stylistic_match])
style_po.order.add_edge(db_query, stylistic_match)

# Choice between preparing for display or arranging a loan
xor_display_loan = OperatorPOWL(operator=Operator.XOR, children=[display_prep, loan_arrange])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    intake,
    prov_check,
    prov_po,
    analysis_po,
    style_po,
    panel_review,
    certify_report,
    condition_assess,
    storage_plan,
    catalog_entry,
    xor_display_loan,
    monitor_setup
])

# Add control-flow dependencies
root.order.add_edge(intake, prov_check)
root.order.add_edge(prov_check, prov_po)
root.order.add_edge(prov_check, analysis_po)
root.order.add_edge(prov_check, style_po)

root.order.add_edge(prov_po, panel_review)
root.order.add_edge(analysis_po, panel_review)
root.order.add_edge(style_po, panel_review)

root.order.add_edge(panel_review, certify_report)
root.order.add_edge(certify_report, condition_assess)
root.order.add_edge(condition_assess, storage_plan)
root.order.add_edge(storage_plan, catalog_entry)
root.order.add_edge(catalog_entry, xor_display_loan)
root.order.add_edge(xor_display_loan, monitor_setup)