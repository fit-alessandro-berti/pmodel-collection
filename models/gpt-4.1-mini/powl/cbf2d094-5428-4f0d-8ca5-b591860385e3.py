# Generated from: cbf2d094-5428-4f0d-8ca5-b591860385e3.json
# Description: This process outlines the comprehensive cycle of an urban vertical farming operation that integrates automated hydroponics with AI-driven crop monitoring to optimize yield in constrained city environments. Starting from seed selection and nutrient calibration, the process includes climate control adjustments, robotic planting, pest bio-control application, and continuous growth analytics. Harvesting is synchronized with demand forecasting to minimize waste, followed by post-harvest sterilization and packaging. Finally, logistics coordination ensures fresh delivery to local markets, while data feedback loops refine future crop cycles for sustainability and efficiency improvements in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Adjust = Transition(label='Climate Adjust')
Planting_Robotic = Transition(label='Planting Robotic')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Water_Recycle = Transition(label='Water Recycle')
Light_Optimize = Transition(label='Light Optimize')
Growth_Analyze = Transition(label='Growth Analyze')
Harvest_Sync = Transition(label='Harvest Sync')
Demand_Forecast = Transition(label='Demand Forecast')
Sterilize_Crop = Transition(label='Sterilize Crop')
Package_Fresh = Transition(label='Package Fresh')
Delivery_Plan = Transition(label='Delivery Plan')
Data_Feedback = Transition(label='Data Feedback')

# Phase 1: Seed selection and nutrient calibration
phase1 = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix])
phase1.order.add_edge(Seed_Select, Nutrient_Mix)

# Phase 2: Climate control adjustments
phase2 = Climate_Adjust

# Phase 3: Robotic planting
phase3 = Planting_Robotic

# Phase 4: Pest bio-control application
phase4 = Pest_Control

# Phase 5: Continuous growth analytics (Growth Monitor, Water Recycle, Light Optimize, Growth Analyze)
growth_analysis_nodes = [Growth_Monitor, Water_Recycle, Light_Optimize, Growth_Analyze]
phase5 = StrictPartialOrder(nodes=growth_analysis_nodes)
# No explicit order among these, they can run concurrently

# Phase 6: Harvesting synchronized with demand forecasting
harvest_sync_and_forecast = StrictPartialOrder(nodes=[Harvest_Sync, Demand_Forecast])
harvest_sync_and_forecast.order.add_edge(Harvest_Sync, Demand_Forecast)

# Phase 7: Post-harvest sterilization and packaging
post_harvest = StrictPartialOrder(nodes=[Sterilize_Crop, Package_Fresh])
post_harvest.order.add_edge(Sterilize_Crop, Package_Fresh)

# Phase 8: Logistics coordination (delivery)
delivery = Delivery_Plan

# Phase 9: Data feedback loop to refine future crop cycles
# Model Data Feedback as a loop node where Data_Feedback loops back to Growth_Monitor
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, Data_Feedback]
)

# Since Growth_Monitor is used inside loop, remove it from phase5 to avoid duplication
phase5 = StrictPartialOrder(nodes=[Water_Recycle, Light_Optimize, Growth_Analyze])

# Complete growth analysis phase is parallel composition of loop and the other growth nodes
growth_phase = StrictPartialOrder(nodes=[loop, phase5])
growth_phase.order.add_edge(loop, phase5)  # loop before others? 
# Actually these three (Water Recycle, Light Optimize, Growth Analyze) can run concurrently with the loop
# So no edges are needed; remove edge

growth_phase = StrictPartialOrder(nodes=[loop, Water_Recycle, Light_Optimize, Growth_Analyze])

# Assemble all phases in order:
root = StrictPartialOrder(
    nodes=[
        phase1,
        phase2,
        phase3,
        phase4,
        growth_phase,
        harvest_sync_and_forecast,
        post_harvest,
        delivery
    ]
)

# Add order edges to reflect the sequence
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, growth_phase)
root.order.add_edge(growth_phase, harvest_sync_and_forecast)
root.order.add_edge(harvest_sync_and_forecast, post_harvest)
root.order.add_edge(post_harvest, delivery)