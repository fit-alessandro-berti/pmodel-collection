# Generated from: c8a5d28f-ffc6-4a17-82b2-16abf23b7f08.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese internationally. Starting from raw milk sourcing from specific breeds, it includes quality testing, controlled fermentation, aging under precise conditions, and sensory evaluation. Following production, the process entails obtaining health certifications, custom labeling, cold-chain packaging, and coordinating with logistics partners specialized in perishable goods. Regulatory compliance checks, export documentation, tariff classification, and final customs clearance are integral. Post-shipment tracking and feedback collection from international clients complete this atypical yet realistic export workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
cheese_molding = Transition(label='Cheese Molding')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')

health_certify = Transition(label='Health Certify')
custom_labeling = Transition(label='Custom Labeling')
cold_packaging = Transition(label='Cold Packaging')
logistics_setup = Transition(label='Logistics Setup')

export_docs = Transition(label='Export Docs')
customs_clearance = Transition(label='Customs Clearance')

shipment_track = Transition(label='Shipment Track')
client_feedback = Transition(label='Client Feedback')

# Production partial order:
# Milk Sourcing -> Quality Testing -> Milk Pasteurize -> Culture Addition 
# -> Curd Cutting -> Whey Drain -> Cheese Molding -> Controlled Aging -> Sensory Check

production_nodes = [
    milk_sourcing, quality_testing, milk_pasteurize, culture_addition,
    curd_cutting, whey_drain, cheese_molding, controlled_aging, sensory_check
]
production = StrictPartialOrder(nodes=production_nodes)
production.order.add_edge(milk_sourcing, quality_testing)
production.order.add_edge(quality_testing, milk_pasteurize)
production.order.add_edge(milk_pasteurize, culture_addition)
production.order.add_edge(culture_addition, curd_cutting)
production.order.add_edge(curd_cutting, whey_drain)
production.order.add_edge(whey_drain, cheese_molding)
production.order.add_edge(cheese_molding, controlled_aging)
production.order.add_edge(controlled_aging, sensory_check)

# Packaging partial order:
# Health Certify -> Custom Labeling -> Cold Packaging -> Logistics Setup
packaging_nodes = [health_certify, custom_labeling, cold_packaging, logistics_setup]
packaging = StrictPartialOrder(nodes=packaging_nodes)
packaging.order.add_edge(health_certify, custom_labeling)
packaging.order.add_edge(custom_labeling, cold_packaging)
packaging.order.add_edge(cold_packaging, logistics_setup)

# Export partial order:
# Export Docs -> Customs Clearance
export = StrictPartialOrder(nodes=[export_docs, customs_clearance])
export.order.add_edge(export_docs, customs_clearance)

# Post-shipment partial order:
# Shipment Track -> Client Feedback
post_shipment = StrictPartialOrder(nodes=[shipment_track, client_feedback])
post_shipment.order.add_edge(shipment_track, client_feedback)

# Overall process combines production, packaging, export, post shipment with partial order edges:
# Sensory Check -> Health Certify (packaging cannot start before production done)
# Logistics Setup -> Export Docs (export docs after logistics ready)
# Customs Clearance -> Shipment Track (tracking after clearance)

root = StrictPartialOrder(
    nodes=[production, packaging, export, post_shipment]
)

# Add edges connecting the phases
root.order.add_edge(production, packaging)          # production done before packaging start
root.order.add_edge(packaging, export)              # packaging done before export start
root.order.add_edge(export, post_shipment)          # export done before post-shipment tracking

# The POWL partial order graph implicitly orders the sub-nodes in child StrictPartialOrders