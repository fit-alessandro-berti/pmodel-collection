# Generated from: 917d80e7-6bd9-4d61-a49d-021454db168c.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular structure assembly, climate control system installation, nutrient solution preparation, and crop selection tailored to indoor environments. Continuous monitoring and automated adjustments optimize plant growth while integrating waste recycling and energy-saving mechanisms. The process concludes with harvesting protocols and market distribution planning, ensuring sustainable urban agriculture with minimal environmental impact and maximum yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
lighting_install = Transition(label='Lighting Install')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
seed_plant = Transition(label='Seed Plant')
irrigation_test = Transition(label='Irrigation Test')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
waste_cycle = Transition(label='Waste Cycle')
energy_audit = Transition(label='Energy Audit')
harvest_plan = Transition(label='Harvest Plan')
market_prep = Transition(label='Market Prep')
logistics_coord = Transition(label='Logistics Coord')

# Build sub-processes and order relations based on the description

# Initial site analysis and design layout sequence
initial_seq = StrictPartialOrder(nodes=[site_survey, design_layout])
initial_seq.order.add_edge(site_survey, design_layout)

# Modular structure assembly after design
modular_seq = StrictPartialOrder(nodes=[modular_build, climate_setup, lighting_install])
modular_seq.order.add_edge(modular_build, climate_setup)
modular_seq.order.add_edge(climate_setup, lighting_install)

# Nutrient and crop setup sequence
nutrient_crop_seq = StrictPartialOrder(nodes=[nutrient_mix, crop_select, seed_plant])
nutrient_crop_seq.order.add_edge(nutrient_mix, crop_select)
nutrient_crop_seq.order.add_edge(crop_select, seed_plant)

# Irrigation testing after seeding
irrigation_test_seq = StrictPartialOrder(nodes=[seed_plant, irrigation_test])
irrigation_test_seq.order.add_edge(seed_plant, irrigation_test)

# Continuous monitoring and pest control loop with waste and energy management integrated
# Define monitoring and pest control sequence
monitor_pest = StrictPartialOrder(nodes=[growth_monitor, pest_control])
monitor_pest.order.add_edge(growth_monitor, pest_control)

# Waste and energy management in parallel (concurrent)
waste_energy = StrictPartialOrder(nodes=[waste_cycle, energy_audit])
# no edges since they are concurrent

# Combine monitoring/pest and waste/energy in parallel (partial order with no edges between them)
monitor_pest_waste_energy = StrictPartialOrder(
    nodes=[monitor_pest, waste_energy]
)
# no edges between these two nodes => concurrent

# Build LOOP:
# Execute monitor_pest_waste_energy, then loop back or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_pest_waste_energy, SilentTransition()])

# Final harvesting and distribution sequence
harvest_dist = StrictPartialOrder(nodes=[harvest_plan, market_prep, logistics_coord])
harvest_dist.order.add_edge(harvest_plan, market_prep)
harvest_dist.order.add_edge(market_prep, logistics_coord)

# Assemble the entire process partial order
root = StrictPartialOrder(
    nodes=[
        initial_seq,
        modular_seq,
        nutrient_crop_seq,
        irrigation_test_seq,
        loop,
        harvest_dist
    ]
)

# Add dependencies based on the process flow
root.order.add_edge(initial_seq, modular_seq)
root.order.add_edge(modular_seq, nutrient_crop_seq)
root.order.add_edge(nutrient_crop_seq, irrigation_test_seq)
root.order.add_edge(irrigation_test_seq, loop)
root.order.add_edge(loop, harvest_dist)