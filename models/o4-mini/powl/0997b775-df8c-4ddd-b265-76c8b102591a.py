# Generated from: 0997b775-df8c-4ddd-b265-76c8b102591a.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for a high-security auction house. It begins with initial artifact intake and condition assessment, followed by multi-layered provenance research including archival verification and expert consultations. Concurrently, advanced scientific analysis such as isotope testing and material composition scanning is conducted to validate authenticity. The process also involves coordinating with legal teams to ensure compliance with international cultural heritage laws. Final steps include generating detailed authentication reports and secure digital certification before artifact cataloging and auction preparation. This atypical process ensures utmost credibility and compliance in a niche but critical domain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
intake         = Transition(label='Artifact Intake')
cond_check     = Transition(label='Condition Check')
prov_research  = Transition(label='Provenance Research')
archive_verify = Transition(label='Archive Verify')
expert_consult = Transition(label='Expert Consult')
isotope_test   = Transition(label='Isotope Testing')
material_scan  = Transition(label='Material Scan')
legal_review   = Transition(label='Legal Review')
compliance_chk = Transition(label='Compliance Check')
report_draft   = Transition(label='Report Draft')
digital_cert   = Transition(label='Digital Certify')
catalog_entry  = Transition(label='Catalog Entry')
auction_prep   = Transition(label='Auction Prep')
client_notify  = Transition(label='Client Notify')
secure_store   = Transition(label='Secure Storage')

# Create the root partial order
root = StrictPartialOrder(nodes=[
    intake, cond_check, prov_research,
    archive_verify, expert_consult,
    isotope_test, material_scan,
    legal_review, compliance_chk,
    report_draft, digital_cert,
    catalog_entry, auction_prep,
    client_notify, secure_store
])

# Define the control-flow (precedence) relations
# 1. Intake -> Condition Check
root.order.add_edge(intake, cond_check)

# 2. Condition Check branches:
#    a) Provenance Research sequence: ProvRes -> Archive Verify -> Expert Consult
root.order.add_edge(cond_check, prov_research)
root.order.add_edge(prov_research, archive_verify)
root.order.add_edge(archive_verify, expert_consult)

#    b) Scientific analysis sequence: Isotope Testing -> Material Scan
root.order.add_edge(cond_check, isotope_test)
root.order.add_edge(isotope_test, material_scan)

# 3. Merge both branches into Legal Review
root.order.add_edge(expert_consult, legal_review)
root.order.add_edge(material_scan, legal_review)

# 4. Compliance path: Legal Review -> Compliance Check
root.order.add_edge(legal_review, compliance_chk)

# 5. Reporting path: Compliance Check -> Report Draft -> Digital Certify
root.order.add_edge(compliance_chk, report_draft)
root.order.add_edge(report_draft, digital_cert)

# 6. Catalog & auction prep: Digital Certify -> Catalog Entry -> Auction Prep
root.order.add_edge(digital_cert, catalog_entry)
root.order.add_edge(catalog_entry, auction_prep)

# 7. Post-prep concurrent tasks: Auction Prep -> Client Notify & Secure Storage
root.order.add_edge(auction_prep, client_notify)
root.order.add_edge(auction_prep, secure_store)