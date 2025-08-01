# Generated from: 18e6d07f-7300-4e72-bcfd-58c28b39c21a.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics, energy optimization, and market demand forecasting. It begins with seed selection based on climate data, followed by automated nutrient mixing and precision lighting adjustments. Continuous environmental monitoring ensures optimal growth conditions, while robotic harvesting coordinates with supply chain logistics to reduce waste. The process also incorporates data feedback loops for yield improvement, energy consumption analysis, and community engagement through local distribution channels. This atypical but realistic process exemplifies the fusion of agriculture, technology, and urban sustainability, involving multidisciplinary coordination across farming, engineering, and business units to achieve efficient, scalable food production in constrained city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
Seed_Select = Transition(label='Seed Select')
Climate_Scan = Transition(label='Climate Scan')
Nutrient_Mix = Transition(label='Nutrient Mix')
Light_Adjust = Transition(label='Light Adjust')
Env_Monitor = Transition(label='Env Monitor')
Growth_Assess = Transition(label='Growth Assess')
Pest_Detect = Transition(label='Pest Detect')
Robotic_Harvest = Transition(label='Robotic Harvest')
Waste_Sort = Transition(label='Waste Sort')
Yield_Analyze = Transition(label='Yield Analyze')
Energy_Audit = Transition(label='Energy Audit')
Data_Feedback = Transition(label='Data Feedback')
Supply_Sync = Transition(label='Supply Sync')
Market_Forecast = Transition(label='Market Forecast')
Local_Distribute = Transition(label='Local Distribute')
Community_Engage = Transition(label='Community Engage')
Maintenance_Check = Transition(label='Maintenance Check')

skip = SilentTransition()  # silent transition for optional/choice usage

# Model the initial seed selection based on climate data:
# Seed_Select --> Climate_Scan (sequential)
init_order = StrictPartialOrder(nodes=[Seed_Select, Climate_Scan])
init_order.order.add_edge(Seed_Select, Climate_Scan)

# Nutrient mix and light adjust happen after climate scan, concurrent
# so create PO for Nutrient_Mix and Light_Adjust with Climate_Scan ordered before both
nutr_light_po = StrictPartialOrder(nodes=[Climate_Scan, Nutrient_Mix, Light_Adjust])
nutr_light_po.order.add_edge(Climate_Scan, Nutrient_Mix)
nutr_light_po.order.add_edge(Climate_Scan, Light_Adjust)

# Environmental monitoring runs continuously during growth - modeled as concurrent with Growth_Assess, Pest_Detect
env_monitor_po = StrictPartialOrder(nodes=[Env_Monitor, Growth_Assess, Pest_Detect])
# Concurrent nodes: no order edges => they run partially ordered/concurrently

# Robotic harvest coordinates with supply logistics; 
# Robotic_Harvest --> Waste_Sort --> Supply_Sync (sequential)
harvest_supply_po = StrictPartialOrder(nodes=[Robotic_Harvest, Waste_Sort, Supply_Sync])
harvest_supply_po.order.add_edge(Robotic_Harvest, Waste_Sort)
harvest_supply_po.order.add_edge(Waste_Sort, Supply_Sync)

# Market forecast happens after supply sync
market_forecast_seq = StrictPartialOrder(nodes=[Supply_Sync, Market_Forecast])
market_forecast_seq.order.add_edge(Supply_Sync, Market_Forecast)

# Local distribution and community engagement happen after market forecast, concurrently
local_comm_po = StrictPartialOrder(nodes=[Local_Distribute, Community_Engage])
# No order edges => concurrent

# Data feedback loop incorporates Yield_Analyze, Energy_Audit, Data_Feedback with a loop back to Growth_Assess
# Represent the loop: 
# * (Yield_Analyze --> Energy_Audit --> Data_Feedback , Growth_Assess)
# Meaning: Execute Yield_Analyze --> Energy_Audit --> Data_Feedback,
# then choose to exit or do Growth_Assess then repeat

# First build the sequence inside the loop body A: Yield_Analyze --> Energy_Audit --> Data_Feedback
loop_body_A = StrictPartialOrder(nodes=[Yield_Analyze, Energy_Audit, Data_Feedback])
loop_body_A.order.add_edge(Yield_Analyze, Energy_Audit)
loop_body_A.order.add_edge(Energy_Audit, Data_Feedback)

# The looping B part is Growth_Assess
loop_body_B = Growth_Assess

data_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body_A, loop_body_B])

# Maintenance check runs in parallel with the main process after harvesting but before data feedback loop

# Assemble main process order:

# Initial steps:
# Seed_Select --> Climate_Scan --> (Nutrient_Mix || Light_Adjust)
# After Nutrient_Mix and Light_Adjust finish, proceed to (Env_Monitor || Pest_Detect || Growth_Assess), 
# however Growth_Assess is part of the loop, so must separate Growth_Assess for loop usage.
# We keep Growth_Assess out of env_monitor_po and model it separately.

