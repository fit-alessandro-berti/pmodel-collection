# Generated from: f2d257b6-15a6-470f-8b22-f0f0e30c57b1.json
# Description: This process involves the meticulous verification of antique artifacts combining scientific analysis, provenance research, and expert consultation to ensure authenticity. Activities range from initial artifact intake and condition assessment to advanced material dating techniques, historical documentation cross-referencing, and collaboration with historians and forensic specialists. The process integrates digital imaging, chemical composition testing, and market trend evaluation to establish artifact legitimacy and value before final certification and archival storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions
artifact_intake    = Transition(label='Artifact Intake')
condition_check    = Transition(label='Condition Check')
material_sampling  = Transition(label='Material Sampling')
radiocarbon_test   = Transition(label='Radiocarbon Test')
provenance_review  = Transition(label='Provenance Review')
imaging_capture    = Transition(label='Imaging Capture')
chemical_analysis  = Transition(label='Chemical Analysis')
historical_match   = Transition(label='Historical Match')
expert_consult     = Transition(label='Expert Consult')
forgery_scan       = Transition(label='Forgery Scan')
market_survey      = Transition(label='Market Survey')
value_estimate     = Transition(label='Value Estimate')
certification      = Transition(label='Certification')
digital_archive    = Transition(label='Digital Archive')
final_storage      = Transition(label='Final Storage')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    artifact_intake, condition_check,
    material_sampling, radiocarbon_test,
    provenance_review, historical_match,
    imaging_capture, forgery_scan,
    chemical_analysis, expert_consult,
    market_survey, value_estimate,
    certification, digital_archive, final_storage
])

# Sequence: intake → check
root.order.add_edge(artifact_intake, condition_check)

# Parallel branches after condition check
root.order.add_edge(condition_check, material_sampling)
root.order.add_edge(material_sampling, radiocarbon_test)

root.order.add_edge(condition_check, provenance_review)
root.order.add_edge(provenance_review, historical_match)

root.order.add_edge(condition_check, imaging_capture)
root.order.add_edge(imaging_capture, forgery_scan)

root.order.add_edge(condition_check, chemical_analysis)
root.order.add_edge(chemical_analysis, expert_consult)

root.order.add_edge(condition_check, market_survey)

# Synchronize branches into value estimate
root.order.add_edge(radiocarbon_test, value_estimate)
root.order.add_edge(historical_match, value_estimate)
root.order.add_edge(forgery_scan, value_estimate)
root.order.add_edge(expert_consult, value_estimate)
root.order.add_edge(market_survey, value_estimate)

# Final sequence: estimate → certification → archive/storage
root.order.add_edge(value_estimate, certification)
root.order.add_edge(certification, digital_archive)
root.order.add_edge(certification, final_storage)