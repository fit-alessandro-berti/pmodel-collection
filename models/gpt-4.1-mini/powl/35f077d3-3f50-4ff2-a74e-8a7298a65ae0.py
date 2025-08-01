# Generated from: 35f077d3-3f50-4ff2-a74e-8a7298a65ae0.json
# Description: This process manages the intricate logistics and legal considerations involved in lending high-value artworks across international borders for exhibitions. It includes authentication, condition reporting, customs clearance, insurance coordination, and installation oversight. The process ensures compliance with cultural heritage laws, coordinates with multiple stakeholders such as museums, insurers, transporters, and customs officials, and manages risk throughout the artwork's journey. Post-exhibition, the process involves de-installation, condition reassessment, and secure return, closing with archival documentation and financial reconciliation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Verify_Artwork = Transition(label='Verify Artwork')
Authenticate_Piece = Transition(label='Authenticate Piece')
Condition_Report = Transition(label='Condition Report')
Insurance_Quote = Transition(label='Insurance Quote')
Contract_Draft = Transition(label='Contract Draft')
Customs_Filing = Transition(label='Customs Filing')
Transport_Booking = Transition(label='Transport Booking')
Packaging_Prep = Transition(label='Packaging Prep')
Secure_Transit = Transition(label='Secure Transit')
Installation_Setup = Transition(label='Installation Setup')
Exhibition_Monitor = Transition(label='Exhibition Monitor')
De_install_Artwork = Transition(label='De-install Artwork')
Return_Transit = Transition(label='Return Transit')
Final_Inspection = Transition(label='Final Inspection')
Archive_Records = Transition(label='Archive Records')

# Build partial orders reflecting the process logic

# Authentication and condition reporting part after verification
auth_and_condition = StrictPartialOrder(nodes=[Authenticate_Piece, Condition_Report])
auth_and_condition.order.add_edge(Authenticate_Piece, Condition_Report)

# Insurance and contract drafting happen after condition report (concurrent with customs filing, transport booking prep)
insurance_and_contract = StrictPartialOrder(nodes=[Insurance_Quote, Contract_Draft])
insurance_and_contract.order.add_edge(Insurance_Quote, Contract_Draft)

# Customs filing and transport booking plus packaging prep proceed concurrently after contract drafting
customs = Customs_Filing
transport_and_packaging = StrictPartialOrder(nodes=[Transport_Booking, Packaging_Prep])

# Secure transit after customs, transport and packaging; these three are concurrent but all must finish before secure transit

# Installation setup and exhibition monitoring happen sequentially after secure transit
installation_and_monitor = StrictPartialOrder(nodes=[Installation_Setup, Exhibition_Monitor])
installation_and_monitor.order.add_edge(Installation_Setup, Exhibition_Monitor)

# Post exhibition: loop of de-install artwork, return transit, final inspection
# We model Post-exhibition loop:
# LOOP body B: de-install artwork, return transit, final inspection (sequential)
# LOOP guard A: Exhibition_Monitor
post_exhibition_work = StrictPartialOrder(nodes=[De_install_Artwork, Return_Transit, Final_Inspection])
post_exhibition_work.order.add_edge(De_install_Artwork, Return_Transit)
post_exhibition_work.order.add_edge(Return_Transit, Final_Inspection)

post_exhibition_loop = OperatorPOWL(operator=Operator.LOOP, children=[Exhibition_Monitor, post_exhibition_work])

# Archive records and financial reconciliation happens after final inspection (so after loop)
# To synchronize with loop: we treat Archive_Records after loop

# Combine secure transit dependencies into a PO
secure_transit_deps = StrictPartialOrder(nodes=[Customs_Filing, Transport_Booking, Packaging_Prep, Secure_Transit])
secure_transit_deps.order.add_edge(Customs_Filing, Secure_Transit)
secure_transit_deps.order.add_edge(Transport_Booking, Secure_Transit)
secure_transit_deps.order.add_edge(Packaging_Prep, Secure_Transit)

# Combine insurance_contract and customs+transport prep concurrently after condition report
# We need to combine insurance_and_contract and secure_transit_deps concurrently, but insurance_and_contract requires condition report,
# so first combine Authenticate->Condition_Report->(insurance+contract || customs+transport+packaging)
after_condition = StrictPartialOrder(
    nodes=[insurance_and_contract, secure_transit_deps]
)
# No order edges between insurance_and_contract and secure_transit_deps to model concurrency

# Main beginning: Verify Artwork -> Authenticate Piece -> Condition Report -> (insurance+contract || customs+transport+packaging) -> Secure Transit -> Installation Setup -> Exhibition Monitor
# We'll combine the beginning part first: Verify Artwork -> Authenticate Piece -> Condition Report

beginning = StrictPartialOrder(nodes=[Verify_Artwork, Authenticate_Piece, Condition_Report])
beginning.order.add_edge(Verify_Artwork, Authenticate_Piece)
beginning.order.add_edge(Authenticate_Piece, Condition_Report)

# Compose the full before secure transit:
before_secure_transit = StrictPartialOrder(
    nodes=[beginning, after_condition]
)
before_secure_transit.order.add_edge(beginning, after_condition)

# Then compose full partial order from the start to installation and exhibition monitor
install_exhibit = StrictPartialOrder(
    nodes=[before_secure_transit, Installation_Setup, post_exhibition_loop, Archive_Records]
)

install_exhibit.order.add_edge(before_secure_transit, Installation_Setup)
install_exhibit.order.add_edge(Installation_Setup, post_exhibition_loop)
install_exhibit.order.add_edge(post_exhibition_loop, Archive_Records)

# Final model:
root = install_exhibit