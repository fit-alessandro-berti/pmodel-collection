# Generated from: f7af61c2-a8e6-4ba7-ab35-c489351b29ed.json
# Description: This process involves establishing a fully operational urban vertical farming system within a repurposed industrial building. It begins with site analysis and structural assessment, followed by modular farm design and environmental control installation. The process then moves to nutrient solution preparation, seed selection, and automated planting. Continuous monitoring of microclimate and plant health is conducted through IoT sensors, with adaptive lighting and irrigation adjustments. Waste recycling and energy optimization are integrated to ensure sustainability. Finally, the system undergoes rigorous quality assurance before commercial crop harvesting and distribution logistics are initiated, enabling efficient year-round urban agriculture production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_analysis    = Transition(label='Site Analysis')
structure_check  = Transition(label='Structure Check')
farm_design      = Transition(label='Farm Design')
env_control      = Transition(label='Env Control')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_selection   = Transition(label='Seed Selection')
automated_plant  = Transition(label='Automated Plant')
sensor_setup     = Transition(label='Sensor Setup')
micro_mon        = Transition(label='Microclimate Mon')
health_mon       = Transition(label='Health Monitor')
light_adjust     = Transition(label='Light Adjust')
irrigation_mod   = Transition(label='Irrigation Mod')
waste_recycle    = Transition(label='Waste Recycle')
energy_optimize  = Transition(label='Energy Optimize')
quality_check    = Transition(label='Quality Check')
crop_harvest     = Transition(label='Crop Harvest')
distribution_pl  = Transition(label='Distribution Plan')

# Build the monitoring-and-adjustment cycle as a partial order
monitor_cycle = StrictPartialOrder(nodes=[micro_mon, health_mon, light_adjust, irrigation_mod])
monitor_cycle.order.add_edge(micro_mon, health_mon)
monitor_cycle.order.add_edge(health_mon, light_adjust)
monitor_cycle.order.add_edge(light_adjust, irrigation_mod)

# Wrap the cycle in a LOOP operator to allow repeated monitoring & adjustment
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_cycle, monitor_cycle])

# Build the top‐level partially ordered workflow
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    farm_design,
    env_control,
    nutrient_prep,
    seed_selection,
    automated_plant,
    sensor_setup,
    monitor_loop,
    waste_recycle,
    energy_optimize,
    quality_check,
    crop_harvest,
    distribution_pl
])

# Sequential dependencies for setup phases
root.order.add_edge(site_analysis,   structure_check)
root.order.add_edge(structure_check, farm_design)
root.order.add_edge(farm_design,     env_control)
root.order.add_edge(env_control,     nutrient_prep)
root.order.add_edge(nutrient_prep,   seed_selection)
root.order.add_edge(seed_selection,  automated_plant)
root.order.add_edge(automated_plant, sensor_setup)

# After sensor setup, start concurrent sustainability & monitoring
root.order.add_edge(sensor_setup, monitor_loop)
root.order.add_edge(sensor_setup, waste_recycle)
root.order.add_edge(sensor_setup, energy_optimize)

# After all sustainability/monitoring activities complete, do quality check
root.order.add_edge(monitor_loop,   quality_check)
root.order.add_edge(waste_recycle,  quality_check)
root.order.add_edge(energy_optimize, quality_check)

# Final sequential wrap‐up
root.order.add_edge(quality_check,  crop_harvest)
root.order.add_edge(crop_harvest,   distribution_pl)