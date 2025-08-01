# Generated from: 1ffd4d38-9ff8-40e7-ac13-2c70c732ed40.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It covers initial site assessment, modular system design tailored to limited urban spaces, installation of IoT-enabled climate controls, selection and sourcing of crop varieties adapted for vertical growth, integration of renewable energy sources, automated nutrient delivery setup, pest management using biocontrol agents, staff training on specialized equipment, pilot crop cycles for yield optimization, real-time data monitoring and analysis, compliance with local zoning and health regulations, marketing strategy development focused on sustainability, and the final commercial launch aimed at supplying local markets efficiently while reducing carbon footprint and water usage significantly.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_survey   = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build  = Transition(label='System Build')
iot_setup     = Transition(label='IoT Setup')
crop_selection= Transition(label='Crop Selection')
energy_install= Transition(label='Energy Install')
nutrient_mix  = Transition(label='Nutrient Mix')
pest_control  = Transition(label='Pest Control')
staff_training= Transition(label='Staff Training')
pilot_cycle   = Transition(label='Pilot Cycle')
data_monitor  = Transition(label='Data Monitor')
regulation_check = Transition(label='Regulation Check')
market_plan   = Transition(label='Market Plan')
launch_prep   = Transition(label='Launch Prep')
supply_chain  = Transition(label='Supply Chain')

# Build the partial order (sequential)
nodes = [
    site_survey,
    design_layout,
    system_build,
    iot_setup,
    crop_selection,
    energy_install,
    nutrient_mix,
    pest_control,
    staff_training,
    pilot_cycle,
    data_monitor,
    regulation_check,
    market_plan,
    launch_prep,
    supply_chain
]

root = StrictPartialOrder(nodes=nodes)
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)