# Generated from: 69a3dd4b-090a-48de-8e00-313f840f4e68.json
# Description: This process outlines the sequential steps for establishing a fully operational urban vertical farm within a repurposed industrial space. It includes site assessment, modular system design, climate control calibration, hydroponic nutrient formulation, automated lighting programming, pest management integration, workforce training, crop scheduling, yield monitoring, waste recycling implementation, and market distribution planning. The process is complex due to the integration of advanced technology, sustainability requirements, and urban logistics, requiring interdisciplinary coordination and continuous optimization to maximize crop output while minimizing environmental impact in a constrained urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activity transitions
site_survey     = Transition(label='Site Survey')
space_planning  = Transition(label='Space Planning')
system_design   = Transition(label='System Design')
climate_setup   = Transition(label='Climate Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
lighting_config = Transition(label='Lighting Config')
pest_control    = Transition(label='Pest Control')
staff_training  = Transition(label='Staff Training')
crop_schedule   = Transition(label='Crop Schedule')
yield_tracking  = Transition(label='Yield Tracking')
waste_sort      = Transition(label='Waste Sort')
water_recycling = Transition(label='Water Recycling')
energy_audit    = Transition(label='Energy Audit')
market_prep     = Transition(label='Market Prep')
distribution    = Transition(label='Distribution')

# Create a strict partial order of the overall workflow
root = StrictPartialOrder(nodes=[
    site_survey, space_planning, system_design, climate_setup,
    nutrient_mix, lighting_config, pest_control, staff_training,
    crop_schedule, yield_tracking, waste_sort, water_recycling,
    energy_audit, market_prep, distribution
])

# Add sequential dependencies
transitions = [
    site_survey, space_planning, system_design, climate_setup,
    nutrient_mix, lighting_config, pest_control, staff_training,
    crop_schedule, yield_tracking, waste_sort, water_recycling,
    energy_audit, market_prep, distribution
]
for i in range(len(transitions) - 1):
    root.order.add_edge(transitions[i], transitions[i + 1])