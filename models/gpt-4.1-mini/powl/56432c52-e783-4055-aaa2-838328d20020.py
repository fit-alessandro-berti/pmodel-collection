# Generated from: 56432c52-e783-4055-aaa2-838328d20020.json
# Description: This process involves sourcing rare milk varieties from remote farms, conducting quality certification through microbiological testing, and aging cheese in controlled cave environments. Packaging requires custom humidity-controlled containers before coordinating multi-modal transport logistics including refrigerated sea freight. Customs clearance demands specialized documentation due to dairy export restrictions. The final step includes retailer training on product handling and shelf-life optimization to ensure premium quality upon delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Batch_Blending = Transition(label='Batch Blending')
Culture_Inoculation = Transition(label='Culture Inoculation')
Cave_Aging = Transition(label='Cave Aging')
Humidity_Control = Transition(label='Humidity Control')
Packaging_Prep = Transition(label='Packaging Prep')
Container_Sealing = Transition(label='Container Sealing')
Logistics_Planning = Transition(label='Logistics Planning')
Freight_Booking = Transition(label='Freight Booking')
Customs_Filing = Transition(label='Customs Filing')
Documentation = Transition(label='Documentation')
Retailer_Training = Transition(label='Retailer Training')
Shelf_Life_Audit = Transition(label='Shelf-Life Audit')
Customer_Feedback = Transition(label='Customer Feedback')

# Partial order modeling the main sourcing and preparation phase
source_quality = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Batch_Blending, Culture_Inoculation])
source_quality.order.add_edge(Milk_Sourcing, Quality_Testing)
source_quality.order.add_edge(Quality_Testing, Batch_Blending)
source_quality.order.add_edge(Batch_Blending, Culture_Inoculation)

# Partial order modeling aging
aging = StrictPartialOrder(nodes=[Culture_Inoculation, Cave_Aging])
aging.order.add_edge(Culture_Inoculation, Cave_Aging)

# Partial order for packaging preparation
packaging_prep = StrictPartialOrder(nodes=[Humidity_Control, Packaging_Prep, Container_Sealing])
packaging_prep.order.add_edge(Humidity_Control, Packaging_Prep)
packaging_prep.order.add_edge(Packaging_Prep, Container_Sealing)

# Partial order for logistics
logistics = StrictPartialOrder(nodes=[Logistics_Planning, Freight_Booking])
logistics.order.add_edge(Logistics_Planning, Freight_Booking)

# Partial order for customs clearance
customs = StrictPartialOrder(nodes=[Customs_Filing, Documentation])
customs.order.add_edge(Customs_Filing, Documentation)

# Partial order for final training and audit
final_steps = StrictPartialOrder(nodes=[Retailer_Training, Shelf_Life_Audit, Customer_Feedback])
final_steps.order.add_edge(Retailer_Training, Shelf_Life_Audit)
final_steps.order.add_edge(Shelf_Life_Audit, Customer_Feedback)

# Combine logistics and customs clearance concurrently
logistics_customs = StrictPartialOrder(nodes=[logistics, customs])
# No order edges => concurrent

# Combine packaging prep with logistics and customs (packaging before logistics and customs)
pack_and_ship = StrictPartialOrder(nodes=[packaging_prep, logistics_customs])
pack_and_ship.order.add_edge(packaging_prep, logistics_customs)

# Combine aging and packaging/shipping (aging before packaging/shipping)
aging_pack_ship = StrictPartialOrder(nodes=[aging, pack_and_ship])
aging_pack_ship.order.add_edge(aging, pack_and_ship)

# Combine source-quality phase with aging-packaging-shipping (source-quality before aging)
root = StrictPartialOrder(nodes=[source_quality, aging_pack_ship, final_steps])
root.order.add_edge(source_quality, aging_pack_ship)
root.order.add_edge(aging_pack_ship, final_steps)