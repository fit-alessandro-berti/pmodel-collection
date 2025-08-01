# Generated from: d1a930d2-6765-459c-9541-64b95a5c5b47.json
# Description: This process involves the detailed verification and authentication of antique artifacts sourced from various international locations. It combines historical research, scientific analysis, provenance validation, and expert consultation. The process begins with initial artifact intake, followed by condition assessment, material testing, stylistic comparison, and carbon dating. Parallelly, provenance documents are scrutinized for legitimacy, and digital imaging techniques are applied to detect restorations or forgeries. The findings are reviewed by a panel of historians and conservators, culminating in a comprehensive authentication report. This rigorous approach ensures the artifact's authenticity is confirmed beyond reasonable doubt before it is cataloged or auctioned.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all transitions
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Scientific analysis branch: Material Test -> Style Compare -> Carbon Dating
sci = StrictPartialOrder(nodes=[material_test, style_compare, carbon_dating])
sci.order.add_edge(material_test, style_compare)
sci.order.add_edge(style_compare, carbon_dating)

# Provenance validation branch with two concurrent sub‐flows:
#   Document Review -> Provenance Check
#   Digital Imaging -> Forgery Scan
prov = StrictPartialOrder(nodes=[document_review, provenance_check, digital_imaging, forgery_scan])
prov.order.add_edge(document_review, provenance_check)
prov.order.add_edge(digital_imaging, forgery_scan)

# Root workflow partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    historical_research,
    sci,
    prov,
    expert_consult,
    panel_review,
    report_draft,
    final_approval,
    catalog_entry
])

# Sequence: Artifact Intake -> Condition Check
root.order.add_edge(artifact_intake, condition_check)

# After condition check, four branches in parallel
for branch in [historical_research, sci, prov, expert_consult]:
    root.order.add_edge(condition_check, branch)

# Synchronize before panel review
for branch in [historical_research, sci, prov, expert_consult]:
    root.order.add_edge(branch, panel_review)

# Final sequence: Panel Review -> Report Draft -> Final Approval -> Catalog Entry
root.order.add_edge(panel_review, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)