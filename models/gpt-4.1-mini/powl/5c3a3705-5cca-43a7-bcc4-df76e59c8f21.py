# Generated from: 5c3a3705-5cca-43a7-bcc4-df76e59c8f21.json
# Description: This process outlines the end-to-end supply chain management for an urban vertical farming operation that integrates local produce cultivation with smart logistics and sustainability practices. Starting with seed procurement, it includes controlled environment monitoring, nutrient blending, crop growth tracking, automated harvesting, quality inspection, packaging customization, cold chain management, dynamic route planning for delivery via electric vehicles, real-time inventory updates, consumer feedback integration, waste recycling, and data analytics for yield optimization. The process ensures fresh, eco-friendly produce reaches urban consumers efficiently, minimizing carbon footprint while maintaining product freshness and maximizing resource utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Activities as transitions
Seed_Sourcing = Transition(label='Seed Sourcing')
Env_Monitoring = Transition(label='Env Monitoring')
Nutrient_Blend = Transition(label='Nutrient Blend')
Crop_Tracking = Transition(label='Crop Tracking')
Automated_Harvest = Transition(label='Automated Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Pack_Customize = Transition(label='Pack Customize')
Cold_Storage = Transition(label='Cold Storage')
Route_Planning = Transition(label='Route Planning')
EV_Dispatch = Transition(label='EV Dispatch')
Inventory_Update = Transition(label='Inventory Update')
Customer_Feedback = Transition(label='Customer Feedback')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analytics = Transition(label='Data Analytics')
Yield_Optimize = Transition(label='Yield Optimize')

# Construct PO with sequential order reflecting the described supply chain flow
root = StrictPartialOrder(
    nodes = [
        Seed_Sourcing,
        Env_Monitoring,
        Nutrient_Blend,
        Crop_Tracking,
        Automated_Harvest,
        Quality_Inspect,
        Pack_Customize,
        Cold_Storage,
        Route_Planning,
        EV_Dispatch,
        Inventory_Update,
        Customer_Feedback,
        Waste_Recycle,
        Data_Analytics,
        Yield_Optimize
    ]
)

# Define the partial order edges (sequential from start to end)
root.order.add_edge(Seed_Sourcing, Env_Monitoring)
root.order.add_edge(Env_Monitoring, Nutrient_Blend)
root.order.add_edge(Nutrient_Blend, Crop_Tracking)
root.order.add_edge(Crop_Tracking, Automated_Harvest)
root.order.add_edge(Automated_Harvest, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Pack_Customize)
root.order.add_edge(Pack_Customize, Cold_Storage)
root.order.add_edge(Cold_Storage, Route_Planning)
root.order.add_edge(Route_Planning, EV_Dispatch)
root.order.add_edge(EV_Dispatch, Inventory_Update)
root.order.add_edge(Inventory_Update, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Data_Analytics)
root.order.add_edge(Data_Analytics, Yield_Optimize)