# Generated from: 94f97a1e-a4f9-4a25-a8f1-3f7d6eda5fab.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm in a densely populated city. It involves assessing structural integrity, securing permits, designing modular planting systems, sourcing sustainable materials, implementing water recycling mechanisms, integrating IoT sensors for monitoring, training staff in urban agriculture techniques, and coordinating with local markets for produce distribution. The workflow ensures environmental compliance, optimizes space utilization, and fosters community engagement through workshops and volunteer programs, ultimately creating a scalable and eco-friendly urban farming solution that enhances food security and green urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions (activities)
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')

permit_apply = Transition(label='Permit Apply')

design_layout = Transition(label='Design Layout')

material_sourcing = Transition(label='Material Sourcing')
modular_build = Transition(label='Modular Build')

soil_prep = Transition(label='Soil Prep')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
system_test = Transition(label='System Test')

staff_training = Transition(label='Staff Training')

crop_planting = Transition(label='Crop Planting')
data_monitoring = Transition(label='Data Monitoring')

market_liaison = Transition(label='Market Liaison')

community_event = Transition(label='Community Event')
waste_manage = Transition(label='Waste Manage')

harvest_plan = Transition(label='Harvest Plan')

# Model description interpretation:
# Step 1: Assess structural integrity: Site Survey --> Load Test
# Step 2: Secure permits: Permit Apply (after Load Test)
# Step 3: Design modular planting systems: Design Layout (after permits)
# Step 4-5: Source materials and Modular Build (concurrent)
# Step 6: Soil Prep, Irrigation Setup, Sensor Install, System Test (sequential)
# Step 7: Staff Training
# Step 8: Crop Planting --> Data Monitoring (monitoring ongoing)
# Step 9: Market Liaison (concurrent with Data Monitoring)
# Step 10: Community Event and Waste Manage (concurrent)
# Step 11: Harvest Plan (final step)

# Partial order for step 4-5 concurrent activities
materials_and_build = StrictPartialOrder(nodes=[material_sourcing, modular_build])
# no order edges between them => concurrent

# Partial order for soil and system setup
soil_and_system = StrictPartialOrder(
    nodes=[soil_prep, irrigation_setup, sensor_install, system_test])
soil_and_system.order.add_edge(soil_prep, irrigation_setup)
soil_and_system.order.add_edge(irrigation_setup, sensor_install)
soil_and_system.order.add_edge(sensor_install, system_test)

# Partial order for Crop Planting and Data Monitoring and Market Liaison (Data Monitoring and Market Liaison concurrent)
crop_and_monitoring_market = StrictPartialOrder(
    nodes=[crop_planting, data_monitoring, market_liaison])
crop_and_monitoring_market.order.add_edge(crop_planting, data_monitoring)
# Market Liaison concurrent, no edges to/from it directly

# Partial order for community event and waste management (concurrent)
community_and_waste = StrictPartialOrder(nodes=[community_event, waste_manage])
# no edge between them

# Step 1-2
step_1_2 = StrictPartialOrder(nodes=[site_survey, load_test, permit_apply])
step_1_2.order.add_edge(site_survey, load_test)
step_1_2.order.add_edge(load_test, permit_apply)

# Step 3
# design layout after permits
step_3 = StrictPartialOrder(nodes=[permit_apply, design_layout])
step_3.order.add_edge(permit_apply, design_layout)

# Combine design_layout -> materials_and_build
step_3_4_5 = StrictPartialOrder(
    nodes=[design_layout, materials_and_build])
step_3_4_5.order.add_edge(design_layout, materials_and_build)

# Combine materials_and_build -> soil_and_system
step_4_5_6 = StrictPartialOrder(
    nodes=[materials_and_build, soil_and_system])
step_4_5_6.order.add_edge(materials_and_build, soil_and_system)

# soil_and_system -> staff_training
step_6_7 = StrictPartialOrder(
    nodes=[soil_and_system, staff_training])
step_6_7.order.add_edge(soil_and_system, staff_training)

# staff_training -> crop_and_monitoring_market
step_7_8_9 = StrictPartialOrder(
    nodes=[staff_training, crop_and_monitoring_market])
step_7_8_9.order.add_edge(staff_training, crop_and_monitoring_market)

# crop_and_monitoring_market -> community_and_waste
step_9_10 = StrictPartialOrder(
    nodes=[crop_and_monitoring_market, community_and_waste])
step_9_10.order.add_edge(crop_and_monitoring_market, community_and_waste)

# community_and_waste -> harvest_plan
final_step = StrictPartialOrder(
    nodes=[community_and_waste, harvest_plan])
final_step.order.add_edge(community_and_waste, harvest_plan)

# Now create the root PartialOrder combining all:
root = StrictPartialOrder(nodes=[
    step_1_2,
    step_3_4_5,
    step_4_5_6,
    step_6_7,
    step_7_8_9,
    step_9_10,
    final_step,
])

# Add partial order edges reflecting sequential steps:
root.order.add_edge(step_1_2, step_3_4_5)
root.order.add_edge(step_3_4_5, step_4_5_6)
root.order.add_edge(step_4_5_6, step_6_7)
root.order.add_edge(step_6_7, step_7_8_9)
root.order.add_edge(step_7_8_9, step_9_10)
root.order.add_edge(step_9_10, final_step)