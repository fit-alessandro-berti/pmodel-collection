# Generated from: c439f889-faad-4311-b32e-0b0b64b52321.json
# Description: This process outlines the unique supply chain management for an urban farming cooperative that integrates local food production with city-wide distribution. It involves sourcing specialized seeds adapted to urban climates, coordinating rooftop and indoor farm schedules, monitoring crop health using IoT sensors, managing vertical farm nutrient cycles, and optimizing harvest timing. The process also includes packaging with sustainable materials, handling last-mile delivery via electric vehicles, and engaging community members for feedback and demand forecasting. This atypical supply chain emphasizes sustainability, technology integration, and community involvement to ensure fresh produce availability in dense urban settings while minimizing waste and carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SeedSourcing = Transition(label='Seed Sourcing')
FarmScheduling = Transition(label='Farm Scheduling')
SensorMonitoring = Transition(label='Sensor Monitoring')
NutrientCycling = Transition(label='Nutrient Cycling')
CropForecasting = Transition(label='Crop Forecasting')
PestInspection = Transition(label='Pest Inspection')
HarvestTiming = Transition(label='Harvest Timing')
QualityCheck = Transition(label='Quality Check')
EcoPackaging = Transition(label='Eco Packaging')
StorageAllocation = Transition(label='Storage Allocation')
OrderProcessing = Transition(label='Order Processing')
RoutePlanning = Transition(label='Route Planning')
VehicleDispatch = Transition(label='Vehicle Dispatch')
CustomerFeedback = Transition(label='Customer Feedback')
DemandAnalysis = Transition(label='Demand Analysis')
WasteManagement = Transition(label='Waste Management')
CommunityOutreach = Transition(label='Community Outreach')

# From description the structure implies ordering and partial concurrency:
# Logical grouping based on thematic connection:
# 1. Seed sourcing, farm scheduling (source and plan)
# 2. Sensor monitoring, nutrient cycling, pest inspection, crop forecasting (monitor & maintain farm)
# 3. Harvest timing, quality check (harvest related)
# 4. Eco packaging, storage allocation (post-harvest packaging and storage)
# 5. Order processing, route planning, vehicle dispatch (delivery logistics)
# 6. Customer feedback, demand analysis, community outreach (community involvement and feedback)
# 7. Waste management ongoing, possibly loop or concurrent with others (sustainability)

# Build partial order segments

# Segment: Farm production preparation and monitoring
prod_prep_monitor = StrictPartialOrder(
    nodes=[SeedSourcing, FarmScheduling,
           SensorMonitoring, NutrientCycling, PestInspection, CropForecasting]
)
# Order: SeedSourcing --> FarmScheduling --> all monitoring can be concurrent but must happen after scheduling
prod_prep_monitor.order.add_edge(SeedSourcing, FarmScheduling)
prod_prep_monitor.order.add_edge(FarmScheduling, SensorMonitoring)
prod_prep_monitor.order.add_edge(FarmScheduling, NutrientCycling)
prod_prep_monitor.order.add_edge(FarmScheduling, PestInspection)
prod_prep_monitor.order.add_edge(FarmScheduling, CropForecasting)

# Segment: Harvest and quality
harvest_quality = StrictPartialOrder(
    nodes=[HarvestTiming, QualityCheck]
)
harvest_quality.order.add_edge(HarvestTiming, QualityCheck)

# Segment: After quality check, packaging and storage concurrent
pack_storage = StrictPartialOrder(
    nodes=[EcoPackaging, StorageAllocation]
)
# no order edges, can be concurrent

# Segment: Delivery logistics order
delivery_logistics = StrictPartialOrder(
    nodes=[OrderProcessing, RoutePlanning, VehicleDispatch]
)
delivery_logistics.order.add_edge(OrderProcessing, RoutePlanning)
delivery_logistics.order.add_edge(RoutePlanning, VehicleDispatch)

# Segment: Community involvement
community = StrictPartialOrder(
    nodes=[CustomerFeedback, DemandAnalysis, CommunityOutreach]
)
# Customer feedback leads to demand analysis, which leads to outreach
community.order.add_edge(CustomerFeedback, DemandAnalysis)
community.order.add_edge(DemandAnalysis, CommunityOutreach)

# Waste management runs concurrently but must start after farm scheduling
# We can model it as a loop that starts after FarmScheduling to represent ongoing waste management during process
# waste_loop = *(WasteManagement, tau)
# But no explicit tau activity given, we can model WasteManagement as a loop with a silent activity to exit loop

skip = SilentTransition()
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[WasteManagement := Transition(label='Waste Management'), skip])

# Now we need to combine all major segments into a global partial order.

# A conservative order:
# prod_prep_monitor --> harvest_quality --> pack_storage & delivery_logistics (concurrent)
# delivery_logistics precedes community involvement

# Create root partial order with nodes:
root_nodes = [prod_prep_monitor,
              harvest_quality,
              pack_storage,
              delivery_logistics,
              community,
              waste_loop]

root = StrictPartialOrder(nodes=root_nodes)

# Define order edges between segments:
root.order.add_edge(prod_prep_monitor, harvest_quality)
root.order.add_edge(harvest_quality, pack_storage)
root.order.add_edge(harvest_quality, delivery_logistics)

root.order.add_edge(delivery_logistics, community)

# Waste loop starts after FarmScheduling but can run concurrently with harvest and beyond
root.order.add_edge(prod_prep_monitor, waste_loop)

# No further order between waste_loop and others - concurrent to most, representing ongoing process

# Final result is root