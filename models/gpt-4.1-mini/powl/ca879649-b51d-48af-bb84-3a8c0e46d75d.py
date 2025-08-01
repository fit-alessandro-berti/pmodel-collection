# Generated from: ca879649-b51d-48af-bb84-3a8c0e46d75d.json
# Description: This process outlines the complex workflow involved in exporting small-batch artisan cheese from local farms to international gourmet markets. It includes sourcing raw milk, quality testing, aging, packaging in climate-controlled conditions, regulatory compliance with export laws, arranging specialized freight, customs clearance, and final delivery to boutique retailers. Each step requires coordination between farmers, quality experts, logistics providers, and customs agents to maintain product integrity and meet strict food safety standards, ensuring the cheese arrives fresh and meets both domestic and foreign regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as labeled transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Batch_Selection = Transition(label='Batch Selection')
Curd_Preparation = Transition(label='Curd Preparation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Prep = Transition(label='Packaging Prep')
Climate_Packing = Transition(label='Climate Packing')
Export_Licensing = Transition(label='Export Licensing')
Customs_Filing = Transition(label='Customs Filing')
Freight_Booking = Transition(label='Freight Booking')
Cold_Storage = Transition(label='Cold Storage')
Transport_Tracking = Transition(label='Transport Tracking')
Retail_Delivery = Transition(label='Retail Delivery')
Feedback_Collection = Transition(label='Feedback Collection')

# Build partial orders to reflect the described dependencies

# Initial sourcing and testing chain
sourcing_testing = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Batch_Selection])
sourcing_testing.order.add_edge(Milk_Sourcing, Quality_Testing)
sourcing_testing.order.add_edge(Quality_Testing, Batch_Selection)

# Cheese preparation and aging chain
preparation_aging = StrictPartialOrder(nodes=[
    Curd_Preparation,
    Pressing_Cheese,
    Aging_Control,
    Flavor_Profiling
])
preparation_aging.order.add_edge(Curd_Preparation, Pressing_Cheese)
preparation_aging.order.add_edge(Pressing_Cheese, Aging_Control)
preparation_aging.order.add_edge(Aging_Control, Flavor_Profiling)

# Packaging chain must follow flavor profiling
packaging = StrictPartialOrder(nodes=[Packaging_Prep, Climate_Packing])
packaging.order.add_edge(Packaging_Prep, Climate_Packing)

# Regulatory and logistics partial order:
regulatory_logistics = StrictPartialOrder(nodes=[
    Export_Licensing,
    Freight_Booking,
    Customs_Filing,
])
# Export Licensing precedes both Freight Booking and Customs Filing
regulatory_logistics.order.add_edge(Export_Licensing, Freight_Booking)
regulatory_logistics.order.add_edge(Export_Licensing, Customs_Filing)

# Cold storage and transport tracking after packaging and freight booking
storage_transport = StrictPartialOrder(nodes=[Cold_Storage, Transport_Tracking])
storage_transport.order.add_edge(Cold_Storage, Transport_Tracking)

# Final delivery and feedback collection chain
final_delivery = StrictPartialOrder(nodes=[Retail_Delivery, Feedback_Collection])
final_delivery.order.add_edge(Retail_Delivery, Feedback_Collection)

# Combine packaging and regulatory_logistics concurrency (must both be after flavor profiling)
packaging_and_regulatory = StrictPartialOrder(nodes=[packaging, regulatory_logistics])
# Since packaging and regulatory_logistics are separate branches concurrent after flavor profiling,
# no edges between them

# Chain: flavor profiling -> packaging and regulatory
flavor_to_packreg = StrictPartialOrder(nodes=[Flavor_Profiling, packaging_and_regulatory])
flavor_to_packreg.order.add_edge(Flavor_Profiling, packaging_and_regulatory)

# Chain: packaging_and_regulatory -> cold storage and transport tracking
packreg_to_storage_transport = StrictPartialOrder(nodes=[packaging_and_regulatory, storage_transport])
packreg_to_storage_transport.order.add_edge(packaging_and_regulatory, storage_transport)

# Chain: storage_transport -> final delivery
storage_to_final = StrictPartialOrder(nodes=[storage_transport, final_delivery])
storage_to_final.order.add_edge(storage_transport, final_delivery)

# Chain: sourcing_testing -> preparation_aging
source_to_prepare = StrictPartialOrder(nodes=[sourcing_testing, preparation_aging])
source_to_prepare.order.add_edge(sourcing_testing, preparation_aging)

# Combine all into root partial order:
root = StrictPartialOrder(nodes=[
    source_to_prepare,
    flavor_to_packreg,
    packreg_to_storage_transport,
    storage_to_final
])

# Add edges forming the sequence of major phases:
root.order.add_edge(source_to_prepare, flavor_to_packreg)
root.order.add_edge(flavor_to_packreg, packreg_to_storage_transport)
root.order.add_edge(packreg_to_storage_transport, storage_to_final)