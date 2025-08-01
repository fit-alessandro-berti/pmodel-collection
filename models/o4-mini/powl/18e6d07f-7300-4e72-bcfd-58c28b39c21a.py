# Generated from: 18e6d07f-7300-4e72-bcfd-58c28b39c21a.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics, energy optimization, and market demand forecasting. It begins with seed selection based on climate data, followed by automated nutrient mixing and precision lighting adjustments. Continuous environmental monitoring ensures optimal growth conditions, while robotic harvesting coordinates with supply chain logistics to reduce waste. The process also incorporates data feedback loops for yield improvement, energy consumption analysis, and community engagement through local distribution channels. This atypical but realistic process exemplifies the fusion of agriculture, technology, and urban sustainability, involving multidisciplinary coordination across farming, engineering, and business units to achieve efficient, scalable food production in constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
t_climate = Transition(label='Climate Scan')
t_seed = Transition(label='Seed Select')
t_nutrient = Transition(label='Nutrient Mix')
t_light = Transition(label='Light Adjust')
t_env = Transition(label='Env Monitor')
t_growth = Transition(label='Growth Assess')
t_pest = Transition(label='Pest Detect')
t_harvest = Transition(label='Robotic Harvest')
t_waste = Transition(label='Waste Sort')
t_market = Transition(label='Market Forecast')
t_supply = Transition(label='Supply Sync')
t_local = Transition(label='Local Distribute')
t_community = Transition(label='Community Engage')
t_maintenance = Transition(label='Maintenance Check')
t_data = Transition(label='Data Feedback')
t_yield = Transition(label='Yield Analyze')
t_energy = Transition(label='Energy Audit')

# Core process A: one iteration of the farming cycle
A = StrictPartialOrder(nodes=[
    t_nutrient, t_light, t_env, t_growth, t_pest,
    t_harvest, t_waste, t_market, t_supply,
    t_local, t_community, t_maintenance
])
A.order.add_edge(t_nutrient, t_env)
A.order.add_edge(t_light, t_env)
A.order.add_edge(t_env, t_growth)
A.order.add_edge(t_growth, t_pest)
A.order.add_edge(t_pest, t_harvest)
A.order.add_edge(t_harvest, t_waste)
A.order.add_edge(t_waste, t_supply)
A.order.add_edge(t_market, t_supply)
A.order.add_edge(t_supply, t_local)
A.order.add_edge(t_local, t_community)
A.order.add_edge(t_community, t_maintenance)

# Feedback cycle B: analysis and audit
B = StrictPartialOrder(nodes=[t_data, t_yield, t_energy])
B.order.add_edge(t_data, t_yield)
B.order.add_edge(t_yield, t_energy)

# Loop operator for repeated improvement cycles
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Root model: initial climate scan and seed selection, then looping core
root = StrictPartialOrder(nodes=[t_climate, t_seed, loop])
root.order.add_edge(t_climate, t_seed)
root.order.add_edge(t_seed, loop)