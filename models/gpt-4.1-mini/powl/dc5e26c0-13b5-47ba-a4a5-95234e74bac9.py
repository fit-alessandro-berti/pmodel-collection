# Generated from: dc5e26c0-13b5-47ba-a4a5-95234e74bac9.json
# Description: This process outlines the establishment of a fully integrated urban vertical farming system within a repurposed industrial building. It involves site analysis, modular system design, climate control integration, IoT sensor deployment for real-time monitoring, nutrient solution preparation, automation programming, crop scheduling, pest management without chemicals, energy optimization through renewable sources, waste recycling, multi-tier planting, harvest logistics, and community engagement strategies. The goal is to maximize yield per square foot while minimizing environmental impact and operational costs in a densely populated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
nutrient_mix = Transition(label='Nutrient Mix')
automation_code = Transition(label='Automation Code')
crop_planning = Transition(label='Crop Planning')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_sort = Transition(label='Waste Sort')
planting_tier = Transition(label='Planting Tier')
harvest_prep = Transition(label='Harvest Prep')
logistics_plan = Transition(label='Logistics Plan')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
system_upgrade = Transition(label='System Upgrade')

# Build loop for continuous improvement: (Data Review + System Upgrade) loop
data_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, system_upgrade])

# Initial partial order: site_survey -> design -> climate -> sensors
po_init = StrictPartialOrder(nodes=[site_survey, design_layout, climate_setup, sensor_install])
po_init.order.add_edge(site_survey, design_layout)
po_init.order.add_edge(design_layout, climate_setup)
po_init.order.add_edge(climate_setup, sensor_install)

# Nutrient mix, automation code, and crop planning are done after sensor install
po_mid = StrictPartialOrder(nodes=[nutrient_mix, automation_code, crop_planning])
# No order inside, these three can run concurrently

# Pest control, energy audit, waste sort can run concurrently after crop planning
po_mid2 = StrictPartialOrder(nodes=[pest_control, energy_audit, waste_sort])

# Planting tier is after pest control, energy audit, waste sort finish
# Harvest prep and logistics plan after planting tier
po_final = StrictPartialOrder(nodes=[planting_tier, harvest_prep, logistics_plan])
po_final.order.add_edge(planting_tier, harvest_prep)
po_final.order.add_edge(harvest_prep, logistics_plan)

# Community meet can happen concurrently with planting tier (community engagement during planting)
# Adding it as concurrent to planting_tier
po_end = StrictPartialOrder(nodes=[po_final, community_meet])
# StrictPartialOrder does not accept nested StrictPartialOrder as node directly,
# So we include nodes explicitly instead:

# Combine planting_tier, harvest_prep, logistics_plan, community_meet in one PO
end_nodes = [planting_tier, harvest_prep, logistics_plan, community_meet]
po_end = StrictPartialOrder(nodes=end_nodes)
po_end.order.add_edge(planting_tier, harvest_prep)
po_end.order.add_edge(harvest_prep, logistics_plan)
# community_meet concurrent (no edges)

# Compose all steps in a final PO with dependencies:
# From sensor_install to nutrient_mix, automation_code, crop_planning (concurrent)
# From crop_planning to pest_control, energy_audit, waste_sort (concurrent)
# From those three to planting_tier
# Then to harvest_prep, logistics_plan
# community_meet concurrent with planting_tier
# data_review_loop runs concurrently with the entire workflow (continuous improvement)

# We need a combined PO for mid and mid2 and end with correct edges

# Combine mid and mid2 and end nodes
mid_mid2_end_nodes = [
    nutrient_mix, automation_code, crop_planning,
    pest_control, energy_audit, waste_sort,
    planting_tier, harvest_prep, logistics_plan, community_meet
]

po_all = StrictPartialOrder(nodes=[site_survey, design_layout, climate_setup, sensor_install] + mid_mid2_end_nodes + [data_review_loop])

# Add known edges:
# Initial chain
po_all.order.add_edge(site_survey, design_layout)
po_all.order.add_edge(design_layout, climate_setup)
po_all.order.add_edge(climate_setup, sensor_install)

# From sensor_install to nutrient_mix, automation_code, crop_planning
for n in [nutrient_mix, automation_code, crop_planning]:
    po_all.order.add_edge(sensor_install, n)

# From crop_planning to pest_control, energy_audit, waste_sort
for n in [pest_control, energy_audit, waste_sort]:
    po_all.order.add_edge(crop_planning, n)

# From pest_control, energy_audit, waste_sort to planting_tier
for n in [pest_control, energy_audit, waste_sort]:
    po_all.order.add_edge(n, planting_tier)

# Planting tier to harvest_prep to logistics_plan
po_all.order.add_edge(planting_tier, harvest_prep)
po_all.order.add_edge(harvest_prep, logistics_plan)

# community_meet concurrent with planting_tier (no edges)

# data_review_loop runs concurrently with entire workflow (no edges)

root = po_all