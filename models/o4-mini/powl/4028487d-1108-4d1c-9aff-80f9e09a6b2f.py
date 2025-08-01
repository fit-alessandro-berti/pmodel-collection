# Generated from: 4028487d-1108-4d1c-9aff-80f9e09a6b2f.json
# Description: This process outlines the end-to-end supply chain management for an urban vertical farming operation that integrates advanced hydroponic cultivation with local distribution. Starting from seed procurement, the process includes nutrient mix optimization, climate monitoring, iterative growth adjustments, pest bio-control application, and automated harvesting. Post-harvest, fresh produce undergoes quality inspection, packaging with biodegradable materials, and dynamic inventory allocation based on real-time demand analytics. The distribution phase involves route optimization for electric delivery vehicles, last-mile cold chain maintenance, and direct-to-consumer subscription management. Additionally, waste biomass recycling and data feedback loops for continuous process improvement are integral to ensure sustainability and operational efficiency within constrained urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_sourcing     = Transition(label="Seed Sourcing")
nutrient_mix      = Transition(label="Nutrient Mix")
data_feedback     = Transition(label="Data Feedback")
climate_check     = Transition(label="Climate Check")
growth_adjust     = Transition(label="Growth Adjust")
pest_control      = Transition(label="Pest Control")
harvest_cycle     = Transition(label="Harvest Cycle")
quality_scan      = Transition(label="Quality Scan")
eco_packaging     = Transition(label="Eco Packaging")
inventory_sort    = Transition(label="Inventory Sort")
demand_forecast   = Transition(label="Demand Forecast")
route_plan        = Transition(label="Route Plan")
cold_chain        = Transition(label="Cold Chain")
delivery_track    = Transition(label="Delivery Track")
subscription_mgmt = Transition(label="Subscription Mgmt")
waste_recycle     = Transition(label="Waste Recycle")

# Loop for continuous improvement feeding back into nutrient mixing
data_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[nutrient_mix, data_feedback]
)

# Loop for iterative growth adjustments informed by climate checks
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[climate_check, growth_adjust]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        seed_sourcing,
        data_loop,
        growth_loop,
        pest_control,
        harvest_cycle,
        quality_scan,
        eco_packaging,
        inventory_sort,
        demand_forecast,
        route_plan,
        cold_chain,
        delivery_track,
        subscription_mgmt,
        waste_recycle
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(seed_sourcing, data_loop)
root.order.add_edge(data_loop, growth_loop)
root.order.add_edge(growth_loop, pest_control)
root.order.add_edge(pest_control, harvest_cycle)

# Post‐harvest branches: quality scan → packaging → inventory → demand forecasting → distribution
root.order.add_edge(harvest_cycle, quality_scan)
root.order.add_edge(quality_scan, eco_packaging)
root.order.add_edge(eco_packaging, inventory_sort)
root.order.add_edge(inventory_sort, demand_forecast)
root.order.add_edge(demand_forecast, route_plan)
root.order.add_edge(route_plan, cold_chain)
root.order.add_edge(cold_chain, delivery_track)
root.order.add_edge(delivery_track, subscription_mgmt)

# Waste recycling runs in parallel with quality inspection/packaging (after harvest)
root.order.add_edge(harvest_cycle, waste_recycle)