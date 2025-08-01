# Generated from: 1ba8656a-9e85-4a88-be21-a20b643d24c5.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating sustainable practices and advanced automation. It begins with site analysis and zoning compliance, followed by modular farm design and climate system installation. Seed selection and automated planting are conducted alongside nutrient formulation development. Continuous monitoring of growth parameters is ensured through IoT sensors, while robotic harvesting and packaging maintain efficiency. Waste recycling and water reclamation systems are incorporated to minimize environmental impact. Finally, product distribution leverages local delivery networks to reduce carbon footprint, completing a closed-loop urban farming ecosystem that supports fresh produce availability year-round.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_analysis   = Transition(label='Site Analysis')
zoning_check    = Transition(label='Zoning Check')
farm_design     = Transition(label='Farm Design')
climate_setup   = Transition(label='Climate Setup')
seed_selection  = Transition(label='Seed Selection')
auto_planting   = Transition(label='Auto Planting')
nutrient_mix    = Transition(label='Nutrient Mix')
sensor_install  = Transition(label='Sensor Install')
growth_monitor  = Transition(label='Growth Monitor')
robotic_harvest = Transition(label='Robotic Harvest')
packaging_prep  = Transition(label='Packaging Prep')
waste_manage    = Transition(label='Waste Manage')
water_reclaim   = Transition(label='Water Reclaim')
local_delivery  = Transition(label='Local Delivery')
data_review     = Transition(label='Data Review')

# Group 3: seed→auto‐planting runs in parallel with nutrient mix
plant_group = StrictPartialOrder(nodes=[seed_selection, auto_planting, nutrient_mix])
plant_group.order.add_edge(seed_selection, auto_planting)

# Group 4: sensor→growth monitoring runs in parallel with robotic harvest→packaging
monitor_harvest_group = StrictPartialOrder(
    nodes=[sensor_install, growth_monitor, robotic_harvest, packaging_prep]
)
monitor_harvest_group.order.add_edge(sensor_install, growth_monitor)
monitor_harvest_group.order.add_edge(robotic_harvest, packaging_prep)

# Group 5: waste manage and water reclaim in parallel
recycle_group = StrictPartialOrder(nodes=[waste_manage, water_reclaim])

# Group 6: local delivery → data review
delivery_group = StrictPartialOrder(nodes=[local_delivery, data_review])
delivery_group.order.add_edge(local_delivery, data_review)

# Root workflow: sequential composition of the above segments
root = StrictPartialOrder(
    nodes=[
        site_analysis, zoning_check,
        farm_design, climate_setup,
        plant_group,
        monitor_harvest_group,
        recycle_group,
        delivery_group
    ]
)
# Sequence edges
root.order.add_edge(site_analysis, zoning_check)
root.order.add_edge(zoning_check, farm_design)
root.order.add_edge(farm_design, climate_setup)
root.order.add_edge(climate_setup, plant_group)
root.order.add_edge(plant_group, monitor_harvest_group)
root.order.add_edge(monitor_harvest_group, recycle_group)
root.order.add_edge(recycle_group, delivery_group)