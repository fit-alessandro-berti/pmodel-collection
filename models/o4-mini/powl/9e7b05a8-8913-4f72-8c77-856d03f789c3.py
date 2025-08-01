# Generated from: 9e7b05a8-8913-4f72-8c77-856d03f789c3.json
# Description: This process manages the complete operational cycle of an urban vertical farm specializing in multi-layer hydroponic crop production. It begins with seed selection based on climate and market demand, followed by nutrient optimization customized per plant type. Automated climate control adjusts humidity, temperature, and light spectra to maximize growth efficiency. Continuous pest monitoring uses AI-driven image recognition to detect early infestations, triggering targeted biocontrol interventions. Wastewater recycling incorporates filtration and mineral rebalancing before reuse. Harvest scheduling synchronizes with local distribution networks to ensure freshness and reduce carbon footprint. Additionally, real-time data analytics inform adaptive planting strategies, while employee training on advanced farming technologies maintains operational excellence. The process concludes with system maintenance and seasonal recalibration to prepare for subsequent cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_select       = Transition(label='Seed Select')
nutrient_mix      = Transition(label='Nutrient Mix')
climate_adjust    = Transition(label='Climate Adjust')
light_control     = Transition(label='Light Control')
growth_monitor    = Transition(label='Growth Monitor')
employee_train    = Transition(label='Employee Train')
data_analyze      = Transition(label='Data Analyze')
water_filter      = Transition(label='Water Filter')
mineral_rebalance = Transition(label='Mineral Rebalance')
waste_process     = Transition(label='Waste Process')
pest_scan         = Transition(label='Pest Scan')
biocontrol_use    = Transition(label='Biocontrol Use')
harvest_plan      = Transition(label='Harvest Plan')
logistics_sync    = Transition(label='Logistics Sync')
system_maintain   = Transition(label='System Maintain')
cycle_recalibrate = Transition(label='Cycle Recalibrate')
inventory_check   = Transition(label='Inventory Check')

# 1) Sequence: Seed Select -> Nutrient Mix
seq_seed_nutrient = StrictPartialOrder(nodes=[seed_select, nutrient_mix])
seq_seed_nutrient.order.add_edge(seed_select, nutrient_mix)

# 2) Parallel activities after Nutrient Mix: Climate Adjust, Light Control, Growth Monitor, Employee Train
par_concurrent = StrictPartialOrder(nodes=[
    climate_adjust, light_control, growth_monitor, employee_train
])
# no ordering among them (fully concurrent)

# 3) Data Analyze after all concurrent steps
seq_concurrent_analyze = StrictPartialOrder(nodes=[par_concurrent, data_analyze])
seq_concurrent_analyze.order.add_edge(par_concurrent, data_analyze)

# 4) Wastewater recycling: Water Filter -> Mineral Rebalance -> Waste Process
seq_water_recycle = StrictPartialOrder(nodes=[
    water_filter, mineral_rebalance, waste_process
])
seq_water_recycle.order.add_edge(water_filter, mineral_rebalance)
seq_water_recycle.order.add_edge(mineral_rebalance, waste_process)

# 5) Continuous pest loop: Pest Scan, optionally Biocontrol Use then repeat scan
pest_body = StrictPartialOrder(nodes=[biocontrol_use, pest_scan])
pest_body.order.add_edge(biocontrol_use, pest_scan)
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scan, pest_body])

# 6) Harvest scheduling: Harvest Plan -> Logistics Sync
seq_harvest = StrictPartialOrder(nodes=[harvest_plan, logistics_sync])
seq_harvest.order.add_edge(harvest_plan, logistics_sync)

# 7) Conclusion: System Maintain -> Cycle Recalibrate -> Inventory Check
seq_close = StrictPartialOrder(nodes=[
    system_maintain, cycle_recalibrate, inventory_check
])
seq_close.order.add_edge(system_maintain, cycle_recalibrate)
seq_close.order.add_edge(cycle_recalibrate, inventory_check)

# Root POWL: combine all steps in order
root = StrictPartialOrder(nodes=[
    seq_seed_nutrient,
    seq_concurrent_analyze,
    seq_water_recycle,
    pest_loop,
    seq_harvest,
    seq_close
])
root.order.add_edge(seq_seed_nutrient, seq_concurrent_analyze)
root.order.add_edge(seq_concurrent_analyze, seq_water_recycle)
root.order.add_edge(seq_water_recycle, pest_loop)
root.order.add_edge(pest_loop, seq_harvest)
root.order.add_edge(seq_harvest, seq_close)