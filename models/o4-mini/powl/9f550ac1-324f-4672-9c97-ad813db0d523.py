# Generated from: 9f550ac1-324f-4672-9c97-ad813db0d523.json
# Description: This process outlines the complex cycle of managing an urban vertical farm that integrates hydroponics, automated nutrient delivery, environmental monitoring, and crop harvesting within a multi-level indoor facility. The workflow begins with seed selection and germination in controlled chambers, followed by transplanting seedlings to vertical growth racks. Continuous monitoring of light intensity, humidity, and nutrient concentration is performed via IoT sensors, enabling real-time adjustments by the central control system. Periodic pest detection and bio-control deployment maintain plant health without chemicals. Harvesting is scheduled based on growth analytics, after which produce undergoes quality inspection and packaging. The process also includes waste recycling to optimize sustainability and data logging for performance analysis and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
seed_select       = Transition(label='Seed Select')
chamber_setup     = Transition(label='Chamber Setup')
germinate_start   = Transition(label='Germinate Start')
seedling_move     = Transition(label='Seedling Move')
rack_install      = Transition(label='Rack Install')
nutrient_mix      = Transition(label='Nutrient Mix')
irrigation_on     = Transition(label='Irrigation On')
light_adjust      = Transition(label='Light Adjust')
sensor_check      = Transition(label='Sensor Check')
pest_scan         = Transition(label='Pest Scan')
bio_control_deploy= Transition(label='Bio-Control Deploy')
growth_monitor    = Transition(label='Growth Monitor')
harvest_plan      = Transition(label='Harvest Plan')
quality_check     = Transition(label='Quality Check')
package_final     = Transition(label='Package Final')
waste_sort        = Transition(label='Waste Sort')
data_log          = Transition(label='Data Log')

# Silent transition for skips
skip = SilentTransition()

# XOR choice: either deploy bio-control or skip
pest_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[bio_control_deploy, skip]
)

# Monitoring‐cycle body: a partial order of sensing, adjusting, monitoring, scanning, then pest decision
monitor_body = StrictPartialOrder(
    nodes=[sensor_check,
           light_adjust,
           nutrient_mix,
           irrigation_on,
           growth_monitor,
           pest_scan,
           pest_xor]
)
monitor_body.order.add_edge(sensor_check,   light_adjust)
monitor_body.order.add_edge(light_adjust,    nutrient_mix)
monitor_body.order.add_edge(nutrient_mix,    irrigation_on)
monitor_body.order.add_edge(irrigation_on,   growth_monitor)
monitor_body.order.add_edge(growth_monitor,  pest_scan)
monitor_body.order.add_edge(pest_scan,       pest_xor)

# Loop: repeat the monitor_body any number of times
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_body, skip]
)

# Root partial order: seed/germination -> transplant -> monitoring loop -> harvest & post‐processing
root = StrictPartialOrder(
    nodes=[
        seed_select,
        chamber_setup,
        germinate_start,
        seedling_move,
        rack_install,
        monitor_loop,
        harvest_plan,
        quality_check,
        package_final,
        waste_sort,
        data_log
    ]
)
root.order.add_edge(seed_select,     chamber_setup)
root.order.add_edge(chamber_setup,   germinate_start)
root.order.add_edge(germinate_start, seedling_move)
root.order.add_edge(seedling_move,   rack_install)
root.order.add_edge(rack_install,    monitor_loop)
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    quality_check)
root.order.add_edge(quality_check,   package_final)
root.order.add_edge(package_final,   waste_sort)
root.order.add_edge(waste_sort,      data_log)