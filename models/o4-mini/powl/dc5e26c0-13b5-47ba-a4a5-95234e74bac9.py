# Generated from: dc5e26c0-13b5-47ba-a4a5-95234e74bac9.json
# Description: This process outlines the establishment of a fully integrated urban vertical farming system within a repurposed industrial building. It involves site analysis, modular system design, climate control integration, IoT sensor deployment for real-time monitoring, nutrient solution preparation, automation programming, crop scheduling, pest management without chemicals, energy optimization through renewable sources, waste recycling, multi-tier planting, harvest logistics, and community engagement strategies. The goal is to maximize yield per square foot while minimizing environmental impact and operational costs in a densely populated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
climate_setup   = Transition(label='Climate Setup')
sensor_install  = Transition(label='Sensor Install')
nutrient_mix    = Transition(label='Nutrient Mix')
automation_code = Transition(label='Automation Code')
crop_planning   = Transition(label='Crop Planning')
pest_control    = Transition(label='Pest Control')
energy_audit    = Transition(label='Energy Audit')
waste_sort      = Transition(label='Waste Sort')
planting_tier   = Transition(label='Planting Tier')
harvest_prep    = Transition(label='Harvest Prep')
logistics_plan  = Transition(label='Logistics Plan')
community_meet  = Transition(label='Community Meet')
data_review     = Transition(label='Data Review')
system_upgrade  = Transition(label='System Upgrade')

# Define loop for continuous improvement (Data Review -> optional System Upgrade -> Data Review)
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, system_upgrade])

# Build the partial-order workflow
root = StrictPartialOrder(nodes=[
    site_survey, design_layout,
    climate_setup, sensor_install,
    nutrient_mix, automation_code, crop_planning,
    pest_control, energy_audit, waste_sort,
    planting_tier, harvest_prep,
    logistics_plan, community_meet,
    loop
])

# Sequential flow: Site Survey -> Design Layout
root.order.add_edge(site_survey, design_layout)

# From Design Layout to parallel setup tasks
root.order.add_edge(design_layout, climate_setup)
root.order.add_edge(design_layout, sensor_install)

# Climate and Sensor ready before mixing nutrients, coding automation, and planning crops
for src in [climate_setup, sensor_install]:
    for tgt in [nutrient_mix, automation_code, crop_planning]:
        root.order.add_edge(src, tgt)

# Nutrient Mix, Automation Code, Crop Planning -> Planting Tier
for src in [nutrient_mix, automation_code, crop_planning]:
    root.order.add_edge(src, planting_tier)

# After planting, run pest control, energy audit, waste sorting in parallel
root.order.add_edge(planting_tier, pest_control)
root.order.add_edge(planting_tier, energy_audit)
root.order.add_edge(planting_tier, waste_sort)

# Those three finish before harvest preparation
for src in [pest_control, energy_audit, waste_sort]:
    root.order.add_edge(src, harvest_prep)

# Harvest Prep -> Logistics Plan -> Community Meet -> Continuous Improvement Loop
root.order.add_edge(harvest_prep, logistics_plan)
root.order.add_edge(logistics_plan, community_meet)
root.order.add_edge(community_meet, loop)