# So break env_monitor_po into Env_Monitor and Pest_Detect (concurrent with each other)
env_monitor_pest_po = StrictPartialOrder(nodes=[Env_Monitor, Pest_Detect])

# Main execution order:
# After Nutrient_Mix and Light_Adjust, Env Monitoring and Pest Detect start concurrently
# Growth_Assess is part of the loop, but also initial Growth_Assess before loop begins?
# We'll assume Growth_Assess is required before entering loop as initial step, after Env_Monitor and Pest_Detect finish

# So we'll enforce Env_Monitor and Pest_Detect --> Growth_Assess

env_pest_growth_po = StrictPartialOrder(nodes=[Env_Monitor, Pest_Detect, Growth_Assess])
env_pest_growth_po.order.add_edge(Env_Monitor, Growth_Assess)
env_pest_growth_po.order.add_edge(Pest_Detect, Growth_Assess)

# However since Growth_Assess will be part of the loop, better to keep the initial Growth_Assess as the same node.
# We can link the initial Growth_Assess to loop starting point

# After Growth_Assess done, the loop starts to analyze yield, energy audit, data feedback, possibly returning to Growth_Assess multiple times

# After loop (data_feedback_loop), robotic harvest starts
# So Growth_Assess --(loop)--> data_feedback_loop --> Robotic_Harvest ...

# We will model that the loop includes Growth_Assess, so that after loop completion, we proceed to Harvest

# Connecting order edges:
# init_order: Seed_Select --> Climate_Scan
# nutr_light_po extends init_order: Climate_Scan --> Nutrient_Mix, Climate_Scan --> Light_Adjust
# env_pest_growth_po to start after nutr_light_po ends:
# Meaning Nutrient_Mix and Light_Adjust --> Env_Monitor and Pest_Detect concurrently, and both --> Growth_Assess

# We'll merge the three partial orders into one main partial order with all nodes and edges accordingly.

all_nodes_main = [
    Seed_Select, Climate_Scan, Nutrient_Mix, Light_Adjust,
    Env_Monitor, Pest_Detect, Growth_Assess
]

main_po = StrictPartialOrder(nodes=all_nodes_main)

# Add order edges:
main_po.order.add_edge(Seed_Select, Climate_Scan)
main_po.order.add_edge(Climate_Scan, Nutrient_Mix)
main_po.order.add_edge(Climate_Scan, Light_Adjust)

main_po.order.add_edge(Nutrient_Mix, Env_Monitor)
main_po.order.add_edge(Nutrient_Mix, Pest_Detect)
main_po.order.add_edge(Light_Adjust, Env_Monitor)
main_po.order.add_edge(Light_Adjust, Pest_Detect)

main_po.order.add_edge(Env_Monitor, Growth_Assess)
main_po.order.add_edge(Pest_Detect, Growth_Assess)

# Next, model the loop starting from Growth_Assess: loop over yield analyze, energy audit, data feedback with Growth_Assess

# We'll connect Growth_Assess to the LOOP node to indicate loop execution flow

# Note that the loop includes Growth_Assess in its looping part

# After finishing the loop, proceed to robotic harvest flow

# harvesting and supply chain partial order:
# Robotic_Harvest --> Waste_Sort --> Supply_Sync --> Market_Forecast --> (Local_Distribute || Community_Engage)

# Compose local_comm_po as parallel local_distribute and community_engage

# Combine harvest_supply_po, market_forecast_seq, and local_comm_po into one big PO maintaining order

harvest_market_nodes = [
    Robotic_Harvest, Waste_Sort, Supply_Sync, Market_Forecast,
    Local_Distribute, Community_Engage
]
harvest_market_po = StrictPartialOrder(nodes=harvest_market_nodes)

harvest_market_po.order.add_edge(Robotic_Harvest, Waste_Sort)
harvest_market_po.order.add_edge(Waste_Sort, Supply_Sync)
harvest_market_po.order.add_edge(Supply_Sync, Market_Forecast)
# Market_Forecast --> Local_Distribute and Market_Forecast --> Community_Engage
harvest_market_po.order.add_edge(Market_Forecast, Local_Distribute)
harvest_market_po.order.add_edge(Market_Forecast, Community_Engage)

# Maintenance check runs concurrently with last part of main process, but for clarity run after loop and before harvest sequence

# We will model sequence:
# main_po --> data_feedback_loop --> Maintenance_Check --> harvest_market_po

# Build a top-level PO to represent this sequence as partial order:
# The nodes will be main_po, data_feedback_loop, Maintenance_Check, harvest_market_po

# Use a StrictPartialOrder with these 4 nodes (main_po and harvest_market_po treated as nodes, as well as loop and Maintenance_Check)

maintenance_node = Maintenance_Check
top_nodes = [main_po, data_feedback_loop, maintenance_node, harvest_market_po]
top_po = StrictPartialOrder(nodes=top_nodes)

top_po.order.add_edge(main_po, data_feedback_loop)
top_po.order.add_edge(data_feedback_loop, maintenance_node)
top_po.order.add_edge(maintenance_node, harvest_market_po)

# Final root is this top level PO
root = top_po