# Generated from: f5832b03-40af-4433-9245-7972f57881aa.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farming system within a repurposed warehouse. It integrates architectural planning, environmental control calibration, crop selection based on microclimate data, automated nutrient delivery setup, waste recycling mechanisms, and real-time growth monitoring. The process demands coordination across construction, agronomy, IoT integration, and sustainability compliance teams to optimize yield while minimizing energy and water consumption in an urban environment. Stakeholder engagement includes local authorities, technology vendors, and community groups to ensure regulatory adherence and social acceptance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
legal_review     = Transition(label='Legal Review')
stakeholder_meet = Transition(label='Stakeholder Meet')
tech_sourcing    = Transition(label='Tech Sourcing')
structural_build = Transition(label='Structural Build')
climate_setup    = Transition(label='Climate Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy    = Transition(label='Sensor Deploy')
waste_system     = Transition(label='Waste System')
crop_select      = Transition(label='Crop Select')
nutrient_prep    = Transition(label='Nutrient Prep')
automation_config = Transition(label='Automation Config')
trial_growth     = Transition(label='Trial Growth')
data_analysis    = Transition(label='Data Analysis')
quality_audit    = Transition(label='Quality Audit')
compliance_check = Transition(label='Compliance Check')

# Build the loop body: Data Analysis → Quality Audit
body_loop = StrictPartialOrder(nodes=[data_analysis, quality_audit])
body_loop.order.add_edge(data_analysis, quality_audit)

# Construct the loop: Trial Growth → (Data Analysis → Quality Audit) → Trial Growth …
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_growth, body_loop]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, legal_review, stakeholder_meet,
    tech_sourcing, structural_build, climate_setup,
    irrigation_install, sensor_deploy, waste_system,
    crop_select, nutrient_prep, automation_config,
    growth_loop, compliance_check
])

# Define the control-flow dependencies
o = root.order
o.add_edge(site_survey,    design_layout)
o.add_edge(design_layout,  legal_review)
o.add_edge(legal_review,   stakeholder_meet)
o.add_edge(stakeholder_meet, tech_sourcing)
o.add_edge(tech_sourcing,  structural_build)
o.add_edge(structural_build, climate_setup)
o.add_edge(climate_setup,  irrigation_install)
o.add_edge(climate_setup,  sensor_deploy)
o.add_edge(climate_setup,  waste_system)
o.add_edge(sensor_deploy,  crop_select)
o.add_edge(crop_select,    nutrient_prep)
o.add_edge(irrigation_install, automation_config)
o.add_edge(nutrient_prep,  automation_config)
o.add_edge(automation_config, growth_loop)
o.add_edge(growth_loop,    compliance_check)