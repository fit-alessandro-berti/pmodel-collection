# Generated from: 164e7104-3c3f-44a4-b7e4-038b50f728e1.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese to international markets. It starts with selecting raw milk from carefully chosen farms, followed by specialized fermentation and aging techniques unique to each cheese type. Quality assurance includes microbial testing and sensory evaluation by expert tasters. Once certified organic and authentic, cheeses undergo custom packaging designed to preserve freshness during long transit. Compliance with export regulations and customs documentation is meticulously handled. The process concludes with logistics coordination for cold-chain shipping and final delivery to boutique retailers overseas, ensuring the product arrives in pristine condition and meets all safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Fermentation = Transition(label='Fermentation')
Aging_Check = Transition(label='Aging Check')
Microbial_Test = Transition(label='Microbial Test')
Sensory_Panel = Transition(label='Sensory Panel')
Organic_Cert = Transition(label='Organic Cert')
Packaging_Design = Transition(label='Packaging Design')
Freshness_Seal = Transition(label='Freshness Seal')
Export_License = Transition(label='Export License')
Customs_Prep = Transition(label='Customs Prep')
Shipping_Coord = Transition(label='Shipping Coord')
Cold_Storage = Transition(label='Cold Storage')
Retail_Handoff = Transition(label='Retail Handoff')
Market_Feedback = Transition(label='Market Feedback')
Compliance_Audit = Transition(label='Compliance Audit')
Inventory_Update = Transition(label='Inventory Update')

# Build sub-partials for Quality Assurance step:
# Microbial Test and Sensory Panel can happen concurrently before Organic Cert
quality_assurance = StrictPartialOrder(nodes=[Microbial_Test, Sensory_Panel])
# no order edges between Microbial_Test and Sensory_Panel, so concurrent

# Organic Cert follows after both
quality_seq = StrictPartialOrder(
    nodes=[quality_assurance, Organic_Cert]
)
quality_seq.order.add_edge(quality_assurance, Organic_Cert)

# Packaging sub-step: Packaging Design -> Freshness Seal (sequential)
packaging_seq = StrictPartialOrder(
    nodes=[Packaging_Design, Freshness_Seal]
)
packaging_seq.order.add_edge(Packaging_Design, Freshness_Seal)

# Export compliance: Export License -> Customs Prep (sequential)
export_seq = StrictPartialOrder(
    nodes=[Export_License, Customs_Prep]
)
export_seq.order.add_edge(Export_License, Customs_Prep)

# Shipping sub-step: Shipping Coord -> Cold Storage -> Retail Handoff (sequential)
shipping_seq = StrictPartialOrder(
    nodes=[Shipping_Coord, Cold_Storage, Retail_Handoff]
)
shipping_seq.order.add_edge(Shipping_Coord, Cold_Storage)
shipping_seq.order.add_edge(Cold_Storage, Retail_Handoff)

# Final concurrent nodes: Market Feedback, Compliance Audit, Inventory Update
final_concurrent = StrictPartialOrder(
    nodes=[Market_Feedback, Compliance_Audit, Inventory_Update]
)
# no order edges, fully concurrent

# Assemble the whole process partial order:
nodes = [
    Milk_Sourcing,
    Fermentation,
    Aging_Check,
    quality_seq,
    packaging_seq,
    export_seq,
    shipping_seq,
    final_concurrent
]

root = StrictPartialOrder(nodes=nodes)

# Add ordering edges according to description:

# Milk Sourcing -> Fermentation -> Aging Check
root.order.add_edge(Milk_Sourcing, Fermentation)
root.order.add_edge(Fermentation, Aging_Check)

# Aging Check -> Quality Assurance (Microbial + Sensory + Organic Cert)
root.order.add_edge(Aging_Check, quality_seq)

# Quality Assurance -> Packaging
root.order.add_edge(quality_seq, packaging_seq)

# Packaging -> Export Compliance
root.order.add_edge(packaging_seq, export_seq)

# Export Compliance -> Shipping
root.order.add_edge(export_seq, shipping_seq)

# Shipping -> Final concurrent activities (Market Feedback, Compliance Audit, Inventory Update)
root.order.add_edge(shipping_seq, final_concurrent)