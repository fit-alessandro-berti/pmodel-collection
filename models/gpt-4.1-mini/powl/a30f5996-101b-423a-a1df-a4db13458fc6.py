# Generated from: a30f5996-101b-423a-a1df-a4db13458fc6.json
# Description: This process involves the end-to-end management of a vertical urban farm's supply chain, integrating hydroponic crop production with automated harvesting, real-time environmental monitoring, dynamic demand forecasting, and direct-to-consumer distribution. It begins with seed selection and nutrient formulation tailored to specific crops and fluctuating urban market trends. Continuous sensor-based climate adjustment ensures optimal growth conditions, while robotic harvesters collect produce with minimal human intervention. Post-harvest, the products undergo automated quality inspection and packaging. Inventory levels are adjusted dynamically based on predictive analytics derived from consumer purchase patterns and urban consumption data. Finally, the system coordinates last-mile delivery using electric vehicles optimized for route efficiency, completing a sustainable and technologically advanced urban agriculture cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Monitor = Transition(label='Climate Monitor')
Growth_Adjust = Transition(label='Growth Adjust')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Robot = Transition(label='Harvest Robot')
Quality_Scan = Transition(label='Quality Scan')
Pack_Produce = Transition(label='Pack Produce')
Inventory_Sync = Transition(label='Inventory Sync')
Demand_Forecast = Transition(label='Demand Forecast')
Order_Process = Transition(label='Order Process')
Route_Plan = Transition(label='Route Plan')
Vehicle_Charge = Transition(label='Vehicle Charge')
Delivery_Track = Transition(label='Delivery Track')
Customer_Feedback = Transition(label='Customer Feedback')
Data_Archive = Transition(label='Data Archive')

# Part 1: Seed Select --> Nutrient Mix (tailoring to crop and market trends)
seed_nutrient = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix])
seed_nutrient.order.add_edge(Seed_Select, Nutrient_Mix)

# Part 2: Climate monitor and growth adjust run continuously and concurrently after Nutrient Mix
# But Growth Adjust depends on Climate Monitor (sensor-based adjustments)
climate_growth = StrictPartialOrder(nodes=[Climate_Monitor, Growth_Adjust])
climate_growth.order.add_edge(Climate_Monitor, Growth_Adjust)

# Pest Detect can happen concurrently with Climate Monitor & Growth Adjust
# So combine as parallel nodes: climate_growth PO + Pest_Detect
# We'll do a partial order with nodes = climate_growth nodes + Pest_Detect, 
# with edges from climate_growth; Pest_Detect unconnected -> concurrent
environment_monitoring_nodes = [Climate_Monitor, Growth_Adjust, Pest_Detect]
environment_monitoring = StrictPartialOrder(nodes=environment_monitoring_nodes)
environment_monitoring.order.add_edge(Climate_Monitor, Growth_Adjust)

# Part 3: Harvest Robot after environmental adjustments and pest detect
# So Harvest Robot depends on Growth Adjust and Pest Detect (both must be done)
harvest_prep = StrictPartialOrder(nodes=[Growth_Adjust, Pest_Detect, Harvest_Robot])
harvest_prep.order.add_edge(Growth_Adjust, Harvest_Robot)
harvest_prep.order.add_edge(Pest_Detect, Harvest_Robot)

# Part 4: Post harvest: Quality Scan --> Pack Produce
quality_pack = StrictPartialOrder(nodes=[Quality_Scan, Pack_Produce])
quality_pack.order.add_edge(Quality_Scan, Pack_Produce)

# Part 5: Inventory Sync after packaging
# Inventory Sync depends on Pack Produce and also on Demand Forecast
# Demand Forecast depends on Data Archive (using consumer purchase and urban data)
demand_forecast_order = StrictPartialOrder(nodes=[Data_Archive, Demand_Forecast])
demand_forecast_order.order.add_edge(Data_Archive, Demand_Forecast)

# Inventory Sync after Demand Forecast and Pack Produce
inventory_sync_order = StrictPartialOrder(nodes=[Demand_Forecast, Pack_Produce, Inventory_Sync])
inventory_sync_order.order.add_edge(Demand_Forecast, Inventory_Sync)
inventory_sync_order.order.add_edge(Pack_Produce, Inventory_Sync)

# Part 6: Order Process after Inventory Sync
order_process = StrictPartialOrder(nodes=[Inventory_Sync, Order_Process])
order_process.order.add_edge(Inventory_Sync, Order_Process)

# Part 7: Last-mile delivery chain:
# Route Plan --> Vehicle Charge --> Delivery Track
route_charge_delivery = StrictPartialOrder(nodes=[Route_Plan, Vehicle_Charge, Delivery_Track])
route_charge_delivery.order.add_edge(Route_Plan, Vehicle_Charge)
route_charge_delivery.order.add_edge(Vehicle_Charge, Delivery_Track)

# Part 8: Customer Feedback and Data Archive happen concurrently after Delivery Track and Order Process
# Customer Feedback depends on delivery completion (Delivery Track)
# Data Archive also depends on feedback (or finished cycle)
feedback_archive = StrictPartialOrder(nodes=[Delivery_Track, Order_Process, Customer_Feedback, Data_Archive])
feedback_archive.order.add_edge(Delivery_Track, Customer_Feedback)
feedback_archive.order.add_edge(Order_Process, Data_Archive)

# Compose the overall order
# Start: seed_nutrient, then environment_monitoring (climate_growth+Pest Detect),
# then harvest_prep,
# then quality_pack,
# then inventory_sync_order,
# then order_process,
# then route_charge_delivery,
# then feedback_archive

nodes = [
    seed_nutrient,
    environment_monitoring,
    harvest_prep,
    quality_pack,
    inventory_sync_order,
    order_process,
    route_charge_delivery,
    feedback_archive,
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(seed_nutrient, environment_monitoring)
root.order.add_edge(environment_monitoring, harvest_prep)
root.order.add_edge(harvest_prep, quality_pack)
root.order.add_edge(quality_pack, inventory_sync_order)
root.order.add_edge(inventory_sync_order, order_process)
root.order.add_edge(order_process, route_charge_delivery)
root.order.add_edge(route_charge_delivery, feedback_archive)