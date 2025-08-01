# Generated from: f0469137-9d56-4175-81bc-231607cd73fd.json
# Description: This process outlines the comprehensive management of an urban vertical farm focusing on optimizing crop yield and sustainability in limited space environments. It begins with site analysis and climate adaptation, followed by nutrient mixing and seed germination in controlled chambers. Automated planting ensures precise spacing, while multi-level irrigation systems deliver water and nutrients. Continuous monitoring through IoT sensors tracks growth parameters and pest presence, triggering targeted drone interventions for pollination or pesticide application. Harvesting involves robotic arms that selectively pick ripe produce, followed by quality inspection and packaging within sterile conditions. The cycle concludes with waste recycling and energy optimization to maintain eco-friendly operations, ensuring a closed-loop agricultural system tailored for urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_analysis = Transition(label='Site Analysis')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_germinate = Transition(label='Seed Germinate')
auto_planting = Transition(label='Auto Planting')
irrigation_setup = Transition(label='Irrigation Setup')
iot_monitoring = Transition(label='IoT Monitoring')
pest_detection = Transition(label='Pest Detection')
drone_pollinate = Transition(label='Drone Pollinate')
pesticide_spray = Transition(label='Pesticide Spray')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
package_product = Transition(label='Package Product')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
data_logging = Transition(label='Data Logging')

# Drone interventions choice: after Pest Detection, choose between Drone Pollinate or Pesticide Spray
drone_intervention = OperatorPOWL(operator=Operator.XOR, children=[drone_pollinate, pesticide_spray])

# Loop around drone intervention and IoT monitoring & pest detection:
# Loop bodies:
# A = IoT Monitoring -> Pest Detection
# B = Drone Intervention (choice of pollinate / spray)
A_loop = StrictPartialOrder(nodes=[iot_monitoring, pest_detection])
A_loop.order.add_edge(iot_monitoring, pest_detection)

# Loop node: * (A, B)
loop_drone = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, drone_intervention])

# Partial order for activities before the loop:
# Site Analysis -> Climate Setup -> Nutrient Mix -> Seed Germinate -> Auto Planting -> Irrigation Setup
pre_loop = StrictPartialOrder(nodes=[
    site_analysis, climate_setup, nutrient_mix, seed_germinate, auto_planting, irrigation_setup
])
pre_loop.order.add_edge(site_analysis, climate_setup)
pre_loop.order.add_edge(climate_setup, nutrient_mix)
pre_loop.order.add_edge(nutrient_mix, seed_germinate)
pre_loop.order.add_edge(seed_germinate, auto_planting)
pre_loop.order.add_edge(auto_planting, irrigation_setup)

# Activities after the loop:
# Robotic Harvest -> Quality Check -> Package Product
post_loop = StrictPartialOrder(nodes=[robotic_harvest, quality_check, package_product])
post_loop.order.add_edge(robotic_harvest, quality_check)
post_loop.order.add_edge(quality_check, package_product)

# Final concurrent activities after post_loop:
# Waste Recycle, Energy Optimize, Data Logging
final_concurrent = StrictPartialOrder(nodes=[waste_recycle, energy_optimize, data_logging])
# no order edges: all concurrent

# Compose all parts in a partial order graph:
# pre_loop -> loop_drone -> post_loop -> final_concurrent
root = StrictPartialOrder(nodes=[pre_loop, loop_drone, post_loop, final_concurrent])
root.order.add_edge(pre_loop, loop_drone)
root.order.add_edge(loop_drone, post_loop)
root.order.add_edge(post_loop, final_concurrent)