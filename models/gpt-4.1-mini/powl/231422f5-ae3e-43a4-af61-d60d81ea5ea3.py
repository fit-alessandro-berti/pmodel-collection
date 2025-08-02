# Generated from: 231422f5-ae3e-43a4-af61-d60d81ea5ea3.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farm integrating hydroponic and aeroponic systems across multiple stacked layers. It begins with seed selection based on environmental adaptability, followed by nutrient solution preparation tailored for each crop type. Automated planting robots sow seeds in specialized growth media. Continuous monitoring of microclimate variables such as humidity, CO2 levels, and light spectrum is performed via IoT sensors. Pest detection employs AI-driven image recognition to trigger targeted biocontrol releases. Harvesting robots operate with precision timing to optimize yield quality. Post-harvest, modular packaging units sanitize and pack produce for local distribution. Data analytics refine each cycle by correlating growth metrics with environmental adjustments, promoting sustainable resource use and minimizing waste. The process concludes with system sanitation and maintenance, ensuring readiness for subsequent planting cycles while integrating feedback loops from urban consumer demand patterns.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
media_prep = Transition(label='Media Prep')
planting_robot = Transition(label='Planting Robot')
climate_monitor = Transition(label='Climate Monitor')
co2_control = Transition(label='CO2 Control')
light_adjust = Transition(label='Light Adjust')
humidity_check = Transition(label='Humidity Check')
pest_detect = Transition(label='Pest Detect')
biocontrol_deploy = Transition(label='BioControl Deploy')
growth_analyze = Transition(label='Growth Analyze')
harvest_robot = Transition(label='Harvest Robot')
pack_produce = Transition(label='Pack Produce')
data_sync = Transition(label='Data Sync')
system_clean = Transition(label='System Clean')
demand_review = Transition(label='Demand Review')

# Build partial order for climate monitoring subactivities, which are concurrent:
climate_subactivities = StrictPartialOrder(nodes=[co2_control, light_adjust, humidity_check])
# no order edges mean concurrent execution of these controls

# Pest detection leads to deployment - sequence
pest_suborder = StrictPartialOrder(nodes=[pest_detect, biocontrol_deploy])
pest_suborder.order.add_edge(pest_detect, biocontrol_deploy)

# Monitoring phase partial order that includes climate monitoring (which itself is concurrent), pest detection/deploy
monitoring = StrictPartialOrder(nodes=[climate_monitor, climate_subactivities, pest_suborder])
# climate_monitor triggers all the climate controls and also pest detection sequence

# For partial order edges inside monitoring:
monitoring.order.add_edge(climate_monitor, climate_subactivities)
monitoring.order.add_edge(climate_monitor, pest_suborder)

# Pre-planting sequence of seed selection, nutrient mix, media prep, planting robot
pre_planting = StrictPartialOrder(nodes=[seed_select, nutrient_mix, media_prep, planting_robot])
pre_planting.order.add_edge(seed_select, nutrient_mix)
pre_planting.order.add_edge(nutrient_mix, media_prep)
pre_planting.order.add_edge(media_prep, planting_robot)

# Post-harvest packaging sequence
post_harvest = StrictPartialOrder(nodes=[pack_produce, data_sync])
post_harvest.order.add_edge(pack_produce, data_sync)

# Harvesting robot precedes post-harvest steps
harvest_phase = StrictPartialOrder(nodes=[harvest_robot, post_harvest])
harvest_phase.order.add_edge(harvest_robot, post_harvest)

# Data sync feeds into growth analyze (analysis)
analysis_phase = StrictPartialOrder(nodes=[data_sync, growth_analyze])
analysis_phase.order.add_edge(data_sync, growth_analyze)

# Demand review happens after growth analyze (feedback loop)
feedback_phase = StrictPartialOrder(nodes=[growth_analyze, demand_review])
feedback_phase.order.add_edge(growth_analyze, demand_review)

# System clean after everything before looping back
clean_phase = system_clean

# Define loop body:
# After pre_planting and monitoring and harvest, packaging, analysis, demand review, then system_clean,
# loop back to pre planting or exit.

# The loop has form LOOP(pre_planting_and_after, feedback_and_clean)
# where
# pre_planting_and_after = sequence of pre_planting -> monitoring -> harvest_phase
pre_planting_and_after = StrictPartialOrder(
    nodes=[pre_planting, monitoring, harvest_phase]
)
pre_planting_and_after.order.add_edge(pre_planting, monitoring)
pre_planting_and_after.order.add_edge(monitoring, harvest_phase)

# feedback_and_clean sequence: feedback_phase (demand review included) then system_clean
feedback_and_clean = StrictPartialOrder(
    nodes=[feedback_phase, clean_phase]
)
feedback_and_clean.order.add_edge(feedback_phase, clean_phase)

# Loop structure, with body pre_planting_and_after and loop part feedback_and_clean
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pre_planting_and_after, feedback_and_clean]
)

root = loop