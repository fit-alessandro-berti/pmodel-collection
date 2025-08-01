# Generated from: 001a421c-d17b-47c6-8508-5cd098f81f0d.json
# Description: This process involves transforming underutilized urban rooftop spaces into productive, sustainable farms. It includes structural assessment to ensure load-bearing capacity, environmental analysis for sunlight and wind patterns, selection of appropriate soil and hydroponic systems, installation of automated irrigation and nutrient delivery, integration of sensor networks for real-time monitoring, community engagement for education and maintenance, and finally, planning for seasonal crop rotation and pest management strategies. The process is designed to maximize green space in cities while promoting local food production and reducing carbon footprints through innovative urban agriculture techniques.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey        = Transition(label='Site Survey')
load_check         = Transition(label='Load Check')
sun_mapping        = Transition(label='Sun Mapping')
wind_study         = Transition(label='Wind Study')
soil_select        = Transition(label='Soil Select')
hydro_setup        = Transition(label='Hydro Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_network     = Transition(label='Sensor Network')
nutrient_plan      = Transition(label='Nutrient Plan')
community_meet     = Transition(label='Community Meet')
training_session   = Transition(label='Training Session')
crop_choice        = Transition(label='Crop Choice')
pest_control       = Transition(label='Pest Control')
harvest_plan       = Transition(label='Harvest Plan')
waste_recycle      = Transition(label='Waste Recycle')
season_switch      = Transition(label='Season Switch')

# Build the loop body for seasonal cycles:
# Pest Control -> Harvest Plan -> Waste Recycle -> Season Switch
body = StrictPartialOrder(nodes=[pest_control, harvest_plan, waste_recycle, season_switch])
body.order.add_edge(pest_control, harvest_plan)
body.order.add_edge(harvest_plan, waste_recycle)
body.order.add_edge(waste_recycle, season_switch)

# Loop: Crop Choice is the entry activity (A), body is B
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_choice, body])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_check,
    sun_mapping,
    wind_study,
    soil_select,
    hydro_setup,
    irrigation_install,
    sensor_network,
    nutrient_plan,
    community_meet,
    training_session,
    seasonal_loop
])

# Add control‐flow dependencies
root.order.add_edge(site_survey,        load_check)
root.order.add_edge(load_check,         sun_mapping)
root.order.add_edge(load_check,         wind_study)
root.order.add_edge(sun_mapping,        soil_select)
root.order.add_edge(wind_study,         soil_select)
root.order.add_edge(sun_mapping,        hydro_setup)
root.order.add_edge(wind_study,         hydro_setup)
root.order.add_edge(hydro_setup,        irrigation_install)
root.order.add_edge(irrigation_install, sensor_network)
root.order.add_edge(sensor_network,     nutrient_plan)
root.order.add_edge(nutrient_plan,      community_meet)
root.order.add_edge(community_meet,     training_session)
root.order.add_edge(training_session,   seasonal_loop)