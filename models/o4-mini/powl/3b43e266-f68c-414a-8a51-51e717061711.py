# Generated from: 3b43e266-f68c-414a-8a51-51e717061711.json
# Description: This process governs the verification and authentication of ancient artifacts prior to acquisition by museums or private collectors. It involves multidisciplinary collaboration across historians, chemists, and legal experts. The workflow begins with preliminary artifact inspection, followed by material composition analysis using spectroscopy, radiocarbon dating, and microscopic examination. Subsequent provenance research entails tracing ownership history through archival records and cross-referencing with known historical events. Legal clearance is obtained to confirm artifact export and import compliance. Conservation specialists then assess preservation needs and recommend restoration protocols. Finally, a comprehensive authentication report is compiled, integrating scientific data, historical context, and legal validation to support acquisition decisions and prevent fraudulent transactions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator  # imported per convention

# Define atomic activities
initial_inspect    = Transition(label='Initial Inspect')
material_test      = Transition(label='Material Test')
radiocarbon_date   = Transition(label='Radiocarbon Date')
microscopic_scan   = Transition(label='Microscopic Scan')
provenance_check   = Transition(label='Provenance Check')
archive_search     = Transition(label='Archive Search')
owner_verify       = Transition(label='Owner Verify')
legal_review       = Transition(label='Legal Review')
export_clearance   = Transition(label='Export Clearance')
import_clearance   = Transition(label='Import Clearance')
conservation_eval  = Transition(label='Conservation Eval')
restoration_plan   = Transition(label='Restoration Plan')
report_draft       = Transition(label='Report Draft')
report_review      = Transition(label='Report Review')
final_approval     = Transition(label='Final Approval')

# Define sub‐workflows
# 1) Material analyses in parallel
material_tests = StrictPartialOrder(nodes=[material_test, radiocarbon_date, microscopic_scan])
# no internal order edges => all three can run concurrently

# 2) Provenance research tasks in parallel
provenance_tasks = StrictPartialOrder(nodes=[archive_search, owner_verify])
# no internal edges => concurrent

# 3) Conservation assessment then restoration planning
conservation_sub = StrictPartialOrder(nodes=[conservation_eval, restoration_plan])
conservation_sub.order.add_edge(conservation_eval, restoration_plan)

# 4) Report compilation, review, and final approval in sequence
report_sub = StrictPartialOrder(nodes=[report_draft, report_review, final_approval])
report_sub.order.add_edge(report_draft, report_review)
report_sub.order.add_edge(report_review, final_approval)

# Assemble the top‐level workflow as a partial order
root = StrictPartialOrder(nodes=[
    initial_inspect,
    material_tests,
    provenance_check,
    provenance_tasks,
    legal_review,
    export_clearance,
    import_clearance,
    conservation_sub,
    report_sub
])

# Define the control‐flow dependencies
root.order.add_edge(initial_inspect, material_tests)
root.order.add_edge(material_tests, provenance_check)
root.order.add_edge(provenance_check, provenance_tasks)
root.order.add_edge(provenance_tasks, legal_review)
root.order.add_edge(legal_review, export_clearance)
root.order.add_edge(export_clearance, import_clearance)
root.order.add_edge(import_clearance, conservation_sub)
root.order.add_edge(conservation_sub, report_sub)