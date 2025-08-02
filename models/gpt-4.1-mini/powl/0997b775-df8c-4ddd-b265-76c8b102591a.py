# Generated from: 0997b775-df8c-4ddd-b265-76c8b102591a.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for a high-security auction house. It begins with initial artifact intake and condition assessment, followed by multi-layered provenance research including archival verification and expert consultations. Concurrently, advanced scientific analysis such as isotope testing and material composition scanning is conducted to validate authenticity. The process also involves coordinating with legal teams to ensure compliance with international cultural heritage laws. Final steps include generating detailed authentication reports and secure digital certification before artifact cataloging and auction preparation. This atypical process ensures utmost credibility and compliance in a niche but critical domain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')

provenance_research = Transition(label='Provenance Research')
archive_verify = Transition(label='Archive Verify')
expert_consult = Transition(label='Expert Consult')

isotope_testing = Transition(label='Isotope Testing')
material_scan = Transition(label='Material Scan')

legal_review = Transition(label='Legal Review')
compliance_check = Transition(label='Compliance Check')

report_draft = Transition(label='Report Draft')
digital_certify = Transition(label='Digital Certify')

catalog_entry = Transition(label='Catalog Entry')
auction_prep = Transition(label='Auction Prep')

client_notify = Transition(label='Client Notify')
secure_storage = Transition(label='Secure Storage')

# Provenance Research detailed: archive_verify and expert_consult in parallel after provenance_research
provenance_po = StrictPartialOrder(
    nodes=[provenance_research, archive_verify, expert_consult]
)
provenance_po.order.add_edge(provenance_research, archive_verify)
provenance_po.order.add_edge(provenance_research, expert_consult)

# Scientific analysis parallel part
science_po = StrictPartialOrder(
    nodes=[isotope_testing, material_scan]
)
# no order edges, both concurrent

# Legal compliance chain
legal_po = StrictPartialOrder(
    nodes=[legal_review, compliance_check]
)
legal_po.order.add_edge(legal_review, compliance_check)

# Report and certification in sequence
report_cert_po = StrictPartialOrder(
    nodes=[report_draft, digital_certify]
)
report_cert_po.order.add_edge(report_draft, digital_certify)

# Catalog and auction prep in sequence
catalog_auction_po = StrictPartialOrder(
    nodes=[catalog_entry, auction_prep]
)
catalog_auction_po.order.add_edge(catalog_entry, auction_prep)

# Final steps to notify client and secure storage, can be concurrent after auction prep
final_po = StrictPartialOrder(
    nodes=[client_notify, secure_storage]
)

# Combine the main flow in strict partial order
# Step1: artifact intake --> condition check
# Then provenance research PO and science PO in parallel (both depend on condition check)
# Then legal PO after provenance & science complete (strictly after both)
# Then report_cert_po after legal_po
# Then catalog_auction_po after report_cert_po
# Then final_po after catalog_auction_po

# Create the main order nodes:
root_nodes = [
    artifact_intake,
    condition_check,
    provenance_po,
    science_po,
    legal_po,
    report_cert_po,
    catalog_auction_po,
    final_po,
]

root = StrictPartialOrder(nodes=root_nodes)

# Build ordering edges:
root.order.add_edge(artifact_intake, condition_check)

root.order.add_edge(condition_check, provenance_po)
root.order.add_edge(condition_check, science_po)

# Both provenance_po and science_po must be completed before legal_po
root.order.add_edge(provenance_po, legal_po)
root.order.add_edge(science_po, legal_po)

root.order.add_edge(legal_po, report_cert_po)

root.order.add_edge(report_cert_po, catalog_auction_po)

root.order.add_edge(catalog_auction_po, final_po)