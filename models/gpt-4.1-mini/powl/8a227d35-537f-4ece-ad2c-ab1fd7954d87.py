# Generated from: 8a227d35-537f-4ece-ad2c-ab1fd7954d87.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponic techniques, environmental monitoring, and automated harvesting. Beginning with seed selection and nutrient calibration, it includes precision climate control, pest detection using AI sensors, and adaptive lighting schedules to optimize plant growth. Post-harvest, produce is quality-checked, packaged, and distributed via local delivery networks, ensuring minimal environmental footprint and fresh supply. The process also incorporates waste recycling and energy recapture to create a sustainable closed-loop system, balancing technological innovation with ecological responsibility in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Prep = Transition(label='Nutrient Prep')
Climate_Setup = Transition(label='Climate Setup')
Water_Cycle = Transition(label='Water Cycle')
Light_Adjustment = Transition(label='Light Adjustment')
Pest_Scan = Transition(label='Pest Scan')
Growth_Monitor = Transition(label='Growth Monitor')
CO2_Control = Transition(label='CO2 Control')
Harvest_Trigger = Transition(label='Harvest Trigger')
Quality_Check = Transition(label='Quality Check')
Automated_Pick = Transition(label='Automated Pick')
Packaging = Transition(label='Packaging')
Waste_Sort = Transition(label='Waste Sort')
Energy_Reclaim = Transition(label='Energy Reclaim')
Local_Dispatch = Transition(label='Local Dispatch')
Data_Logging = Transition(label='Data Logging')

# Build partial orders for preparatory phase (Seed Selection -> Nutrient Prep)
prep_phase = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Prep])
prep_phase.order.add_edge(Seed_Selection, Nutrient_Prep)

# Environment control phase: Climate Setup -> concurrent activities: Water Cycle, CO2 Control, Light Adjustment
# After environment configured Water Cycle, CO2 Control and Light Adjustment run concurrently in monitoring loop with Pest Scan and Growth Monitor
env_setup = StrictPartialOrder(nodes=[Climate_Setup, Water_Cycle, CO2_Control, Light_Adjustment])
env_setup.order.add_edge(Climate_Setup, Water_Cycle)
env_setup.order.add_edge(Climate_Setup, CO2_Control)
env_setup.order.add_edge(Climate_Setup, Light_Adjustment)

# Monitoring activities concurrent: Pest Scan, Growth Monitor, Data Logging
monitoring = StrictPartialOrder(nodes=[Pest_Scan, Growth_Monitor, Data_Logging])
# no order edges, fully concurrent

# Loop for environment & monitoring repeated cycles, adapting Light Adjustment and CO2 Control before Harvest Trigger
# Build loop: loop body (B) contains monitoring + adjustments (Light_Adjustment, CO2_Control)
# Seed phase (A) is Harvest Trigger, but it should run after loop
# This is logically: execute (loop body B) then execute Harvest Trigger (A) when loop ends

# However according to LOOP definition: * (A,B): execute A once, then either exit or execute B then A again
# Our process:
# After preparatory and environment setup, we enter a loop where:
#   - Harvest Trigger is A (executed each iteration)
#   - B is monitoring + adjustments that happen before next harvest cycle

loop_body = StrictPartialOrder(nodes=[Pest_Scan, Growth_Monitor, Data_Logging, Light_Adjustment, CO2_Control])
# No edges → concurrent

loop = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Trigger, loop_body])

# Post-harvest activities sequence
post_harvest = StrictPartialOrder(nodes=[Quality_Check, Automated_Pick, Packaging, Local_Dispatch])
post_harvest.order.add_edge(Quality_Check, Automated_Pick)
post_harvest.order.add_edge(Automated_Pick, Packaging)
post_harvest.order.add_edge(Packaging, Local_Dispatch)

# Sustainability concurrent after or during process - Waste Sort and Energy Reclaim
sustainability = StrictPartialOrder(nodes=[Waste_Sort, Energy_Reclaim])
# no order edges, concurrent

# Compose main flow: prep_phase -> env_setup -> loop -> post_harvest
# sustainability happens concurrently with post_harvest or at end
main_flow = StrictPartialOrder(
    nodes=[prep_phase, env_setup, loop, post_harvest, sustainability]
)
main_flow.order.add_edge(prep_phase, env_setup)
main_flow.order.add_edge(env_setup, loop)
main_flow.order.add_edge(loop, post_harvest)
main_flow.order.add_edge(loop, sustainability)

root = main_flow