# Generated from: d14ba506-0d58-4af4-be6b-354e7d87b3f7.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed commercial building. It begins with site analysis and structural assessment, followed by modular rack installation for crops. Integrated hydroponic and aeroponic systems are then calibrated to optimize water and nutrient delivery. Environmental controls including LED lighting, temperature, and humidity sensors are programmed for crop-specific growth cycles. The process also includes waste recycling loops for organic matter and water reuse. Staff training on system maintenance and crop monitoring is conducted before initiating a test grow phase. Finally, continuous data analytics are implemented to refine yields and operational efficiency, ensuring sustainability and profitability in an urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
rack_install = Transition(label='Rack Install')
system_setup = Transition(label='System Setup')
hydroponics_config = Transition(label='Hydroponics Config')
aeroponics_tune = Transition(label='Aeroponics Tune')
lighting_setup = Transition(label='Lighting Setup')
enviro_control = Transition(label='Enviro Control')
sensor_deploy = Transition(label='Sensor Deploy')
waste_recycle = Transition(label='Waste Recycle')
water_reuse = Transition(label='Water Reuse')
staff_training = Transition(label='Staff Training')
test_grow = Transition(label='Test Grow')
data_analytics = Transition(label='Data Analytics')
yield_optimize = Transition(label='Yield Optimize')

# Waste recycling loop: waste_recycle and water_reuse form a loop
# Loop(* (A, B)) means execute A once, then loop B and A repeatedly or exit after A
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, water_reuse])

# Setup phase (System Setup includes Hydroponics Config and Aeroponics Tune in partial order)
# Hydroponics Config and Aeroponics Tune are concurrent after System Setup
setup_partial = StrictPartialOrder(nodes=[system_setup, hydroponics_config, aeroponics_tune])
setup_partial.order.add_edge(system_setup, hydroponics_config)
setup_partial.order.add_edge(system_setup, aeroponics_tune)

# Environmental controls partial order: Lighting Setup, Enviro Control, Sensor Deploy (concurrent)
enviro_partial = StrictPartialOrder(nodes=[lighting_setup, enviro_control, sensor_deploy])
# no order edges: all concurrent

# Full process partial order nodes: 
#   Site Analysis -> Structural Check -> Rack Install -> Setup Partial
#   Setup Partial -> Enviro Partial -> Waste Loop -> Staff Training -> Test Grow -> Data Analytics -> Yield Optimize

# First build partial order up to Rack Install
pre_setup_partial = StrictPartialOrder(
    nodes=[site_analysis, structural_check, rack_install]
)
pre_setup_partial.order.add_edge(site_analysis, structural_check)
pre_setup_partial.order.add_edge(structural_check, rack_install)

# Compose all in strict partial order
root = StrictPartialOrder(nodes=[
    pre_setup_partial,        # partial order for initial activities
    setup_partial,            # system and hydroponics/aeroponics
    enviro_partial,           # environment setup concurrent activities
    waste_loop,               # waste recycle loop
    staff_training,
    test_grow,
    data_analytics,
    yield_optimize,
])

# Define the order edges among these nodes/partials
# pre_setup_partial --> setup_partial
root.order.add_edge(pre_setup_partial, setup_partial)
# setup_partial --> enviro_partial
root.order.add_edge(setup_partial, enviro_partial)
# enviro_partial --> waste_loop
root.order.add_edge(enviro_partial, waste_loop)
# waste_loop --> staff_training
root.order.add_edge(waste_loop, staff_training)
# staff_training --> test_grow
root.order.add_edge(staff_training, test_grow)
# test_grow --> data_analytics
root.order.add_edge(test_grow, data_analytics)
# data_analytics --> yield_optimize
root.order.add_edge(data_analytics, yield_optimize)