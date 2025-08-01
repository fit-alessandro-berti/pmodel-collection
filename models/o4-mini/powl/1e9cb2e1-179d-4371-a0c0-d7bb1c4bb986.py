# Generated from: 1e9cb2e1-179d-4371-a0c0-d7bb1c4bb986.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a constrained city environment, integrating hydroponic and aeroponic systems. It involves site assessment, modular design, environmental calibration, seed selection, nutrient cycling, pest monitoring, and automated harvesting. The process also includes community engagement, energy optimization, waste recycling, and real-time data analytics to ensure sustainable production and market readiness of fresh produce. Each phase is interdependent, requiring cross-disciplinary coordination between agronomists, engineers, and city planners to maximize yield and minimize ecological footprint in an atypical urban agriculture context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
system_build   = Transition(label='System Build')
env_calibration= Transition(label='Env Calibration')
seed_selection = Transition(label='Seed Selection')
nutrient_mix   = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
pest_scan      = Transition(label='Pest Scan')
growth_monitor = Transition(label='Growth Monitor')
water_cycle    = Transition(label='Water Cycle')
energy_audit   = Transition(label='Energy Audit')
waste_process  = Transition(label='Waste Process')
harvest_plan   = Transition(label='Harvest Plan')
data_sync      = Transition(label='Data Sync')
market_prep    = Transition(label='Market Prep')
community_meet = Transition(label='Community Meet')

# Silent transition for loop re-entry
skip = SilentTransition()

# Define the monitoring & maintenance body
monitor_body = StrictPartialOrder(nodes=[pest_scan, growth_monitor, water_cycle, energy_audit, waste_process])
monitor_body.order.add_edge(pest_scan, growth_monitor)
monitor_body.order.add_edge(growth_monitor, water_cycle)
monitor_body.order.add_edge(water_cycle, energy_audit)
monitor_body.order.add_edge(energy_audit, waste_process)

# Loop: repeat monitoring_body until exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, skip])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_build, env_calibration,
    seed_selection, nutrient_mix, planting_setup,
    monitor_loop, harvest_plan, data_sync, market_prep,
    community_meet
])
root.order.add_edge(site_survey,    design_layout)
root.order.add_edge(design_layout,  system_build)
root.order.add_edge(system_build,   env_calibration)
root.order.add_edge(env_calibration, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix,   planting_setup)
root.order.add_edge(planting_setup, monitor_loop)
root.order.add_edge(monitor_loop,   harvest_plan)
root.order.add_edge(harvest_plan,   data_sync)
root.order.add_edge(data_sync,      market_prep)

# 'community_meet' is left unconstrained to run concurrently at any point