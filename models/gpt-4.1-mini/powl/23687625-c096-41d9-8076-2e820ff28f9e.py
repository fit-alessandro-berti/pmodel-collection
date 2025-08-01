# Generated from: 23687625-c096-41d9-8076-2e820ff28f9e.json
# Description: This process involves the multi-layered verification of historical artifacts sourced from various private collectors, museums, and archaeological sites. Initially, artifacts undergo physical inspection and provenance validation, followed by advanced material composition analysis using spectroscopy. Concurrently, experts perform stylistic comparisons against known databases. The process includes legal clearance for export/import regulations and digital cataloging with blockchain certification for authenticity. Finally, artifacts are prepared for exhibition or sale, ensuring compliance with cultural heritage laws and ethical standards. This atypical workflow demands coordination among historians, scientists, legal advisors, and curators to guarantee artifact legitimacy and secure transfer.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
initial_inspect = Transition(label='Initial Inspect')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
spectroscopy_test = Transition(label='Spectroscopy Test')
stylistic_match = Transition(label='Stylistic Match')
database_query = Transition(label='Database Query')
legal_review = Transition(label='Legal Review')
export_clearance = Transition(label='Export Clearance')
blockchain_certify = Transition(label='Blockchain Certify')
digital_catalog = Transition(label='Digital Catalog')
expert_panel = Transition(label='Expert Panel')
condition_report = Transition(label='Condition Report')
ethics_audit = Transition(label='Ethics Audit')
exhibit_prep = Transition(label='Exhibit Prep')
final_approval = Transition(label='Final Approval')
transfer_log = Transition(label='Transfer Log')

# Physical inspection and provenance validation sequence
inspection_seq = StrictPartialOrder(nodes=[initial_inspect, provenance_check])
inspection_seq.order.add_edge(initial_inspect, provenance_check)

# Material scan followed by spectroscopy test sequence
material_seq = StrictPartialOrder(nodes=[material_scan, spectroscopy_test])
material_seq.order.add_edge(material_scan, spectroscopy_test)

# Stylistic comparison concurrent with material analysis, itself composed of stylistic_match then database_query
stylistic_seq = StrictPartialOrder(nodes=[stylistic_match, database_query])
stylistic_seq.order.add_edge(stylistic_match, database_query)

# Concurrent material analysis (material_seq) and stylistic_seq
analysis_concurrent = StrictPartialOrder(nodes=[material_seq, stylistic_seq])
# no edges between material_seq and stylistic_seq means concurrency

# After provenance_check, both analysis_concurrent and legal review run concurrently
legal_seq = StrictPartialOrder(nodes=[legal_review, export_clearance])
legal_seq.order.add_edge(legal_review, export_clearance)

# Concurrent block: legal clearance (legal_seq) and digital catalog with blockchain certification concurrent
catalog_seq = StrictPartialOrder(nodes=[blockchain_certify, digital_catalog])
# No edge => concurrent

legal_and_catalog = StrictPartialOrder(nodes=[legal_seq, catalog_seq])
# no edge between legal_seq and catalog_seq => concurrent

# After analysis and legal/catalog concurrency, run expert panel, condition report and ethics audit sequentially
post_analysis_seq = StrictPartialOrder(nodes=[expert_panel, condition_report, ethics_audit])
post_analysis_seq.order.add_edge(expert_panel, condition_report)
post_analysis_seq.order.add_edge(condition_report, ethics_audit)

# Final sequence: exhibit prep -> final approval -> transfer log
final_seq = StrictPartialOrder(nodes=[exhibit_prep, final_approval, transfer_log])
final_seq.order.add_edge(exhibit_prep, final_approval)
final_seq.order.add_edge(final_approval, transfer_log)

# Compose the overall partial order:
# initial inspection -> provenance check -> (analysis_concurrent) and (legal_and_catalog) concurrent
# Then -> post_analysis_seq -> final_seq

# Step 1: after provenance_check, analysis_concurrent and legal_and_catalog concurrent
middle_level = StrictPartialOrder(nodes=[analysis_concurrent, legal_and_catalog])
# no edge between these two: concurrent

# Step 2: combine provenance_check --> middle_level
after_prov = StrictPartialOrder(nodes=[provenance_check, middle_level])
after_prov.order.add_edge(provenance_check, middle_level)

# Step 3: combine initial sequence before provenance_check
before_mid = StrictPartialOrder(nodes=[initial_inspect, after_prov])
before_mid.order.add_edge(initial_inspect, after_prov)

# Step 4: combine after processing to post analysis sequence, then final sequence
post_and_final = StrictPartialOrder(nodes=[post_analysis_seq, final_seq])
post_and_final.order.add_edge(post_analysis_seq, final_seq)

# Step 5: full root combining before_mid --> post_and_final
root = StrictPartialOrder(nodes=[before_mid, post_and_final])
root.order.add_edge(before_mid, post_and_final)