# Generated from: d6c6ede5-218c-42b8-b8c3-753047694a75.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It involves initial feasibility studies including structural assessments, microclimate analysis, and local regulations review. Following approvals, the process continues with soil-less system design, procurement of specialized equipment such as hydroponic trays and automated irrigation systems, installation of solar-powered sensors for real-time monitoring, and staff training on sustainable farming practices. Finally, the setup includes pilot planting, data collection on crop yield and environmental impact, ongoing maintenance scheduling, and community engagement initiatives to promote urban agriculture awareness and participation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_survey    = Transition(label='Site Survey')
load_test      = Transition(label='Load Test')
climate_study  = Transition(label='Climate Study')
permit_check   = Transition(label='Permit Check')
system_design  = Transition(label='System Design')
equipment_buy  = Transition(label='Equipment Buy')
sensor_setup   = Transition(label='Sensor Setup')
irrigation_fit = Transition(label='Irrigation Fit')
solar_install  = Transition(label='Solar Install')
staff_train    = Transition(label='Staff Train')
pilot_plant    = Transition(label='Pilot Plant')
crop_harvest   = Transition(label='Crop Harvest')
data_monitor   = Transition(label='Data Monitor')
maintenance_plan = Transition(label='Maintenance Plan')
community_meet   = Transition(label='Community Meet')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_study, permit_check,
    system_design, equipment_buy,
    sensor_setup, irrigation_fit, solar_install, staff_train,
    pilot_plant, crop_harvest, data_monitor,
    maintenance_plan, community_meet
])

# Initial feasibility: site survey → (load, climate, permit) in parallel
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, permit_check)

# After feasibility all three feed into design
root.order.add_edge(load_test, system_design)
root.order.add_edge(climate_study, system_design)
root.order.add_edge(permit_check, system_design)

# Design → procurement
root.order.add_edge(system_design, equipment_buy)

# Procurement → parallel installations
root.order.add_edge(equipment_buy, sensor_setup)
root.order.add_edge(equipment_buy, irrigation_fit)
root.order.add_edge(equipment_buy, solar_install)

# Installations → staff training
root.order.add_edge(sensor_setup, staff_train)
root.order.add_edge(irrigation_fit, staff_train)
root.order.add_edge(solar_install, staff_train)

# Training → pilot planting → harvest → data monitoring
root.order.add_edge(staff_train, pilot_plant)
root.order.add_edge(pilot_plant, crop_harvest)
root.order.add_edge(crop_harvest, data_monitor)

# Data monitoring → (maintenance planning, community engagement) in parallel
root.order.add_edge(data_monitor, maintenance_plan)
root.order.add_edge(data_monitor, community_meet)