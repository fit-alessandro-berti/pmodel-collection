# Generated from: e41e7346-30d3-4a3c-a13d-032dedb867b4.json
# Description: This process governs the integrated management of an urban vertical farm, combining hydroponics, climate control, and automated logistics. It begins with seed selection based on market demand and environmental factors, followed by nutrient mix calibration tailored for each plant species. The system continuously monitors microclimate parameters such as humidity, CO2, and light spectrum, adjusting them dynamically. Crop growth is tracked via AI-driven imaging, predicting harvest readiness and potential pest outbreaks. Harvested produce is sorted, packaged using biodegradable materials, and dispatched through automated delivery drones. Waste is recycled into bio-compost used to enhance future cycles. The entire process ensures sustainability, efficiency, and responsiveness to urban consumers' needs while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_select    = Transition(label='Seed Select')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_setup  = Transition(label='Climate Setup')

light_adjust   = Transition(label='Light Adjust')
co2_control    = Transition(label='CO2 Control')
humidity_tune  = Transition(label='Humidity Tune')
growth_monitor = Transition(label='Growth Monitor')
pest_detect    = Transition(label='Pest Detect')

harvest_plan    = Transition(label='Harvest Plan')
produce_sort    = Transition(label='Produce Sort')
pack_biodeg     = Transition(label='Pack Biodeg')
drone_dispatch  = Transition(label='Drone Dispatch')
waste_recycle   = Transition(label='Waste Recycle')
compost_create  = Transition(label='Compost Create')
cycle_review    = Transition(label='Cycle Review')

# Initial sequence: Seed Select -> Nutrient Mix -> Climate Setup
initial_po = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_setup])
initial_po.order.add_edge(seed_select, nutrient_mix)
initial_po.order.add_edge(nutrient_mix, climate_setup)

# Monitoring & adjustment grouped together (concurrent)
monitor_adjust_po = StrictPartialOrder(nodes=[
    light_adjust, co2_control, humidity_tune,
    growth_monitor, pest_detect
])
# no internal order: all five can happen concurrently

# Inner loop: repeat the monitor/adjust phase until ready for harvest
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_adjust_po, monitor_adjust_po]
)

# After-monitor sequence: monitor_loop -> Harvest Plan -> Produce Sort -> Pack -> Dispatch -> Recycle -> Compost -> Review
after_po = StrictPartialOrder(nodes=[
    monitor_loop,
    harvest_plan,
    produce_sort,
    pack_biodeg,
    drone_dispatch,
    waste_recycle,
    compost_create,
    cycle_review
])
after_po.order.add_edge(monitor_loop,   harvest_plan)
after_po.order.add_edge(harvest_plan,   produce_sort)
after_po.order.add_edge(produce_sort,   pack_biodeg)
after_po.order.add_edge(pack_biodeg,    drone_dispatch)
after_po.order.add_edge(drone_dispatch, waste_recycle)
after_po.order.add_edge(waste_recycle,  compost_create)
after_po.order.add_edge(compost_create, cycle_review)

# Outer loop: run initial setup, then the rest, then repeat whole cycle
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[initial_po, after_po]
)