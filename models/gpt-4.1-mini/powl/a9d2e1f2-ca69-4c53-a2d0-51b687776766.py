# Generated from: a9d2e1f2-ca69-4c53-a2d0-51b687776766.json
# Description: This process manages the end-to-end supply chain of artisan cheese production, starting from milk sourcing through seasonal farm visits. It includes quality testing at multiple stages, temperature-controlled transport coordination, aging room inventory tracking, and niche market distribution. Unique to this process is the integration of sensory evaluation panels and small batch customization requests, ensuring each cheese batch meets specific flavor profiles. Additionally, the process tracks environmental impact metrics related to pasture grazing and waste recycling, supporting sustainability goals while maintaining artisan authenticity and compliance with regional food regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Inspection = Transition(label='Farm Inspection')
Milk_Testing = Transition(label='Milk Testing')
Cheese_Making = Transition(label='Cheese Making')
Batch_Labeling = Transition(label='Batch Labeling')
Aging_Tracking = Transition(label='Aging Tracking')
Sensory_Panel = Transition(label='Sensory Panel')
Quality_Audit = Transition(label='Quality Audit')
Temp_Monitoring = Transition(label='Temp Monitoring')
Inventory_Check = Transition(label='Inventory Check')
Waste_Sorting = Transition(label='Waste Sorting')
Custom_Orders = Transition(label='Custom Orders')
Transport_Booking = Transition(label='Transport Booking')
Market_Delivery = Transition(label='Market Delivery')
Impact_Reporting = Transition(label='Impact Reporting')
Reg_Compliance = Transition(label='Reg Compliance')

# Build POWL structure step by step, reflecting the description

# 1. Milk sourcing and farm inspection (sequential)
sourcing_process = StrictPartialOrder(nodes=[Milk_Sourcing, Farm_Inspection])
sourcing_process.order.add_edge(Milk_Sourcing, Farm_Inspection)

# 2. Milk testing after farm inspection
milk_test_process = StrictPartialOrder(nodes=[Farm_Inspection, Milk_Testing])
milk_test_process.order.add_edge(Farm_Inspection, Milk_Testing)

# 3. Cheese making after milk testing
cheese_making_proc = StrictPartialOrder(nodes=[Milk_Testing, Cheese_Making])
cheese_making_proc.order.add_edge(Milk_Testing, Cheese_Making)

# 4. Batch Labeling after cheese making
labeling_proc = StrictPartialOrder(nodes=[Cheese_Making, Batch_Labeling])
labeling_proc.order.add_edge(Cheese_Making, Batch_Labeling)

# 5. Aging tracking after batch labeling
aging_proc = StrictPartialOrder(nodes=[Batch_Labeling, Aging_Tracking])
aging_proc.order.add_edge(Batch_Labeling, Aging_Tracking)

# 6. Sensory Panel and Quality Audit are parallel after aging tracking
quality_check = StrictPartialOrder(nodes=[Aging_Tracking, Sensory_Panel, Quality_Audit])
quality_check.order.add_edge(Aging_Tracking, Sensory_Panel)
quality_check.order.add_edge(Aging_Tracking, Quality_Audit)

# 7. Temperature monitoring and inventory check run concurrently after quality checks
temp_inventory = StrictPartialOrder(nodes=[Sensory_Panel, Quality_Audit, Temp_Monitoring, Inventory_Check])
temp_inventory.order.add_edge(Sensory_Panel, Temp_Monitoring)
temp_inventory.order.add_edge(Quality_Audit, Inventory_Check)

# 8. Waste sorting and custom orders happen concurrently after temp & inventory monitoring
# So Waste Sorting depends on Temp Monitoring,
# Custom Orders depends on Inventory Check,
# Waste Sorting and Custom Orders are concurrent
waste_custom = StrictPartialOrder(nodes=[Temp_Monitoring, Inventory_Check, Waste_Sorting, Custom_Orders])
waste_custom.order.add_edge(Temp_Monitoring, Waste_Sorting)
waste_custom.order.add_edge(Inventory_Check, Custom_Orders)

# 9. Transport booking after waste sorting and custom orders
transport_proc = StrictPartialOrder(nodes=[Waste_Sorting, Custom_Orders, Transport_Booking])
transport_proc.order.add_edge(Waste_Sorting, Transport_Booking)
transport_proc.order.add_edge(Custom_Orders, Transport_Booking)

# 10. Market delivery and impact reporting happen concurrently after transport booking
market_impact = StrictPartialOrder(nodes=[Transport_Booking, Market_Delivery, Impact_Reporting])
market_impact.order.add_edge(Transport_Booking, Market_Delivery)
market_impact.order.add_edge(Transport_Booking, Impact_Reporting)

# 11. Regulatory compliance after market delivery and impact reporting
reg_compliance_proc = StrictPartialOrder(nodes=[Market_Delivery, Impact_Reporting, Reg_Compliance])
reg_compliance_proc.order.add_edge(Market_Delivery, Reg_Compliance)
reg_compliance_proc.order.add_edge(Impact_Reporting, Reg_Compliance)

