# Generated from: 0c1f9bfe-a114-45bf-afb8-985999331140.json
# Description: This process outlines the establishment of an urban vertical farm within a multi-story building in a dense city environment. It involves initial site assessment for structural integrity, followed by modular hydroponic system installation. Climate control calibration is performed to optimize plant growth, including lighting and humidity adjustments. Nutrient solution recipes are developed and tested for various crops. Automation systems integrate sensor data for real-time monitoring. Workforce training is conducted to manage technology and manual tasks. Waste recycling strategies are implemented to minimize environmental impact. Finally, distribution channels are coordinated with local markets and restaurants, ensuring fresh produce delivery within tight urban logistics constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess    = Transition(label='Site Assess')
load_test      = Transition(label='Load Test')
modular_install= Transition(label='Modular Install')
hydro_setup    = Transition(label='Hydro Setup')
climate_tune   = Transition(label='Climate Tune')
light_adjust   = Transition(label='Light Adjust')
nutrient_mix   = Transition(label='Nutrient Mix')
crop_trial     = Transition(label='Crop Trial')
sensor_deploy  = Transition(label='Sensor Deploy')
system_sync    = Transition(label='System Sync')
staff_train    = Transition(label='Staff Train')
waste_plan     = Transition(label='Waste Plan')
market_link    = Transition(label='Market Link')
route_plan     = Transition(label='Route Plan')
delivery_set   = Transition(label='Delivery Set')

# Build partial order
root = StrictPartialOrder(nodes=[
    site_assess, load_test, modular_install, hydro_setup,
    climate_tune, light_adjust, nutrient_mix, crop_trial,
    sensor_deploy, system_sync, staff_train, waste_plan,
    market_link, route_plan, delivery_set
])

# Add dependencies
root.order.add_edge(site_assess, load_test)
root.order.add_edge(load_test, modular_install)
root.order.add_edge(modular_install, hydro_setup)
root.order.add_edge(hydro_setup, climate_tune)
root.order.add_edge(climate_tune, light_adjust)
root.order.add_edge(light_adjust, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_trial)
root.order.add_edge(crop_trial, sensor_deploy)
root.order.add_edge(sensor_deploy, system_sync)
root.order.add_edge(system_sync, staff_train)
root.order.add_edge(staff_train, waste_plan)
# After waste planning, distribution channels setup in parallel
root.order.add_edge(waste_plan, market_link)
root.order.add_edge(waste_plan, route_plan)
# Both market and route plans precede final delivery
root.order.add_edge(market_link, delivery_set)
root.order.add_edge(route_plan, delivery_set)