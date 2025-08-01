# Generated from: a37aa9af-77ae-4e90-87d5-68917812c8da.json
# Description: This process outlines the deployment of a fully automated urban vertical farming system within a dense metropolitan environment. It includes site analysis, modular infrastructure setup, integration of IoT sensors for real-time monitoring, AI-driven crop optimization, automated nutrient delivery, energy consumption balancing using renewable sources, waste recycling, and community engagement programs. The process also involves regulatory compliance checks, data analytics for yield forecasting, adaptive pest control mechanisms, and dynamic market demand adjustments to maximize efficiency and sustainability in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
permit_check = Transition(label='Permit Check')
modular_build = Transition(label='Modular Build')
iot_install = Transition(label='IoT Install')
sensor_sync = Transition(label='Sensor Sync')
ai_setup = Transition(label='AI Setup')
crop_plan = Transition(label='Crop Plan')
nutrient_mix = Transition(label='Nutrient Mix')
energy_align = Transition(label='Energy Align')
waste_process = Transition(label='Waste Process')
pest_monitor = Transition(label='Pest Monitor')
data_analyze = Transition(label='Data Analyze')
yield_forecast = Transition(label='Yield Forecast')
market_adjust = Transition(label='Market Adjust')
community_engage = Transition(label='Community Engage')
compliance_audit = Transition(label='Compliance Audit')

# This is a complex process. We assume a partial order with some concurrency and control flow structure.

# Logical process ordering inferred from description and flow:
# Site Survey -> Permit Check -> Modular Build -> (IoT Install and Compliance Audit are concurrent)
# IoT Install -> Sensor Sync -> AI Setup -> Crop Plan -> Nutrient Mix -> Energy Align -> Waste Process -> Pest Monitor -> Data Analyze -> Yield Forecast -> Market Adjust -> Community Engage

# Compliance Audit runs concurrently after Permit Check and before or in parallel with IoT Install etc.

# Create a partial order first for the main chain:
main_chain_nodes = [
    site_survey,
    permit_check,
    modular_build,
    iot_install,
    sensor_sync,
    ai_setup,
    crop_plan,
    nutrient_mix,
    energy_align,
    waste_process,
    pest_monitor,
    data_analyze,
    yield_forecast,
    market_adjust,
    community_engage
]

root = StrictPartialOrder(nodes=main_chain_nodes + [compliance_audit])

# Add edges on main chain (sequential order)
for i in range(len(main_chain_nodes) - 1):
    root.order.add_edge(main_chain_nodes[i], main_chain_nodes[i + 1])

# Permit Check before Compliance Audit
root.order.add_edge(permit_check, compliance_audit)

# Compliance Audit concurrent with IoT Install onwards.
# So edges for synchronization between modular_build -> iot_install AND modular_build -> compliance_audit
root.order.add_edge(modular_build, iot_install)
root.order.add_edge(modular_build, compliance_audit)

# Note: IoT Install and Compliance Audit are concurrent: no edge between them.

# That models concurrency between IoT Install path and Compliance Audit

# Final root is the partial order as constructed.