# Generated from: a0284ca4-0ef2-4ded-87b4-9c51a0a55a45.json
# Description: This process outlines the complex setup and operationalization of an urban vertical farming facility designed to optimize space in densely populated areas. It involves site assessment, modular rack installation, climate system calibration, nutrient solution formulation, seed selection, automated planting, growth monitoring via IoT sensors, pest management with integrated biological controls, data analytics for yield forecasting, energy consumption optimization, waste recycling integration, staff training on advanced hydroponics, regulatory compliance checks, and market channel development for direct consumer sales. Each step ensures sustainability, efficiency, and scalability while adapting to urban constraints and fluctuating environmental conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Rack_Install = Transition(label='Rack Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Select = Transition(label='Seed Select')
Auto_Plant = Transition(label='Auto Plant')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Waste_Cycle = Transition(label='Waste Cycle')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Market_Setup = Transition(label='Market Setup')
Data_Review = Transition(label='Data Review')

# To reflect some concurrency with partial order:
# Group 1 (setup initial infrastructure): Site Survey -> Rack Install -> Climate Setup
# Group 2 (prepare resources) Nutrient Mix and Seed Select can proceed after Climate Setup
# Auto Plant depends on Nutrient Mix and Seed Select
# Sensor Deploy and Pest Control concurrent after Auto Plant
# Yield Forecast after Sensor Deploy and Pest Control
# Energy Audit and Waste Cycle concurrent after Climate Setup
# Staff Train after Waste Cycle and Energy Audit
# Compliance Check after Staff Train and Yield Forecast
# Market Setup after Compliance Check
# Data Review after Market Setup

# Create the partial order model
nodes = [
    Site_Survey,
    Rack_Install,
    Climate_Setup,
    Nutrient_Mix,
    Seed_Select,
    Auto_Plant,
    Sensor_Deploy,
    Pest_Control,
    Yield_Forecast,
    Energy_Audit,
    Waste_Cycle,
    Staff_Train,
    Compliance_Check,
    Market_Setup,
    Data_Review,
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges based on dependencies

root.order.add_edge(Site_Survey, Rack_Install)
root.order.add_edge(Rack_Install, Climate_Setup)

root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Climate_Setup, Seed_Select)
root.order.add_edge(Climate_Setup, Energy_Audit)
root.order.add_edge(Climate_Setup, Waste_Cycle)

root.order.add_edge(Nutrient_Mix, Auto_Plant)
root.order.add_edge(Seed_Select, Auto_Plant)

root.order.add_edge(Auto_Plant, Sensor_Deploy)
root.order.add_edge(Auto_Plant, Pest_Control)

root.order.add_edge(Sensor_Deploy, Yield_Forecast)
root.order.add_edge(Pest_Control, Yield_Forecast)

root.order.add_edge(Energy_Audit, Staff_Train)
root.order.add_edge(Waste_Cycle, Staff_Train)

root.order.add_edge(Staff_Train, Compliance_Check)
root.order.add_edge(Yield_Forecast, Compliance_Check)

root.order.add_edge(Compliance_Check, Market_Setup)

root.order.add_edge(Market_Setup, Data_Review)