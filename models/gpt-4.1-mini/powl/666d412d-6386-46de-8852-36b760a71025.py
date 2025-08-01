# Generated from: 666d412d-6386-46de-8852-36b760a71025.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming facility within a repurposed industrial building. It includes site analysis, environmental impact assessments, modular system design, selection of crop varieties optimized for vertical growth, installation of automated irrigation and lighting systems, integration of IoT sensors for real-time monitoring, staff recruitment and training focused on hydroponic techniques, implementation of pest control measures using biological agents, establishment of nutrient delivery schedules, continuous data analysis for yield optimization, compliance with local agricultural regulations, marketing strategy development targeting urban consumers, logistics planning for distribution within city limits, and periodic facility maintenance to ensure sustainability and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
system_design = Transition(label='System Design')
crop_selection = Transition(label='Crop Selection')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
sensor_integration = Transition(label='Sensor Integration')
staff_hiring = Transition(label='Staff Hiring')
training_sessions = Transition(label='Training Sessions')
pest_control = Transition(label='Pest Control')
nutrient_plan = Transition(label='Nutrient Plan')
data_analysis = Transition(label='Data Analysis')
regulation_check = Transition(label='Regulation Check')
marketing_plan = Transition(label='Marketing Plan')
logistics_setup = Transition(label='Logistics Setup')
facility_audit = Transition(label='Facility Audit')

# Create a strict partial order of nodes
root = StrictPartialOrder(
    nodes=[
        site_survey,
        impact_study,
        system_design,
        crop_selection,
        irrigation_setup,
        lighting_install,
        sensor_integration,
        staff_hiring,
        training_sessions,
        pest_control,
        nutrient_plan,
        data_analysis,
        regulation_check,
        marketing_plan,
        logistics_setup,
        facility_audit
    ]
)

# Define the order edges based on the described process workflow:
# Site Survey -> Impact Study -> System Design
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, system_design)

# System Design -> Crop Selection -> Irrigation Setup and Lighting Install and Sensor Integration (these 3 concurrent)
root.order.add_edge(system_design, crop_selection)
root.order.add_edge(crop_selection, irrigation_setup)
root.order.add_edge(crop_selection, lighting_install)
root.order.add_edge(crop_selection, sensor_integration)

# Irrigation Setup, Lighting Install, Sensor Integration must finish before Staff Hiring
root.order.add_edge(irrigation_setup, staff_hiring)
root.order.add_edge(lighting_install, staff_hiring)
root.order.add_edge(sensor_integration, staff_hiring)

# Staff Hiring -> Training Sessions
root.order.add_edge(staff_hiring, training_sessions)

# Training Sessions -> Pest Control -> Nutrient Plan -> Data Analysis
root.order.add_edge(training_sessions, pest_control)
root.order.add_edge(pest_control, nutrient_plan)
root.order.add_edge(nutrient_plan, data_analysis)

# Data Analysis -> Regulation Check
root.order.add_edge(data_analysis, regulation_check)

# Regulation Check -> Marketing Plan -> Logistics Setup
root.order.add_edge(regulation_check, marketing_plan)
root.order.add_edge(marketing_plan, logistics_setup)

# Logistics Setup -> Facility Audit
root.order.add_edge(logistics_setup, facility_audit)