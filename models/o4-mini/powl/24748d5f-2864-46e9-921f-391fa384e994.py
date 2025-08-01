# Generated from: 24748d5f-2864-46e9-921f-391fa384e994.json
# Description: This process describes the adaptive urban farming cycle designed to optimize crop yield in constrained city environments by integrating sensor data, real-time environmental analysis, and community feedback. Starting with soil prep and seed selection, the cycle involves continuous monitoring, nutrient balancing, pest detection, and automated irrigation adjustments. It incorporates periodic crop rotation based on predictive analytics, waste recycling into compost, and community workshops to educate urban farmers. The process dynamically adapts to weather patterns and urban pollution levels, ensuring sustainable produce with minimal resource waste while fostering local engagement and resilience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
soil_prep       = Transition(label='Soil Prep')
seed_select     = Transition(label='Seed Select')
plant_setup     = Transition(label='Plant Setup')
sensor_install  = Transition(label='Sensor Install')
env_monitor     = Transition(label='Env Monitor')
data_analyze    = Transition(label='Data Analyze')
irrigation_adj  = Transition(label='Irrigation Adjust')
nutrient_mix    = Transition(label='Nutrient Mix')
pest_detect     = Transition(label='Pest Detect')
crop_rotate     = Transition(label='Crop Rotate')
waste_collect   = Transition(label='Waste Collect')
compost_make    = Transition(label='Compost Make')
weather_check   = Transition(label='Weather Check')
pollution_assess= Transition(label='Pollution Assess')
community_meet  = Transition(label='Community Meet')
feedback_loop   = Transition(label='Feedback Loop')

# Monitoring & analysis partial order: Env Monitor -> Data Analyze
monitor_po = StrictPartialOrder(nodes=[env_monitor, data_analyze])
monitor_po.order.add_edge(env_monitor, data_analyze)

# Adjustment actions concurrent: Irrigation Adjust, Nutrient Mix, Pest Detect
adjust_po = StrictPartialOrder(nodes=[irrigation_adj, nutrient_mix, pest_detect])
# no edges => all three can happen concurrently

# Loop: do (monitor_po) then either exit or do (adjust_po) then repeat monitor_po
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_po, adjust_po])

# Waste cycle: Waste Collect -> Compost Make
waste_cycle = StrictPartialOrder(nodes=[waste_collect, compost_make])
waste_cycle.order.add_edge(waste_collect, compost_make)

# Community engagement cycle: Community Meet -> Feedback Loop
community_cycle = StrictPartialOrder(nodes=[community_meet, feedback_loop])
community_cycle.order.add_edge(community_meet, feedback_loop)

# Assemble the root partial order of the entire process
root = StrictPartialOrder(nodes=[
    soil_prep,
    seed_select,
    plant_setup,
    sensor_install,
    monitor_loop,
    crop_rotate,
    waste_cycle,
    weather_check,
    pollution_assess,
    community_cycle
])

# Define the global sequencing constraints
root.order.add_edge(soil_prep,       seed_select)
root.order.add_edge(seed_select,     plant_setup)
root.order.add_edge(plant_setup,     sensor_install)
root.order.add_edge(sensor_install,  monitor_loop)
root.order.add_edge(monitor_loop,    crop_rotate)
root.order.add_edge(crop_rotate,     waste_cycle)
root.order.add_edge(waste_cycle,     weather_check)
root.order.add_edge(weather_check,   pollution_assess)
root.order.add_edge(pollution_assess,community_cycle)