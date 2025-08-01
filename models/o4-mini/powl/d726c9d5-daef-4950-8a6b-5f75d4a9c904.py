# Generated from: d726c9d5-daef-4950-8a6b-5f75d4a9c904.json
# Description: This process outlines the establishment of an urban rooftop farming system in a dense metropolitan area. It involves site assessment, structural evaluation, soil and water testing, and selecting suitable crops based on microclimate data. The procedure also includes procuring eco-friendly materials, installing modular planters, integrating automated irrigation and nutrient delivery systems, and setting up solar-powered sensors for real-time environmental monitoring. Additionally, community engagement and training sessions are conducted to ensure sustainable maintenance and maximize local participation. The process concludes with periodic yield analysis and adaptive adjustments to optimize productivity while minimizing environmental impact in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey      = Transition(label='Site Survey')
structure_check  = Transition(label='Structure Check')
soil_sample      = Transition(label='Soil Sample')
water_test       = Transition(label='Water Test')
crop_selection   = Transition(label='Crop Selection')
material_order   = Transition(label='Material Order')
planter_setup    = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy    = Transition(label='Sensor Deploy')
solar_setup      = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet   = Transition(label='Community Meet')
training_session = Transition(label='Training Session')
yield_monitor    = Transition(label='Yield Monitor')
adjust_plan      = Transition(label='Adjust Plan')

# Loop for periodic yield monitoring and adaptive adjustments
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitor, adjust_plan]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_check,
    soil_sample,
    water_test,
    crop_selection,
    material_order,
    planter_setup,
    irrigation_install,
    sensor_deploy,
    solar_setup,
    data_integration,
    community_meet,
    training_session,
    monitor_loop
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, soil_sample)
root.order.add_edge(structure_check, water_test)
root.order.add_edge(soil_sample, crop_selection)
root.order.add_edge(water_test, crop_selection)
root.order.add_edge(crop_selection, material_order)
root.order.add_edge(material_order, planter_setup)
root.order.add_edge(planter_setup, irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy, solar_setup)
root.order.add_edge(solar_setup, data_integration)
root.order.add_edge(data_integration, community_meet)
root.order.add_edge(community_meet, training_session)
root.order.add_edge(training_session, monitor_loop)