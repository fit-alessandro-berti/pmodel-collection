# Generated from: c439f889-faad-4311-b32e-0b0b64b52321.json
# Description: This process outlines the unique supply chain management for an urban farming cooperative that integrates local food production with city-wide distribution. It involves sourcing specialized seeds adapted to urban climates, coordinating rooftop and indoor farm schedules, monitoring crop health using IoT sensors, managing vertical farm nutrient cycles, and optimizing harvest timing. The process also includes packaging with sustainable materials, handling last-mile delivery via electric vehicles, and engaging community members for feedback and demand forecasting. This atypical supply chain emphasizes sustainability, technology integration, and community involvement to ensure fresh produce availability in dense urban settings while minimizing waste and carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_sourcing      = Transition(label='Seed Sourcing')
farm_scheduling    = Transition(label='Farm Scheduling')
sensor_monitoring  = Transition(label='Sensor Monitoring')
pest_inspection    = Transition(label='Pest Inspection')
nutrient_cycling   = Transition(label='Nutrient Cycling')
crop_forecasting   = Transition(label='Crop Forecasting')
harvest_timing     = Transition(label='Harvest Timing')
quality_check      = Transition(label='Quality Check')
eco_packaging      = Transition(label='Eco Packaging')
waste_management   = Transition(label='Waste Management')
storage_allocation = Transition(label='Storage Allocation')
order_processing   = Transition(label='Order Processing')
route_planning     = Transition(label='Route Planning')
vehicle_dispatch   = Transition(label='Vehicle Dispatch')
customer_feedback  = Transition(label='Customer Feedback')
demand_analysis    = Transition(label='Demand Analysis')
community_outreach = Transition(label='Community Outreach')

# Build the repeated growth‐monitoring loop: Sensor → Pest → Nutrient → Forecast
growth_cycle = StrictPartialOrder(nodes=[
    sensor_monitoring,
    pest_inspection,
    nutrient_cycling,
    crop_forecasting
])
growth_cycle.order.add_edge(sensor_monitoring, pest_inspection)
growth_cycle.order.add_edge(pest_inspection, nutrient_cycling)
growth_cycle.order.add_edge(nutrient_cycling, crop_forecasting)

# LOOP operator: do growth_cycle at least once, then decide to repeat or exit
skip = SilentTransition()
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_cycle, skip]
)

# After quality check, either package or discard
packaging_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[eco_packaging, waste_management]
)

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    seed_sourcing,
    farm_scheduling,
    growth_loop,
    harvest_timing,
    quality_check,
    packaging_choice,
    storage_allocation,
    order_processing,
    route_planning,
    vehicle_dispatch,
    customer_feedback,
    demand_analysis,
    community_outreach
])

# Define control‐flow (partial order) edges
root.order.add_edge(seed_sourcing,      farm_scheduling)
root.order.add_edge(farm_scheduling,    growth_loop)
root.order.add_edge(growth_loop,        harvest_timing)
root.order.add_edge(harvest_timing,     quality_check)
root.order.add_edge(quality_check,      packaging_choice)
root.order.add_edge(packaging_choice,   storage_allocation)
root.order.add_edge(storage_allocation, order_processing)
root.order.add_edge(order_processing,   route_planning)
root.order.add_edge(route_planning,     vehicle_dispatch)
# After dispatch, three community‐oriented tasks happen (in parallel)
root.order.add_edge(vehicle_dispatch,   customer_feedback)
root.order.add_edge(vehicle_dispatch,   demand_analysis)
root.order.add_edge(vehicle_dispatch,   community_outreach)