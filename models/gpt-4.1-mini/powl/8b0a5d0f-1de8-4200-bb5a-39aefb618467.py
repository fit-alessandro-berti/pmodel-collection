# Generated from: 8b0a5d0f-1de8-4200-bb5a-39aefb618467.json
# Description: This process involves the end-to-end setup and operationalization of an urban vertical farming system within a repurposed industrial building. It begins with site assessment and environmental analysis, followed by modular rack installation and hydroponic system integration. Subsequent steps include seed selection, nutrient calibration, and automated climate control programming. The process also covers pest monitoring using AI-driven sensors, energy optimization via smart grids, crop growth tracking through IoT devices, and waste recycling for zero-impact sustainability. Finally, it concludes with harvest scheduling, packaging automation, and distribution logistics coordination, ensuring fresh produce delivery within tight urban supply chains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions with given labels
site_assess = Transition(label='Site Assess')
env_analyze = Transition(label='Env Analyze')
rack_install = Transition(label='Rack Install')
hydro_setup = Transition(label='Hydro Setup')
seed_select = Transition(label='Seed Select')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
climate_program = Transition(label='Climate Program')
pest_monitor = Transition(label='Pest Monitor')
energy_optimize = Transition(label='Energy Optimize')
growth_track = Transition(label='Growth Track')
waste_recycle = Transition(label='Waste Recycle')
harvest_schedule = Transition(label='Harvest Schedule')
package_automate = Transition(label='Package Automate')
logistics_plan = Transition(label='Logistics Plan')
supply_chain = Transition(label='Supply Chain')

# Construct partial order with dependencies as per described sequence

# Phase 1: Site assessment and environmental analysis (sequential)
# Phase 2: Modular rack installation and hydroponic system integration (sequential)
# Phase 3: Seed selection, nutrient calibration, automated climate control (sequential)
# Phase 4: Pest monitoring, energy optimization, crop growth tracking, waste recycling (mostly concurrent after phase 3)
# Phase 5: Harvest scheduling, packaging automation, logistics planning and supply chain (sequential)

# We create the nodes list
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
    supply_chain,
]

# Define partial order edges reflecting dependencies:

# Phase 1 order
# Site Assess --> Env Analyze
# Phase 2 starts after Env Analyze
# Env Analyze --> Rack Install --> Hydro Setup
# Phase 3 after Hydro Setup
# Hydro Setup --> Seed Select --> Nutrient Calibrate --> Climate Program
# Phase 4 after Climate Program; pest_monitor, energy_optimize, growth_track, waste_recycle run concurrent (no order among them but all depend on Climate Program)
# Phase 5 after all 4 above; harvest_schedule --> package_automate --> logistics_plan --> supply_chain

order = set()

order.add((site_assess, env_analyze))

order.add((env_analyze, rack_install))
order.add((rack_install, hydro_setup))

order.add((hydro_setup, seed_select))
order.add((seed_select, nutrient_calibrate))
order.add((nutrient_calibrate, climate_program))

order.add((climate_program, pest_monitor))
order.add((climate_program, energy_optimize))
order.add((climate_program, growth_track))
order.add((climate_program, waste_recycle))

# all 4 phase 4 activities must complete before phase 5
# connect each phase4 activity to harvest_schedule
order.add((pest_monitor, harvest_schedule))
order.add((energy_optimize, harvest_schedule))
order.add((growth_track, harvest_schedule))
order.add((waste_recycle, harvest_schedule))

order.add((harvest_schedule, package_automate))
order.add((package_automate, logistics_plan))
order.add((logistics_plan, supply_chain))

root = StrictPartialOrder(nodes=nodes)
for src, tgt in order:
    root.order.add_edge(src, tgt)