# Generated from: fa09b7c6-8b90-46bd-9840-9af1cf8c882e.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farming system in a repurposed warehouse. It involves site analysis, environmental control calibration, hydroponic system installation, crop selection based on market trends, nutrient solution management, integration of IoT sensors for real-time monitoring, energy optimization, pest management using bio-controls, staff training for specialized urban agriculture techniques, marketing strategy development targeting local consumers, regulatory compliance with urban zoning laws, logistics planning for fresh produce distribution, and continuous data-driven yield optimization to ensure sustainability and profitability in an unconventional farming environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_lighting = Transition(label='Install Lighting')
setup_hydroponics = Transition(label='Setup Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
mix_nutrients = Transition(label='Mix Nutrients')
deploy_iot = Transition(label='Deploy IoT')
energy_audit = Transition(label='Energy Audit')
train_staff = Transition(label='Train Staff')
pest_control = Transition(label='Pest Control')
legal_review = Transition(label='Legal Review')
market_analysis = Transition(label='Market Analysis')
plan_logistics = Transition(label='Plan Logistics')
yield_review = Transition(label='Yield Review')

# Model the process as a partial order with causal relations

# Initial: Site Survey must be done first
# Then design and setup-related activities can be done concurrently where possible
# Logical order assumptions based on dependencies:

# After Site Survey:
# Design Layout, Setup Hydroponics, Install Lighting, Calibrate Sensors depend on survey

# Calibration depends on Install Lighting and Setup Hydroponics
# Select Crops and Mix Nutrients can happen after Setup Hydroponics
# Deploy IoT after Calibrate Sensors
# Energy Audit after Deploy IoT
# Pest Control and Train Staff can happen in parallel after Setup Hydroponics
# Legal Review and Market Analysis in parallel after Train Staff and Pest Control
# Plan Logistics after Market Analysis and Legal Review
# Yield Review last, after Plan Logistics and Energy Audit (data-driven optimization after logistics and energy)

# Create nodes list
nodes = [
    site_survey,
    design_layout,
    install_lighting,
    setup_hydroponics,
    calibrate_sensors,
    select_crops,
    mix_nutrients,
    deploy_iot,
    energy_audit,
    train_staff,
    pest_control,
    legal_review,
    market_analysis,
    plan_logistics,
    yield_review,
]

root = StrictPartialOrder(nodes=nodes)

order = root.order
# Site Survey --> Design Layout, Install Lighting, Setup Hydroponics
order.add_edge(site_survey, design_layout)
order.add_edge(site_survey, install_lighting)
order.add_edge(site_survey, setup_hydroponics)

# Install Lighting --> Calibrate Sensors
order.add_edge(install_lighting, calibrate_sensors)
# Setup Hydroponics --> Calibrate Sensors
order.add_edge(setup_hydroponics, calibrate_sensors)

# Setup Hydroponics --> Select Crops, Mix Nutrients, Pest Control, Train Staff
order.add_edge(setup_hydroponics, select_crops)
order.add_edge(setup_hydroponics, mix_nutrients)
order.add_edge(setup_hydroponics, pest_control)
order.add_edge(setup_hydroponics, train_staff)

# Calibrate Sensors --> Deploy IoT
order.add_edge(calibrate_sensors, deploy_iot)

# Deploy IoT --> Energy Audit
order.add_edge(deploy_iot, energy_audit)

# Pest Control --> Legal Review
order.add_edge(pest_control, legal_review)

# Train Staff --> Market Analysis
order.add_edge(train_staff, market_analysis)

# Legal Review, Market Analysis --> Plan Logistics
order.add_edge(legal_review, plan_logistics)
order.add_edge(market_analysis, plan_logistics)

# Plan Logistics --> Yield Review
order.add_edge(plan_logistics, yield_review)

# Energy Audit --> Yield Review
order.add_edge(energy_audit, yield_review)