# Generated from: f2d257b6-15a6-470f-8b22-f0f0e30c57b1.json
# Description: This process involves the meticulous verification of antique artifacts combining scientific analysis, provenance research, and expert consultation to ensure authenticity. Activities range from initial artifact intake and condition assessment to advanced material dating techniques, historical documentation cross-referencing, and collaboration with historians and forensic specialists. The process integrates digital imaging, chemical composition testing, and market trend evaluation to establish artifact legitimacy and value before final certification and archival storage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_sampling = Transition(label='Material Sampling')
radiocarbon_test = Transition(label='Radiocarbon Test')
provenance_review = Transition(label='Provenance Review')
imaging_capture = Transition(label='Imaging Capture')
chemical_analysis = Transition(label='Chemical Analysis')
historical_match = Transition(label='Historical Match')
expert_consult = Transition(label='Expert Consult')
forgery_scan = Transition(label='Forgery Scan')
market_survey = Transition(label='Market Survey')
value_estimate = Transition(label='Value Estimate')
certification = Transition(label='Certification')
digital_archive = Transition(label='Digital Archive')
final_storage = Transition(label='Final Storage')

# Loop for advanced material dating techniques: Material Sampling + Radiocarbon Test repeated until exit
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, radiocarbon_test])

# Loop for expert consultation and forgery scan repeated until exit
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, forgery_scan])

# Parallel advanced analyses: Provenance Review, Imaging Capture, Chemical Analysis, and the loops material_loop and expert_loop are concurrent
# We model this by a partial order with those nodes concurrent except input dependencies

# Historical Match depends on Provenance Review
# Value Estimate depends on Market Survey and expert_loop and analyses

# Partial order 1: from Artifact Intake to Condition Check
# Then condition_check leads to advanced analyses:
# -> Provenance Review --> Historical Match
# -> Imaging Capture (concurrent)
# -> Chemical Analysis (concurrent)
# -> material_loop (concurrent)
# -> expert_loop (concurrent)
# After all analyses, forge market survey, then Value Estimate
# Then Certification, then digital archive and final storage in parallel

# Construct partial order for advanced analyses and their dependencies:
# nodes = Provenance Review, Historical Match, Imaging Capture, Chemical Analysis, material_loop, expert_loop, Market Survey, Value Estimate

# We'll model that Historical Match depends on Provenance Review
# Value Estimate depends on Market Survey, expert_loop, Historical Match, Imaging Capture, Chemical Analysis, material_loop
# Market Survey can run concurrently with other analyses (except the loops must finish before Value Estimate)
# certification after Value Estimate
# Digital Archive and Final Storage concurrent after Certification

# Define nodes for advanced analyses and value evaluation
nodes_advanced = [
    provenance_review,
    historical_match,
    imaging_capture,
    chemical_analysis,
    material_loop,
    expert_loop,
    market_survey,
    value_estimate,
]

root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    provenance_review,
    historical_match,
    imaging_capture,
    chemical_analysis,
    material_loop,
    expert_loop,
    market_survey,
    value_estimate,
    certification,
    digital_archive,
    final_storage,
])

# Order:
# artifact_intake --> condition_check
root.order.add_edge(artifact_intake, condition_check)

# condition_check --> provenance_review, imaging_capture, chemical_analysis, material_loop, expert_loop
root.order.add_edge(condition_check, provenance_review)
root.order.add_edge(condition_check, imaging_capture)
root.order.add_edge(condition_check, chemical_analysis)
root.order.add_edge(condition_check, material_loop)
root.order.add_edge(condition_check, expert_loop)

# provenance_review --> historical_match
root.order.add_edge(provenance_review, historical_match)

# historical_match and imaging_capture, chemical_analysis, material_loop, expert_loop finish before value_estimate
root.order.add_edge(historical_match, value_estimate)
root.order.add_edge(imaging_capture, value_estimate)
root.order.add_edge(chemical_analysis, value_estimate)
root.order.add_edge(material_loop, value_estimate)
root.order.add_edge(expert_loop, value_estimate)

# market_survey --> value_estimate
root.order.add_edge(market_survey, value_estimate)

# value_estimate --> certification
root.order.add_edge(value_estimate, certification)

# certification --> digital_archive and final_storage
root.order.add_edge(certification, digital_archive)
root.order.add_edge(certification, final_storage)