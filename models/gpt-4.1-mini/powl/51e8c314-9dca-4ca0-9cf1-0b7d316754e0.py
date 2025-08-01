# Generated from: 51e8c314-9dca-4ca0-9cf1-0b7d316754e0.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to optimize space and resources in dense city environments. It begins with site analysis and zoning compliance checks, followed by infrastructure design tailored to vertical stacking of crops. The workflow includes environmental control calibration, hydroponic system installation, and seedling propagation. Advanced nutrient delivery and pest management protocols are integrated, along with real-time monitoring setup using IoT devices. Staff training on automated systems and continuous yield optimization strategies are conducted. Finally, the process culminates in a phased crop harvesting schedule and waste recycling plan to ensure sustainability and profitability within an atypical urban agricultural model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

site_analysis = Transition(label='Site Analysis')
zoning_review = Transition(label='Zoning Review')

design_layout = Transition(label='Design Layout')
stack_assembly = Transition(label='Stack Assembly')

env_control = Transition(label='Env Control')
hydro_install = Transition(label='Hydro Install')
seed_propagation = Transition(label='Seed Propagation')

nutrient_mix = Transition(label='Nutrient Mix')
pest_monitor = Transition(label='Pest Monitor')

iot_setup = Transition(label='IoT Setup')

staff_training = Transition(label='Staff Training')
yield_audit = Transition(label='Yield Audit')

harvest_plan = Transition(label='Harvest Plan')
waste_manage = Transition(label='Waste Manage')
market_prep = Transition(label='Market Prep')

# Partial order for initial site analysis and zoning review (concurrent)
init_po = StrictPartialOrder(
    nodes=[site_analysis, zoning_review]
)
# No order edges means concurrent activities.

# Infrastructure design partial order: design_layout then stack_assembly
infra_po = StrictPartialOrder(
    nodes=[design_layout, stack_assembly]
)
infra_po.order.add_edge(design_layout, stack_assembly)

# Environmental control calibration, hydroponic install and seed propagation can be concurrent, 
# but need to complete before nutrient_mix and pest_monitor
env_hydro_seed = StrictPartialOrder(
    nodes=[env_control, hydro_install, seed_propagation]
)
# no order edges => concurrent

nutrient_pest = StrictPartialOrder(
    nodes=[nutrient_mix, pest_monitor]
)
# nutrient_mix and pest_monitor can be concurrent

# nutrient_pest start after env_hydro_seed finish
env_and_nutri_po = StrictPartialOrder(
    nodes=[env_hydro_seed, nutrient_pest]
)
env_and_nutri_po.order.add_edge(env_hydro_seed, nutrient_pest)

# iot_setup after nutrient_pest
iot_po = StrictPartialOrder(
    nodes=[nutrient_pest, iot_setup]
)
iot_po.order.add_edge(nutrient_pest, iot_setup)

# Staff training and yield audit can be concurrent after iot_setup
training_yield = StrictPartialOrder(
    nodes=[staff_training, yield_audit]
)

# Both start after iot_setup
start_training_yield_po = StrictPartialOrder(
    nodes=[iot_setup, training_yield]
)
start_training_yield_po.order.add_edge(iot_setup, training_yield)

# Harvest plan and waste manage after training_yield
harvest_waste = StrictPartialOrder(
    nodes=[harvest_plan, waste_manage]
)
# concurrent

after_training_po = StrictPartialOrder(
    nodes=[training_yield, harvest_waste]
)
after_training_po.order.add_edge(training_yield, harvest_waste)

# market prep after harvest and waste
final_po = StrictPartialOrder(
    nodes=[harvest_waste, market_prep]
)
final_po.order.add_edge(harvest_waste, market_prep)

# Now chain all together

# 1. init_po -> infra_po
first_block = StrictPartialOrder(
    nodes=[init_po, infra_po]
)
first_block.order.add_edge(init_po, infra_po)

# 2. infra_po -> env_and_nutri_po (which includes env_hydro_seed and nutrient_pest)
second_block = StrictPartialOrder(
    nodes=[infra_po, env_and_nutri_po]
)
second_block.order.add_edge(infra_po, env_and_nutri_po)

# 3. env_and_nutri_po -> iot_setup (already inside iot_po)

# We have iot_po contains nutrient_pest and iot_setup, nutrient_pest after env_hydro_seed
# To integrate iot_po correctly, we use the env_and_nutri_po as its base and add iot_setup after nutrient_pest

# As env_and_nutri_po already models env_hydro_seed->nutrient_pest,
# just add iot_setup to the order after nutrient_pest
# Done in iot_po

# 4. then iot_po -> training_yield (start_training_yield_po)
# training_yield after iot_setup

# 5. training_yield -> harvest_waste (after_training_po)
# 6. harvest_waste -> market_prep (final_po)

# Now combine all top-level partial orders:
root = StrictPartialOrder(
    nodes=[
        first_block,
        second_block,
        iot_po,
        start_training_yield_po,
        after_training_po,
        final_po
    ]
)

# Add ordering edges to connect blocks in sequence:

root.order.add_edge(first_block, second_block)
root.order.add_edge(second_block, iot_po)
root.order.add_edge(iot_po, start_training_yield_po)
root.order.add_edge(start_training_yield_po, after_training_po)
root.order.add_edge(after_training_po, final_po)