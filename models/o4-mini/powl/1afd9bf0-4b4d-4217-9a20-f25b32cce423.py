# Generated from: 1afd9bf0-4b4d-4217-9a20-f25b32cce423.json
# Description: This process outlines the complex integration of urban vertical farming systems into existing city infrastructure. It involves site assessment, modular farm design, environmental control calibration, crop selection based on microclimates, waste recycling setup, IoT sensor deployment for real-time monitoring, energy management, automated nutrient delivery, pest control automation, data analytics for yield optimization, community engagement programs, regulatory compliance verification, supply chain coordination for urban markets, and continuous system maintenance with adaptive improvements. The goal is to maximize sustainable food production within limited urban spaces while ensuring economic viability and ecological balance through innovative technologies and stakeholder collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label="Site Survey")
design_modules    = Transition(label="Design Modules")
calibrate_sensors = Transition(label="Calibrate Sensors")
select_crops      = Transition(label="Select Crops")
setup_recycling   = Transition(label="Setup Recycling")
deploy_iot        = Transition(label="Deploy IoT")
manage_energy     = Transition(label="Manage Energy")
deliver_nutrients = Transition(label="Deliver Nutrients")
automate_pest     = Transition(label="Automate Pest")
analyze_data      = Transition(label="Analyze Data")
engage_community  = Transition(label="Engage Community")
verify_compliance = Transition(label="Verify Compliance")
coordinate_supply = Transition(label="Coordinate Supply")
maintain_systems  = Transition(label="Maintain Systems")
adapt_improvements= Transition(label="Adapt Improvements")

# Loop for continuous maintenance and improvement
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintain_systems, adapt_improvements]
)

# Build the main partial order
root = StrictPartialOrder(
    nodes=[
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
        maintenance_loop
    ]
)

# Define the sequence of dependencies
edges = [
    (site_survey, design_modules),
    (design_modules, calibrate_sensors),
    (calibrate_sensors, select_crops),
    (select_crops, setup_recycling),
    (setup_recycling, deploy_iot),
    (deploy_iot, manage_energy),
    (manage_energy, deliver_nutrients),
    (deliver_nutrients, automate_pest),
    (automate_pest, analyze_data),
    (analyze_data, engage_community),
    (engage_community, verify_compliance),
    (verify_compliance, coordinate_supply),
    (coordinate_supply, maintenance_loop)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)