# Generated from: 15f27f99-e557-4656-980b-195f0b45ef4c.json
# Description: This process entails the comprehensive evaluation and authentication of ancient artifacts submitted by collectors or museums. It begins with initial intake and documentation, followed by non-invasive imaging techniques and material composition analysis. Specialists conduct provenance research and cross-reference historical databases. Parallel steps include microscopic surface examination and radiocarbon dating. Findings are compiled into a detailed report, which undergoes peer review. Contingent on results, legal and ethical clearance is secured before final certification. The process concludes with secure archival of all data and returning the artifact under controlled conditions, ensuring traceability and authenticity verification for future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as Transitions
intake_review    = Transition(label='Intake Review')
image_capture    = Transition(label='Image Capture')
material_test    = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
database_search  = Transition(label='Database Search')
surface_scan     = Transition(label='Surface Scan')
radiocarbon_date = Transition(label='Radiocarbon Date')
report_draft     = Transition(label='Report Draft')
peer_review      = Transition(label='Peer Review')
legal_clear      = Transition(label='Legal Clear')
ethical_audit    = Transition(label='Ethical Audit')
certify_artifact = Transition(label='Certify Artifact')
archive_data     = Transition(label='Archive Data')
return_artifact  = Transition(label='Return Artifact')
traceability_log = Transition(label='Traceability Log')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    intake_review,
    image_capture,
    material_test,
    provenance_check,
    database_search,
    surface_scan,
    radiocarbon_date,
    report_draft,
    peer_review,
    legal_clear,
    ethical_audit,
    certify_artifact,
    archive_data,
    return_artifact,
    traceability_log
])

# 1. After intake, run image capture & material test in parallel
root.order.add_edge(intake_review, image_capture)
root.order.add_edge(intake_review, material_test)

# 2. After imaging & material test, do provenance check & database search in parallel
root.order.add_edge(image_capture, provenance_check)
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(image_capture, database_search)
root.order.add_edge(material_test, database_search)

# 3. After research, run surface scan & radiocarbon dating in parallel
root.order.add_edge(provenance_check, surface_scan)
root.order.add_edge(database_search, surface_scan)
root.order.add_edge(provenance_check, radiocarbon_date)
root.order.add_edge(database_search, radiocarbon_date)

# 4. Compile report, then peer review
root.order.add_edge(surface_scan, report_draft)
root.order.add_edge(radiocarbon_date, report_draft)
root.order.add_edge(report_draft, peer_review)

# 5. After peer review, perform legal clearance & ethical audit in parallel
root.order.add_edge(peer_review, legal_clear)
root.order.add_edge(peer_review, ethical_audit)

# 6. After both clearances, certify artifact
root.order.add_edge(legal_clear, certify_artifact)
root.order.add_edge(ethical_audit, certify_artifact)

# 7. Finally archive data, return artifact, and log traceability in parallel
root.order.add_edge(certify_artifact, archive_data)
root.order.add_edge(certify_artifact, return_artifact)
root.order.add_edge(certify_artifact, traceability_log)