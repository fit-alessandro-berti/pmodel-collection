# Generated from: e989a21a-4800-401e-ac00-a64f68c733fd.json
# Description: This complex process involves verifying the authenticity of rare and valuable artworks through a multi-disciplinary approach combining scientific analysis, provenance research, expert consultation, and advanced imaging technologies. It begins with initial visual inspection and historical documentation gathering, followed by pigment and material composition testing using spectroscopy. Next, experts analyze stylistic elements and compare them against known artist techniques. Provenance chains are meticulously traced to identify any gaps or suspicious transfers. Digital imaging techniques such as infrared reflectography and X-ray fluorescence are employed to reveal underdrawings and alterations. A cross-functional team then consolidates findings to assess authenticity, with a final report generated for stakeholders. This process helps prevent forgery circulation and ensures cultural heritage preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
visual_inspect    = Transition(label='Visual Inspect')
document_gather   = Transition(label='Document Gather')
material_test     = Transition(label='Material Test')
pigment_analyze   = Transition(label='Pigment Analyze')
style_compare     = Transition(label='Style Compare')
provenance_trace  = Transition(label='Provenance Trace')
infrared_scan     = Transition(label='Infrared Scan')
xray_fluoresce    = Transition(label='Xray Fluoresce')
expert_consult    = Transition(label='Expert Consult')
data_crosscheck   = Transition(label='Data Crosscheck')
forgery_detect    = Transition(label='Forgery Detect')
report_draft      = Transition(label='Report Draft')
stakeholder_review= Transition(label='Stakeholder Review')
final_approval    = Transition(label='Final Approval')
archive_store     = Transition(label='Archive Store')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    visual_inspect, document_gather,
    material_test, pigment_analyze,
    style_compare, provenance_trace,
    infrared_scan, xray_fluoresce, expert_consult,
    data_crosscheck, forgery_detect,
    report_draft, stakeholder_review,
    final_approval, archive_store
])

# 1) After Visual Inspect & Document Gather → Material Test & Pigment Analyze
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(visual_inspect, pigment_analyze)
root.order.add_edge(document_gather, pigment_analyze)

# 2) After Material Test & Pigment Analyze → Style Compare & Provenance Trace
for src in (material_test, pigment_analyze):
    root.order.add_edge(src, style_compare)
    root.order.add_edge(src, provenance_trace)

# 3) After Style Compare & Provenance Trace → Infrared Scan, Xray Fluoresce, Expert Consult
for src in (style_compare, provenance_trace):
    root.order.add_edge(src, infrared_scan)
    root.order.add_edge(src, xray_fluoresce)
    root.order.add_edge(src, expert_consult)

# 4) After imaging & expert consult → Data Crosscheck
for src in (infrared_scan, xray_fluoresce, expert_consult):
    root.order.add_edge(src, data_crosscheck)

# 5) Then Forgery Detect → Report Draft → Stakeholder Review → Final Approval → Archive Store
root.order.add_edge(data_crosscheck, forgery_detect)
root.order.add_edge(forgery_detect, report_draft)
root.order.add_edge(report_draft, stakeholder_review)
root.order.add_edge(stakeholder_review, final_approval)
root.order.add_edge(final_approval, archive_store)