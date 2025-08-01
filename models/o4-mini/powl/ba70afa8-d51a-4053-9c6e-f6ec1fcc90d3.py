# Generated from: ba70afa8-d51a-4053-9c6e-f6ec1fcc90d3.json
# Description: This process manages the end-to-end supply chain of an urban vertical farming operation specializing in microgreens and specialty herbs. It includes seed sourcing from niche suppliers, controlled environment planting, automated growth monitoring with AI sensors, nutrient solution adjustments, and on-demand harvesting schedules. Post-harvest, the process incorporates rapid packaging in eco-friendly materials, cold chain logistics with real-time tracking, dynamic order allocation for local markets and restaurants, and feedback loops from clients to optimize crop varieties. The system uniquely integrates waste recycling by converting plant residues into biofertilizers used internally, closing the sustainability loop while maintaining high product quality and minimizing urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
seed_sourcing      = Transition(label="Seed Sourcing")
planting_setup     = Transition(label="Planting Setup")
growth_monitoring  = Transition(label="Growth Monitoring")
nutrient_mixing    = Transition(label="Nutrient Mixing")
climate_control    = Transition(label="Climate Control")
pest_scanning      = Transition(label="Pest Scanning")
harvest_planning   = Transition(label="Harvest Planning")
selective_picking  = Transition(label="Selective Picking")
waste_sorting      = Transition(label="Waste Sorting")
biofert_prep       = Transition(label="Biofertilizer Prep")
packaging_prep     = Transition(label="Packaging Prep")
cold_storage       = Transition(label="Cold Storage")
order_allocation   = Transition(label="Order Allocation")
delivery_routing   = Transition(label="Delivery Routing")
client_feedback    = Transition(label="Client Feedback")
data_analysis      = Transition(label="Data Analysis")

# Production phase: seed → planting → growth loop → harvest → waste recycling
production = StrictPartialOrder(nodes=[
    seed_sourcing,
    planting_setup,
    growth_monitoring,
    nutrient_mixing,
    climate_control,
    pest_scanning,
    harvest_planning,
    selective_picking,
    waste_sorting,
    biofert_prep
])
production.order.add_edge(seed_sourcing,     planting_setup)
production.order.add_edge(planting_setup,    growth_monitoring)
production.order.add_edge(growth_monitoring, nutrient_mixing)
production.order.add_edge(nutrient_mixing,   climate_control)
production.order.add_edge(climate_control,   pest_scanning)
production.order.add_edge(pest_scanning,     harvest_planning)
production.order.add_edge(harvest_planning,  selective_picking)
production.order.add_edge(selective_picking, waste_sorting)
production.order.add_edge(waste_sorting,     biofert_prep)

# Post-harvest phase: packaging → cold storage → allocation → routing → feedback → analysis
post_harvest = StrictPartialOrder(nodes=[
    packaging_prep,
    cold_storage,
    order_allocation,
    delivery_routing,
    client_feedback,
    data_analysis
])
post_harvest.order.add_edge(packaging_prep,   cold_storage)
post_harvest.order.add_edge(cold_storage,     order_allocation)
post_harvest.order.add_edge(order_allocation, delivery_routing)
post_harvest.order.add_edge(delivery_routing, client_feedback)
post_harvest.order.add_edge(client_feedback,  data_analysis)

# Combine into a LOOP: do production, then post-harvest, then optionally repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[production, post_harvest]
)