# Generated from: 1d21af9b-7f4c-45fd-a2c4-0b40eeae3eaa.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a dense metropolitan environment. It includes site evaluation for structural integrity, microclimate assessment, integration of automated hydroponic systems, real-time nutrient monitoring, energy optimization using renewable sources, vertical crop rotation planning, waste recycling loops, IoT sensor calibration, pest control through bioengineering, and community engagement for local food distribution. The process ensures sustainable food production while balancing technology, environment, and urban constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey     = Transition(label='Site Survey')
load_test       = Transition(label='Load Test')
climate_map     = Transition(label='Climate Map')
system_design   = Transition(label='System Design')
hydro_setup     = Transition(label='Hydro Setup')
sensor_install  = Transition(label='Sensor Install')
nutrient_mix    = Transition(label='Nutrient Mix')
data_sync       = Transition(label='Data Sync')
waste_loop_act  = Transition(label='Waste Loop')
water_cycle     = Transition(label='Water Cycle')
energy_audit    = Transition(label='Energy Audit')
crop_planning   = Transition(label='Crop Planning')
pest_control    = Transition(label='Pest Control')
yield_forecast  = Transition(label='Yield Forecast')
community_link  = Transition(label='Community Link')

# Define the loops
nutrient_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[nutrient_mix, data_sync]
)

waste_recycle_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[waste_loop_act, water_cycle]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_map, system_design,
    hydro_setup, sensor_install, energy_audit, crop_planning,
    pest_control, yield_forecast, community_link,
    nutrient_loop, waste_recycle_loop
])

# Define the control-flow dependencies
# 1. Structural assessment
root.order.add_edge(site_survey, load_test)
# 2. Microclimate assessment
root.order.add_edge(load_test, climate_map)
# 3. Design & setup
root.order.add_edge(climate_map, system_design)
root.order.add_edge(system_design, hydro_setup)
# 4. Sensor installation
root.order.add_edge(hydro_setup, sensor_install)
# 5. After sensor install:
#    - energy audit
#    - nutrient monitoring loop
#    - waste recycling loop
root.order.add_edge(sensor_install, energy_audit)
root.order.add_edge(sensor_install, nutrient_loop)
root.order.add_edge(sensor_install, waste_recycle_loop)
# 6. Proceed to planning & control
root.order.add_edge(energy_audit, crop_planning)
root.order.add_edge(crop_planning, pest_control)
# 7. Final forecast needs results from loops and pest control
root.order.add_edge(pest_control, yield_forecast)
root.order.add_edge(nutrient_loop, yield_forecast)
root.order.add_edge(waste_recycle_loop, yield_forecast)
# 8. Community engagement at the end
root.order.add_edge(yield_forecast, community_link)