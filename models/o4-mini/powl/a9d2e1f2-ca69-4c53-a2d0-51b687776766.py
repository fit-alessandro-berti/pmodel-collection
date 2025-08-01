# Generated from: a9d2e1f2-ca69-4c53-a2d0-51b687776766.json
# Description: This process manages the end-to-end supply chain of artisan cheese production, starting from milk sourcing through seasonal farm visits. It includes quality testing at multiple stages, temperature-controlled transport coordination, aging room inventory tracking, and niche market distribution. Unique to this process is the integration of sensory evaluation panels and small batch customization requests, ensuring each cheese batch meets specific flavor profiles. Additionally, the process tracks environmental impact metrics related to pasture grazing and waste recycling, supporting sustainability goals while maintaining artisan authenticity and compliance with regional food regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
farm_inspection  = Transition(label='Farm Inspection')
milk_testing     = Transition(label='Milk Testing')
cheese_making    = Transition(label='Cheese Making')
batch_labeling   = Transition(label='Batch Labeling')
aging_tracking   = Transition(label='Aging Tracking')
sensory_panel    = Transition(label='Sensory Panel')
quality_audit    = Transition(label='Quality Audit')
temp_monitoring  = Transition(label='Temp Monitoring')
inventory_check  = Transition(label='Inventory Check')
waste_sorting    = Transition(label='Waste Sorting')
custom_orders    = Transition(label='Custom Orders')
transport_booking= Transition(label='Transport Booking')
market_delivery  = Transition(label='Market Delivery')
impact_reporting = Transition(label='Impact Reporting')
reg_compliance   = Transition(label='Reg Compliance')

# Silent skip for optional custom orders
skip = SilentTransition()

# Loop for repeated sensory evaluation + audit
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_panel, quality_audit])

# Exclusive choice: either handle a custom order or skip
xor_custom = OperatorPOWL(operator=Operator.XOR, children=[custom_orders, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, farm_inspection, milk_testing, cheese_making, batch_labeling,
    aging_tracking, sensory_loop, inventory_check, waste_sorting, impact_reporting,
    xor_custom, temp_monitoring, transport_booking, market_delivery, reg_compliance
])

# Define the control-flow (partial order edges)
# 1. Core production sequence
root.order.add_edge(milk_sourcing, farm_inspection)
root.order.add_edge(farm_inspection, milk_testing)
root.order.add_edge(milk_testing, cheese_making)
root.order.add_edge(cheese_making, batch_labeling)
root.order.add_edge(batch_labeling, aging_tracking)

# 2. After aging, spawn sensory loop and environmental tasks in parallel
root.order.add_edge(aging_tracking, sensory_loop)
root.order.add_edge(aging_tracking, inventory_check)
root.order.add_edge(aging_tracking, waste_sorting)
root.order.add_edge(aging_tracking, impact_reporting)

# 3. Join all branches into the custom‐order choice
root.order.add_edge(sensory_loop, xor_custom)
root.order.add_edge(inventory_check, xor_custom)
root.order.add_edge(waste_sorting, xor_custom)
root.order.add_edge(impact_reporting, xor_custom)

# 4. Shipping and final compliance
root.order.add_edge(xor_custom, temp_monitoring)
root.order.add_edge(temp_monitoring, transport_booking)
root.order.add_edge(transport_booking, market_delivery)
root.order.add_edge(market_delivery, reg_compliance)