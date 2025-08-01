# Generated from: 164e7104-3c3f-44a4-b7e4-038b50f728e1.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese to international markets. It starts with selecting raw milk from carefully chosen farms, followed by specialized fermentation and aging techniques unique to each cheese type. Quality assurance includes microbial testing and sensory evaluation by expert tasters. Once certified organic and authentic, cheeses undergo custom packaging designed to preserve freshness during long transit. Compliance with export regulations and customs documentation is meticulously handled. The process concludes with logistics coordination for cold-chain shipping and final delivery to boutique retailers overseas, ensuring the product arrives in pristine condition and meets all safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
milk           = Transition(label='Milk Sourcing')
fermentation   = Transition(label='Fermentation')
aging_check    = Transition(label='Aging Check')
microbial_test = Transition(label='Microbial Test')
sensory_panel  = Transition(label='Sensory Panel')
organic_cert   = Transition(label='Organic Cert')
packaging      = Transition(label='Packaging Design')
freshness_seal = Transition(label='Freshness Seal')
export_license = Transition(label='Export License')
customs_prep   = Transition(label='Customs Prep')
shipping_coord = Transition(label='Shipping Coord')
cold_storage   = Transition(label='Cold Storage')
retail_handoff = Transition(label='Retail Handoff')
market_fb      = Transition(label='Market Feedback')
compliance_aud = Transition(label='Compliance Audit')
inventory_upd  = Transition(label='Inventory Update')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    milk,
    fermentation,
    aging_check,
    microbial_test,
    sensory_panel,
    organic_cert,
    packaging,
    freshness_seal,
    export_license,
    customs_prep,
    shipping_coord,
    cold_storage,
    retail_handoff,
    market_fb,
    compliance_aud,
    inventory_upd
])

# Sequencing and concurrency constraints
root.order.add_edge(milk,           fermentation)
root.order.add_edge(fermentation,   aging_check)
# QA steps in parallel
root.order.add_edge(aging_check,    microbial_test)
root.order.add_edge(aging_check,    sensory_panel)
# Both QA must finish before certification
root.order.add_edge(microbial_test, organic_cert)
root.order.add_edge(sensory_panel,  organic_cert)
# Continue linear workflow
root.order.add_edge(organic_cert,   packaging)
root.order.add_edge(packaging,      freshness_seal)
root.order.add_edge(freshness_seal, export_license)
root.order.add_edge(export_license, customs_prep)
root.order.add_edge(customs_prep,   shipping_coord)
root.order.add_edge(shipping_coord, cold_storage)
root.order.add_edge(cold_storage,   retail_handoff)
root.order.add_edge(retail_handoff, market_fb)
root.order.add_edge(market_fb,      compliance_aud)
root.order.add_edge(compliance_aud, inventory_upd)