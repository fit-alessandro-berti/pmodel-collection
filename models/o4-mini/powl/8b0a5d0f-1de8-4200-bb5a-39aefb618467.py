# Generated from: 8b0a5d0f-1de8-4200-bb5a-39aefb618467.json
# Description: This process involves the end-to-end setup and operationalization of an urban vertical farming system within a repurposed industrial building. It begins with site assessment and environmental analysis, followed by modular rack installation and hydroponic system integration. Subsequent steps include seed selection, nutrient calibration, and automated climate control programming. The process also covers pest monitoring using AI-driven sensors, energy optimization via smart grids, crop growth tracking through IoT devices, and waste recycling for zero-impact sustainability. Finally, it concludes with harvest scheduling, packaging automation, and distribution logistics coordination, ensuring fresh produce delivery within tight urban supply chains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
site_assess        = Transition(label='Site Assess')
env_analyze        = Transition(label='Env Analyze')
rack_install       = Transition(label='Rack Install')
hydro_setup        = Transition(label='Hydro Setup')
seed_select        = Transition(label='Seed Select')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
climate_program    = Transition(label='Climate Program')
pest_monitor       = Transition(label='Pest Monitor')
energy_optimize    = Transition(label='Energy Optimize')
growth_track       = Transition(label='Growth Track')
waste_recycle      = Transition(label='Waste Recycle')
harvest_schedule   = Transition(label='Harvest Schedule')
package_automate   = Transition(label='Package Automate')
logistics_plan     = Transition(label='Logistics Plan')
supply_chain       = Transition(label='Supply Chain')

# Collect them in a list to define the sequential order
nodes = [
    site_assess,
    env_analyze,
    rack_install,
    hydro_setup,
    seed_select,
    nutrient_calibrate,
    climate_program,
    pest_monitor,
    energy_optimize,
    growth_track,
    waste_recycle,
    harvest_schedule,
    package_automate,
    logistics_plan,
    supply_chain
]

# Build a strict partial order where each activity follows its predecessor
root = StrictPartialOrder(nodes=nodes)
for predecessor, successor in zip(nodes, nodes[1:]):
    root.order.add_edge(predecessor, successor)