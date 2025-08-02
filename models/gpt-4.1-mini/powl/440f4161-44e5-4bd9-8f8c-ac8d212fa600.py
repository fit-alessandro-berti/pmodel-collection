# Generated from: 440f4161-44e5-4bd9-8f8c-ac8d212fa600.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a repurposed commercial building. It includes site analysis for light and structural integrity, advanced environmental control system installation, nutrient recycling design, integration of AI-driven crop monitoring, and community engagement for sustainable sourcing. The process also manages regulatory compliance, energy optimization, waste management, and post-harvest distribution logistics, ensuring a fully operational, efficient, and eco-friendly urban agriculture solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
site_survey = Transition(label='Site Survey')
light_audit = Transition(label='Light Audit')
structural_check = Transition(label='Structural Check')
layout_design = Transition(label='Layout Design')
system_install = Transition(label='System Install')
nutrient_setup = Transition(label='Nutrient Setup')
ai_integration = Transition(label='AI Integration')
sensor_calibration = Transition(label='Sensor Calibration')
water_recycling = Transition(label='Water Recycling')
energy_mapping = Transition(label='Energy Mapping')
waste_planning = Transition(label='Waste Planning')
compliance_review = Transition(label='Compliance Review')
crop_scheduling = Transition(label='Crop Scheduling')
staff_training = Transition(label='Staff Training')
launch_testing = Transition(label='Launch Testing')
community_outreach = Transition(label='Community Outreach')
harvest_plan = Transition(label='Harvest Plan')
distribution_setup = Transition(label='Distribution Setup')

# Step 1: Site Survey splits into Light Audit and Structural Check in parallel,
# both needed before Layout Design
step1 = StrictPartialOrder(
    nodes=[site_survey, light_audit, structural_check, layout_design]
)
step1.order.add_edge(site_survey, light_audit)
step1.order.add_edge(site_survey, structural_check)
step1.order.add_edge(light_audit, layout_design)
step1.order.add_edge(structural_check, layout_design)

# Step 2: Layout Design followed by System Install, then Nutrient Setup
step2 = StrictPartialOrder(
    nodes=[layout_design, system_install, nutrient_setup]
)
step2.order.add_edge(layout_design, system_install)
step2.order.add_edge(system_install, nutrient_setup)

# Step 3: AI Integration and Sensor Calibration in parallel after Nutrient Setup
# both before Water Recycling
step3 = StrictPartialOrder(
    nodes=[nutrient_setup, ai_integration, sensor_calibration, water_recycling]
)
step3.order.add_edge(nutrient_setup, ai_integration)
step3.order.add_edge(nutrient_setup, sensor_calibration)
step3.order.add_edge(ai_integration, water_recycling)
step3.order.add_edge(sensor_calibration, water_recycling)

# Step 4: Energy Mapping and Waste Planning parallel after Water Recycling,
# then Compliance Review
step4 = StrictPartialOrder(
    nodes=[water_recycling, energy_mapping, waste_planning, compliance_review]
)
step4.order.add_edge(water_recycling, energy_mapping)
step4.order.add_edge(water_recycling, waste_planning)
step4.order.add_edge(energy_mapping, compliance_review)
step4.order.add_edge(waste_planning, compliance_review)

# Step 5: Compliance Review leads to Crop Scheduling & Staff Training in parallel,
# both before Launch Testing
step5 = StrictPartialOrder(
    nodes=[compliance_review, crop_scheduling, staff_training, launch_testing]
)
step5.order.add_edge(compliance_review, crop_scheduling)
step5.order.add_edge(compliance_review, staff_training)
step5.order.add_edge(crop_scheduling, launch_testing)
step5.order.add_edge(staff_training, launch_testing)

# Step 6: Launch Testing followed by Community Outreach and Harvest Plan in parallel,
# both before Distribution Setup
step6 = StrictPartialOrder(
    nodes=[launch_testing, community_outreach, harvest_plan, distribution_setup]
)
step6.order.add_edge(launch_testing, community_outreach)
step6.order.add_edge(launch_testing, harvest_plan)
step6.order.add_edge(community_outreach, distribution_setup)
step6.order.add_edge(harvest_plan, distribution_setup)

# Compose overall process partial order of steps 1-6 sequentially
root = StrictPartialOrder(
    nodes=[step1, step2, step3, step4, step5, step6]
)
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)