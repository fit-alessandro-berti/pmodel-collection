# Generated from: a30f5996-101b-423a-a1df-a4db13458fc6.json
# Description: This process involves the end-to-end management of a vertical urban farm's supply chain, integrating hydroponic crop production with automated harvesting, real-time environmental monitoring, dynamic demand forecasting, and direct-to-consumer distribution. It begins with seed selection and nutrient formulation tailored to specific crops and fluctuating urban market trends. Continuous sensor-based climate adjustment ensures optimal growth conditions, while robotic harvesters collect produce with minimal human intervention. Post-harvest, the products undergo automated quality inspection and packaging. Inventory levels are adjusted dynamically based on predictive analytics derived from consumer purchase patterns and urban consumption data. Finally, the system coordinates last-mile delivery using electric vehicles optimized for route efficiency, completing a sustainable and technologically advanced urban agriculture cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select      = Transition(label="Seed Select")
nutrient_mix     = Transition(label="Nutrient Mix")
climate_monitor  = Transition(label="Climate Monitor")
growth_adjust    = Transition(label="Growth Adjust")
pest_detect      = Transition(label="Pest Detect")
harvest_robot    = Transition(label="Harvest Robot")
quality_scan     = Transition(label="Quality Scan")
pack_produce     = Transition(label="Pack Produce")
demand_forecast  = Transition(label="Demand Forecast")
inventory_sync   = Transition(label="Inventory Sync")
order_process    = Transition(label="Order Process")
route_plan       = Transition(label="Route Plan")
vehicle_charge   = Transition(label="Vehicle Charge")
delivery_track   = Transition(label="Delivery Track")
customer_feedback= Transition(label="Customer Feedback")
data_archive     = Transition(label="Data Archive")

# Build the climate‐adjustment loop: monitor → (adjust → pest detect)∗
climate_body = StrictPartialOrder(nodes=[growth_adjust, pest_detect])
climate_body.order.add_edge(growth_adjust, pest_detect)
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_monitor, climate_body])

# Assemble the top‐level workflow
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    climate_loop,
    harvest_robot,
    quality_scan,
    pack_produce,
    demand_forecast,
    inventory_sync,
    order_process,
    route_plan,
    vehicle_charge,
    delivery_track,
    customer_feedback,
    data_archive
])

# Define the control‐flow (partial order) edges
root.order.add_edge(seed_select,       nutrient_mix)
root.order.add_edge(nutrient_mix,      climate_loop)
root.order.add_edge(climate_loop,      harvest_robot)
root.order.add_edge(harvest_robot,     quality_scan)
root.order.add_edge(quality_scan,      pack_produce)
root.order.add_edge(pack_produce,      demand_forecast)
root.order.add_edge(demand_forecast,   inventory_sync)
root.order.add_edge(inventory_sync,    order_process)
root.order.add_edge(order_process,     route_plan)
root.order.add_edge(route_plan,        vehicle_charge)
root.order.add_edge(vehicle_charge,    delivery_track)
root.order.add_edge(delivery_track,    customer_feedback)
root.order.add_edge(customer_feedback, data_archive)