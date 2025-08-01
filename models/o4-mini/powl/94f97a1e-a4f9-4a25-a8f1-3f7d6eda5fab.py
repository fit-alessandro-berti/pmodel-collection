# Generated from: 94f97a1e-a4f9-4a25-a8f1-3f7d6eda5fab.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm in a densely populated city. It involves assessing structural integrity, securing permits, designing modular planting systems, sourcing sustainable materials, implementing water recycling mechanisms, integrating IoT sensors for monitoring, training staff in urban agriculture techniques, and coordinating with local markets for produce distribution. The workflow ensures environmental compliance, optimizes space utilization, and fosters community engagement through workshops and volunteer programs, ultimately creating a scalable and eco-friendly urban farming solution that enhances food security and green urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey      = Transition(label='Site Survey')
load_test        = Transition(label='Load Test')
permit_apply     = Transition(label='Permit Apply')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
modular_build    = Transition(label='Modular Build')
soil_prep        = Transition(label='Soil Prep')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install   = Transition(label='Sensor Install')
system_test      = Transition(label='System Test')
data_monitoring  = Transition(label='Data Monitoring')
staff_training   = Transition(label='Staff Training')
crop_planting    = Transition(label='Crop Planting')
harvest_plan     = Transition(label='Harvest Plan')
market_liaison   = Transition(label='Market Liaison')
community_event  = Transition(label='Community Event')
waste_manage     = Transition(label='Waste Manage')

# Model the test-monitor loop: do system test, then either exit or monitor then test again
test_monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[system_test, data_monitoring]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    permit_apply,
    design_layout,
    material_sourcing,
    modular_build,
    soil_prep,
    irrigation_setup,
    sensor_install,
    test_monitor_loop,
    staff_training,
    crop_planting,
    harvest_plan,
    market_liaison,
    community_event,
    waste_manage
])

# Define precedence relations
o = root.order
o.add_edge(site_survey,      load_test)
o.add_edge(load_test,        permit_apply)
o.add_edge(permit_apply,     design_layout)
o.add_edge(design_layout,    material_sourcing)
o.add_edge(material_sourcing,modular_build)

# After the modular build: prepare soil, set up irrigation, and handle construction waste
o.add_edge(modular_build, soil_prep)
o.add_edge(modular_build, irrigation_setup)
o.add_edge(modular_build, waste_manage)

# Sensor installation after ground and irrigation ready
o.add_edge(soil_prep,        sensor_install)
o.add_edge(irrigation_setup, sensor_install)

# Then enter the test–monitor loop
o.add_edge(sensor_install,   test_monitor_loop)

# After the loop, train staff, liaise with markets, and run community events in parallel
o.add_edge(test_monitor_loop, staff_training)
o.add_edge(test_monitor_loop, market_liaison)
o.add_edge(test_monitor_loop, community_event)

# Staff training leads to planting; marketing & community lead into harvest planning
o.add_edge(staff_training,   crop_planting)
o.add_edge(crop_planting,    harvest_plan)
o.add_edge(market_liaison,   harvest_plan)
o.add_edge(community_event,   harvest_plan)

# Ensure waste management (cleanup/recycling) is done before final harvest plan
o.add_edge(waste_manage,     harvest_plan)