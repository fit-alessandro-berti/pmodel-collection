# Generated from: 35f077d3-3f50-4ff2-a74e-8a7298a65ae0.json
# Description: This process manages the intricate logistics and legal considerations involved in lending high-value artworks across international borders for exhibitions. It includes authentication, condition reporting, customs clearance, insurance coordination, and installation oversight. The process ensures compliance with cultural heritage laws, coordinates with multiple stakeholders such as museums, insurers, transporters, and customs officials, and manages risk throughout the artwork's journey. Post-exhibition, the process involves de-installation, condition reassessment, and secure return, closing with archival documentation and financial reconciliation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities as POWL transitions
verify_artwork      = Transition(label='Verify Artwork')
authenticate_piece  = Transition(label='Authenticate Piece')
condition_report    = Transition(label='Condition Report')
insurance_quote     = Transition(label='Insurance Quote')
contract_draft      = Transition(label='Contract Draft')
customs_filing      = Transition(label='Customs Filing')
transport_booking   = Transition(label='Transport Booking')
packaging_prep      = Transition(label='Packaging Prep')
secure_transit      = Transition(label='Secure Transit')
installation_setup  = Transition(label='Installation Setup')
exhibition_monitor  = Transition(label='Exhibition Monitor')
deinstall_artwork   = Transition(label='De-install Artwork')
final_inspection    = Transition(label='Final Inspection')
return_transit      = Transition(label='Return Transit')
archive_records     = Transition(label='Archive Records')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    verify_artwork,
    authenticate_piece,
    condition_report,
    insurance_quote,
    contract_draft,
    customs_filing,
    transport_booking,
    packaging_prep,
    secure_transit,
    installation_setup,
    exhibition_monitor,
    deinstall_artwork,
    final_inspection,
    return_transit,
    archive_records
])

# Define the control‐flow dependencies
# Initial preparation
root.order.add_edge(verify_artwork, authenticate_piece)
root.order.add_edge(authenticate_piece, condition_report)

# Parallel legal and insurance tasks after condition report
root.order.add_edge(condition_report, insurance_quote)
root.order.add_edge(condition_report, contract_draft)
# Both must complete before customs filing
root.order.add_edge(insurance_quote, customs_filing)
root.order.add_edge(contract_draft, customs_filing)

# Logistics and transport
root.order.add_edge(customs_filing, transport_booking)
root.order.add_edge(transport_booking, packaging_prep)
root.order.add_edge(packaging_prep, secure_transit)

# Installation and exhibition
root.order.add_edge(secure_transit, installation_setup)
root.order.add_edge(installation_setup, exhibition_monitor)

# Post‐exhibition teardown and return
root.order.add_edge(exhibition_monitor, deinstall_artwork)
root.order.add_edge(deinstall_artwork, final_inspection)
root.order.add_edge(final_inspection, return_transit)
root.order.add_edge(return_transit, archive_records)