# Generated from: 9bd60723-0319-4af0-b3f2-f210685f73ee.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes site analysis, structural modifications, environmental system integration, crop selection based on microclimate data, automated irrigation programming, LED spectrum adjustments, pest monitoring through AI, nutrient solution formulation, workforce training on specialized equipment, yield forecasting, compliance auditing with local agricultural regulations, marketing strategy development targeting urban consumers, and continuous sustainability assessments to optimize resource usage and minimize environmental impact over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with their exact names
site_survey = Transition(label='Site Survey')
structural_review = Transition(label='Structural Review')
system_design = Transition(label='System Design')
crop_selection = Transition(label='Crop Selection')
enviro_setup = Transition(label='Enviro Setup')
irrigation_plan = Transition(label='Irrigation Plan')
led_calibration = Transition(label='LED Calibration')
pest_scan = Transition(label='Pest Scan')
nutrient_mix = Transition(label='Nutrient Mix')
staff_training = Transition(label='Staff Training')
yield_forecast = Transition(label='Yield Forecast')
compliance_check = Transition(label='Compliance Check')
marketing_prep = Transition(label='Marketing Prep')
sustainability = Transition(label='Sustainability')
resource_audit = Transition(label='Resource Audit')

# Create the strict partial order of the process
# Logical dependencies from description:
# 1) Site Survey --> Structural Review --> System Design
# 2) System Design splits into two parallel flows:
#    - Environmental setup flow (Enviro Setup --> Irrigation Plan --> LED Calibration --> Pest Scan --> Nutrient Mix)
#    - Crop selection flow (Crop Selection)
# Both environmental setup and crop selection must complete before Staff Training
# Followed by Yield Forecast
# Then Compliance Check
# Then Marketing Prep
# Sustainability and Resource Audit are continuous and can be concurrent to the end phases: 
# We will assume Sustainability and Resource Audit run concurrently with the last three and also after Staff Training.

# Nodes
nodes = [
    site_survey,
    structural_review,
    system_design,
    enviro_setup,
    irrigation_plan,
    led_calibration,
    pest_scan,
    nutrient_mix,
    crop_selection,
    staff_training,
    yield_forecast,
    compliance_check,
    marketing_prep,
    sustainability,
    resource_audit
]

root = StrictPartialOrder(nodes=nodes)

o = root.order
# Sequential dependencies
o.add_edge(site_survey, structural_review)
o.add_edge(structural_review, system_design)

# After system design:
# enviro_setup and crop_selection can start concurrently
o.add_edge(system_design, enviro_setup)
o.add_edge(system_design, crop_selection)

# Enviro setup chain
o.add_edge(enviro_setup, irrigation_plan)
o.add_edge(irrigation_plan, led_calibration)
o.add_edge(led_calibration, pest_scan)
o.add_edge(pest_scan, nutrient_mix)

# Both nutrient_mix and crop_selection must finish before staff_training
o.add_edge(nutrient_mix, staff_training)
o.add_edge(crop_selection, staff_training)

# After staff_training:
o.add_edge(staff_training, yield_forecast)
o.add_edge(yield_forecast, compliance_check)
o.add_edge(compliance_check, marketing_prep)

# Sustainability and resource audit start after staff_training, concurrent with yield_forecast and later
o.add_edge(staff_training, sustainability)
o.add_edge(staff_training, resource_audit)

# No order between sustainability and resource audit (concurrent)

# As sustainability and resource audit are continuous, no edges going out from them

# This models the major dependencies and concurrency as described.