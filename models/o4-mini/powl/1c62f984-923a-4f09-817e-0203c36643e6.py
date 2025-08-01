# Generated from: 1c62f984-923a-4f09-817e-0203c36643e6.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site assessment, environmental simulation, modular installation, nutrient cycling optimization, and integration of AI-driven crop monitoring. The workflow also covers regulatory compliance, energy management, and community engagement to ensure sustainable and scalable food production in densely populated areas. Each activity is designed to address unique challenges of urban agriculture, such as limited space, resource efficiency, and real-time data analytics for yield maximization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Transitions
site_survey = Transition(label='Site Survey')
struct_test = Transition(label='Structural Test')
reg_review = Transition(label='Regulation Review')
energy_audit = Transition(label='Energy Audit')
light_setup = Transition(label='Light Setup')
climate_ctrl = Transition(label='Climate Control')
sensor_install = Transition(label='Sensor Install')
ai_integration = Transition(label='AI Integration')
water_loop = Transition(label='Water Loop')
nutrient_mix = Transition(label='Nutrient Mix')
waste_cycle = Transition(label='Waste Cycle')
crop_seeding = Transition(label='Crop Seeding')
growth_monitor = Transition(label='Growth Monitor')
pest_check = Transition(label='Pest Check')
community_meet = Transition(label='Community Meet')
yield_report = Transition(label='Yield Report')

# Operators
xor_nutri = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_cycle])
loop_nutri = OperatorPOWL(operator=Operator.LOOP, children=[water_loop, xor_nutri])
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_check])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, struct_test, reg_review, energy_audit,
    light_setup, climate_ctrl, sensor_install, ai_integration,
    xor_nutri, loop_nutri, community_meet,
    crop_seeding, loop_growth, yield_report
])

# Control-flow dependencies
root.order.add_edge(site_survey, struct_test)
root.order.add_edge(struct_test, reg_review)
root.order.add_edge(struct_test, energy_audit)

root.order.add_edge(reg_review, light_setup)
root.order.add_edge(reg_review, climate_ctrl)
root.order.add_edge(energy_audit, light_setup)
root.order.add_edge(energy_audit, climate_ctrl)

root.order.add_edge(light_setup, sensor_install)
root.order.add_edge(climate_ctrl, sensor_install)

root.order.add_edge(sensor_install, ai_integration)
root.order.add_edge(ai_integration, loop_nutri)
root.order.add_edge(ai_integration, community_meet)

root.order.add_edge(loop_nutri, crop_seeding)
root.order.add_edge(community_meet, crop_seeding)

root.order.add_edge(crop_seeding, loop_growth)
root.order.add_edge(loop_growth, yield_report)