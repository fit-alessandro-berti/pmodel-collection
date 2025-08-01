# Generated from: 2fc8bff0-0554-4024-8681-5983899c402a.json
# Description: This process outlines the complex operations involved in managing an urban vertical farm, integrating advanced hydroponics, AI-driven environmental controls, and community engagement. Activities include seed selection based on seasonal data, nutrient formula adjustments, automated lighting calibration, pest monitoring through drone surveillance, real-time growth analytics, waste recycling, and crop harvesting. Post-harvest steps involve quality grading, packaging with sustainable materials, distribution logistics tailored to minimize carbon footprint, and feedback collection from local customers. The cycle emphasizes sustainability, technology integration, and urban food security, requiring coordination between agronomists, engineers, and marketing teams to optimize yield and community impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Calibrate = Transition(label='Water Calibrate')
Light_Adjust = Transition(label='Light Adjust')
Drone_Scan = Transition(label='Drone Scan')
Pest_Detect = Transition(label='Pest Detect')
Growth_Track = Transition(label='Growth Track')
Waste_Process = Transition(label='Waste Process')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Grade = Transition(label='Quality Grade')
Package_Goods = Transition(label='Package Goods')
Route_Plan = Transition(label='Route Plan')
Delivery_Dispatch = Transition(label='Delivery Dispatch')
Customer_Survey = Transition(label='Customer Survey')
Feedback_Analyze = Transition(label='Feedback Analyze')
System_Update = Transition(label='System Update')

# Front-end planting and preparation partial order
prep_po = StrictPartialOrder(
    nodes=[Seed_Select, Nutrient_Mix, Water_Calibrate, Light_Adjust]
)
prep_po.order.add_edge(Seed_Select, Nutrient_Mix)
prep_po.order.add_edge(Nutrient_Mix, Water_Calibrate)
prep_po.order.add_edge(Water_Calibrate, Light_Adjust)

# Monitoring partial order (can proceed concurrently after prep)
monitoring_po = StrictPartialOrder(
    nodes=[Drone_Scan, Pest_Detect, Growth_Track]
)
# No order between Drone Scan, Pest Detect, Growth Track (concurrent)

# Waste process after or during monitoring to allow concurrency
waste_after_monitoring_po = StrictPartialOrder(
    nodes=[monitoring_po, Waste_Process]
)
# Let Waste_Process be concurrent, so no edges from monitoring to Waste_Process

# Harvesting partial order
harvest_po = StrictPartialOrder(
    nodes=[Harvest_Crop, Quality_Grade, Package_Goods]
)
harvest_po.order.add_edge(Harvest_Crop, Quality_Grade)
harvest_po.order.add_edge(Quality_Grade, Package_Goods)

# Delivery partial order
delivery_po = StrictPartialOrder(
    nodes=[Route_Plan, Delivery_Dispatch]
)
delivery_po.order.add_edge(Route_Plan, Delivery_Dispatch)

# Post-delivery feedback partial order (sequential)
feedback_po = StrictPartialOrder(
    nodes=[Customer_Survey, Feedback_Analyze]
)
feedback_po.order.add_edge(Customer_Survey, Feedback_Analyze)

# System update activity after feedback analyze
sys_update_po = StrictPartialOrder(
    nodes=[System_Update]
)

# Compose two concurrent partial orders: 
# (prep -> monitoring + waste) and (harvest -> delivery -> feedback -> sys_update)

# Compose monitoring + waste as one PO with concurrency
monitoring_waste_po = StrictPartialOrder(
    nodes=[monitoring_po, Waste_Process]
)
# No edges between monitoring_po and Waste_Process (concurrent)

# Compose preparation PO before monitoring+waste
prep_to_monitoring_waste_po = StrictPartialOrder(
    nodes=[prep_po, monitoring_waste_po]
)
prep_to_monitoring_waste_po.order.add_edge(prep_po, monitoring_waste_po)

# Compose harvest -> delivery
harvest_delivery_po = StrictPartialOrder(
    nodes=[harvest_po, delivery_po]
)
harvest_delivery_po.order.add_edge(harvest_po, delivery_po)

# Compose harvest_delivery -> feedback_po
harvest_delivery_feedback_po = StrictPartialOrder(
    nodes=[harvest_delivery_po, feedback_po]
)
harvest_delivery_feedback_po.order.add_edge(harvest_delivery_po, feedback_po)

# Compose entire post-harvest chain including system update
post_harvest_po = StrictPartialOrder(
    nodes=[harvest_delivery_feedback_po, sys_update_po]
)
post_harvest_po.order.add_edge(harvest_delivery_feedback_po, sys_update_po)

# Finally, the entire process:
# prep_to_monitoring_waste_po --> Harvest crop chain (post_harvest_po)

root = StrictPartialOrder(
    nodes=[prep_to_monitoring_waste_po, post_harvest_po]
)
root.order.add_edge(prep_to_monitoring_waste_po, post_harvest_po)