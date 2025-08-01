# Generated from: 4346d4fd-72ef-4418-981d-75a58374f91a.json
# Description: This process outlines the complex steps involved in establishing a vertical farm within an urban environment, integrating advanced hydroponics, IoT monitoring, renewable energy sourcing, and community engagement. It includes site evaluation, structural adaptation, multi-layer crop planning, automated nutrient delivery, environmental control calibration, waste recycling, and data-driven yield optimization. Additionally, it manages regulatory compliance, partner coordination, and market launch strategies to ensure sustainable production and profitability in constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_design = Transition(label='Structure Design')
permit_filing    = Transition(label='Permit Filing')
energy_setup     = Transition(label='Energy Setup')
waste_system     = Transition(label='Waste System')
hydroponic_install = Transition(label='Hydroponic Install')
sensor_deploy    = Transition(label='Sensor Deploy')
crop_mapping     = Transition(label='Crop Mapping')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
partner_meet     = Transition(label='Partner Meet')
market_plan      = Transition(label='Market Plan')
launch_event     = Transition(label='Launch Event')
data_sync        = Transition(label='Data Sync')
quality_check    = Transition(label='Quality Check')
feedback_loop    = Transition(label='Feedback Loop')

# Initial sequence: site survey -> structure design -> permit -> energy -> waste
# -> hydroponic install -> sensor deploy -> crop mapping -> nutrient mix
# -> climate adjust -> partner meet -> market plan -> launch event
initial = StrictPartialOrder(nodes=[
    site_survey, structure_design, permit_filing,
    energy_setup, waste_system, hydroponic_install,
    sensor_deploy, crop_mapping, nutrient_mix,
    climate_adjust, partner_meet, market_plan,
    launch_event
])
initial.order.add_edge(site_survey,      structure_design)
initial.order.add_edge(structure_design, permit_filing)
initial.order.add_edge(permit_filing,    energy_setup)
initial.order.add_edge(energy_setup,     waste_system)
initial.order.add_edge(waste_system,     hydroponic_install)
initial.order.add_edge(hydroponic_install, sensor_deploy)
initial.order.add_edge(sensor_deploy,    crop_mapping)
initial.order.add_edge(crop_mapping,     nutrient_mix)
initial.order.add_edge(nutrient_mix,     climate_adjust)
initial.order.add_edge(climate_adjust,   partner_meet)
initial.order.add_edge(partner_meet,     market_plan)
initial.order.add_edge(market_plan,      launch_event)

# Define the loop body: data sync -> quality check
body = StrictPartialOrder(nodes=[data_sync, quality_check])
body.order.add_edge(data_sync, quality_check)

# LOOP: execute (data sync -> quality check), then either exit or do feedback_loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback_loop])

# Root POWL: initial sequence followed by the feedback loop structure
root = StrictPartialOrder(nodes=[initial, loop])
root.order.add_edge(initial, loop)