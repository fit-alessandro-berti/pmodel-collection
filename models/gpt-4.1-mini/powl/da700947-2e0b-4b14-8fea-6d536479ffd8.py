# Generated from: da700947-2e0b-4b14-8fea-6d536479ffd8.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It encompasses site evaluation, environmental control system design, modular planting setup, nutrient delivery automation, pest monitoring with AI integration, energy optimization through renewable sources, and yield forecasting using data analytics. The process also includes community engagement programs, regulatory compliance checks, staff training on specialized equipment, and continuous improvement loops based on sensor feedback. This atypical yet realistic sequence enables sustainable, high-density crop production in urban environments, reducing transportation emissions and supporting local food systems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Climate_Design = Transition(label='Climate Design')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
Pest_Scan = Transition(label='Pest Scan')
Energy_Audit = Transition(label='Energy Audit')
Renewable_Sync = Transition(label='Renewable Sync')
Data_Modeling = Transition(label='Data Modeling')
Staff_Briefing = Transition(label='Staff Briefing')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Yield_Review = Transition(label='Yield Review')
Feedback_Loop = Transition(label='Feedback Loop')

# Construct sequential flows as partial orders where appropriate
# Step 1: Site Survey -> Structural Audit (site evaluation)
site_eval = StrictPartialOrder(nodes=[Site_Survey, Structural_Audit])
site_eval.order.add_edge(Site_Survey, Structural_Audit)

# Step 2: Environmental control system design (Climate Design -> Lighting Setup -> Irrigation Plan -> Nutrient Mix)
env_control = StrictPartialOrder(nodes=[Climate_Design, Lighting_Setup, Irrigation_Plan, Nutrient_Mix])
env_control.order.add_edge(Climate_Design, Lighting_Setup)
env_control.order.add_edge(Lighting_Setup, Irrigation_Plan)
env_control.order.add_edge(Irrigation_Plan, Nutrient_Mix)

# Step 3: Pest monitoring with AI integration (Sensor Install -> AI Calibration -> Pest Scan)
pest_monitoring = StrictPartialOrder(nodes=[Sensor_Install, AI_Calibration, Pest_Scan])
pest_monitoring.order.add_edge(Sensor_Install, AI_Calibration)
pest_monitoring.order.add_edge(AI_Calibration, Pest_Scan)

# Step 4: Energy optimization through renewable sources (Energy Audit -> Renewable Sync)
energy_opt = StrictPartialOrder(nodes=[Energy_Audit, Renewable_Sync])
energy_opt.order.add_edge(Energy_Audit, Renewable_Sync)

# Step 5: Yield forecasting using data analytics (Data Modeling)
yield_forecast = Data_Modeling

# Step 6: Community engagement programs & regulatory compliance & staff training
# They can happen concurrently but staff training needs compliance check before it
compliance_then_staff = StrictPartialOrder(nodes=[Compliance_Check, Staff_Briefing])
compliance_then_staff.order.add_edge(Compliance_Check, Staff_Briefing)
community_engagement = Community_Meet

# Step 7: Continuous improvement loops based on sensor feedback
# This is a LOOP on Feedback_Loop followed by yield review
# Per definition: *(A,B) means execute A, then either exit or do B then A again
# We'll treat Yield_Review as A (body), Feedback_Loop as B (loop)
improvement_loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Review, Feedback_Loop])

# Now assemble the main partial order:
# Overall order:
# Site eval -> Env control -> Pest monitoring -> Energy opt -> yield forecasting
# Also compliance & staff briefing after site eval concurrently (community engagement concurrent too)
# Finally improvement loop after yield forecasting

# Put partial orders together, concurrency where no edge
nodes = [
    site_eval,
    env_control,
    pest_monitoring,
    energy_opt,
    yield_forecast,
    compliance_then_staff,
    community_engagement,
    improvement_loop
]

root = StrictPartialOrder(nodes=nodes)

# Define ordering edges:
# site_eval before env_control
root.order.add_edge(site_eval, env_control)
# env_control before pest_monitoring
root.order.add_edge(env_control, pest_monitoring)
# pest_monitoring before energy_opt
root.order.add_edge(pest_monitoring, energy_opt)
# energy_opt before yield_forecast
root.order.add_edge(energy_opt, yield_forecast)

# site_eval before compliance_then_staff and community engagement (they start after site surveying)
root.order.add_edge(site_eval, compliance_then_staff)
root.order.add_edge(site_eval, community_engagement)

# yield_forecast before improvement_loop
root.order.add_edge(yield_forecast, improvement_loop)