# Generated from: 06e0aa93-0c99-4889-a361-f7da4f69fa6b.json
# Description: This process outlines the establishment of an urban rooftop farming system on commercial buildings in densely populated areas. It involves site analysis for structural integrity, microclimate assessment, and local biodiversity considerations. The workflow includes selecting suitable crops based on sunlight exposure and pollution levels, installing modular hydroponic systems, integrating IoT sensors for real-time monitoring, and establishing water recycling loops. The process also requires community engagement for education and maintenance, regulatory compliance checks, and developing a logistics plan for produce distribution directly to local markets. Continuous performance evaluation and iterative improvements ensure sustainability and scalability of the rooftop farm over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label='Site Survey')
load_test         = Transition(label='Load Test')
climate_map       = Transition(label='Climate Map')
crop_select       = Transition(label='Crop Select')
system_design     = Transition(label='System Design')
hydro_install     = Transition(label='Hydro Install')
sensor_setup      = Transition(label='Sensor Setup')
water_loop        = Transition(label='Water Loop')
soil_prep         = Transition(label='Soil Prep')
planting_day      = Transition(label='Planting Day')
data_sync         = Transition(label='Data Sync')
compliance_check  = Transition(label='Compliance Check')
community_meet    = Transition(label='Community Meet')
market_plan       = Transition(label='Market Plan')
maintenance       = Transition(label='Maintenance')
performance_eval  = Transition(label='Performance Eval')

# Loop for continuous performance evaluation and maintenance
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_eval, maintenance]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_map, crop_select,
    system_design, hydro_install, sensor_setup,
    water_loop, soil_prep, planting_day,
    data_sync, compliance_check, community_meet,
    market_plan, loop
])

# Site analysis: survey then structural and climate checks (concurrent)
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, climate_map)

# Crop selection after both tests
root.order.add_edge(load_test, crop_select)
root.order.add_edge(climate_map, crop_select)

# Design and installation sequence
root.order.add_edge(crop_select, system_design)
root.order.add_edge(system_design, hydro_install)
root.order.add_edge(hydro_install, sensor_setup)
root.order.add_edge(sensor_setup, water_loop)

# Planting preparation and execution
root.order.add_edge(water_loop, soil_prep)
root.order.add_edge(soil_prep, planting_day)

# Post‐installation activities
root.order.add_edge(planting_day, data_sync)
root.order.add_edge(planting_day, compliance_check)
root.order.add_edge(compliance_check, community_meet)
root.order.add_edge(community_meet, market_plan)

# Start the continuous improvement loop after data sync and market plan
root.order.add_edge(data_sync, loop)
root.order.add_edge(market_plan, loop)