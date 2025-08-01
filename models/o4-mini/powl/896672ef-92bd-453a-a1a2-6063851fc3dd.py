# Generated from: 896672ef-92bd-453a-a1a2-6063851fc3dd.json
# Description: This process involves the continuous cycle of managing an urban vertical farm, integrating advanced agricultural techniques with smart technology. It begins with environmental calibration to optimize conditions, followed by seed selection tailored to urban microclimates. Automated seeding is then performed, before nutrient dosing is precisely managed via hydroponic systems. Real-time growth monitoring leverages AI-driven imaging, triggering adaptive lighting and climate adjustments. Periodic pest control is executed using biocontrol agents to maintain ecological balance. Harvest scheduling coordinates labor and logistics to ensure freshness, while waste recycling incorporates organic matter into composting units. Post-harvest quality checks maintain standards for distribution. Finally, data analytics review system efficiency and crop yield trends, enabling continuous improvement in sustainable urban farming practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL Transitions
env_cal = Transition(label="Env Calibration")
seed_sel = Transition(label="Seed Selection")
auto_seed = Transition(label="Auto Seeding")
nutrient_dose = Transition(label="Nutrient Dosing")
growth_mon = Transition(label="Growth Monitoring")
light_adj = Transition(label="Light Adjustment")
climate_ctrl = Transition(label="Climate Control")
pest_ctrl = Transition(label="Pest Control")
harvest_sched = Transition(label="Harvest Scheduling")
labor_coord = Transition(label="Labor Coordination")
waste_recyc = Transition(label="Waste Recycling")
compost_proc = Transition(label="Compost Processing")
quality_chk = Transition(label="Quality Checking")
dist_prep = Transition(label="Distribution Prep")
data_anal = Transition(label="Data Analytics")

# Silent transition for loop repetition
skip = SilentTransition()

# Build one cycle of the urban farm process as a partial order
cycle = StrictPartialOrder(
    nodes=[
        env_cal, seed_sel, auto_seed, nutrient_dose, growth_mon,
        light_adj, climate_ctrl, pest_ctrl, harvest_sched, labor_coord,
        waste_recyc, compost_proc, quality_chk, dist_prep, data_anal
    ]
)

# Define the linear sequence up to growth monitoring
cycle.order.add_edge(env_cal, seed_sel)
cycle.order.add_edge(seed_sel, auto_seed)
cycle.order.add_edge(auto_seed, nutrient_dose)
cycle.order.add_edge(nutrient_dose, growth_mon)

# From growth monitoring, spawn adaptive lighting and climate control concurrently
cycle.order.add_edge(growth_mon, light_adj)
cycle.order.add_edge(growth_mon, climate_ctrl)

# After both adjustments, proceed to pest control
cycle.order.add_edge(light_adj, pest_ctrl)
cycle.order.add_edge(climate_ctrl, pest_ctrl)

# Continue the rest of the sequence
cycle.order.add_edge(pest_ctrl, harvest_sched)
cycle.order.add_edge(harvest_sched, labor_coord)
cycle.order.add_edge(labor_coord, waste_recyc)
cycle.order.add_edge(waste_recyc, compost_proc)
cycle.order.add_edge(compost_proc, quality_chk)
cycle.order.add_edge(quality_chk, dist_prep)
cycle.order.add_edge(dist_prep, data_anal)

# Wrap the cycle in a loop: perform 'cycle', then either exit or do 'skip' and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])