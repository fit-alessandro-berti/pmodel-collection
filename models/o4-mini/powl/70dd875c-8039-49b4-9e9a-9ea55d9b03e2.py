# Generated from: 70dd875c-8039-49b4-9e9a-9ea55d9b03e2.json
# Description: This complex process involves the design, implementation, and ongoing optimization of urban farming systems tailored to specific city environments. It starts with site analysis to assess sunlight, soil quality, and local climate, followed by modular farm design incorporating vertical farming, hydroponics, and aquaponics tailored to available spaces. The process continues with sourcing sustainable materials and specialized equipment, installation of automated irrigation and nutrient delivery systems, and integration of IoT sensors for real-time monitoring of crop health and environmental conditions. Subsequent activities include staff training on unique urban farming techniques, ongoing maintenance and pest management using eco-friendly methods, data analysis for yield optimization, and community engagement programs to promote urban agriculture awareness. The final stages involve scaling the model to multiple sites while maintaining quality control and adapting the design based on evolving urban policies and technological advancements, ensuring a sustainable and profitable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define all atomic activities
site_survey        = Transition(label='Site Survey')
climate_study      = Transition(label='Climate Study')
soil_testing       = Transition(label='Soil Testing')
design_layout      = Transition(label='Design Layout')
material_sourcing  = Transition(label='Material Sourcing')
equipment_setup    = Transition(label='Equipment Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy      = Transition(label='Sensor Deploy')
system_config      = Transition(label='System Config')
staff_training     = Transition(label='Staff Training')
crop_planting      = Transition(label='Crop Planting')
pest_control       = Transition(label='Pest Control')
data_capture       = Transition(label='Data Capture')
yield_review       = Transition(label='Yield Review')
community_outreach = Transition(label='Community Outreach')
scale_expansion    = Transition(label='Scale Expansion')
policy_adapt       = Transition(label='Policy Adapt')

# a silent transition to use if needed in more complex variants
skip = SilentTransition()

# 1) Site‐analysis phase: the three tasks can happen in parallel
site_analysis = StrictPartialOrder(
    nodes=[site_survey, climate_study, soil_testing]
)
# no edges → they are concurrent

# 2) Ongoing maintenance/optimization loop:
#    A = pest_control and data_capture in parallel
A = StrictPartialOrder(
    nodes=[pest_control, data_capture]
)
#    B = yield_review and community_outreach in parallel
B = StrictPartialOrder(
    nodes=[yield_review, community_outreach]
)
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, B]
)

# 3) Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_analysis,
        design_layout,
        material_sourcing,
        equipment_setup,
        irrigation_install,
        sensor_deploy,
        system_config,
        staff_training,
        crop_planting,
        maintenance_loop,
        scale_expansion,
        policy_adapt
    ]
)

# 4) Define the sequential dependencies
root.order.add_edge(site_analysis,      design_layout)
root.order.add_edge(design_layout,      material_sourcing)
root.order.add_edge(material_sourcing,  equipment_setup)
root.order.add_edge(equipment_setup,    irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy,      system_config)
root.order.add_edge(system_config,      staff_training)
root.order.add_edge(staff_training,     crop_planting)
root.order.add_edge(crop_planting,      maintenance_loop)
root.order.add_edge(maintenance_loop,   scale_expansion)
root.order.add_edge(scale_expansion,    policy_adapt)