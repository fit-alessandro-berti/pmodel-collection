# Generated from: ef4c7e9b-2e50-4a92-9d87-411a39fe63cb.json
# Description: This process describes the intricate operations involved in managing an urban vertical farming facility, integrating advanced hydroponics, AI-based growth monitoring, and automated logistics. Starting from seed selection and nutrient mixing, the cycle includes environmental calibration, pest detection using machine vision, dynamic lighting adjustment, and robotic harvesting. Post-harvest activities involve quality inspection, data logging, and packaging optimization. The process also covers waste recycling, energy consumption analysis, and supply chain coordination with local retailers, ensuring sustainability while maximizing yield and freshness in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
pest_scan = Transition(label='Pest Scan')
light_control = Transition(label='Light Control')
growth_monitor = Transition(label='Growth Monitor')
water_cycle = Transition(label='Water Cycle')
air_quality = Transition(label='Air Quality')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
data_logging = Transition(label='Data Logging')
packaging = Transition(label='Packaging')
waste_sort = Transition(label='Waste Sort')
energy_audit = Transition(label='Energy Audit')
retail_sync = Transition(label='Retail Sync')

# Construct the POWL structure of the process

# Initial preparation partial order (seed selection → nutrient mix → environment setup)
prep = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup])
prep.order.add_edge(seed_selection, nutrient_mix)
prep.order.add_edge(nutrient_mix, environment_setup)

# Growing cycle partial order:
# Pest scan and light control can happen after environment setup, concurrently
# Growth monitor depends on pest_scan and light_control and runs concurrently with water_cycle and air_quality
growing_1 = StrictPartialOrder(
    nodes=[environment_setup, pest_scan, light_control, growth_monitor, water_cycle, air_quality]
)
growing_1.order.add_edge(environment_setup, pest_scan)
growing_1.order.add_edge(environment_setup, light_control)
growing_1.order.add_edge(pest_scan, growth_monitor)
growing_1.order.add_edge(light_control, growth_monitor)
# water_cycle and air_quality run in parallel after environment setup (no order edges needed from environment_setup)
growing_1.order.add_edge(environment_setup, water_cycle)
growing_1.order.add_edge(environment_setup, air_quality)

# Harvesting node after growth monitor completes
harvest = robotic_harvest

# Post-harvest partial order: quality check → data logging → packaging
post_harvest = StrictPartialOrder(nodes=[quality_check, data_logging, packaging])
post_harvest.order.add_edge(quality_check, data_logging)
post_harvest.order.add_edge(data_logging, packaging)

# Sustainability parallel activities: waste sort, energy audit, retail sync
sustainability = StrictPartialOrder(nodes=[waste_sort, energy_audit, retail_sync])
# no order - all concurrent

# Loop over the growing cycle part (growth & environment adjustments + harvest + post-harvest)
# We model a LOOP to represent repeating cycles of growth, harvest, and post-harvest activities

# Body of loop: growing + harvest + post-harvest
body = StrictPartialOrder(nodes=[growing_1, harvest, post_harvest])
body.order.add_edge(growing_1, harvest)
body.order.add_edge(harvest, post_harvest)

# Loop: execute prep once, then loop body (grow→harvest→post-harvest), repeat growing cycles until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, SilentTransition()])  # B is silent transition: exit

# Root PO: prep → loop with sustainability running concurrent to it
root = StrictPartialOrder(nodes=[prep, loop, sustainability])
root.order.add_edge(prep, loop)
# sustainability parallel, no edges to/from sustainability nodes allowing concurrency