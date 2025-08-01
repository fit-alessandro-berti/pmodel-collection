# Generated from: 1afd9bf0-4b4d-4217-9a20-f25b32cce423.json
# Description: This process outlines the complex integration of urban vertical farming systems into existing city infrastructure. It involves site assessment, modular farm design, environmental control calibration, crop selection based on microclimates, waste recycling setup, IoT sensor deployment for real-time monitoring, energy management, automated nutrient delivery, pest control automation, data analytics for yield optimization, community engagement programs, regulatory compliance verification, supply chain coordination for urban markets, and continuous system maintenance with adaptive improvements. The goal is to maximize sustainable food production within limited urban spaces while ensuring economic viability and ecological balance through innovative technologies and stakeholder collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
setup_recycling = Transition(label='Setup Recycling')
deploy_iot = Transition(label='Deploy IoT')
manage_energy = Transition(label='Manage Energy')
deliver_nutrients = Transition(label='Deliver Nutrients')
automate_pest = Transition(label='Automate Pest')
analyze_data = Transition(label='Analyze Data')
engage_community = Transition(label='Engage Community')
verify_compliance = Transition(label='Verify Compliance')
coordinate_supply = Transition(label='Coordinate Supply')
maintain_systems = Transition(label='Maintain Systems')
adapt_improvements = Transition(label='Adapt Improvements')

# Create a StrictPartialOrder to reflect natural flow and some concurrency
# Logical ordering based on the description:

# Site Survey first
# Design Modules after Site Survey
# Calibrate Sensors after Design Modules
# Select Crops after Calibrate Sensors
# Setup Recycling after Site Survey (can start after survey, parallel with design modules)
# Deploy IoT after Calibrate Sensors
# Manage Energy after Deploy IoT
# Deliver Nutrients after Manage Energy
# Automate Pest after Deliver Nutrients
# Analyze Data after Automate Pest
# Engage Community in parallel (can start after Setup Recycling)
# Verify Compliance after Analyze Data
# Coordinate Supply after Verify Compliance
# Maintain Systems after Coordinate Supply
# Adapt Improvements after Maintain Systems

root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    calibrate_sensors,
    select_crops,
    setup_recycling,
    deploy_iot,
    manage_energy,
    deliver_nutrients,
    automate_pest,
    analyze_data,
    engage_community,
    verify_compliance,
    coordinate_supply,
    maintain_systems,
    adapt_improvements
])

# Define order edges
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, calibrate_sensors)
root.order.add_edge(calibrate_sensors, select_crops)

root.order.add_edge(site_survey, setup_recycling)  # setup recycling concurrent with design modules
root.order.add_edge(calibrate_sensors, deploy_iot)
root.order.add_edge(deploy_iot, manage_energy)
root.order.add_edge(manage_energy, deliver_nutrients)
root.order.add_edge(deliver_nutrients, automate_pest)
root.order.add_edge(automate_pest, analyze_data)

root.order.add_edge(setup_recycling, engage_community)  # community engagement after recycling setup

root.order.add_edge(analyze_data, verify_compliance)
root.order.add_edge(verify_compliance, coordinate_supply)
root.order.add_edge(coordinate_supply, maintain_systems)
root.order.add_edge(maintain_systems, adapt_improvements)