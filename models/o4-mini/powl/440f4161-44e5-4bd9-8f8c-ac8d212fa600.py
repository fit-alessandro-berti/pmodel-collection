# Generated from: 440f4161-44e5-4bd9-8f8c-ac8d212fa600.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a repurposed commercial building. It includes site analysis for light and structural integrity, advanced environmental control system installation, nutrient recycling design, integration of AI-driven crop monitoring, and community engagement for sustainable sourcing. The process also manages regulatory compliance, energy optimization, waste management, and post-harvest distribution logistics, ensuring a fully operational, efficient, and eco-friendly urban agriculture solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey        = Transition(label='Site Survey')
light_audit        = Transition(label='Light Audit')
structural_check   = Transition(label='Structural Check')
layout_design      = Transition(label='Layout Design')
system_install     = Transition(label='System Install')
nutrient_setup     = Transition(label='Nutrient Setup')
ai_integration     = Transition(label='AI Integration')
sensor_calibration = Transition(label='Sensor Calibration')
water_recycling    = Transition(label='Water Recycling')
energy_mapping     = Transition(label='Energy Mapping')
waste_planning     = Transition(label='Waste Planning')
compliance_review  = Transition(label='Compliance Review')
crop_scheduling    = Transition(label='Crop Scheduling')
staff_training     = Transition(label='Staff Training')
launch_testing     = Transition(label='Launch Testing')
community_outreach = Transition(label='Community Outreach')
harvest_plan       = Transition(label='Harvest Plan')
distribution_setup = Transition(label='Distribution Setup')

# Loop for iterative AI integration and sensor calibration
env_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ai_integration, sensor_calibration]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, light_audit, structural_check,
    layout_design, system_install, nutrient_setup,
    env_loop,
    water_recycling, energy_mapping,
    waste_planning, compliance_review,
    crop_scheduling, staff_training, launch_testing,
    community_outreach, harvest_plan, distribution_setup
])

# Define ordering relations
root.order.add_edge(site_survey, light_audit)
root.order.add_edge(site_survey, structural_check)

root.order.add_edge(light_audit, layout_design)
root.order.add_edge(structural_check, layout_design)

root.order.add_edge(layout_design, system_install)
root.order.add_edge(system_install, nutrient_setup)
root.order.add_edge(nutrient_setup, env_loop)

# After the loop, proceed to resource planning
root.order.add_edge(env_loop, water_recycling)
root.order.add_edge(env_loop, energy_mapping)

# Waste planning depends on water recycling
root.order.add_edge(water_recycling, waste_planning)
# Compliance review depends on energy mapping
root.order.add_edge(energy_mapping, compliance_review)

# Both waste planning and compliance must finish before scheduling
root.order.add_edge(waste_planning, crop_scheduling)
root.order.add_edge(compliance_review, crop_scheduling)

# Final rollout steps
root.order.add_edge(crop_scheduling, staff_training)
root.order.add_edge(staff_training, launch_testing)
root.order.add_edge(launch_testing, community_outreach)
root.order.add_edge(community_outreach, harvest_plan)
root.order.add_edge(harvest_plan, distribution_setup)