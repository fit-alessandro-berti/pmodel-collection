# Generated from: fa09b7c6-8b90-46bd-9840-9af1cf8c882e.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farming system in a repurposed warehouse. It involves site analysis, environmental control calibration, hydroponic system installation, crop selection based on market trends, nutrient solution management, integration of IoT sensors for real-time monitoring, energy optimization, pest management using bio-controls, staff training for specialized urban agriculture techniques, marketing strategy development targeting local consumers, regulatory compliance with urban zoning laws, logistics planning for fresh produce distribution, and continuous data-driven yield optimization to ensure sustainability and profitability in an unconventional farming environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the core activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
install_lighting= Transition(label='Install Lighting')
setup_hydroponics= Transition(label='Setup Hydroponics')
calibrate_sensors= Transition(label='Calibrate Sensors')
select_crops    = Transition(label='Select Crops')
mix_nutrients   = Transition(label='Mix Nutrients')
deploy_iot      = Transition(label='Deploy IoT')
energy_audit    = Transition(label='Energy Audit')
train_staff     = Transition(label='Train Staff')
pest_control    = Transition(label='Pest Control')
legal_review    = Transition(label='Legal Review')
plan_logistics  = Transition(label='Plan Logistics')

# Define the loop‐body activities for continuous optimization
ma_loop = Transition(label='Market Analysis')
yr_loop = Transition(label='Yield Review')
ea_loop = Transition(label='Energy Audit')
pc_loop = Transition(label='Pest Control')

# Build the loop body as a small partial order: Market Analysis -> Yield Review -> Energy Audit -> Pest Control
loop_body = StrictPartialOrder(nodes=[ma_loop, yr_loop, ea_loop, pc_loop])
loop_body.order.add_edge(ma_loop, yr_loop)
loop_body.order.add_edge(yr_loop, ea_loop)
loop_body.order.add_edge(ea_loop, pc_loop)

# A silent transition to act as the "exit" prologue for the loop
skip = SilentTransition()

# Define the LOOP operator: zero or more repetitions of loop_body
loop_operator = OperatorPOWL(operator=Operator.LOOP, children=[skip, loop_body])

# Assemble all nodes for the root partial order, including the loop operator
nodes = [
    site_survey, design_layout, install_lighting, setup_hydroponics,
    calibrate_sensors, select_crops, mix_nutrients, deploy_iot,
    energy_audit, train_staff, pest_control, legal_review,
    plan_logistics, loop_operator
]

# Build the root partial order and add the control‐flow edges
root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(site_survey,     design_layout)
root.order.add_edge(design_layout,   install_lighting)
root.order.add_edge(install_lighting,setup_hydroponics)
root.order.add_edge(setup_hydroponics,calibrate_sensors)
root.order.add_edge(calibrate_sensors,select_crops)
root.order.add_edge(select_crops,    mix_nutrients)
root.order.add_edge(mix_nutrients,   deploy_iot)
root.order.add_edge(deploy_iot,      energy_audit)
root.order.add_edge(energy_audit,    train_staff)
root.order.add_edge(train_staff,     pest_control)
root.order.add_edge(pest_control,    legal_review)
root.order.add_edge(legal_review,    plan_logistics)
# After initial setup and planning, engage in continuous yield optimization
root.order.add_edge(plan_logistics,  loop_operator)