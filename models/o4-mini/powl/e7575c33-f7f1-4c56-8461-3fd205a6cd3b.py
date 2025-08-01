# Generated from: e7575c33-f7f1-4c56-8461-3fd205a6cd3b.json
# Description: This process involves the detailed examination and validation of antique artifacts to verify their authenticity and provenance. It begins with initial artifact intake and cataloging, followed by expert visual inspection and advanced material analysis using spectroscopy. Historical research is conducted to trace ownership and origin, complemented by comparative stylistic evaluation with verified pieces. The process includes digital 3D scanning for condition assessment and creating a preservation plan. Legal compliance checks ensure adherence to cultural heritage laws. Finally, a comprehensive authentication report is generated and archived, with recommendations for conservation or sale preparation if applicable.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic transitions
artifact_intake     = Transition(label="Artifact Intake")
catalog_entry       = Transition(label="Catalog Entry")
visual_inspect      = Transition(label="Visual Inspect")
material_test       = Transition(label="Material Test")
spectroscopy        = Transition(label="Spectroscopy")
historical_check    = Transition(label="Historical Check")
provenance_trace    = Transition(label="Provenance Trace")
style_compare       = Transition(label="Style Compare")
scanning            = Transition(label="3D Scanning")
condition_assess    = Transition(label="Condition Assess")
preservation_plan   = Transition(label="Preservation Plan")
legal_review        = Transition(label="Legal Review")
report_draft        = Transition(label="Report Draft")
report_finalize     = Transition(label="Report Finalize")
archive_data        = Transition(label="Archive Data")
sale_prep           = Transition(label="Sale Prep")

# Optional sale preparation
skip                = SilentTransition()
sale_xor            = OperatorPOWL(operator=Operator.XOR, children=[sale_prep, skip])

# Build the partially ordered workflow
root = StrictPartialOrder(nodes=[
    artifact_intake,
    catalog_entry,
    visual_inspect,
    material_test,
    spectroscopy,
    historical_check,
    provenance_trace,
    style_compare,
    scanning,
    condition_assess,
    preservation_plan,
    legal_review,
    report_draft,
    report_finalize,
    archive_data,
    sale_xor
])

# Define the control‐flow partial order
# 1. Intake and cataloging
root.order.add_edge(artifact_intake, catalog_entry)

# 2. After catalog, two concurrent branches: visual and material analysis
root.order.add_edge(catalog_entry, visual_inspect)
root.order.add_edge(catalog_entry, material_test)

# 3. Material test followed by spectroscopy
root.order.add_edge(material_test, spectroscopy)

# 4. Both visual_inspect and spectroscopy must complete before historical_check
root.order.add_edge(visual_inspect, historical_check)
root.order.add_edge(spectroscopy, historical_check)

# 5. Historical research → provenance trace → style comparison
root.order.add_edge(historical_check, provenance_trace)
root.order.add_edge(provenance_trace, style_compare)

# 6. 3D scanning after stylistic evaluation
root.order.add_edge(style_compare, scanning)

# 7. Condition assessment and preservation planning
root.order.add_edge(scanning, condition_assess)
root.order.add_edge(condition_assess, preservation_plan)

# 8. Legal compliance check
root.order.add_edge(preservation_plan, legal_review)

# 9. Report drafting and finalization
root.order.add_edge(legal_review, report_draft)
root.order.add_edge(report_draft, report_finalize)

# 10. Archive data and optional sale preparation
root.order.add_edge(report_finalize, archive_data)
root.order.add_edge(archive_data, sale_xor)