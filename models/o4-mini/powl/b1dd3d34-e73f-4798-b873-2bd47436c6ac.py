# Generated from: b1dd3d34-e73f-4798-b873-2bd47436c6ac.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponic techniques, climate control, and automated nutrient delivery to maximize crop yield within confined city spaces. It begins with seed selection and germination, followed by transplanting seedlings into vertically stacked trays. Continuous monitoring of environmental parameters such as humidity, temperature, and light ensures optimal growth conditions. The system employs robotic arms for pruning and harvesting, while integrated sensors detect pest presence or nutrient deficiencies, triggering corrective actions. Wastewater is recycled through a closed-loop system, minimizing environmental impact and resource consumption. Finally, harvested produce undergoes quality inspection and packaging before distribution to local markets, closing the sustainable urban agriculture loop.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
seed_selection     = Transition(label='Seed Selection')
germinate_seeds    = Transition(label='Germinate Seeds')
tray_transplant    = Transition(label='Tray Transplant')
climate_setup      = Transition(label='Climate Setup')
nutrient_main      = Transition(label='Nutrient Mix')
monitor_sensors    = Transition(label='Monitor Sensors')
adjust_lighting    = Transition(label='Adjust Lighting')
pest_detection     = Transition(label='Pest Detection')
robotic_prune      = Transition(label='Robotic Prune')
harvest_crop       = Transition(label='Harvest Crop')
wastewater_recycle = Transition(label='Wastewater Recycle')
quality_inspect    = Transition(label='Quality Inspect')
package_produce    = Transition(label='Package Produce')
market_dispatch    = Transition(label='Market Dispatch')
data_logging       = Transition(label='Data Logging')

# Silent transitions for skipping in loops/choices
skip_correction = SilentTransition()
skip_waste     = SilentTransition()

# 1) Initial setup sequence: Seed Selection -> Germinate Seeds -> Tray Transplant -> Climate Setup -> Nutrient Mix
seq_init = StrictPartialOrder(nodes=[
    seed_selection,
    germinate_seeds,
    tray_transplant,
    climate_setup,
    nutrient_main
])
seq_init.order.add_edge(seed_selection,  germinate_seeds)
seq_init.order.add_edge(germinate_seeds, tray_transplant)
seq_init.order.add_edge(tray_transplant, climate_setup)
seq_init.order.add_edge(climate_setup,   nutrient_main)

# 2) Monitoring loop: 
#    Body  A = Monitor Sensors
#    Redo  B = Pest Detection -> (XOR of corrective actions: Robotic Prune, Adjust Lighting, Nutrient Mix, or skip)
nutrient_correction = Transition(label='Nutrient Mix')
correction_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[
        robotic_prune,
        adjust_lighting,
        nutrient_correction,
        skip_correction
    ]
)
b_redo = StrictPartialOrder(nodes=[pest_detection, correction_choice])
b_redo.order.add_edge(pest_detection, correction_choice)

loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_sensors, b_redo]
)

# 3) Wastewater recycle loop: Wastewater Recycle repeated until skip
loop_waste = OperatorPOWL(
    operator=Operator.LOOP,
    children=[wastewater_recycle, skip_waste]
)

# 4) Finalization sequence: Harvest -> Quality Inspect -> Package -> Market Dispatch -> Data Logging
# Build the root partial order combining everything
root = StrictPartialOrder(nodes=[
    seq_init,
    loop_monitor,
    loop_waste,
    harvest_crop,
    quality_inspect,
    package_produce,
    market_dispatch,
    data_logging
])

# Order edges between the subprocesses
root.order.add_edge(seq_init,       loop_monitor)
root.order.add_edge(seq_init,       loop_waste)
root.order.add_edge(loop_monitor,   harvest_crop)
root.order.add_edge(loop_waste,     harvest_crop)
root.order.add_edge(harvest_crop,   quality_inspect)
root.order.add_edge(quality_inspect, package_produce)
root.order.add_edge(package_produce, market_dispatch)
root.order.add_edge(market_dispatch, data_logging)