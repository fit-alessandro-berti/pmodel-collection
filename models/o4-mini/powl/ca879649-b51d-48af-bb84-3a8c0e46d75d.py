# Generated from: ca879649-b51d-48af-bb84-3a8c0e46d75d.json
# Description: This process outlines the complex workflow involved in exporting small-batch artisan cheese from local farms to international gourmet markets. It includes sourcing raw milk, quality testing, aging, packaging in climate-controlled conditions, regulatory compliance with export laws, arranging specialized freight, customs clearance, and final delivery to boutique retailers. Each step requires coordination between farmers, quality experts, logistics providers, and customs agents to maintain product integrity and meet strict food safety standards, ensuring the cheese arrives fresh and meets both domestic and foreign regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
batch_selection    = Transition(label='Batch Selection')
curd_preparation   = Transition(label='Curd Preparation')
pressing_cheese    = Transition(label='Pressing Cheese')
aging_control      = Transition(label='Aging Control')
flavor_profiling   = Transition(label='Flavor Profiling')
packaging_prep     = Transition(label='Packaging Prep')
climate_packing    = Transition(label='Climate Packing')
export_licensing   = Transition(label='Export Licensing')
customs_filing     = Transition(label='Customs Filing')
freight_booking    = Transition(label='Freight Booking')
cold_storage       = Transition(label='Cold Storage')
transport_tracking = Transition(label='Transport Tracking')
retail_delivery    = Transition(label='Retail Delivery')
feedback_collection= Transition(label='Feedback Collection')

# Create the partial‐order workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, batch_selection,
    curd_preparation, pressing_cheese, aging_control,
    flavor_profiling, packaging_prep, climate_packing,
    export_licensing, customs_filing, freight_booking,
    cold_storage, transport_tracking, retail_delivery,
    feedback_collection
])

# Define the control‐flow ordering (concurrent branches for packaging vs. export logistics)
root.order.add_edge(milk_sourcing,      quality_testing)
root.order.add_edge(quality_testing,    batch_selection)
root.order.add_edge(batch_selection,    curd_preparation)
root.order.add_edge(curd_preparation,   pressing_cheese)
root.order.add_edge(pressing_cheese,    aging_control)
root.order.add_edge(aging_control,      flavor_profiling)

# Packaging branch
root.order.add_edge(flavor_profiling,   packaging_prep)
root.order.add_edge(packaging_prep,     climate_packing)
root.order.add_edge(climate_packing,    cold_storage)
root.order.add_edge(cold_storage,       transport_tracking)

# Export‐logistics branch
root.order.add_edge(quality_testing,    export_licensing)
root.order.add_edge(export_licensing,   customs_filing)
root.order.add_edge(customs_filing,     freight_booking)
root.order.add_edge(freight_booking,    transport_tracking)

# Final delivery and feedback
root.order.add_edge(transport_tracking,  retail_delivery)
root.order.add_edge(retail_delivery,    feedback_collection)