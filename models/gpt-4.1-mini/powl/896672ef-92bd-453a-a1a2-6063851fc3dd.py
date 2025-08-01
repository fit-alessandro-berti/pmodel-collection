# Generated from: 896672ef-92bd-453a-a1a2-6063851fc3dd.json
# Description: This process involves the continuous cycle of managing an urban vertical farm, integrating advanced agricultural techniques with smart technology. It begins with environmental calibration to optimize conditions, followed by seed selection tailored to urban microclimates. Automated seeding is then performed, before nutrient dosing is precisely managed via hydroponic systems. Real-time growth monitoring leverages AI-driven imaging, triggering adaptive lighting and climate adjustments. Periodic pest control is executed using biocontrol agents to maintain ecological balance. Harvest scheduling coordinates labor and logistics to ensure freshness, while waste recycling incorporates organic matter into composting units. Post-harvest quality checks maintain standards for distribution. Finally, data analytics review system efficiency and crop yield trends, enabling continuous improvement in sustainable urban farming practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
env_cal = Transition(label='Env Calibration')
seed_sel = Transition(label='Seed Selection')
auto_seed = Transition(label='Auto Seeding')
nutrient = Transition(label='Nutrient Dosing')
growth_mon = Transition(label='Growth Monitoring')
light_adj = Transition(label='Light Adjustment')
climate_ctrl = Transition(label='Climate Control')
pest_ctrl = Transition(label='Pest Control')
harvest_sch = Transition(label='Harvest Scheduling')
labor_coord = Transition(label='Labor Coordination')
waste_recy = Transition(label='Waste Recycling')
compost_proc = Transition(label='Compost Processing')
quality_chk = Transition(label='Quality Checking')
dist_prep = Transition(label='Distribution Prep')
data_anal = Transition(label='Data Analytics')

# Growth monitoring triggers lighting and climate adjustments that happen concurrently
adjustments = StrictPartialOrder(nodes=[light_adj, climate_ctrl])  # concurrent

# Harvest scheduling coordinates labor (sequential)
harvest_part = StrictPartialOrder(nodes=[harvest_sch, labor_coord])
harvest_part.order.add_edge(harvest_sch, labor_coord)

# Waste recycling followed by compost processing (sequential)
waste_part = StrictPartialOrder(nodes=[waste_recy, compost_proc])
waste_part.order.add_edge(waste_recy, compost_proc)

# Post-harvest quality checking before distribution preparation (sequential)
post_harvest = StrictPartialOrder(nodes=[quality_chk, dist_prep])
post_harvest.order.add_edge(quality_chk, dist_prep)

# Real-time monitoring, then adjustments concurrently
monitor_and_adjust = StrictPartialOrder(nodes=[growth_mon, adjustments])
monitor_and_adjust.order.add_edge(growth_mon, adjustments)

# After data analytics, process loops back to Env Calibration (loop)
# Loop: body = (Env Calibration -> Seed Selection -> Auto Seeding -> Nutrient Dosing -> monitor_and_adjust -> Pest Control -> harvest_part -> waste_part -> post_harvest -> Data Analytics)
# Then loop repeats or exits

# Build main sequence inside loop body:
loop_body_nodes = [
    env_cal,
    seed_sel,
    auto_seed,
    nutrient,
    monitor_and_adjust,
    pest_ctrl,
    harvest_part,
    waste_part,
    post_harvest,
    data_anal
]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)

# Add edges in main sequence:
loop_body.order.add_edge(env_cal, seed_sel)
loop_body.order.add_edge(seed_sel, auto_seed)
loop_body.order.add_edge(auto_seed, nutrient)
loop_body.order.add_edge(nutrient, monitor_and_adjust)
loop_body.order.add_edge(monitor_and_adjust, pest_ctrl)
loop_body.order.add_edge(pest_ctrl, harvest_part)
loop_body.order.add_edge(harvest_part, waste_part)
loop_body.order.add_edge(waste_part, post_harvest)
loop_body.order.add_edge(post_harvest, data_anal)

# Define loop with empty exit (silent transition)
from pm4py.objects.powl.obj import SilentTransition

exit_loop = SilentTransition()

root = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, exit_loop])