# Generated from: 69315215-f7c2-409d-9bcc-4c09ac52d525.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating advanced hydroponics, AI-driven climate control, and renewable energy sources. The workflow begins with site assessment and structural analysis, followed by modular rack installation and sensor network deployment. Nutrient solution calibration and seed selection are conducted simultaneously to optimize growth cycles. Continuous monitoring and adaptive lighting adjustments ensure maximum yield. Waste recycling and water reclamation are embedded to maintain sustainability. The process concludes with harvest scheduling and distribution logistics, emphasizing traceability and minimal carbon footprint throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_assess     = Transition(label='Site Assess')
structure_scan  = Transition(label='Structure Scan')
rack_install    = Transition(label='Rack Install')
sensor_deploy   = Transition(label='Sensor Deploy')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_choose     = Transition(label='Seed Choose')
growth_monitor  = Transition(label='Growth Monitor')
light_adjust    = Transition(label='Light Adjust')
climate_tune    = Transition(label='Climate Tune')
water_cycle     = Transition(label='Water Cycle')
waste_recycle   = Transition(label='Waste Recycle')
energy_sync     = Transition(label='Energy Sync')
harvest_plan    = Transition(label='Harvest Plan')
trace_verify    = Transition(label='Trace Verify')
distribute_crop = Transition(label='Distribute Crop')
data_log        = Transition(label='Data Log')

# Build the monitoring & sustainability loop body
loop_body = StrictPartialOrder(nodes=[
    growth_monitor, light_adjust, climate_tune,
    water_cycle, waste_recycle, energy_sync
])
# Growth monitor triggers all adjustments and cycles
loop_body.order.add_edge(growth_monitor, light_adjust)
loop_body.order.add_edge(growth_monitor, climate_tune)
loop_body.order.add_edge(growth_monitor, water_cycle)
loop_body.order.add_edge(growth_monitor, waste_recycle)
loop_body.order.add_edge(growth_monitor, energy_sync)

# Silent transition for loop repetition decision
tau = SilentTransition()

# Loop operator: continuous monitoring & adjustments
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, tau])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_scan,
    rack_install, sensor_deploy,
    nutrient_mix, seed_choose,
    monitor_loop,
    harvest_plan, trace_verify,
    distribute_crop, data_log
])

# Define the control-flow dependencies
root.order.add_edge(site_assess, structure_scan)
root.order.add_edge(structure_scan, rack_install)
root.order.add_edge(structure_scan, sensor_deploy)

root.order.add_edge(rack_install, nutrient_mix)
root.order.add_edge(sensor_deploy, nutrient_mix)
root.order.add_edge(rack_install, seed_choose)
root.order.add_edge(sensor_deploy, seed_choose)

root.order.add_edge(nutrient_mix, monitor_loop)
root.order.add_edge(seed_choose, monitor_loop)

root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, trace_verify)
root.order.add_edge(trace_verify, distribute_crop)
root.order.add_edge(harvest_plan, data_log)