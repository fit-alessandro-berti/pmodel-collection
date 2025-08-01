# Generated from: 9bd60723-0319-4af0-b3f2-f210685f73ee.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes site analysis, structural modifications, environmental system integration, crop selection based on microclimate data, automated irrigation programming, LED spectrum adjustments, pest monitoring through AI, nutrient solution formulation, workforce training on specialized equipment, yield forecasting, compliance auditing with local agricultural regulations, marketing strategy development targeting urban consumers, and continuous sustainability assessments to optimize resource usage and minimize environmental impact over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey      = Transition(label='Site Survey')
structural_rev   = Transition(label='Structural Review')
system_design    = Transition(label='System Design')
crop_selection   = Transition(label='Crop Selection')
enviro_setup     = Transition(label='Enviro Setup')
irrigation_plan  = Transition(label='Irrigation Plan')
led_calibration  = Transition(label='LED Calibration')
pest_scan        = Transition(label='Pest Scan')
nutrient_mix     = Transition(label='Nutrient Mix')
staff_training   = Transition(label='Staff Training')
yield_forecast   = Transition(label='Yield Forecast')
compliance_check = Transition(label='Compliance Check')
marketing_prep   = Transition(label='Marketing Prep')
sustainability   = Transition(label='Sustainability')
resource_audit   = Transition(label='Resource Audit')

# Build a linear partial order (sequential execution of all steps)
nodes = [
    site_survey,
    structural_rev,
    system_design,
    crop_selection,
    enviro_setup,
    irrigation_plan,
    led_calibration,
    pest_scan,
    nutrient_mix,
    staff_training,
    yield_forecast,
    compliance_check,
    marketing_prep,
    sustainability,
    resource_audit
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to enforce the sequence
for prev, nxt in zip(nodes, nodes[1:]):
    root.order.add_edge(prev, nxt)