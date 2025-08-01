# Generated from: 1bba2009-03b1-4712-8021-3d9757dc9351.json
# Description: This process outlines the establishment of an urban vertical farm inside a repurposed high-rise building. It involves initial site evaluation, structural adaptation for hydroponic systems, environmental controls installation, crop selection based on urban microclimates, seedling propagation, nutrient solution preparation, automated monitoring setup, pest control strategies, harvesting schedules, post-harvest processing, packaging optimization for local distribution, waste recycling protocols, energy consumption tracking, and continuous improvement cycles to maximize yield and sustainability in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_retrofit = Transition(label='Structure Retrofit')
system_install   = Transition(label='System Install')
crop_select      = Transition(label='Crop Select')
seedling_prep    = Transition(label='Seedling Prep')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_setup     = Transition(label='Sensor Setup')
pest_control     = Transition(label='Pest Control')
water_cycle      = Transition(label='Water Cycle')
lighting_adjust  = Transition(label='Lighting Adjust')
harvest_plan     = Transition(label='Harvest Plan')
post_harvest     = Transition(label='Post Harvest')
packaging        = Transition(label='Packaging')
waste_process    = Transition(label='Waste Process')
energy_audit     = Transition(label='Energy Audit')

# Define the continuous improvement loop: Waste Process -> Energy Audit, then repeat or exit
improve_cycle = StrictPartialOrder(nodes=[waste_process, energy_audit])
improve_cycle.order.add_edge(waste_process, energy_audit)
improve_loop = OperatorPOWL(operator=Operator.LOOP, children=[improve_cycle, SilentTransition()])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_retrofit, system_install, crop_select, seedling_prep,
    nutrient_mix, sensor_setup, pest_control, water_cycle, lighting_adjust,
    harvest_plan, post_harvest, packaging, improve_loop
])

# Add the sequential dependencies
root.order.add_edge(site_survey, structure_retrofit)
root.order.add_edge(structure_retrofit, system_install)
root.order.add_edge(system_install, crop_select)
root.order.add_edge(crop_select, seedling_prep)
root.order.add_edge(seedling_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, pest_control)
root.order.add_edge(pest_control, water_cycle)
root.order.add_edge(water_cycle, lighting_adjust)
root.order.add_edge(lighting_adjust, harvest_plan)
root.order.add_edge(harvest_plan, post_harvest)
root.order.add_edge(post_harvest, packaging)
root.order.add_edge(packaging, improve_loop)  # enter the improvement loop