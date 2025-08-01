# Generated from: 4346d4fd-72ef-4418-981d-75a58374f91a.json
# Description: This process outlines the complex steps involved in establishing a vertical farm within an urban environment, integrating advanced hydroponics, IoT monitoring, renewable energy sourcing, and community engagement. It includes site evaluation, structural adaptation, multi-layer crop planning, automated nutrient delivery, environmental control calibration, waste recycling, and data-driven yield optimization. Additionally, it manages regulatory compliance, partner coordination, and market launch strategies to ensure sustainable production and profitability in constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
structure_design = Transition(label='Structure Design')
permit_filing = Transition(label='Permit Filing')
energy_setup = Transition(label='Energy Setup')
hydroponic_install = Transition(label='Hydroponic Install')
sensor_deploy = Transition(label='Sensor Deploy')
crop_mapping = Transition(label='Crop Mapping')
nutrient_mix = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
waste_system = Transition(label='Waste System')
data_sync = Transition(label='Data Sync')
quality_check = Transition(label='Quality Check')
partner_meet = Transition(label='Partner Meet')
market_plan = Transition(label='Market Plan')
launch_event = Transition(label='Launch Event')
feedback_loop = Transition(label='Feedback Loop')

# Construct a loop: after Launch Event, Feedback Loop optionally repeats some part
# We'll model the Feedback Loop as a loop with two children: A=process to repeat (Quality Check + Data Sync + ...) and B=some rework or silent step

# Let's define the iterative loop body as:
# Loop body A: Quality Check, Partner Meet, Data Sync (strict order)
# Loop body B: Feedback Loop step (which could be modeling rework or corrective action)

# Since the Feedback Loop is part of the activities, it serves well as the "B" in loop definition,
# and "A" is the evaluation/coordination steps that precede it.

# Sub-loop: review cycle
review_cycle_nodes = [quality_check, partner_meet, data_sync]
review_cycle = StrictPartialOrder(nodes=review_cycle_nodes)
review_cycle.order.add_edge(quality_check, partner_meet)
review_cycle.order.add_edge(partner_meet, data_sync)

loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[review_cycle, feedback_loop])

# After Launch Event, the feedback loop occurs
# Before Launch Event: Market Plan

# Partial order for final launch phase: Market Plan -> Launch Event -> loop_feedback
launch_phase = StrictPartialOrder(nodes=[market_plan, launch_event, loop_feedback])
launch_phase.order.add_edge(market_plan, launch_event)
launch_phase.order.add_edge(launch_event, loop_feedback)

# Environmental and installation setup partial order:
# Energy Setup happens before Hydroponic Install and Sensor Deploy (can be concurrent)
# Waste System and Climate Adjust can be concurrent after Hydroponic Install and Sensor Deploy

setup_phase_nodes = [energy_setup, hydroponic_install, sensor_deploy, waste_system, climate_adjust]

setup_phase = StrictPartialOrder(nodes=setup_phase_nodes)
setup_phase.order.add_edge(energy_setup, hydroponic_install)
setup_phase.order.add_edge(energy_setup, sensor_deploy)
setup_phase.order.add_edge(hydroponic_install, waste_system)
setup_phase.order.add_edge(sensor_deploy, waste_system)
setup_phase.order.add_edge(hydroponic_install, climate_adjust)
setup_phase.order.add_edge(sensor_deploy, climate_adjust)

# Crop planning and nutrient:
# Crop Mapping -> Nutrient Mix (strict)
crop_phase = StrictPartialOrder(nodes=[crop_mapping, nutrient_mix])
crop_phase.order.add_edge(crop_mapping, nutrient_mix)

# Regulatory and structural: Site Survey -> Structure Design -> Permit Filing
regulatory_phase = StrictPartialOrder(nodes=[site_survey, structure_design, permit_filing])
regulatory_phase.order.add_edge(site_survey, structure_design)
regulatory_phase.order.add_edge(structure_design, permit_filing)

# Now build main partial order:
# 1. regulatory_phase must finish before setup_phase
# 2. crop_phase depends on hydroponic_install (needs installation done to plan crops/nutrients)
# 3. setup_phase also must complete before crop_phase (implying install/sensor set up before crop planning)
# 4. crop_phase must finish before launch_phase

main_nodes = [regulatory_phase, setup_phase, crop_phase, launch_phase]

root = StrictPartialOrder(nodes=main_nodes)

# Add cross edges for dependencies between sub-PoWL nodes (partial orders):

# regulatory_phase --> setup_phase
root.order.add_edge(regulatory_phase, setup_phase)

# setup_phase --> crop_phase
root.order.add_edge(setup_phase, crop_phase)

# crop_phase --> launch_phase
root.order.add_edge(crop_phase, launch_phase)