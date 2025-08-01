# Generated from: 1dbe4107-276a-42de-9724-f30b83472625.json
# Description: This process involves a multi-stage verification and validation of rare artifacts submitted by private collectors for authentication and provenance certification. Starting with initial documentation review, the artifact undergoes physical inspection, material analysis, and stylistic comparison with known exemplars. Parallel background checks on ownership history and cross-referencing with global databases are performed to detect forgeries or illegal acquisitions. Expert panels are convened for consensus opinions, followed by risk assessment for market impact. Finally, a digital certificate is issued, embedding blockchain-based authenticity records. This atypical process ensures trust and legal compliance in high-value artifact trading.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
doc_review       = Transition(label='Doc Review')
artifact_scan    = Transition(label='Artifact Scan')
material_test    = Transition(label='Material Test')
style_match      = Transition(label='Style Match')
owner_check      = Transition(label='Owner Check')
database_cross   = Transition(label='Database Cross')
forgery_detect   = Transition(label='Forgery Detect')
legal_verify     = Transition(label='Legal Verify')
expert_panel     = Transition(label='Expert Panel')
consensus_vote   = Transition(label='Consensus Vote')
risk_assess      = Transition(label='Risk Assess')
market_impact    = Transition(label='Market Impact')
cert_generate    = Transition(label='Cert Generate')
blockchain_link  = Transition(label='Blockchain Link')
client_notify    = Transition(label='Client Notify')
archive_store    = Transition(label='Archive Store')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    doc_review,
    artifact_scan,
    material_test,
    style_match,
    owner_check,
    database_cross,
    forgery_detect,
    legal_verify,
    expert_panel,
    consensus_vote,
    risk_assess,
    market_impact,
    cert_generate,
    blockchain_link,
    client_notify,
    archive_store
])

# Sequence: Doc Review → Artifact Scan → Material Test → Style Match
root.order.add_edge(doc_review,    artifact_scan)
root.order.add_edge(artifact_scan, material_test)
root.order.add_edge(material_test, style_match)

# Parallel background checks after style match
root.order.add_edge(style_match, owner_check)
root.order.add_edge(style_match, database_cross)

# Both checks must finish before forgery detection
root.order.add_edge(owner_check,    forgery_detect)
root.order.add_edge(database_cross, forgery_detect)

# Then legal verification, expert panel, consensus, risk & market impact
root.order.add_edge(forgery_detect, legal_verify)
root.order.add_edge(legal_verify,   expert_panel)
root.order.add_edge(expert_panel,   consensus_vote)
root.order.add_edge(consensus_vote, risk_assess)
root.order.add_edge(risk_assess,    market_impact)

# Certificate issuance & blockchain linking
root.order.add_edge(market_impact,  cert_generate)
root.order.add_edge(cert_generate,  blockchain_link)

# Finally, notify client and archive the record in parallel
root.order.add_edge(blockchain_link, client_notify)
root.order.add_edge(blockchain_link, archive_store)