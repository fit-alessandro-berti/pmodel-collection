# Generated from: 95f2b779-22be-45e5-a785-43deb2bc45a1.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It begins with site analysis and structural assessment to ensure the building can support multi-layered grow racks. Following this, environmental controls such as lighting, humidity, and temperature systems are installed and calibrated. The integration of hydroponic or aeroponic systems is next, requiring precise plumbing and nutrient delivery setups. Crop selection and seeding protocols are established based on market demand and growth cycles. Automated monitoring and AI-driven adjustments optimize plant health. Periodic maintenance routines and yield tracking ensure sustainability and profitability. The process concludes with packaging and distribution planning tailored for urban consumers, incorporating waste recycling strategies to minimize environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')

system_design = Transition(label='System Design')

lighting_setup = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')

water_install = Transition(label='Water Install')
nutrient_mix = Transition(label='Nutrient Mix')

rack_assembly = Transition(label='Rack Assembly')

seed_planting = Transition(label='Seed Planting')

sensor_install = Transition(label='Sensor Install')
ai_calibration = Transition(label='AI Calibration')
growth_monitor = Transition(label='Growth Monitor')

maintenance = Transition(label='Maintenance')
harvest_prep = Transition(label='Harvest Prep')

packaging = Transition(label='Packaging')
waste_manage = Transition(label='Waste Manage')
distribution = Transition(label='Distribution')

# 1) Site analysis and structural assessment
site_structure = StrictPartialOrder(
    nodes=[site_survey, structure_check]
)
site_structure.order.add_edge(site_survey, structure_check)

# 2) Environmental controls installed & calibrated (lighting, humidity, temperature)
env_control = StrictPartialOrder(
    nodes=[lighting_setup, climate_control]
)
# concurrent: no edges

# 3) Integration of hydroponic or aeroponic systems (water and nutrient setup)
water_nutrient = StrictPartialOrder(
    nodes=[water_install, nutrient_mix]
)
# concurrent: no edges

# 4) Rack assembly (after structural check)
# Will be done after structure_check
# So rack_assembly after structure_check

# 5) Crop selection and seeding protocols
crop_seed = StrictPartialOrder(
    nodes=[seed_planting]
)

# 6) Automated monitoring and AI-driven adjustments (sensor install, AI calibration, growth monitor)
monitor_ai = StrictPartialOrder(
    nodes=[sensor_install, ai_calibration, growth_monitor]
)
monitor_ai.order.add_edge(sensor_install, ai_calibration)
monitor_ai.order.add_edge(ai_calibration, growth_monitor)

# 7) Periodic maintenance and yield tracking (maintenance, harvest prep)
maintain_harvest = StrictPartialOrder(
    nodes=[maintenance, harvest_prep]
)
# concurrent no edges

# 8) Packaging and distribution planning with waste manage
pack_waste_dist = StrictPartialOrder(
    nodes=[packaging, waste_manage, distribution]
)
pack_waste_dist.order.add_edge(packaging, waste_manage)
pack_waste_dist.order.add_edge(waste_manage, distribution)

# Build the main process partial order:

# After site_structure, system_design is done
main_order1 = StrictPartialOrder(
    nodes=[site_structure, system_design]
)
main_order1.order.add_edge(site_structure, system_design)

# After system_design, environmental controls and water/nutrient can run in parallel
env_and_water = StrictPartialOrder(
    nodes=[env_control, water_nutrient]
)

# rack_assembly after structure_check - nest structure_check inside site_structure, but since site_structure is a PO of site_survey --> structure_check,
# we must model rack_assembly after structure_check only, so create a PO with structure_check --> rack_assembly
rack_after_structure = StrictPartialOrder(
    nodes=[structure_check, rack_assembly]
)
rack_after_structure.order.add_edge(structure_check, rack_assembly)

# crop_seed depends on rack_assembly done
crop_after_rack = StrictPartialOrder(
    nodes=[rack_assembly, seed_planting]
)
crop_after_rack.order.add_edge(rack_assembly, seed_planting)

# monitoring depends on sensor_install, ai_calibration, growth_monitor → those are already sequenced

# Maintenance and harvest prep can be started after growth monitor
maint_after_monitor = StrictPartialOrder(
    nodes=[growth_monitor, maintenance, harvest_prep]
)
maint_after_monitor.order.add_edge(growth_monitor, maintenance)
maint_after_monitor.order.add_edge(growth_monitor, harvest_prep)

