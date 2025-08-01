# Generated from: 3fcba11c-d263-44a0-95cf-9991d5c50dd4.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm that integrates sustainable practices, IoT monitoring, and community engagement. It begins with seed selection based on climate data and market trends, followed by nutrient optimization using hydroponic systems. Continuous environmental adjustments ensure optimal growth, while real-time data analytics predict harvest times. Post-harvest, crops undergo quality assessment and packaging tailored for local distribution. The cycle incorporates waste recycling through composting and energy recovery. Finally, the process concludes with customer feedback integration and adaptive planning for subsequent planting cycles, ensuring both ecological balance and economic viability within an urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
seed_select     = Transition(label='Seed Select')
climate_analyze = Transition(label='Climate Analyze')
nutrient_mix    = Transition(label='Nutrient Mix')
system_calibrate= Transition(label='System Calibrate')
planting_setup  = Transition(label='Planting Setup')

growth_monitor  = Transition(label='Growth Monitor')
env_adjust      = Transition(label='Environment Adjust')
data_analyze    = Transition(label='Data Analyze')
pest_inspect    = Transition(label='Pest Inspect')

harvest_plan    = Transition(label='Harvest Plan')
crop_harvest    = Transition(label='Crop Harvest')
quality_check   = Transition(label='Quality Check')
package_prepare = Transition(label='Package Prepare')

waste_process   = Transition(label='Waste Process')
energy_recover  = Transition(label='Energy Recover')
distribute_local= Transition(label='Distribute Local')

feedback_collect= Transition(label='Feedback Collect')
cycle_review    = Transition(label='Cycle Review')

# Silent transition for loop exits
tau = SilentTransition()

# Inner loop: continuous monitoring cycle
monitoring_seq = StrictPartialOrder(nodes=[growth_monitor, env_adjust, data_analyze, pest_inspect])
monitoring_seq.order.add_edge(growth_monitor, env_adjust)
monitoring_seq.order.add_edge(env_adjust, data_analyze)
monitoring_seq.order.add_edge(data_analyze, pest_inspect)

inner_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_seq, tau])

# Single cycle partial order
cycle_seq = StrictPartialOrder(nodes=[
    seed_select, climate_analyze, nutrient_mix, system_calibrate, planting_setup,
    inner_monitor_loop,
    harvest_plan, crop_harvest, quality_check, package_prepare,
    waste_process, energy_recover,
    distribute_local, feedback_collect, cycle_review
])
# Sequential edges for the cycle
cycle_seq.order.add_edge(seed_select,     climate_analyze)
cycle_seq.order.add_edge(climate_analyze, nutrient_mix)
cycle_seq.order.add_edge(nutrient_mix,    system_calibrate)
cycle_seq.order.add_edge(system_calibrate,planting_setup)
cycle_seq.order.add_edge(planting_setup,  inner_monitor_loop)
cycle_seq.order.add_edge(inner_monitor_loop, harvest_plan)
cycle_seq.order.add_edge(harvest_plan,    crop_harvest)
cycle_seq.order.add_edge(crop_harvest,    quality_check)
cycle_seq.order.add_edge(quality_check,   package_prepare)
cycle_seq.order.add_edge(package_prepare, waste_process)
cycle_seq.order.add_edge(waste_process,   energy_recover)
cycle_seq.order.add_edge(energy_recover,  distribute_local)
cycle_seq.order.add_edge(distribute_local, feedback_collect)
cycle_seq.order.add_edge(feedback_collect, cycle_review)

# Outer loop: repeat entire cycle for adaptive planning
root = OperatorPOWL(operator=Operator.LOOP, children=[cycle_seq, tau])