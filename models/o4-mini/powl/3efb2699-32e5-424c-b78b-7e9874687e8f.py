# Generated from: 3efb2699-32e5-424c-b78b-7e9874687e8f.json
# Description: This process involves the intricate steps required to authenticate and verify the provenance of rare historical artifacts. It includes multidisciplinary expert consultations, chemical composition analysis, provenance chain reconstruction, condition assessment, and advanced imaging techniques. The process aims to ensure the artifact's legitimacy, historical value, and legal ownership by integrating scientific, historical, and legal evaluations before final certification and cataloging for auction or museum acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake     = Transition(label="Artifact Intake")
preliminary_scan    = Transition(label="Preliminary Scan")
expert_consult      = Transition(label="Expert Consult")
material_testing    = Transition(label="Material Testing")
provenance_check    = Transition(label="Provenance Check")
condition_report    = Transition(label="Condition Report")
imaging_capture     = Transition(label="Imaging Capture")
historical_context  = Transition(label="Historical Context")
legal_review        = Transition(label="Legal Review")
ownership_trace     = Transition(label="Ownership Trace")
radiocarbon_test    = Transition(label="Radiocarbon Test")
forgery_analysis    = Transition(label="Forgery Analysis")
data_integration    = Transition(label="Data Integration")
certification_prep  = Transition(label="Certification Prep")
final_approval      = Transition(label="Final Approval")
catalog_entry       = Transition(label="Catalog Entry")
auction_notify      = Transition(label="Auction Notify")

# Define the final choice: auction or museum cataloging
end_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[catalog_entry, auction_notify]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    preliminary_scan,
    expert_consult,
    material_testing,
    provenance_check,
    condition_report,
    imaging_capture,
    historical_context,
    legal_review,
    ownership_trace,
    radiocarbon_test,
    forgery_analysis,
    data_integration,
    certification_prep,
    final_approval,
    end_choice
])

# Sequence & concurrency relations
# 1. Intake → Scan
root.order.add_edge(artifact_intake, preliminary_scan)

# 2. After scan, do core analyses in parallel
for nxt in [expert_consult, material_testing, provenance_check, condition_report, imaging_capture]:
    root.order.add_edge(preliminary_scan, nxt)

# 3. Expert consult yields three parallel subtasks
root.order.add_edge(expert_consult, historical_context)
root.order.add_edge(expert_consult, legal_review)
root.order.add_edge(expert_consult, ownership_trace)

# 4. Material testing yields two parallel subtasks
root.order.add_edge(material_testing, radiocarbon_test)
root.order.add_edge(material_testing, forgery_analysis)

# 5. All subtasks feed into data integration
for src in [
    historical_context,
    legal_review,
    ownership_trace,
    radiocarbon_test,
    forgery_analysis,
    provenance_check,
    condition_report,
    imaging_capture
]:
    root.order.add_edge(src, data_integration)

# 6. Integration → certification preparation → final approval
root.order.add_edge(data_integration, certification_prep)
root.order.add_edge(certification_prep, final_approval)

# 7. After final approval, choose auction or catalog
root.order.add_edge(final_approval, end_choice)