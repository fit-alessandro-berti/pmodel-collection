# Generated from: 184bf411-abe9-4d61-8bce-5c577be2da95.json
# Description: This process outlines the complex steps required to establish a sustainable urban rooftop farm in a metropolitan environment. It involves assessing structural viability, securing permits, selecting crop types based on microclimate analysis, installing modular hydroponic systems, integrating IoT sensors for environment monitoring, implementing water recycling mechanisms, training staff in vertical farming techniques, managing pest control using organic methods, coordinating with local suppliers for seed and nutrient sourcing, establishing a community engagement program for education and outreach, scheduling regular maintenance and yield optimization, and finally setting up distribution channels to local markets and restaurants. The process ensures environmental sustainability, maximizes limited urban space, and fosters local food production with a focus on innovation and community involvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
load_test        = Transition(label='Load Test')
permit_apply     = Transition(label='Permit Apply')
crop_select      = Transition(label='Crop Select')
system_design    = Transition(label='System Design')
sensor_setup     = Transition(label='Sensor Setup')
water_recycle    = Transition(label='Water Recycle')
staff_train      = Transition(label='Staff Train')
pest_control     = Transition(label='Pest Control')
supplier_link    = Transition(label='Supplier Link')
community_engage = Transition(label='Community Engage')
maintenance_plan = Transition(label='Maintenance Plan')
yield_monitor    = Transition(label='Yield Monitor')
market_setup     = Transition(label='Market Setup')
logistics_plan   = Transition(label='Logistics Plan')

# Loop for ongoing maintenance and yield monitoring
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance_plan, yield_monitor]
)

# Build the partial order (root)
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    permit_apply,
    crop_select,
    system_design,
    sensor_setup,
    water_recycle,
    staff_train,
    pest_control,
    supplier_link,
    community_engage,
    maintenance_loop,
    market_setup,
    logistics_plan
])

# Specify ordering constraints
root.order.add_edge(site_survey,      load_test)
root.order.add_edge(load_test,        permit_apply)
root.order.add_edge(permit_apply,     crop_select)
root.order.add_edge(crop_select,      system_design)
root.order.add_edge(system_design,    sensor_setup)
root.order.add_edge(sensor_setup,     water_recycle)
root.order.add_edge(water_recycle,    staff_train)

# After staff training, pest control and supplier linking can proceed in parallel
root.order.add_edge(staff_train,      pest_control)
root.order.add_edge(staff_train,      supplier_link)

# Both pest control and supplier link precede community engagement
root.order.add_edge(pest_control,     community_engage)
root.order.add_edge(supplier_link,    community_engage)

# Community engagement leads into the maintenance loop
root.order.add_edge(community_engage, maintenance_loop)

# After maintenance loop, set up distribution channels
root.order.add_edge(maintenance_loop, market_setup)
root.order.add_edge(market_setup,     logistics_plan)