# Generated from: 1ffd4d38-9ff8-40e7-ac13-2c70c732ed40.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It covers initial site assessment, modular system design tailored to limited urban spaces, installation of IoT-enabled climate controls, selection and sourcing of crop varieties adapted for vertical growth, integration of renewable energy sources, automated nutrient delivery setup, pest management using biocontrol agents, staff training on specialized equipment, pilot crop cycles for yield optimization, real-time data monitoring and analysis, compliance with local zoning and health regulations, marketing strategy development focused on sustainability, and the final commercial launch aimed at supplying local markets efficiently while reducing carbon footprint and water usage significantly.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
iot_setup = Transition(label='IoT Setup')
crop_selection = Transition(label='Crop Selection')
energy_install = Transition(label='Energy Install')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
pilot_cycle = Transition(label='Pilot Cycle')
data_monitor = Transition(label='Data Monitor')
regulation_check = Transition(label='Regulation Check')
market_plan = Transition(label='Market Plan')
launch_prep = Transition(label='Launch Prep')
supply_chain = Transition(label='Supply Chain')

# Model logical groupings or concurrency:
# After 'Site Survey' -> 'Design Layout' -> 'System Build' -> 'IoT Setup'
# 'Crop Selection', 'Energy Install', 'Nutrient Mix', 'Pest Control' can be done concurrently after system build/iot setup
# Then 'Staff Training' and 'Pilot Cycle' after that
# Then 'Data Monitor' and 'Regulation Check' concurrently after pilot cycle
# Then 'Market Plan' after regulation check
# Then 'Launch Prep' after market plan
# Then final 'Supply Chain'

# First partial order for initial steps
initial_PO = StrictPartialOrder(nodes=[site_survey, design_layout, system_build, iot_setup])
initial_PO.order.add_edge(site_survey, design_layout)
initial_PO.order.add_edge(design_layout, system_build)
initial_PO.order.add_edge(system_build, iot_setup)

# Concurrent setup activities after IoT Setup
setup_steps = StrictPartialOrder(nodes=[crop_selection, energy_install, nutrient_mix, pest_control])
# concurrent so no edges

# After IoT Setup -> all setup steps concurrently
# We'll connect iot_setup to each setup activity in a larger PO
setup_PO = StrictPartialOrder(nodes=[iot_setup, crop_selection, energy_install, nutrient_mix, pest_control])
setup_PO.order.add_edge(iot_setup, crop_selection)
setup_PO.order.add_edge(iot_setup, energy_install)
setup_PO.order.add_edge(iot_setup, nutrient_mix)
setup_PO.order.add_edge(iot_setup, pest_control)

# Staff Training after all setup steps - so after a partial order of all setup steps
# We can model setup steps partial order + edges to staff_training
setup_staff_PO = StrictPartialOrder(
    nodes=[crop_selection, energy_install, nutrient_mix, pest_control, staff_training])
setup_staff_PO.order.add_edge(crop_selection, staff_training)
setup_staff_PO.order.add_edge(energy_install, staff_training)
setup_staff_PO.order.add_edge(nutrient_mix, staff_training)
setup_staff_PO.order.add_edge(pest_control, staff_training)

# Pilot Cycle after Staff Training
staff_pilot_PO = StrictPartialOrder(nodes=[staff_training, pilot_cycle])
staff_pilot_PO.order.add_edge(staff_training, pilot_cycle)

# Data Monitor and Regulation Check concurrently after Pilot Cycle
post_pilot_PO = StrictPartialOrder(nodes=[pilot_cycle, data_monitor, regulation_check])
post_pilot_PO.order.add_edge(pilot_cycle, data_monitor)
post_pilot_PO.order.add_edge(pilot_cycle, regulation_check)

# Market Plan after Regulation Check
reg_market_PO = StrictPartialOrder(nodes=[regulation_check, market_plan])
reg_market_PO.order.add_edge(regulation_check, market_plan)

# Launch Prep after Market Plan
mp_launch_PO = StrictPartialOrder(nodes=[market_plan, launch_prep])
mp_launch_PO.order.add_edge(market_plan, launch_prep)

# Supply Chain after Launch Prep
launch_supply_PO = StrictPartialOrder(nodes=[launch_prep, supply_chain])
launch_supply_PO.order.add_edge(launch_prep, supply_chain)

# Now combine all partial orders into one big PO,
# with edges to bind them together:

# Combine all basic nodes into one StrictPartialOrder
# We first merge all nodes (without duplicates)
all_nodes = {
    site_survey, design_layout, system_build, iot_setup,
    crop_selection, energy_install, nutrient_mix, pest_control,
    staff_training, pilot_cycle, data_monitor, regulation_check,
    market_plan, launch_prep, supply_chain
}

root = StrictPartialOrder(nodes=list(all_nodes))

# Add edges corresponding to each partial order:

# initial_PO edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build)
root.order.add_edge(system_build, iot_setup)

# setup_PO edges (from IoT Setup to parallel setup steps)
root.order.add_edge(iot_setup, crop_selection)
root.order.add_edge(iot_setup, energy_install)
root.order.add_edge(iot_setup, nutrient_mix)
root.order.add_edge(iot_setup, pest_control)

# setup_staff_PO edges (from all setup steps to Staff Training)
root.order.add_edge(crop_selection, staff_training)
root.order.add_edge(energy_install, staff_training)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(pest_control, staff_training)

# Staff Training to Pilot Cycle
root.order.add_edge(staff_training, pilot_cycle)

# Pilot Cycle to Data Monitor and Regulation Check
root.order.add_edge(pilot_cycle, data_monitor)
root.order.add_edge(pilot_cycle, regulation_check)

# Regulation Check to Market Plan
root.order.add_edge(regulation_check, market_plan)

# Market Plan to Launch Prep
root.order.add_edge(market_plan, launch_prep)

# Launch Prep to Supply Chain
root.order.add_edge(launch_prep, supply_chain)