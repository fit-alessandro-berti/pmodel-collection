# Generated from: c2675bd4-bf9c-424a-b68e-17ced25d8f0a.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a dense city environment. It involves site analysis, structural assessments, soil and water testing, regulatory compliance checks, installation of modular planters, irrigation system setup, selection of crop varieties suited for rooftop conditions, pest management strategies, community engagement, ongoing maintenance scheduling, harvest planning, and integration with local markets. The process ensures environmental sustainability, optimizes limited space usage, and fosters urban food security while adhering to safety and zoning regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
load_test       = Transition(label='Load Test')
soil_sample     = Transition(label='Soil Sample')
water_check     = Transition(label='Water Check')
permit_review   = Transition(label='Permit Review')
planter_install = Transition(label='Planter Install')
irrigation_setup= Transition(label='Irrigation Setup')
crop_select     = Transition(label='Crop Select')
community_meet  = Transition(label='Community Meet')
maintenance_plan= Transition(label='Maintenance Plan')
pest_control    = Transition(label='Pest Control')
waste_manage    = Transition(label='Waste Manage')
energy_audit    = Transition(label='Energy Audit')
harvest_prep    = Transition(label='Harvest Prep')
market_link     = Transition(label='Market Link')

# Define the maintenance loop body: Pest Control -> Waste Manage -> Energy Audit
maintenance_body = StrictPartialOrder(nodes=[pest_control, waste_manage, energy_audit])
maintenance_body.order.add_edge(pest_control, waste_manage)
maintenance_body.order.add_edge(waste_manage, energy_audit)

# Loop: execute Maintenance Plan, then optionally the maintenance body repeatedly
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance_plan, maintenance_body]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, water_check, permit_review,
    planter_install, irrigation_setup, crop_select, community_meet,
    maintenance_loop, harvest_prep, market_link
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,     load_test)
root.order.add_edge(load_test,       soil_sample)
root.order.add_edge(load_test,       water_check)
root.order.add_edge(soil_sample,     permit_review)
root.order.add_edge(water_check,     permit_review)
root.order.add_edge(permit_review,   planter_install)
root.order.add_edge(planter_install, irrigation_setup)
root.order.add_edge(irrigation_setup,crop_select)
root.order.add_edge(crop_select,     community_meet)
root.order.add_edge(crop_select,     maintenance_loop)
root.order.add_edge(maintenance_loop,harvest_prep)
root.order.add_edge(community_meet,  harvest_prep)
root.order.add_edge(harvest_prep,    market_link)