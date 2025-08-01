# Generated from: a0284ca4-0ef2-4ded-87b4-9c51a0a55a45.json
# Description: This process outlines the complex setup and operationalization of an urban vertical farming facility designed to optimize space in densely populated areas. It involves site assessment, modular rack installation, climate system calibration, nutrient solution formulation, seed selection, automated planting, growth monitoring via IoT sensors, pest management with integrated biological controls, data analytics for yield forecasting, energy consumption optimization, waste recycling integration, staff training on advanced hydroponics, regulatory compliance checks, and market channel development for direct consumer sales. Each step ensures sustainability, efficiency, and scalability while adapting to urban constraints and fluctuating environmental conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
rack_install    = Transition(label='Rack Install')
climate_setup   = Transition(label='Climate Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_select     = Transition(label='Seed Select')
auto_plant      = Transition(label='Auto Plant')
sensor_deploy   = Transition(label='Sensor Deploy')
pest_control    = Transition(label='Pest Control')
yield_forecast  = Transition(label='Yield Forecast')
energy_audit    = Transition(label='Energy Audit')
waste_cycle     = Transition(label='Waste Cycle')
staff_train     = Transition(label='Staff Train')
compliance_check= Transition(label='Compliance Check')
market_setup    = Transition(label='Market Setup')
data_review     = Transition(label='Data Review')

# Sequence them in a strict partial order
sequence = [
    site_survey,
    rack_install,
    climate_setup,
    nutrient_mix,
    seed_select,
    auto_plant,
    sensor_deploy,
    pest_control,
    yield_forecast,
    energy_audit,
    waste_cycle,
    staff_train,
    compliance_check,
    market_setup,
    data_review
]

root = StrictPartialOrder(nodes=sequence)
# Add dependencies so each step follows its predecessor
for prev, nxt in zip(sequence, sequence[1:]):
    root.order.add_edge(prev, nxt)