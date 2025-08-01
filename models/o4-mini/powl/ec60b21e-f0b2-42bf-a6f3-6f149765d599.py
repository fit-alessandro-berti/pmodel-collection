# Generated from: ec60b21e-f0b2-42bf-a6f3-6f149765d599.json
# Description: This process outlines the comprehensive steps required to establish a vertical farming system within an urban environment. It involves site analysis, modular design, environmental control calibration, nutrient solution preparation, seed selection, crop scheduling, automated monitoring, pest management, data analytics integration, and supply chain coordination. The process ensures optimized plant growth through controlled lighting, humidity, and temperature, while incorporating sustainable resource management and waste recycling. Stakeholder engagement and regulatory compliance are integrated to meet urban agricultural standards and community expectations, aiming for high yield and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
modular_design   = Transition(label='Modular Design')
system_build     = Transition(label='System Build')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
env_control      = Transition(label='Env Control')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
planting_setup   = Transition(label='Planting Setup')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
water_cycle      = Transition(label='Water Cycle')
data_capture     = Transition(label='Data Capture')
yield_forecast   = Transition(label='Yield Forecast')
waste_reuse      = Transition(label='Waste Reuse')
supply_sync      = Transition(label='Supply Sync')

# Initial calibration & preparation: Env Control -> Nutrient Mix -> Seed Selection
initial_preparation = StrictPartialOrder(nodes=[env_control, nutrient_mix, seed_selection])
initial_preparation.order.add_edge(env_control, nutrient_mix)
initial_preparation.order.add_edge(nutrient_mix, seed_selection)

# Production cycle body:
# Planting Setup -> {Growth Monitor, Pest Control, Water Cycle, Data Capture} -> Yield Forecast -> Waste Reuse
production_body = StrictPartialOrder(
    nodes=[planting_setup, growth_monitor, pest_control, water_cycle, data_capture, yield_forecast, waste_reuse]
)
production_body.order.add_edge(planting_setup, growth_monitor)
production_body.order.add_edge(planting_setup, pest_control)
production_body.order.add_edge(planting_setup, water_cycle)
production_body.order.add_edge(planting_setup, data_capture)
production_body.order.add_edge(growth_monitor, yield_forecast)
production_body.order.add_edge(pest_control, yield_forecast)
production_body.order.add_edge(water_cycle, yield_forecast)
production_body.order.add_edge(data_capture, yield_forecast)
production_body.order.add_edge(yield_forecast, waste_reuse)

# Loop: do initial_preparation once, then repeat production_body any number of times
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_preparation, production_body])

# Main process partial order
root = StrictPartialOrder(
    nodes=[site_survey, modular_design, system_build, stakeholder_meet,
           compliance_check, production_loop, supply_sync]
)
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)
root.order.add_edge(compliance_check, production_loop)
root.order.add_edge(production_loop, supply_sync)