# Generated from: 8a227d35-537f-4ece-ad2c-ab1fd7954d87.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponic techniques, environmental monitoring, and automated harvesting. Beginning with seed selection and nutrient calibration, it includes precision climate control, pest detection using AI sensors, and adaptive lighting schedules to optimize plant growth. Post-harvest, produce is quality-checked, packaged, and distributed via local delivery networks, ensuring minimal environmental footprint and fresh supply. The process also incorporates waste recycling and energy recapture to create a sustainable closed-loop system, balancing technological innovation with ecological responsibility in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
seed_selection   = Transition(label='Seed Selection')
nutrient_prep    = Transition(label='Nutrient Prep')
climate_setup    = Transition(label='Climate Setup')
water_cycle      = Transition(label='Water Cycle')
light_adjustment = Transition(label='Light Adjustment')
pest_scan        = Transition(label='Pest Scan')
growth_monitor   = Transition(label='Growth Monitor')
co2_control      = Transition(label='CO2 Control')
harvest_trigger  = Transition(label='Harvest Trigger')
automated_pick   = Transition(label='Automated Pick')
quality_check    = Transition(label='Quality Check')
packaging        = Transition(label='Packaging')
local_dispatch   = Transition(label='Local Dispatch')
waste_sort       = Transition(label='Waste Sort')
energy_reclaim   = Transition(label='Energy Reclaim')
data_logging     = Transition(label='Data Logging')

# Define the main production sub-process (A)
A = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_prep,
    climate_setup,
    water_cycle,
    light_adjustment,
    pest_scan,
    growth_monitor,
    co2_control,
    harvest_trigger,
    automated_pick,
    quality_check,
    packaging,
    local_dispatch
])
# Seed -> Nutrient -> Climate
A.order.add_edge(seed_selection, nutrient_prep)
A.order.add_edge(nutrient_prep, climate_setup)
# After climate setup, environmental controls can run in parallel
for env in [water_cycle, light_adjustment, pest_scan, growth_monitor, co2_control]:
    A.order.add_edge(climate_setup, env)
    A.order.add_edge(env, harvest_trigger)
# Harvest -> Pick -> QC -> Packaging -> Dispatch
A.order.add_edge(harvest_trigger, automated_pick)
A.order.add_edge(automated_pick, quality_check)
A.order.add_edge(quality_check, packaging)
A.order.add_edge(packaging, local_dispatch)

# Define the recycling & data sub-process (B)
B = StrictPartialOrder(nodes=[waste_sort, energy_reclaim, data_logging])
B.order.add_edge(waste_sort, energy_reclaim)
B.order.add_edge(energy_reclaim, data_logging)

# Combine into a loop: execute A, then optionally run B and repeat A, until exit
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, B]
)