# Packaging, waste, distribution after harvest prep
pack_after_harvest = StrictPartialOrder(
    nodes=[harvest_prep, packaging]
)
pack_after_harvest.order.add_edge(harvest_prep, packaging)

# Compose packaging → waste → distribution already modeled in pack_waste_dist

# Compose all together stepwise:

# 1. site_survey -> structure_check -> rack_assembly -> seed_planting
seq1 = StrictPartialOrder(
    nodes=[site_survey, structure_check, rack_assembly, seed_planting]
)
seq1.order.add_edge(site_survey, structure_check)
seq1.order.add_edge(structure_check, rack_assembly)
seq1.order.add_edge(rack_assembly, seed_planting)

# 2. system_design after site_structure completion (which means after structure_check), so add edge structure_check -> system_design
seq2 = StrictPartialOrder(
    nodes=[structure_check, system_design]
)
seq2.order.add_edge(structure_check, system_design)

# 3. env_control and water_nutrient after system_design, these two sets can run concurrently
env_water_nodes = [lighting_setup, climate_control, water_install, nutrient_mix]
env_water = StrictPartialOrder(nodes=env_water_nodes)  # no order among these
seq3_nodes = [system_design, env_water]
# We have a POWL with nodes: system_design and env_water group → but env_water is a PO itself
# We can create a single PO with nodes = system_design + env_water nodes, and edges system_design --> all env_water nodes
seq3 = StrictPartialOrder(
    nodes=[system_design] + env_water_nodes
)
for node in env_water_nodes:
    seq3.order.add_edge(system_design, node)

# 4. monitoring after env and water installations
# So all env_water nodes --> sensor_install (start monitoring)
seq4_nodes = env_water_nodes + [sensor_install]
seq4 = StrictPartialOrder(
    nodes=seq4_nodes
)
for node in env_water_nodes:
    seq4.order.add_edge(node, sensor_install)

# The monitor_ai PO already models sensor_install -> ai_calibration -> growth_monitor

# 5. maintenance and harvest prep after growth_monitor
seq5 = StrictPartialOrder(
    nodes=[growth_monitor, maintenance, harvest_prep]
)
seq5.order.add_edge(growth_monitor, maintenance)
seq5.order.add_edge(growth_monitor, harvest_prep)

# 6. packaging after harvest prep, then waste_manage then distribution (pack_waste_dist PO)
# pack_waste_dist models packaging -> waste_manage -> distribution

# Put packaging start after harvest_prep
seq6 = StrictPartialOrder(
    nodes=[harvest_prep, packaging]
)
seq6.order.add_edge(harvest_prep, packaging)

# Now construct the full model as a PO of all big steps:
# Steps:
# (site_survey → structure_check → rack_assembly → seed_planting)
# →
# (structure_check → system_design)
# →
# (system_design → env_water nodes concurrent)
# →
# (env_water nodes → sensor_install)
# →
# (sensor_install → ai_calibration → growth_monitor)
# →
# (growth_monitor → maintenance & harvest_prep)
# →
# (harvest_prep → packaging → waste_manage → distribution)

# For clarity, unify all nodes:
all_nodes = [
    site_survey, structure_check, rack_assembly, seed_planting,
    system_design,
    lighting_setup, climate_control, water_install, nutrient_mix,
    sensor_install, ai_calibration, growth_monitor,
    maintenance, harvest_prep,
    packaging, waste_manage, distribution
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges:

# site_survey -> structure_check -> rack_assembly -> seed_planting
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, rack_assembly)
root.order.add_edge(rack_assembly, seed_planting)

# structure_check -> system_design
root.order.add_edge(structure_check, system_design)

# system_design -> all env_water nodes
for n in [lighting_setup, climate_control, water_install, nutrient_mix]:
    root.order.add_edge(system_design, n)

# all env_water nodes -> sensor_install
for n in [lighting_setup, climate_control, water_install, nutrient_mix]:
    root.order.add_edge(n, sensor_install)

# sensor_install -> ai_calibration -> growth_monitor
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, growth_monitor)

# growth_monitor -> maintenance & harvest_prep (concurrent)
root.order.add_edge(growth_monitor, maintenance)
root.order.add_edge(growth_monitor, harvest_prep)

# harvest_prep -> packaging -> waste_manage -> distribution
root.order.add_edge(harvest_prep, packaging)
root.order.add_edge(packaging, waste_manage)
root.order.add_edge(waste_manage, distribution)