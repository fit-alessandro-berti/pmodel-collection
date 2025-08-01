# Generated from: 2ab36c58-3fed-4370-9c02-5d4173e42004.json
# Description: This process outlines the establishment of an urban vertical farm integrating advanced hydroponics and IoT monitoring systems. It involves site analysis, modular structure assembly, nutrient solution calibration, climate control optimization, crop selection tailored to urban microclimates, and continuous data-driven adjustments to maximize yield and sustainability. The process also includes community engagement for local sourcing and waste recycling to close the resource loop, ensuring minimal environmental impact and high operational efficiency within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
design_plan    = Transition(label='Design Plan')
structure_build= Transition(label='Structure Build')
system_install = Transition(label='System Install')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_setup  = Transition(label='Climate Setup')
crop_select    = Transition(label='Crop Select')
seed_plant     = Transition(label='Seed Plant')
sensor_deploy  = Transition(label='Sensor Deploy')
data_monitor   = Transition(label='Data Monitor')
growth_track   = Transition(label='Growth Track')
lighting_adjust= Transition(label='Lighting Adjust')
water_cycle    = Transition(label='Water Cycle')
harvest_prep   = Transition(label='Harvest Prep')
waste_recycle  = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')

# Build the adjustment sequence PO: Growth Track -> Lighting Adjust -> Water Cycle
adjust_seq = StrictPartialOrder(nodes=[growth_track, lighting_adjust, water_cycle])
adjust_seq.order.add_edge(growth_track, lighting_adjust)
adjust_seq.order.add_edge(lighting_adjust, water_cycle)

# Loop around Data Monitor and adjustment sequence
# semantics: do data_monitor, then either exit or do adjust_seq then data_monitor again
adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, adjust_seq])

# Main process PO
root = StrictPartialOrder(nodes=[
    site_survey, design_plan, structure_build, system_install,
    nutrient_mix, climate_setup, crop_select, seed_plant,
    sensor_deploy, adjust_loop, harvest_prep,
    waste_recycle, community_meet
])

# Define the main sequence
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(design_plan, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, crop_select)
root.order.add_edge(crop_select, seed_plant)
root.order.add_edge(seed_plant, sensor_deploy)
root.order.add_edge(sensor_deploy, adjust_loop)
root.order.add_edge(adjust_loop, harvest_prep)

# After harvest, do recycling and community engagement in parallel
root.order.add_edge(harvest_prep, waste_recycle)
root.order.add_edge(harvest_prep, community_meet)