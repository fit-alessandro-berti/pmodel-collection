# Generated from: 917d80e7-6bd9-4d61-a49d-021454db168c.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular structure assembly, climate control system installation, nutrient solution preparation, and crop selection tailored to indoor environments. Continuous monitoring and automated adjustments optimize plant growth while integrating waste recycling and energy-saving mechanisms. The process concludes with harvesting protocols and market distribution planning, ensuring sustainable urban agriculture with minimal environmental impact and maximum yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
modular_build  = Transition(label='Modular Build')
climate_setup  = Transition(label='Climate Setup')
lighting_install = Transition(label='Lighting Install')
nutrient_mix   = Transition(label='Nutrient Mix')
crop_select    = Transition(label='Crop Select')
seed_plant     = Transition(label='Seed Plant')
irrigation_test= Transition(label='Irrigation Test')
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
waste_cycle    = Transition(label='Waste Cycle')
energy_audit   = Transition(label='Energy Audit')
harvest_plan   = Transition(label='Harvest Plan')
market_prep    = Transition(label='Market Prep')
logistics_coord= Transition(label='Logistics Coord')

# Define the "adjustments" sub‐graph (concurrent pest control, waste cycle, energy audit)
adjustments = StrictPartialOrder(
    nodes=[pest_control, waste_cycle, energy_audit]
)
# no edges => they can occur in parallel

# Define the monitoring/adjustment loop: (* (Growth Monitor, adjustments))
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, adjustments]
)

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        modular_build,
        climate_setup,
        lighting_install,
        nutrient_mix,
        crop_select,
        seed_plant,
        irrigation_test,
        monitor_loop,
        harvest_plan,
        market_prep,
        logistics_coord
    ]
)

# Add ordering constraints
o = root.order
o.add_edge(site_survey,   design_layout)
o.add_edge(design_layout, modular_build)
# After the structure is built, climate and lighting can be done in parallel
o.add_edge(modular_build, climate_setup)
o.add_edge(modular_build, lighting_install)
# Nutrient mix after both climate & lighting
o.add_edge(climate_setup, nutrient_mix)
o.add_edge(lighting_install, nutrient_mix)
# Crop selection, seeding, irrigation in sequence
o.add_edge(nutrient_mix,  crop_select)
o.add_edge(crop_select,   seed_plant)
o.add_edge(seed_plant,    irrigation_test)
# Then enter the continuous monitoring/adjustment loop
o.add_edge(irrigation_test, monitor_loop)
# After exiting the loop, harvesting and distribution
o.add_edge(monitor_loop,   harvest_plan)
o.add_edge(harvest_plan,   market_prep)
o.add_edge(market_prep,    logistics_coord)