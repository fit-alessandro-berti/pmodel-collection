# Generated from: 1ba8656a-9e85-4a88-be21-a20b643d24c5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating sustainable practices and advanced automation. It begins with site analysis and zoning compliance, followed by modular farm design and climate system installation. Seed selection and automated planting are conducted alongside nutrient formulation development. Continuous monitoring of growth parameters is ensured through IoT sensors, while robotic harvesting and packaging maintain efficiency. Waste recycling and water reclamation systems are incorporated to minimize environmental impact. Finally, product distribution leverages local delivery networks to reduce carbon footprint, completing a closed-loop urban farming ecosystem that supports fresh produce availability year-round.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
zoning_check = Transition(label='Zoning Check')
farm_design = Transition(label='Farm Design')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
auto_planting = Transition(label='Auto Planting')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
robotic_harvest = Transition(label='Robotic Harvest')
packaging_prep = Transition(label='Packaging Prep')
waste_manage = Transition(label='Waste Manage')
water_reclaim = Transition(label='Water Reclaim')
local_delivery = Transition(label='Local Delivery')
data_review = Transition(label='Data Review')

# Site analysis and zoning check sequentially
site_zoning = StrictPartialOrder(nodes=[site_analysis, zoning_check])
site_zoning.order.add_edge(site_analysis, zoning_check)

# Farm design and climate setup sequentially
farm_climate = StrictPartialOrder(nodes=[farm_design, climate_setup])
farm_climate.order.add_edge(farm_design, climate_setup)

# Seed selection and auto planting concurrent with nutrient mix
seed_plant = StrictPartialOrder(nodes=[seed_selection, auto_planting])
seed_plant.order.add_edge(seed_selection, auto_planting)  # auto planting after seed selection

# Nutrient mix concurrent with seed_plant
seed_nutrient = StrictPartialOrder(nodes=[seed_plant, nutrient_mix])  
# No order edges, fully concurrent

# Sensor install, growth monitor sequentially
monitoring = StrictPartialOrder(nodes=[sensor_install, growth_monitor])
monitoring.order.add_edge(sensor_install, growth_monitor)

# Robotic harvest and packaging prep sequentially
harvest_packaging = StrictPartialOrder(nodes=[robotic_harvest, packaging_prep])
harvest_packaging.order.add_edge(robotic_harvest, packaging_prep)

# Waste manage and water reclaim concurrent
waste_water = StrictPartialOrder(nodes=[waste_manage, water_reclaim])
# No order edges, concurrent

# Final distribution and data review sequentially
distribution = StrictPartialOrder(nodes=[local_delivery, data_review])
distribution.order.add_edge(local_delivery, data_review)

# Combine seed_nutrient and monitoring concurrently 
seed_nutrient_monitor = StrictPartialOrder(nodes=[seed_nutrient, monitoring])
# No order edges between seed_nutrient and monitoring

# Combine harvest_packaging and waste_water concurrently
harvest_waste = StrictPartialOrder(nodes=[harvest_packaging, waste_water])
# No order edges between harvest_packaging and waste_water

# Combine seed_nutrient_monitor and harvest_waste concurrently
post_farm = StrictPartialOrder(nodes=[seed_nutrient_monitor, harvest_waste])
# No order edges between them

# Combine farm_climate and post_farm with order farm_climate --> post_farm
farm_and_post = StrictPartialOrder(nodes=[farm_climate, post_farm])
farm_and_post.order.add_edge(farm_climate, post_farm)

# Combine site_zoning and farm_and_post with order site_zoning --> farm_and_post
pre_harvest = StrictPartialOrder(nodes=[site_zoning, farm_and_post])
pre_harvest.order.add_edge(site_zoning, farm_and_post)

# Finally order pre_harvest --> distribution
root = StrictPartialOrder(nodes=[pre_harvest, distribution])
root.order.add_edge(pre_harvest, distribution)