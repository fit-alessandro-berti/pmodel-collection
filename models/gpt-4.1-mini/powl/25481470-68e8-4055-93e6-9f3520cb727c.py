# Generated from: 25481470-68e8-4055-93e6-9f3520cb727c.json
# Description: This process outlines the complex and multi-disciplinary steps involved in establishing an urban rooftop farm. It includes site analysis, environmental impact assessment, structural integrity checks, soil and water testing, sourcing sustainable materials, installation of hydroponic systems, seed selection, pest management planning, community engagement, and continuous monitoring for crop optimization. The process demands coordination between architects, agronomists, environmental scientists, and local authorities to ensure compliance with regulations and maximize productivity while maintaining urban ecological balance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Create transitions for each activity
site_survey = Transition(label='Site Survey')
impact_review = Transition(label='Impact Review')
structure_check = Transition(label='Structure Check')
soil_testing = Transition(label='Soil Testing')
water_analysis = Transition(label='Water Analysis')
material_sourcing = Transition(label='Material Sourcing')
system_install = Transition(label='System Install')
seed_selection = Transition(label='Seed Selection')
pest_planning = Transition(label='Pest Planning')
community_meet = Transition(label='Community Meet')
regulation_review = Transition(label='Regulation Review')
crop_planting = Transition(label='Crop Planting')
irrigation_setup = Transition(label='Irrigation Setup')
growth_monitor = Transition(label='Growth Monitor')
yield_assess = Transition(label='Yield Assess')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')

# Environmental & structural assessments partial order:
# Site Survey --> Impact Review --> Structure Check
# Site Survey --> Impact Review --> Soil Testing
# Site Survey --> Impact Review --> Water Analysis
env_struct = StrictPartialOrder(
    nodes=[site_survey, impact_review, structure_check, soil_testing, water_analysis]
)
env_struct.order.add_edge(site_survey, impact_review)
env_struct.order.add_edge(impact_review, structure_check)
env_struct.order.add_edge(impact_review, soil_testing)
env_struct.order.add_edge(impact_review, water_analysis)

# Materials sourcing and system installation sequence:
# Material Sourcing --> System Install
mat_sys = StrictPartialOrder(
    nodes=[material_sourcing, system_install]
)
mat_sys.order.add_edge(material_sourcing, system_install)

# Crop planning and planting phase:
# Seed Selection --> Pest Planning --> Crop Planting
crop_plan = StrictPartialOrder(
    nodes=[seed_selection, pest_planning, crop_planting]
)
crop_plan.order.add_edge(seed_selection, pest_planning)
crop_plan.order.add_edge(pest_planning, crop_planting)

# Setup irrigation after planting:
# Crop Planting --> Irrigation Setup
irrigation_phase = StrictPartialOrder(
    nodes=[crop_planting, irrigation_setup]
)
irrigation_phase.order.add_edge(crop_planting, irrigation_setup)

# Monitoring phase loop: Growth Monitor --> Yield Assess --> Waste Manage --> Energy Audit --> loop back to Growth Monitor
# This is a loop of continuous monitoring and management.
monitoring_loop_body = StrictPartialOrder(
    nodes=[yield_assess, waste_manage, energy_audit]
)
monitoring_loop_body.order.add_edge(yield_assess, waste_manage)
monitoring_loop_body.order.add_edge(waste_manage, energy_audit)

monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        growth_monitor,
        monitoring_loop_body
    ]
)

# Community engagement and regulation:
# Community Meet and Regulation Review can happen concurrently after initial Site Survey
community_regulation = StrictPartialOrder(
    nodes=[community_meet, regulation_review]
)
# no order edges = concurrent

# Now compose the overall process partial order:

# Order:
# 1) env_struct partial order done first
# 2) community_regulation and mat_sys occur concurrently after env_struct
# 3) after mat_sys and community_regulation complete, crop_plan starts
# 4) after crop_plan irrigation_phase starts
# 5) after irrigation_phase monitoring_loop starts

root = StrictPartialOrder(
    nodes=[
        env_struct,
        community_regulation,
        mat_sys,
        crop_plan,
        irrigation_phase,
        monitoring_loop
    ]
)

# Add order edges between sub-processes
root.order.add_edge(env_struct, community_regulation)
root.order.add_edge(env_struct, mat_sys)
root.order.add_edge(community_regulation, crop_plan)
root.order.add_edge(mat_sys, crop_plan)
root.order.add_edge(crop_plan, irrigation_phase)
root.order.add_edge(irrigation_phase, monitoring_loop)