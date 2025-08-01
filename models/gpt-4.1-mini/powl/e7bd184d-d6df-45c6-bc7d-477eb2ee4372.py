# Generated from: e7bd184d-d6df-45c6-bc7d-477eb2ee4372.json
# Description: This process involves establishing an urban vertical farm within a repurposed industrial building. It starts with site analysis and structural assessment, followed by environmental system design including hydroponics and aeroponics integration. The process continues with procuring specialized lighting and water recycling systems, then installing modular growing racks. Next, seed selection and germination protocols are established alongside nutrient formula calibration. Staff training on automated monitoring and pest management takes place before launching a pilot crop cycle. Data collection and yield optimization conclude the process, ensuring sustainable urban agriculture with minimal environmental impact and maximized crop density in limited space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')

enviro_design = Transition(label='Enviro Design')
hydro_setup = Transition(label='Hydro Setup')
aeroponics_add = Transition(label='Aeroponics Add')

lighting_procure = Transition(label='Lighting Procure')
water_recycle = Transition(label='Water Recycle')

rack_install = Transition(label='Rack Install')

seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
nutrient_mix = Transition(label='Nutrient Mix')

staff_train = Transition(label='Staff Train')
pest_control = Transition(label='Pest Control')

pilot_crop = Transition(label='Pilot Crop')

data_gather = Transition(label='Data Gather')
yield_optimize = Transition(label='Yield Optimize')

# Environmental system design partial order: Enviro Design --> Hydro Setup --> Aeroponics Add
enviro_system_po = StrictPartialOrder(
    nodes=[enviro_design, hydro_setup, aeroponics_add]
)
enviro_system_po.order.add_edge(enviro_design, hydro_setup)
enviro_system_po.order.add_edge(hydro_setup, aeroponics_add)

# Seed and nutrient partial order: Seed Select --> Germinate Seeds, Seed Select --> Nutrient Mix (concurrent branches)
seed_nutrient_po = StrictPartialOrder(
    nodes=[seed_select, germinate_seeds, nutrient_mix]
)
seed_nutrient_po.order.add_edge(seed_select, germinate_seeds)
seed_nutrient_po.order.add_edge(seed_select, nutrient_mix)

# Staff training partial order: Staff Train --> Pest Control
staff_training_po = StrictPartialOrder(
    nodes=[staff_train, pest_control]
)
staff_training_po.order.add_edge(staff_train, pest_control)

# Data gather and yield optimize partial order: Data Gather --> Yield Optimize
data_yield_po = StrictPartialOrder(
    nodes=[data_gather, yield_optimize]
)
data_yield_po.order.add_edge(data_gather, yield_optimize)

# First phase partial order: Site Analysis --> Structure Check --> Enviro System --> Procurements --> Rack Install
first_phase_po = StrictPartialOrder(
    nodes=[site_analysis, structure_check, enviro_system_po, lighting_procure, water_recycle, rack_install]
)
first_phase_po.order.add_edge(site_analysis, structure_check)
first_phase_po.order.add_edge(structure_check, enviro_system_po)
first_phase_po.order.add_edge(enviro_system_po, lighting_procure)
first_phase_po.order.add_edge(enviro_system_po, water_recycle)
first_phase_po.order.add_edge(lighting_procure, rack_install)
first_phase_po.order.add_edge(water_recycle, rack_install)

# Second phase partial order: Seed and nutrient --> Staff training --> Pilot crop
second_phase_po = StrictPartialOrder(
    nodes=[seed_nutrient_po, staff_training_po, pilot_crop]
)
second_phase_po.order.add_edge(seed_nutrient_po, staff_training_po)
second_phase_po.order.add_edge(staff_training_po, pilot_crop)

# Final phase partial order: Pilot crop --> Data gather & yield optimize (with their PO)
final_phase_po = StrictPartialOrder(
    nodes=[pilot_crop, data_yield_po]
)
final_phase_po.order.add_edge(pilot_crop, data_yield_po)

# Combine all main phases into root partial order
root = StrictPartialOrder(
    nodes=[first_phase_po, second_phase_po, final_phase_po]
)
root.order.add_edge(first_phase_po, second_phase_po)
root.order.add_edge(second_phase_po, final_phase_po)