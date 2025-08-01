# Generated from: a37aa9af-77ae-4e90-87d5-68917812c8da.json
# Description: This process outlines the deployment of a fully automated urban vertical farming system within a dense metropolitan environment. It includes site analysis, modular infrastructure setup, integration of IoT sensors for real-time monitoring, AI-driven crop optimization, automated nutrient delivery, energy consumption balancing using renewable sources, waste recycling, and community engagement programs. The process also involves regulatory compliance checks, data analytics for yield forecasting, adaptive pest control mechanisms, and dynamic market demand adjustments to maximize efficiency and sustainability in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
permit_check     = Transition(label='Permit Check')
modular_build    = Transition(label='Modular Build')
iot_install      = Transition(label='IoT Install')
sensor_sync      = Transition(label='Sensor Sync')
ai_setup         = Transition(label='AI Setup')
crop_plan        = Transition(label='Crop Plan')
nutrient_mix     = Transition(label='Nutrient Mix')
energy_align     = Transition(label='Energy Align')
waste_process    = Transition(label='Waste Process')
pest_monitor     = Transition(label='Pest Monitor')
data_analyze     = Transition(label='Data Analyze')
yield_forecast   = Transition(label='Yield Forecast')
market_adjust    = Transition(label='Market Adjust')
community_engage = Transition(label='Community Engage')
compliance_audit = Transition(label='Compliance Audit')

# Loop for adaptive pest control: monitor, then analyze, repeat until done
pest_cycle = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, data_analyze])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, modular_build, 
    iot_install, sensor_sync, ai_setup, crop_plan, nutrient_mix,
    energy_align, waste_process, pest_cycle,
    yield_forecast, market_adjust, community_engage, compliance_audit
])

# Define the control‐flow dependencies (partial order)
o = root.order
o.add_edge(site_survey,      permit_check)
o.add_edge(permit_check,     modular_build)
o.add_edge(modular_build,    iot_install)
o.add_edge(iot_install,      sensor_sync)
o.add_edge(sensor_sync,      ai_setup)
o.add_edge(sensor_sync,      energy_align)
o.add_edge(ai_setup,         crop_plan)
o.add_edge(crop_plan,        nutrient_mix)
o.add_edge(modular_build,    waste_process)

# All three branches feed into the pest‐control loop
o.add_edge(nutrient_mix,     pest_cycle)
o.add_edge(energy_align,     pest_cycle)
o.add_edge(waste_process,    pest_cycle)

# After the loop, forecast yield and adjust to market/community/regulations
o.add_edge(pest_cycle,       yield_forecast)
o.add_edge(yield_forecast,   market_adjust)
o.add_edge(market_adjust,    community_engage)
o.add_edge(community_engage,  compliance_audit)