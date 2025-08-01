# Generated from: cb08ee58-551d-4d2e-bada-fcf761cb518d.json
# Description: This process outlines the complex establishment of an urban vertical farming facility within a dense metropolitan area. It involves site selection based on sunlight and water access, modular system design tailored to building constraints, integration of IoT sensors for real-time crop monitoring, specialized nutrient delivery setup, automated climate control calibration, and compliance with local agricultural and safety regulations. The process also includes community engagement for sustainable practices, energy source assessment emphasizing renewable options, staff training on hydroponic and aeroponic techniques, and post-installation performance optimization to maximize yield while minimizing resource consumption. Throughout, synchronization with urban infrastructure and environmental impact assessments are critical to ensure feasibility and sustainability in an atypical urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey   = Transition(label='Site Survey')
light_map     = Transition(label='Light Mapping')
water_test    = Transition(label='Water Testing')
design        = Transition(label='Design Modules')
reg_check     = Transition(label='Regulatory Check')
iot_setup     = Transition(label='IoT Setup')
sensor_cal    = Transition(label='Sensor Calibration')
nutrient      = Transition(label='Nutrient Mix')
climate       = Transition(label='Climate Control')
community     = Transition(label='Community Meet')
energy        = Transition(label='Energy Audit')
training      = Transition(label='Staff Training')
install       = Transition(label='Installation')
testing       = Transition(label='System Testing')
yield_a       = Transition(label='Yield Analysis')
resource      = Transition(label='Resource Audit')
impact        = Transition(label='Impact Review')

# Loop for iterative design → regulatory check
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design, reg_check])
# Loop for iterative sensor calibration → system testing
test_loop   = OperatorPOWL(operator=Operator.LOOP, children=[sensor_cal, testing])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_map, water_test,
    design_loop, iot_setup, test_loop,
    nutrient, climate, community, energy, training,
    install,
    yield_a, resource, impact
])

# Define the ordering relations
root.order.add_edge(site_survey, light_map)
root.order.add_edge(site_survey, water_test)

root.order.add_edge(light_map, design_loop)
root.order.add_edge(water_test, design_loop)

root.order.add_edge(design_loop, iot_setup)
root.order.add_edge(iot_setup, test_loop)

# After testing loop, five parallel activities
for act in (nutrient, climate, community, energy, training):
    root.order.add_edge(test_loop, act)
    root.order.add_edge(act, install)

# Final analysis steps
root.order.add_edge(install, yield_a)
root.order.add_edge(install, resource)
root.order.add_edge(install, impact)