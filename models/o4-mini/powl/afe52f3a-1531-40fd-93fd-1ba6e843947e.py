# Generated from: afe52f3a-1531-40fd-93fd-1ba6e843947e.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure, combining agricultural technology, supply chain logistics, and municipal regulations to produce fresh, sustainable crops in city environments. It involves site assessment, modular system installation, climate control calibration, automated nutrient delivery, crop monitoring using AI, waste recycling, energy optimization, community engagement, and real-time yield forecasting. The process ensures minimal environmental impact while maximizing productivity and urban space utilization, requiring collaboration between agronomists, engineers, city planners, and local stakeholders to create a resilient and scalable urban farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic transitions
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
permits_check   = Transition(label='Permits Check')
module_install  = Transition(label='Module Install')
climate_setup   = Transition(label='Climate Setup')
nutrient_flow   = Transition(label='Nutrient Flow')
ai_monitoring   = Transition(label='AI Monitoring')
data_sync       = Transition(label='Data Sync')
pest_control    = Transition(label='Pest Control')
waste_cycle     = Transition(label='Waste Cycle')
energy_audit    = Transition(label='Energy Audit')
community_meet  = Transition(label='Community Meet')
logistics_plan  = Transition(label='Logistics Plan')
yield_forecast  = Transition(label='Yield Forecast')
harvest_pack    = Transition(label='Harvest Pack')
skip            = SilentTransition()

# Loop for continuous monitoring and data synchronization
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ai_monitoring, data_sync]
)

# Choice for pest control (either do it or skip)
pest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[pest_control, skip]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permits_check,
    module_install,
    climate_setup,
    nutrient_flow,
    loop_node,
    pest_choice,
    waste_cycle,
    energy_audit,
    community_meet,
    logistics_plan,
    yield_forecast,
    harvest_pack
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey,   design_layout)
root.order.add_edge(site_survey,   permits_check)
root.order.add_edge(design_layout, module_install)
root.order.add_edge(permits_check, module_install)
root.order.add_edge(module_install, climate_setup)
root.order.add_edge(climate_setup,  nutrient_flow)
root.order.add_edge(nutrient_flow,  loop_node)
root.order.add_edge(loop_node,      pest_choice)
root.order.add_edge(pest_choice,    waste_cycle)
root.order.add_edge(pest_choice,    energy_audit)
root.order.add_edge(waste_cycle,    community_meet)
root.order.add_edge(energy_audit,   community_meet)
root.order.add_edge(waste_cycle,    logistics_plan)
root.order.add_edge(energy_audit,   logistics_plan)
root.order.add_edge(community_meet, yield_forecast)
root.order.add_edge(logistics_plan, yield_forecast)
root.order.add_edge(yield_forecast, harvest_pack)