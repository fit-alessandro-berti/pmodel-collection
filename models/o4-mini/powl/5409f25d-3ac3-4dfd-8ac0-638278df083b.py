# Generated from: 5409f25d-3ac3-4dfd-8ac0-638278df083b.json
# Description: This process outlines the establishment of an urban rooftop farm involving site assessment, environmental analysis, and installation of modular hydroponic systems. Activities include coordination with local authorities, sourcing sustainable materials, implementing water recycling solutions, and integrating IoT sensors for climate control. The process also covers staff training on crop management, pest control without chemicals, and community engagement to promote local food production. Continuous monitoring and data analysis ensure optimal yield and resource efficiency in an atypical but increasingly vital urban agricultural practice.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label='Site Survey')
permit_request   = Transition(label='Permit Request')
soil_testing     = Transition(label='Soil Testing')
material_sourcing= Transition(label='Material Sourcing')
system_design    = Transition(label='System Design')
water_setup      = Transition(label='Water Setup')
sensor_install   = Transition(label='Sensor Install')
climate_setup    = Transition(label='Climate Setup')
plant_selection  = Transition(label='Plant Selection')
seed_planting    = Transition(label='Seed Planting')
irrigation_config= Transition(label='Irrigation Config')
staff_training   = Transition(label='Staff Training')
community_meet   = Transition(label='Community Meet')
pest_monitoring  = Transition(label='Pest Monitoring')
yield_tracking   = Transition(label='Yield Tracking')
data_analysis    = Transition(label='Data Analysis')
waste_manage     = Transition(label='Waste Manage')

# Silent transition for loop exit
skip = SilentTransition()

# Define the continuous monitoring loop body
loop_body = StrictPartialOrder(nodes=[
    pest_monitoring,
    yield_tracking,
    data_analysis,
    waste_manage
])
# Within the loop, monitoring & yield feed into analysis, then waste management
loop_body.order.add_edge(pest_monitoring, data_analysis)
loop_body.order.add_edge(yield_tracking, data_analysis)
loop_body.order.add_edge(data_analysis, waste_manage)

# LOOP operator: repeat monitoring until exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_request,
    soil_testing,
    material_sourcing,
    system_design,
    water_setup,
    sensor_install,
    climate_setup,
    plant_selection,
    seed_planting,
    irrigation_config,
    staff_training,
    community_meet,
    monitor_loop
])

# Define the control-flow edges
root.order.add_edge(site_survey,      permit_request)
root.order.add_edge(site_survey,      soil_testing)
root.order.add_edge(permit_request,   material_sourcing)
root.order.add_edge(permit_request,   system_design)
root.order.add_edge(soil_testing,     system_design)
root.order.add_edge(material_sourcing, water_setup)
root.order.add_edge(system_design,     water_setup)
root.order.add_edge(water_setup,       sensor_install)
root.order.add_edge(sensor_install,    climate_setup)
root.order.add_edge(climate_setup,     plant_selection)
root.order.add_edge(plant_selection,   seed_planting)
root.order.add_edge(seed_planting,     irrigation_config)
# After irrigation configuration, train staff and engage community in parallel
root.order.add_edge(irrigation_config, staff_training)
root.order.add_edge(irrigation_config, community_meet)
# Once training and community meeting are done, enter the monitoring loop
root.order.add_edge(staff_training,    monitor_loop)
root.order.add_edge(community_meet,    monitor_loop)