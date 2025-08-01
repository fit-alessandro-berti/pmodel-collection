# Generated from: 7cc4c4f6-2474-465a-8e4a-7b9f47cca9e8.json
# Description: This process outlines the complex operational workflow of an urban vertical farming facility integrating automated environmental controls, real-time data analytics, and multi-crop management to maximize yield. The cycle begins with seed selection and preparation, followed by nutrient solution formulation tailored to each crop. Automated seeding and planting occur next, supported by environmental monitoring that adjusts lighting, humidity, and temperature dynamically. Growth phases are tracked via sensor arrays and AI-driven health assessments, triggering targeted interventions such as pest control or nutrient adjustments. Harvesting is scheduled based on optimal maturity indices and coordinated with packaging and cold storage systems. Waste recycling and water reclamation subsystems ensure sustainability. Finally, data is archived for continuous improvement and market forecasting, completing a closed-loop, tech-enabled agricultural ecosystem uncommon in traditional farming yet realistic for modern urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_prep       = Transition(label='Seed Prep')
nutr_mix        = Transition(label='Nutrient Mix')
auto_plant      = Transition(label='Automated Plant')
env_monitor     = Transition(label='Env Monitor')
light_adjust    = Transition(label='Light Adjust')
humidity_control= Transition(label='Humidity Control')
temp_regulate   = Transition(label='Temp Regulate')
growth_track    = Transition(label='Growth Track')
health_assess   = Transition(label='Health Assess')
pest_control    = Transition(label='Pest Control')
nutrient_boost  = Transition(label='Nutrient Boost')
harvest_plan    = Transition(label='Harvest Plan')
packaging_prep  = Transition(label='Packaging Prep')
cold_storage    = Transition(label='Cold Storage')
waste_recycle   = Transition(label='Waste Recycle')
water_reclaim   = Transition(label='Water Reclaim')
data_archive    = Transition(label='Data Archive')
market_forecast = Transition(label='Market Forecast')

# 1) Seed prep -> Nutrient mix -> Automated plant
initial_seq = StrictPartialOrder(nodes=[seed_prep, nutr_mix, auto_plant])
initial_seq.order.add_edge(seed_prep, nutr_mix)
initial_seq.order.add_edge(nutr_mix, auto_plant)

# 2) Env monitor -> (Light adjust, Humidity control, Temp regulate) in parallel
env_seq = StrictPartialOrder(nodes=[env_monitor, light_adjust, humidity_control, temp_regulate])
for adj in [light_adjust, humidity_control, temp_regulate]:
    env_seq.order.add_edge(env_monitor, adj)

# 3) Growth tracking and health assessment
growth = StrictPartialOrder(nodes=[growth_track, health_assess])
growth.order.add_edge(growth_track, health_assess)

# 4) Intervention choice: Pest control xor Nutrient boost
intervene_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, nutrient_boost])

# 5) Loop: do (growth->assess), then optionally intervene and repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, intervene_xor])

# 6) Harvest plan -> Packaging -> Cold storage
harvest_seq = StrictPartialOrder(nodes=[harvest_plan, packaging_prep, cold_storage])
harvest_seq.order.add_edge(harvest_plan, packaging_prep)
harvest_seq.order.add_edge(packaging_prep, cold_storage)

# 7) Waste recycle and water reclaim in parallel (no ordering between them)
recycle_seq = StrictPartialOrder(nodes=[waste_recycle, water_reclaim])

# 8) Archive data -> Market forecast
archive_seq = StrictPartialOrder(nodes=[data_archive, market_forecast])
archive_seq.order.add_edge(data_archive, market_forecast)

# 9) Assemble top‐level partial order
root = StrictPartialOrder(nodes=[
    initial_seq,
    env_seq,
    growth_loop,
    harvest_seq,
    recycle_seq,
    archive_seq
])
root.order.add_edge(initial_seq, env_seq)
root.order.add_edge(env_seq, growth_loop)
root.order.add_edge(growth_loop, harvest_seq)
root.order.add_edge(harvest_seq, recycle_seq)
root.order.add_edge(recycle_seq, archive_seq)