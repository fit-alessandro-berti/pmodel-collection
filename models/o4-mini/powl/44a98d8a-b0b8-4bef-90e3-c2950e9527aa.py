# Generated from: 44a98d8a-b0b8-4bef-90e3-c2950e9527aa.json
# Description: This process outlines the comprehensive onboarding of a new urban vertical farm into a city's sustainable food supply network. It involves site evaluation, modular system installation, environmental calibration, crop selection tailored to local demand, integration with renewable energy sources, staff training on automated systems, real-time monitoring setup, waste recycling integration, and compliance verification with urban agricultural regulations. The process also includes community engagement initiatives to promote local awareness and partnerships with retailers for direct-to-consumer distribution, ensuring a seamless launch and operational sustainability within a densely populated urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
module_setup    = Transition(label='Module Setup')
env_cal         = Transition(label='Env Calibration')
crop_planning   = Transition(label='Crop Planning')
energy_sync     = Transition(label='Energy Sync')
staff_training  = Transition(label='Staff Training')
sensor_install  = Transition(label='Sensor Install')
data_integration= Transition(label='Data Integration')
waste_setup     = Transition(label='Waste Setup')
reg_review      = Transition(label='Reg Review')
community_meet  = Transition(label='Community Meet')
retail_align    = Transition(label='Retail Align')
launch_prep     = Transition(label='Launch Prep')
system_testing  = Transition(label='System Testing')
feedback_loop   = Transition(label='Feedback Loop')

# Build the LOOP operator: do system testing, then either exit or do feedback_loop and retest
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[system_testing, feedback_loop]
)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, module_setup, env_cal, crop_planning, energy_sync,
    staff_training, sensor_install, data_integration, waste_setup,
    reg_review, community_meet, retail_align, launch_prep, loop_node
])

# Declare the control‐flow edges
root.order.add_edge(site_survey,      module_setup)
root.order.add_edge(module_setup,     env_cal)
root.order.add_edge(env_cal,          crop_planning)
root.order.add_edge(crop_planning,    energy_sync)
root.order.add_edge(energy_sync,      staff_training)
root.order.add_edge(staff_training,   sensor_install)
root.order.add_edge(sensor_install,   data_integration)
root.order.add_edge(data_integration, waste_setup)
root.order.add_edge(waste_setup,      reg_review)

# Parallel community & retail tasks after regulatory review
root.order.add_edge(reg_review,     community_meet)
root.order.add_edge(reg_review,     retail_align)

# Both branches synchronize into launch preparation
root.order.add_edge(community_meet,  launch_prep)
root.order.add_edge(retail_align,    launch_prep)

# Finally launch prep leads into the test&feedback loop
root.order.add_edge(launch_prep,     loop_node)