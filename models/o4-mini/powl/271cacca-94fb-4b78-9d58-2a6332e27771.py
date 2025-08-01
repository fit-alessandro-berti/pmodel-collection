# Generated from: 271cacca-94fb-4b78-9d58-2a6332e27771.json
# Description: This process involves the integrated management of an urban vertical farm, combining hydroponics, climate control, and automated harvesting to optimize crop yield within a limited city space. It begins with seed selection and conditioning, followed by nutrient solution preparation and precise environmental calibration. Continuous monitoring through IoT sensors enables adaptive adjustments to light intensity, humidity, and temperature. Harvesting robots collect mature produce, which is then quality-checked and packaged onsite. Waste materials are recycled into compost to sustain the growth cycle, while data analytics provide insights for future crop planning. The entire cycle emphasizes sustainability, efficiency, and minimal resource usage, making it an innovative model for urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_prep = Transition(label='Seed Prep')
nutrient_mix = Transition(label='Nutrient Mix')
climate_set = Transition(label='Climate Set')
sensor_install = Transition(label='Sensor Install')

light_adjust_init     = Transition(label='Light Adjust')
humidity_control_init = Transition(label='Humidity Control')
temperature_tune_init = Transition(label='Temperature Tune')

growth_monitor = Transition(label='Growth Monitor')
pest_inspect   = Transition(label='Pest Inspect')

light_adjust_adj     = Transition(label='Light Adjust')
humidity_control_adj = Transition(label='Humidity Control')
temperature_tune_adj = Transition(label='Temperature Tune')

harvest_collect = Transition(label='Harvest Collect')
quality_check   = Transition(label='Quality Check')
packaging       = Transition(label='Packaging')
waste_sort      = Transition(label='Waste Sort')
compost_create  = Transition(label='Compost Create')

data_analyze    = Transition(label='Data Analyze')

# Initial environmental calibration block
initial_calibration = StrictPartialOrder(
    nodes=[light_adjust_init, humidity_control_init, temperature_tune_init]
)

# Continuous monitoring task
monitor_task = StrictPartialOrder(
    nodes=[growth_monitor, pest_inspect]
)
monitor_task.order.add_edge(growth_monitor, pest_inspect)

# Adjustment tasks within the monitoring loop
adjust_tasks = StrictPartialOrder(
    nodes=[light_adjust_adj, humidity_control_adj, temperature_tune_adj]
)

# Loop: monitor -> (adjust -> monitor)* 
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_task, adjust_tasks]
)

# One cycle of the farm process (before analytics & possible restart)
cycle_body = StrictPartialOrder(
    nodes=[
        seed_prep,
        nutrient_mix,
        climate_set,
        sensor_install,
        initial_calibration,
        monitor_loop,
        harvest_collect,
        quality_check,
        packaging,
        waste_sort,
        compost_create
    ]
)
# Sequential ordering inside the cycle
cycle_body.order.add_edge(seed_prep,       nutrient_mix)
cycle_body.order.add_edge(nutrient_mix,    climate_set)
cycle_body.order.add_edge(climate_set,     sensor_install)
cycle_body.order.add_edge(sensor_install,  initial_calibration)
cycle_body.order.add_edge(initial_calibration, monitor_loop)
cycle_body.order.add_edge(monitor_loop,    harvest_collect)
cycle_body.order.add_edge(harvest_collect, quality_check)
cycle_body.order.add_edge(quality_check,   packaging)
cycle_body.order.add_edge(packaging,       waste_sort)
cycle_body.order.add_edge(waste_sort,      compost_create)

# Top‐level loop: run one cycle then data‐analyze, repeat or exit
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle_body, data_analyze]
)