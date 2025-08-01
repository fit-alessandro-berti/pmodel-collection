# Generated from: 2ab36c58-3fed-4370-9c02-5d4173e42004.json
# Description: This process outlines the establishment of an urban vertical farm integrating advanced hydroponics and IoT monitoring systems. It involves site analysis, modular structure assembly, nutrient solution calibration, climate control optimization, crop selection tailored to urban microclimates, and continuous data-driven adjustments to maximize yield and sustainability. The process also includes community engagement for local sourcing and waste recycling to close the resource loop, ensuring minimal environmental impact and high operational efficiency within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
design_plan = Transition(label='Design Plan')
structure_build = Transition(label='Structure Build')
system_install = Transition(label='System Install')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
crop_select = Transition(label='Crop Select')
seed_plant = Transition(label='Seed Plant')
sensor_deploy = Transition(label='Sensor Deploy')
data_monitor = Transition(label='Data Monitor')
water_cycle = Transition(label='Water Cycle')
lighting_adjust = Transition(label='Lighting Adjust')
growth_track = Transition(label='Growth Track')
harvest_prep = Transition(label='Harvest Prep')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')

# Build the sequential site analysis and design phase
site_analysis_design = StrictPartialOrder(nodes=[site_survey, design_plan])
site_analysis_design.order.add_edge(site_survey, design_plan)

# Build the modular structure assembly and system install phase
structure_system = StrictPartialOrder(nodes=[structure_build, system_install])
structure_system.order.add_edge(structure_build, system_install)

# Nutrient and climate setup in parallel (concurrent)
nutrient_climate = StrictPartialOrder(nodes=[nutrient_mix, climate_setup])
# no order edges = concurrent

# Crop select -> seed plant sequence
crop_plant = StrictPartialOrder(nodes=[crop_select, seed_plant])
crop_plant.order.add_edge(crop_select, seed_plant)

# Sensor deploy followed by monitoring and adjustments done in partial order
# Data monitor, water cycle, lighting adjust, and growth track are partially ordered (concurrent)
monitoring_adjustment = StrictPartialOrder(nodes=[sensor_deploy, data_monitor, water_cycle, lighting_adjust, growth_track])
# sensor_deploy must happen before others
for activity in [data_monitor, water_cycle, lighting_adjust, growth_track]:
    monitoring_adjustment.order.add_edge(sensor_deploy, activity)

# Harvest prep occurs after growth tracking
harvest_phase = StrictPartialOrder(nodes=[growth_track, harvest_prep])
harvest_phase.order.add_edge(growth_track, harvest_prep)

# Waste recycle and community meet run in parallel with some final synchronization:
# Assume community meet and waste recycle can happen concurrently after harvest prep

final_phase = StrictPartialOrder(nodes=[harvest_prep, waste_recycle, community_meet])
final_phase.order.add_edge(harvest_prep, waste_recycle)
final_phase.order.add_edge(harvest_prep, community_meet)

# Now combine all main phases in partial order:

# Order the main phases as:
# site_analysis_design --> structure_system --> nutrient_climate --> crop_plant --> monitoring_adjustment --> harvest_phase --> final_phase

main_process = StrictPartialOrder(
    nodes=[
        site_analysis_design,
        structure_system,
        nutrient_climate,
        crop_plant,
        monitoring_adjustment,
        harvest_phase,
        final_phase
    ]
)

main_process.order.add_edge(site_analysis_design, structure_system)
main_process.order.add_edge(structure_system, nutrient_climate)
main_process.order.add_edge(nutrient_climate, crop_plant)
main_process.order.add_edge(crop_plant, monitoring_adjustment)
main_process.order.add_edge(monitoring_adjustment, harvest_phase)
main_process.order.add_edge(harvest_phase, final_phase)

root = main_process