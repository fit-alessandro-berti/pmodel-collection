# Generated from: 77a46753-dad3-412d-9313-d40a5c051962.json
# Description: This process outlines the end-to-end cycle of managing a vertical urban farming supply chain, starting from crop selection and seed procurement through controlled environment cultivation, automated nutrient delivery, real-time growth monitoring, harvesting, post-harvest processing, quality assurance, packaging, and distribution to local markets. It integrates IoT sensor data analytics with manual inspection to optimize yield and sustainability in densely populated areas. The process also includes waste recycling, energy consumption tracking, and customer feedback integration to continuously improve the urban farming ecosystem while minimizing environmental impact and maximizing freshness and nutritional value for consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Sourcing = Transition(label='Seed Sourcing')
Crop_Planning = Transition(label='Crop Planning')
Environment_Setup = Transition(label='Environment Setup')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Automated_Feeding = Transition(label='Automated Feeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Data_Analysis = Transition(label='Data Analysis')
Manual_Inspection = Transition(label='Manual Inspection')
Harvest_Scheduling = Transition(label='Harvest Scheduling')
Crop_Harvesting = Transition(label='Crop Harvesting')
Post_Harvest = Transition(label='Post-Harvest')
Quality_Testing = Transition(label='Quality Testing')
Packaging_Prep = Transition(label='Packaging Prep')
Distribution_Plan = Transition(label='Distribution Plan')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Tracking = Transition(label='Energy Tracking')
Customer_Feedback = Transition(label='Customer Feedback')

# Construct partial order for the main end-to-end activities
# Sequential order from start to distribution
main_order_nodes = [
    Seed_Sourcing,
    Crop_Planning,
    Environment_Setup,
    Nutrient_Mixing,
    Automated_Feeding,
    # Growth Monitoring and inspections run in parallel after Automated Feeding
    Growth_Monitoring,
    Data_Analysis,
    Manual_Inspection,
    Harvest_Scheduling,
    Crop_Harvesting,
    Post_Harvest,
    Quality_Testing,
    Packaging_Prep,
    Distribution_Plan,
]

main_PO = StrictPartialOrder(nodes=main_order_nodes)
# Define linear sequence up to Automated Feeding
main_PO.order.add_edge(Seed_Sourcing, Crop_Planning)
main_PO.order.add_edge(Crop_Planning, Environment_Setup)
main_PO.order.add_edge(Environment_Setup, Nutrient_Mixing)
main_PO.order.add_edge(Nutrient_Mixing, Automated_Feeding)

# Growth Monitoring branch (Data Analysis parallel to Growth Monitoring)
main_PO.order.add_edge(Automated_Feeding, Growth_Monitoring)
main_PO.order.add_edge(Automated_Feeding, Manual_Inspection)

# Data Analysis depends on Growth Monitoring
main_PO.order.add_edge(Growth_Monitoring, Data_Analysis)
# Manual Inspection is parallel to Data Analysis; no order edge between them

# Both Data Analysis and Manual Inspection must complete before Harvest Scheduling
main_PO.order.add_edge(Data_Analysis, Harvest_Scheduling)
main_PO.order.add_edge(Manual_Inspection, Harvest_Scheduling)

# Continue linear sequence
main_PO.order.add_edge(Harvest_Scheduling, Crop_Harvesting)
main_PO.order.add_edge(Crop_Harvesting, Post_Harvest)
main_PO.order.add_edge(Post_Harvest, Quality_Testing)
main_PO.order.add_edge(Quality_Testing, Packaging_Prep)
main_PO.order.add_edge(Packaging_Prep, Distribution_Plan)

# Waste Recycling, Energy Tracking, and Customer Feedback happen concurrently with main flow for continuous improvement/environmental impact
# They can be concurrent with the main process, but let's add a silent start and silent end node to indicate continuous concurrent activities.

# Silent start and end for concurrent activities
silent_start = SilentTransition()
silent_end = SilentTransition()

# Waste Recycling loop: no internal loop is specified, so just a standalone activity concurrent with the main process
Waste_Recycling_PO = StrictPartialOrder(nodes=[Waste_Recycling])

# Energy Tracking loop: concurrent
Energy_Tracking_PO = StrictPartialOrder(nodes=[Energy_Tracking])

# Customer Feedback loop: concurrent
Customer_Feedback_PO = StrictPartialOrder(nodes=[Customer_Feedback])

# Group these three concurrent activities in a partial order without order edges (fully concurrent)
concurrent_nodes = [Waste_Recycling_PO, Energy_Tracking_PO, Customer_Feedback_PO]

# We want to model that these three run concurrently with the main process.
# Since main_PO and the others are StrictPartialOrder, they are nodes for a new POWL model
# For proper concurrency, all 4 nodes (main_PO, Waste_Recycling_PO, Energy_Tracking_PO, Customer_Feedback_PO) together are in a StrictPartialOrder with no edges.

root = StrictPartialOrder(
    nodes=[main_PO, Waste_Recycling_PO, Energy_Tracking_PO, Customer_Feedback_PO]
)
# No order edges between these 4, so these four run concurrently.

# The final structure:
# - main_PO: the main sequential and partially concurrent flow.
# - Waste_Recycling_PO: independent activity concurrent.
# - Energy_Tracking_PO: independent activity concurrent.
# - Customer_Feedback_PO: independent activity concurrent.