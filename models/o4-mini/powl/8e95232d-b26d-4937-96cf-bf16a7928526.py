# Generated from: 8e95232d-b26d-4937-96cf-bf16a7928526.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating hydroponics, AI-driven environmental controls, and sustainable waste recycling. Activities include seed selection, nutrient mixing, automated planting, continuous growth monitoring, pest bio-control, adaptive lighting adjustment, climate regulation, precision harvesting, biomass repurposing, energy optimization, data analytics feedback, and distribution logistics. The cycle emphasizes minimizing resource use while maximizing yield and quality, involving multiple feedback loops and cross-functional coordination between agronomy, engineering, and supply chain teams to ensure efficient, eco-friendly urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection     = Transition(label='Seed Selection')
nutrient_mix       = Transition(label='Nutrient Mix')
automated_planting = Transition(label='Automated Planting')
growth_monitor     = Transition(label='Growth Monitor')
pest_control       = Transition(label='Pest Control')
light_adjust       = Transition(label='Light Adjust')
climate_regulate   = Transition(label='Climate Regulate')
water_recycle      = Transition(label='Water Recycle')
harvest_crop       = Transition(label='Harvest Crop')
biomass_repurpose  = Transition(label='Biomass Repurpose')
energy_optimize    = Transition(label='Energy Optimize')
quality_check      = Transition(label='Quality Check')
data_analyze       = Transition(label='Data Analyze')
supply_pack        = Transition(label='Supply Pack')
delivery_schedule  = Transition(label='Delivery Schedule')

# Concurrent environmental controls after each growth monitor
env_controls = StrictPartialOrder(
    nodes=[pest_control, light_adjust, climate_regulate, water_recycle]
)

# Loop: growth monitor then optionally iterate through environmental controls
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, env_controls]
)

# Loop: quality check followed by data analysis for feedback
quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_check, data_analyze]
)

# Root partial order: sequence + parallel branches + loops
root = StrictPartialOrder(
    nodes=[
        seed_selection,
        nutrient_mix,
        automated_planting,
        growth_loop,
        harvest_crop,
        biomass_repurpose,
        energy_optimize,
        quality_loop,
        supply_pack,
        delivery_schedule
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(seed_selection,     nutrient_mix)
root.order.add_edge(nutrient_mix,       automated_planting)
root.order.add_edge(automated_planting, growth_loop)
root.order.add_edge(growth_loop,        harvest_crop)
root.order.add_edge(harvest_crop,       biomass_repurpose)
root.order.add_edge(harvest_crop,       energy_optimize)
root.order.add_edge(harvest_crop,       quality_loop)
root.order.add_edge(quality_loop,       supply_pack)
root.order.add_edge(supply_pack,        delivery_schedule)