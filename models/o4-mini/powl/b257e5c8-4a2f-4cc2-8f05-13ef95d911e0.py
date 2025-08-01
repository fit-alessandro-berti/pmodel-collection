# Generated from: b257e5c8-4a2f-4cc2-8f05-13ef95d911e0.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It includes initial site evaluation, structural integrity checks, environmental impact assessments, securing permits from multiple authorities, designing modular planting systems, sourcing sustainable soil and water solutions, integrating IoT sensors for monitoring, training staff for urban agriculture techniques, marketing to local communities, and establishing supply chains for fresh produce distribution. The process ensures compliance with city regulations, maximizes yield in limited space, and promotes sustainable urban food production while addressing logistical and environmental challenges unique to rooftop farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey   = Transition(label='Site Survey')
load_test     = Transition(label='Load Test')
impact_study  = Transition(label='Impact Study')
permit_apply  = Transition(label='Permit Apply')
design_layout = Transition(label='Design Layout')
soil_source   = Transition(label='Soil Source')
water_setup   = Transition(label='Water Setup')
sensor_install= Transition(label='Sensor Install')
staff_train   = Transition(label='Staff Train')
plant_seed    = Transition(label='Plant Seed')
irrigation_ck = Transition(label='Irrigation Check')
pest_control  = Transition(label='Pest Control')
harvest_plan  = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
delivery_route= Transition(label='Delivery Route')
waste_manage  = Transition(label='Waste Manage')

# Loop: perform irrigation check, then either exit or do pest control then irrigation check again
loop_irrigation = OperatorPOWL(
    operator=Operator.LOOP,
    children=[irrigation_ck, pest_control]
)

# Compose the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, impact_study, permit_apply,
    design_layout, soil_source, water_setup,
    sensor_install, staff_train, plant_seed,
    loop_irrigation, harvest_plan, market_launch,
    delivery_route, waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,   load_test)
root.order.add_edge(load_test,     impact_study)
root.order.add_edge(impact_study,  permit_apply)
root.order.add_edge(permit_apply,  design_layout)

# After design, soil sourcing and water setup can run in parallel
root.order.add_edge(design_layout, soil_source)
root.order.add_edge(design_layout, water_setup)

# Both soil and water must complete before installing sensors
root.order.add_edge(soil_source,   sensor_install)
root.order.add_edge(water_setup,   sensor_install)

root.order.add_edge(sensor_install, staff_train)
root.order.add_edge(staff_train,    plant_seed)

# After planting, enter the irrigation/pest-control loop
root.order.add_edge(plant_seed,     loop_irrigation)

# Once the loop finishes, plan the harvest
root.order.add_edge(loop_irrigation, harvest_plan)

# Then launch marketing
root.order.add_edge(harvest_plan,   market_launch)

# Finally, distribution (delivery) and waste management can proceed in parallel
root.order.add_edge(market_launch,  delivery_route)
root.order.add_edge(market_launch,  waste_manage)