# Generated from: 4c52a71f-479e-4155-994f-5689039fcc74.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It involves securing rooftop space, designing modular hydroponic systems, obtaining necessary permits, sourcing specialized LED lighting, installing climate control units, and integrating IoT sensors for real-time monitoring. Activities include coordinating with local authorities for zoning approvals, selecting crop varieties suited for indoor growth, training staff on maintenance protocols, and implementing automated nutrient delivery mechanisms. The process also covers marketing strategies targeting local restaurants and markets, establishing supply chain logistics for fresh produce delivery, and continuous optimization based on data analytics to maximize yield while minimizing energy consumption and waste. The complexity arises from balancing urban regulations, technological integration, and sustainable farming practices, all within a limited spatial footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
t_site_survey    = Transition(label="Site Survey")
t_permit_request = Transition(label="Permit Request")
t_design_layout  = Transition(label="Design Layout")

# Concurrent hardware/system preparation
t_system_sourcing = Transition(label="System Sourcing")
t_lighting_setup  = Transition(label="Lighting Setup")
t_climate_install = Transition(label="Climate Install")
t_sensor_deploy   = Transition(label="Sensor Deploy")
po_hardware = StrictPartialOrder(nodes=[
    t_system_sourcing,
    t_lighting_setup,
    t_climate_install,
    t_sensor_deploy
])
# no edges ⇒ fully concurrent

# Sequential follow‐up
t_crop_select     = Transition(label="Crop Select")
t_staff_training  = Transition(label="Staff Training")
t_nutrient_mix    = Transition(label="Nutrient Mix")
t_automation_setup = Transition(label="Automation Setup")

# Concurrent market/logistics planning
t_marketing_plan = Transition(label="Marketing Plan")
t_logistics_plan = Transition(label="Logistics Plan")
po_marketing = StrictPartialOrder(nodes=[
    t_marketing_plan,
    t_logistics_plan
])
# no edges ⇒ fully concurrent

# Continuous optimization loop: Data Review ⇒ (Yield Optimize ‖ Waste Manage)
t_data_review    = Transition(label="Data Review")
t_yield_optimize = Transition(label="Yield Optimize")
t_waste_manage   = Transition(label="Waste Manage")
po_optimize = StrictPartialOrder(nodes=[
    t_yield_optimize,
    t_waste_manage
])
# no edges ⇒ they are concurrent in each iteration

loop_optimization = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_data_review, po_optimize]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    t_site_survey,
    t_permit_request,
    t_design_layout,
    po_hardware,
    t_crop_select,
    t_staff_training,
    t_nutrient_mix,
    t_automation_setup,
    po_marketing,
    loop_optimization
])

# Define the control‐flow dependencies (a chain of tasks with parallel blocks in between)
root.order.add_edge(t_site_survey,    t_permit_request)
root.order.add_edge(t_permit_request, t_design_layout)
root.order.add_edge(t_design_layout,  po_hardware)
root.order.add_edge(po_hardware,      t_crop_select)
root.order.add_edge(t_crop_select,    t_staff_training)
root.order.add_edge(t_staff_training, t_nutrient_mix)
root.order.add_edge(t_nutrient_mix,   t_automation_setup)
root.order.add_edge(t_automation_setup, po_marketing)
root.order.add_edge(po_marketing,     loop_optimization)