# Now combine all partial orders in sequence respecting their causal dependencies
# We chain the main phases by edges between the last nodes of one PO to the first nodes of the next PO

# But to do so, we need to understand the overall sequence:
# sourcing_process -> milk_test_process -> cheese_making_proc -> labeling_proc -> aging_proc -> quality_check -> temp_inventory -> waste_custom -> transport_proc -> market_impact -> reg_compliance_proc

# We create a big StrictPartialOrder, whose nodes are these composed POWL models and all atomic activities used above,
# but for clarity, we compose them hierarchically.

# Instead, we create nested StrictPartialOrders chaining them.

# Chain 1: sourcing_process -> milk_test_process (note Farm Inspection in common, so chain ordering the main nodes)
seq1 = StrictPartialOrder(
    nodes=[
        sourcing_process,
        Milk_Testing
    ])
seq1.order.add_edge(sourcing_process, Milk_Testing)

# Chain 2: Cheese making after Milk testing
seq2 = StrictPartialOrder(
    nodes=[seq1, Cheese_Making])
seq2.order.add_edge(seq1, Cheese_Making)

# Chain 3: Batch labeling after cheese making
seq3 = StrictPartialOrder(
    nodes=[seq2, Batch_Labeling])
seq3.order.add_edge(seq2, Batch_Labeling)

# Chain 4: Aging tracking after batch labeling
seq4 = StrictPartialOrder(
    nodes=[seq3, Aging_Tracking])
seq4.order.add_edge(seq3, Aging_Tracking)

# Chain 5: Include quality_check (Sensory Panel, Quality Audit) after aging tracking
seq5 = StrictPartialOrder(
    nodes=[seq4, quality_check])
seq5.order.add_edge(seq4, quality_check)

# Chain 6: temp_inventory after quality_check
seq6 = StrictPartialOrder(
    nodes=[seq5, temp_inventory])
seq6.order.add_edge(seq5, temp_inventory)

# Chain 7: waste_custom after temp_inventory
seq7 = StrictPartialOrder(
    nodes=[seq6, waste_custom])
seq7.order.add_edge(seq6, waste_custom)

# Chain 8: transport_proc after waste_custom
seq8 = StrictPartialOrder(
    nodes=[seq7, transport_proc])
seq8.order.add_edge(seq7, transport_proc)

# Chain 9: market_impact after transport_proc
seq9 = StrictPartialOrder(
    nodes=[seq8, market_impact])
seq9.order.add_edge(seq8, market_impact)

# Chain 10: reg_compliance_proc after market_impact
root = StrictPartialOrder(
    nodes=[seq9, reg_compliance_proc])
root.order.add_edge(seq9, reg_compliance_proc)

# Because we have many nested StrictPartialOrders, we can simplify by flattening the process:
# Or instead of nesting partial orders deeply, just create one big StrictPartialOrder with all nodes and edges.

# Alternative flattened approach:

# Collect all activities
all_activities = [
    Milk_Sourcing, Farm_Inspection, Milk_Testing, Cheese_Making, Batch_Labeling,
    Aging_Tracking, Sensory_Panel, Quality_Audit, Temp_Monitoring, Inventory_Check,
    Waste_Sorting, Custom_Orders, Transport_Booking, Market_Delivery,
    Impact_Reporting, Reg_Compliance
]

root = StrictPartialOrder(nodes=all_activities)

# Add edges representing causal dependencies according to the description

# 1 -> 2 -> 3 -> 4 -> 5
root.order.add_edge(Milk_Sourcing, Farm_Inspection)
root.order.add_edge(Farm_Inspection, Milk_Testing)
root.order.add_edge(Milk_Testing, Cheese_Making)
root.order.add_edge(Cheese_Making, Batch_Labeling)
root.order.add_edge(Batch_Labeling, Aging_Tracking)

# Aging tracking -> Sensory Panel and Quality Audit (parallel)
root.order.add_edge(Aging_Tracking, Sensory_Panel)
root.order.add_edge(Aging_Tracking, Quality_Audit)

# Sensory panel -> Temp Monitoring
root.order.add_edge(Sensory_Panel, Temp_Monitoring)

# Quality Audit -> Inventory Check
root.order.add_edge(Quality_Audit, Inventory_Check)

# Temp Monitoring -> Waste Sorting
root.order.add_edge(Temp_Monitoring, Waste_Sorting)

# Inventory Check -> Custom Orders
root.order.add_edge(Inventory_Check, Custom_Orders)

# Waste Sorting & Custom Orders are concurrent, both lead to Transport Booking
root.order.add_edge(Waste_Sorting, Transport_Booking)
root.order.add_edge(Custom_Orders, Transport_Booking)

# Transport Booking -> Market Delivery & Impact Reporting (concurrent)
root.order.add_edge(Transport_Booking, Market_Delivery)
root.order.add_edge(Transport_Booking, Impact_Reporting)

# Market Delivery & Impact Reporting -> Reg Compliance
root.order.add_edge(Market_Delivery, Reg_Compliance)
root.order.add_edge(Impact_Reporting, Reg_Compliance)