# Generated from: 551ea399-b140-4310-81eb-64ae9e10994a.json
# Description: This process details the comprehensive cycle of urban vertical farming, integrating IoT-enabled environmental control and AI-driven crop management. Starting from seed selection tailored to microclimate data, it involves automated nutrient mixing, precise hydroponic irrigation, real-time pest detection via drone surveillance, adaptive lighting adjustment based on growth stages, and continual yield forecasting. The cycle concludes with post-harvest quality sorting, packaging optimized for urban logistics, and dynamic market demand analysis to adjust future planting schedules. This atypical process blends advanced technology with sustainable agriculture in constrained urban environments, ensuring maximum resource efficiency and crop output while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Climate_Analyze = Transition(label='Climate Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
Irrigation_Control = Transition(label='Irrigation Control')
Pest_Detect = Transition(label='Pest Detect')
Drone_Survey = Transition(label='Drone Survey')
Light_Adjust = Transition(label='Light Adjust')
Growth_Monitor = Transition(label='Growth Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Sort = Transition(label='Quality Sort')
Package_Goods = Transition(label='Package Goods')
Logistics_Plan = Transition(label='Logistics Plan')
Market_Analyze = Transition(label='Market Analyze')
Schedule_Update = Transition(label='Schedule Update')

# Model reasoning:
# The process cycles through:
# - Seed Select and Climate Analyze as start (seed selection tailored to microclimate data).
# - Then Nutrient Mix and Irrigation Control as automated preparations.
# - Pest Detect and Drone Survey are related monitoring activities - can be concurrent.
# - Then Light Adjust and Growth Monitor as adaptive control activities.
# - Yield Forecast follows growth monitoring.
# - Harvest Crop after forecasting.
# - Then Quality Sort, Package Goods, Logistics Plan sequentially for post-harvest operations.
# - Finally Market Analyze and Schedule Update to adjust future planting schedules.
# The description implies a cycle, so incorporate a LOOP around the growing/monitoring stages before harvest.

# Define partial order for initial preparation:
prep_po = StrictPartialOrder(nodes=[Seed_Select, Climate_Analyze, Nutrient_Mix, Irrigation_Control])
prep_po.order.add_edge(Seed_Select, Climate_Analyze)
prep_po.order.add_edge(Climate_Analyze, Nutrient_Mix)
prep_po.order.add_edge(Nutrient_Mix, Irrigation_Control)

# Pest Detect and Drone Survey can run concurrently after Irrigation Control:
monitor_po = StrictPartialOrder(nodes=[Pest_Detect, Drone_Survey])
# Light Adjust and Growth Monitor run after pest/drone monitoring:
light_growth_po = StrictPartialOrder(nodes=[Light_Adjust, Growth_Monitor])
light_growth_po.order.add_edge(Light_Adjust, Growth_Monitor)

# The monitoring and adjusting cycle (loop body):
cycle_body_po = StrictPartialOrder(nodes=[monitor_po, light_growth_po])
# Because monitor_po and light_growth_po are partial orders themselves, 
# We need to combine their nodes in one StrictPartialOrder manually:

# Nodes combined for cycle body
cycle_nodes = [Pest_Detect, Drone_Survey, Light_Adjust, Growth_Monitor]
cycle_body_po = StrictPartialOrder(nodes=cycle_nodes)
# Pest Detect and Drone Survey concurrent, so no order between them
# Both must precede Light Adjust (since Light Adjust adaptive on those)
# The problem says adaptive lighting adjustment based on growth stages, after pest/drone detection
cycle_body_po.order.add_edge(Pest_Detect, Light_Adjust)
cycle_body_po.order.add_edge(Drone_Survey, Light_Adjust)
cycle_body_po.order.add_edge(Light_Adjust, Growth_Monitor)

# Loop: execute cycle_body_po, then decide to loop or proceed.
# This loop models the repeated monitoring and adjustment cycle until exit.

loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body_po, Yield_Forecast])

# After the loop yield forecast is done.

# Harvest and post harvesting partial order:
post_harvest_po = StrictPartialOrder(nodes=[Harvest_Crop, Quality_Sort, Package_Goods, Logistics_Plan])
post_harvest_po.order.add_edge(Harvest_Crop, Quality_Sort)
post_harvest_po.order.add_edge(Quality_Sort, Package_Goods)
post_harvest_po.order.add_edge(Package_Goods, Logistics_Plan)

# Market Analyze and Schedule Update come last sequentially:
market_po = StrictPartialOrder(nodes=[Market_Analyze, Schedule_Update])
market_po.order.add_edge(Market_Analyze, Schedule_Update)

# Combine post harvest and market analysis sequence:
final_po = StrictPartialOrder(nodes=[post_harvest_po, market_po])
# We need to merge nodes explicitly
final_nodes = [Harvest_Crop, Quality_Sort, Package_Goods, Logistics_Plan, Market_Analyze, Schedule_Update]
final_po = StrictPartialOrder(nodes=final_nodes)
final_po.order.add_edge(Harvest_Crop, Quality_Sort)
final_po.order.add_edge(Quality_Sort, Package_Goods)
final_po.order.add_edge(Package_Goods, Logistics_Plan)
final_po.order.add_edge(Logistics_Plan, Market_Analyze)
final_po.order.add_edge(Market_Analyze, Schedule_Update)

# Combine all main parts in a partial order:
root_nodes = [prep_po, loop, final_po]
root = StrictPartialOrder(nodes=root_nodes)
root.order.add_edge(prep_po, loop)
root.order.add_edge(loop, final_po)