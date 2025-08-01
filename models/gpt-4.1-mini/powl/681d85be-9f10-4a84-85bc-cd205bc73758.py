# Generated from: 681d85be-9f10-4a84-85bc-cd205bc73758.json
# Description: This process manages the supply chain and operational flow of an urban vertical farm specializing in microgreens and exotic herbs. It begins with seed sourcing from specialized breeders, followed by environmental calibration of grow chambers using IoT sensors. Nutrient solutions are mixed precisely by automated systems, and planting is executed by robotic arms. Continuous monitoring detects plant health issues early, triggering adaptive lighting and humidity controls. Harvesting involves selective picking to maximize yield quality, with immediate packaging in biodegradable containers. Quality assurance includes rapid microbial testing and flavor profiling through AI analysis. The process concludes with dynamic distribution scheduling to local markets and restaurants, optimizing freshness and minimizing carbon footprint, while integrating customer feedback for iterative improvements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SeedSourcing = Transition(label='Seed Sourcing')
ChamberSetup = Transition(label='Chamber Setup')
NutrientMixing = Transition(label='Nutrient Mixing')
RoboticPlanting = Transition(label='Robotic Planting')
HealthMonitoring = Transition(label='Health Monitoring')
LightingControl = Transition(label='Lighting Control')
HumidityAdjust = Transition(label='Humidity Adjust')
SelectiveHarvest = Transition(label='Selective Harvest')
BioPackaging = Transition(label='Bio Packaging')
MicrobialTest = Transition(label='Microbial Test')
FlavorProfile = Transition(label='Flavor Profile')
QualityAudit = Transition(label='Quality Audit')
OrderScheduling = Transition(label='Order Scheduling')
DeliveryRoute = Transition(label='Delivery Route')
FeedbackReview = Transition(label='Feedback Review')
InventorySync = Transition(label='Inventory Sync')

# Loop: HealthMonitoring followed by a loop of (LightingControl, HumidityAdjust)
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[HealthMonitoring,
                                                             StrictPartialOrder(nodes=[LightingControl, HumidityAdjust])])

# Partial order for MicrobialTest and FlavorProfile concurrent, then QualityAudit
quality_tests = StrictPartialOrder(nodes=[MicrobialTest, FlavorProfile, QualityAudit])
quality_tests.order.add_edge(MicrobialTest, QualityAudit)
quality_tests.order.add_edge(FlavorProfile, QualityAudit)
# MicrobialTest and FlavorProfile concurrent (no order between them)

# Partial order for OrderScheduling and DeliveryRoute concurrent
distribution = StrictPartialOrder(nodes=[OrderScheduling, DeliveryRoute])

# Partial order for FeedbackReview and InventorySync concurrent after distribution
post_distribution = StrictPartialOrder(nodes=[FeedbackReview, InventorySync])

# Partial order for selective harvest and packaging
harvest_packaging = StrictPartialOrder(nodes=[SelectiveHarvest, BioPackaging])
harvest_packaging.order.add_edge(SelectiveHarvest, BioPackaging)

# Build the main process partial order
root = StrictPartialOrder(nodes=[SeedSourcing, ChamberSetup, NutrientMixing, RoboticPlanting, health_loop,
                                 harvest_packaging, quality_tests, distribution, post_distribution])

# Add order edges following the described sequence
root.order.add_edge(SeedSourcing, ChamberSetup)
root.order.add_edge(ChamberSetup, NutrientMixing)
root.order.add_edge(NutrientMixing, RoboticPlanting)
root.order.add_edge(RoboticPlanting, health_loop)
root.order.add_edge(health_loop, harvest_packaging)
root.order.add_edge(harvest_packaging, quality_tests)
root.order.add_edge(quality_tests, distribution)
root.order.add_edge(distribution, post_distribution)