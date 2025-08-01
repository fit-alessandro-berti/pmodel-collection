# Generated from: ab399c8c-a391-4ef7-99c5-558691184609.json
# Description: This process involves the detailed examination and verification of antique artifacts to establish their authenticity and provenance. It starts with initial artifact intake and visual inspection, followed by multi-disciplinary scientific testing including radiocarbon dating, material composition analysis, and microscopic surface evaluation. Expert consultations with historians and art conservators are incorporated to cross-reference historical records and stylistic attributes. Documentation is meticulously prepared, and legal provenance is verified through archival research. The process concludes with an authentication report and recommendations for preservation or restoration, ensuring the artifact's historical integrity is maintained while enabling confident acquisition or exhibition decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
artifact_intake    = Transition(label='Artifact Intake')
visual_inspect     = Transition(label='Visual Inspect')
radiocarbon_test   = Transition(label='Radiocarbon Test')
material_analysis  = Transition(label='Material Analysis')
surface_microscopy = Transition(label='Surface Microscopy')
expert_consult     = Transition(label='Expert Consult')
historical_review  = Transition(label='Historical Review')
stylistic_compare  = Transition(label='Stylistic Compare')
condition_report   = Transition(label='Condition Report')
archival_research  = Transition(label='Archival Research')
provenance_check   = Transition(label='Provenance Check')
legal_verification = Transition(label='Legal Verification')
authentication_draft = Transition(label='Authentication Draft')
preservation_plan  = Transition(label='Preservation Plan')
final_report       = Transition(label='Final Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, visual_inspect,
    radiocarbon_test, material_analysis, surface_microscopy,
    expert_consult,
    historical_review, stylistic_compare,
    condition_report, archival_research, provenance_check, legal_verification,
    authentication_draft, preservation_plan, final_report
])

# Add precedence relations
root.order.add_edge(artifact_intake, visual_inspect)

root.order.add_edge(visual_inspect, radiocarbon_test)
root.order.add_edge(visual_inspect, material_analysis)
root.order.add_edge(visual_inspect, surface_microscopy)

root.order.add_edge(radiocarbon_test, expert_consult)
root.order.add_edge(material_analysis, expert_consult)
root.order.add_edge(surface_microscopy, expert_consult)

root.order.add_edge(expert_consult, historical_review)
root.order.add_edge(expert_consult, stylistic_compare)

root.order.add_edge(historical_review, condition_report)
root.order.add_edge(stylistic_compare, condition_report)

root.order.add_edge(historical_review, archival_research)
root.order.add_edge(archival_research, provenance_check)
root.order.add_edge(provenance_check, legal_verification)

root.order.add_edge(condition_report, authentication_draft)
root.order.add_edge(legal_verification, authentication_draft)

root.order.add_edge(authentication_draft, preservation_plan)
root.order.add_edge(preservation_plan, final_report)