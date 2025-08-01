# Generated from: 6ac3a718-dca7-457d-a572-dba7af01cd16.json
# Description: This process involves the verification and authentication of historical artifacts using a combination of physical examination, chemical analysis, provenance validation, and blockchain recording. Initially, artifacts undergo visual inspection to detect anomalies, followed by microscopic and spectroscopic tests to determine material composition. Concurrently, provenance documents are digitized and cross-referenced with global registries. Verified data is then encrypted and logged into a blockchain ledger to ensure immutable record keeping. Finally, an expert panel reviews consolidated findings for final certification, and a digital twin is created for virtual display and further analysis. The process ensures authenticity while integrating modern technology with traditional expertise, reducing fraud in the antiquities market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
visual_scan        = Transition(label='Visual Scan')
material_test      = Transition(label='Material Test')
chemical_analysis  = Transition(label='Chemical Analysis')
microscopic_review = Transition(label='Microscopic Review')
document_digitize  = Transition(label='Document Digitize')
registry_crossref  = Transition(label='Registry Crossref')
provenance_check   = Transition(label='Provenance Check')
data_encryption    = Transition(label='Data Encryption')
blockchain_log     = Transition(label='Blockchain Log')
expert_panel       = Transition(label='Expert Panel')
final_certification= Transition(label='Final Certification')
digital_twin       = Transition(label='Digital Twin')
virtual_display    = Transition(label='Virtual Display')
fraud_detect       = Transition(label='Fraud Detect')
report_generate    = Transition(label='Report Generate')
archive_storage    = Transition(label='Archive Storage')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    visual_scan,
    material_test,
    chemical_analysis,
    microscopic_review,
    document_digitize,
    registry_crossref,
    provenance_check,
    data_encryption,
    blockchain_log,
    expert_panel,
    final_certification,
    digital_twin,
    virtual_display,
    fraud_detect,
    report_generate,
    archive_storage
])

# Define the control‐flow (partial order) edges
# 1. Visual inspection leads to both material testing and provenance digitization
root.order.add_edge(visual_scan, material_test)
root.order.add_edge(visual_scan, document_digitize)

# 2. Material testing splits into chemical analysis and microscopic review
root.order.add_edge(material_test, chemical_analysis)
root.order.add_edge(material_test, microscopic_review)

# 3. Provenance path: digitize → crossref → check
root.order.add_edge(document_digitize, registry_crossref)
root.order.add_edge(registry_crossref, provenance_check)

# 4. After both analysis branches complete, encrypt and log on blockchain
root.order.add_edge(chemical_analysis, data_encryption)
root.order.add_edge(microscopic_review, data_encryption)
root.order.add_edge(provenance_check, data_encryption)
root.order.add_edge(data_encryption, blockchain_log)

# 5. Expert review and final certification
root.order.add_edge(blockchain_log, expert_panel)
root.order.add_edge(expert_panel, final_certification)

# 6. Post‐certification: create digital twin (→ virtual display) and fraud reporting
root.order.add_edge(final_certification, digital_twin)
root.order.add_edge(final_certification, fraud_detect)
root.order.add_edge(digital_twin, virtual_display)
root.order.add_edge(fraud_detect, report_generate)
root.order.add_edge(report_generate, archive_storage)