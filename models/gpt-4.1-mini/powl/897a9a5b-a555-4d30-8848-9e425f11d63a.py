# Generated from: 897a9a5b-a555-4d30-8848-9e425f11d63a.json
# Description: This process describes the complex operational cycle of an urban vertical farming system integrating IoT sensors, AI-driven environmental controls, and automated nutrient delivery. It begins with seed selection based on seasonal data, followed by precision planting in modular trays. Continuous monitoring adjusts lighting, humidity, and temperature to optimize growth. Concurrently, water recycling and pest management systems operate autonomously. Harvesting is synchronized with market demand predictions using machine learning. Post-harvest, produce undergoes quality sorting and packaging in a sterile environment. Finally, logistics scheduling ensures timely distribution to urban retailers while maintaining freshness and minimizing waste through dynamic routing and inventory management. This atypical yet realistic process blends agriculture, technology, and supply chain coordination uniquely tailored for metropolitan settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Seed_Select = Transition(label='Seed Select')
Tray_Setup = Transition(label='Tray Setup')
Planting_Start = Transition(label='Planting Start')
Sensor_Deploy = Transition(label='Sensor Deploy')
Env_Monitor = Transition(label='Env Monitor')
Light_Adjust = Transition(label='Light Adjust')
Humidity_Control = Transition(label='Humidity Control')
Temp_Regulate = Transition(label='Temp Regulate')
Nutrient_Feed = Transition(label='Nutrient Feed')
Water_Recycle = Transition(label='Water Recycle')
Pest_Scan = Transition(label='Pest Scan')
Growth_Analyze = Transition(label='Growth Analyze')
Harvest_Sync = Transition(label='Harvest Sync')
Quality_Sort = Transition(label='Quality Sort')
Package_Produce = Transition(label='Package Produce')
Route_Plan = Transition(label='Route Plan')
Inventory_Update = Transition(label='Inventory Update')
Delivery_Track = Transition(label='Delivery Track')

# Environmental control activities partial order (concurrent but with Env Monitor before adjustments)
env_order = StrictPartialOrder(
    nodes=[Env_Monitor, Light_Adjust, Humidity_Control, Temp_Regulate]
)
env_order.order.add_edge(Env_Monitor, Light_Adjust)
env_order.order.add_edge(Env_Monitor, Humidity_Control)
env_order.order.add_edge(Env_Monitor, Temp_Regulate)

# Planting and nutrient feed partial order (nutrient feed after planting start)
planting_nutrient = StrictPartialOrder(
    nodes=[Planting_Start, Nutrient_Feed]
)
planting_nutrient.order.add_edge(Planting_Start, Nutrient_Feed)

# Water recycling and pest scan run concurrently and autonomously
water_pest = StrictPartialOrder(nodes=[Water_Recycle, Pest_Scan])

# Growth analyze after environmental controls, nutrient feed, water recycle and pest scan 
growth_dependencies = StrictPartialOrder(
    nodes=[env_order, planting_nutrient, water_pest, Growth_Analyze]
)
growth_dependencies.order.add_edge(env_order, Growth_Analyze)
growth_dependencies.order.add_edge(planting_nutrient, Growth_Analyze)
growth_dependencies.order.add_edge(water_pest, Growth_Analyze)

# Initial sequence: Seed Select -> Tray Setup -> Planting Start -> Sensor Deploy
initial_seq = StrictPartialOrder(
    nodes=[Seed_Select, Tray_Setup, Planting_Start, Sensor_Deploy]
)
initial_seq.order.add_edge(Seed_Select, Tray_Setup)
initial_seq.order.add_edge(Tray_Setup, Planting_Start)
initial_seq.order.add_edge(Planting_Start, Sensor_Deploy)

# Combine initial sequence with growth dependencies:
start_to_growth = StrictPartialOrder(
    nodes=[initial_seq, growth_dependencies]
)
start_to_growth.order.add_edge(initial_seq, growth_dependencies)

# Harvest Sync after growth analyze
harvest = StrictPartialOrder(nodes=[Growth_Analyze, Harvest_Sync])
harvest.order.add_edge(Growth_Analyze, Harvest_Sync)

# Quality sort and package produce, sequential after harvest sync
quality_packaging = StrictPartialOrder(
    nodes=[Quality_Sort, Package_Produce]
)
quality_packaging.order.add_edge(Quality_Sort, Package_Produce)

# Logistics scheduling partial order: Route Plan and Inventory Update concurrent before Delivery Track
logistics_plan = StrictPartialOrder(
    nodes=[Route_Plan, Inventory_Update, Delivery_Track]
)
logistics_plan.order.add_edge(Route_Plan, Delivery_Track)
logistics_plan.order.add_edge(Inventory_Update, Delivery_Track)

# Combine quality packaging with logistics (quality_packaging before logistics_plan)
final_processing = StrictPartialOrder(
    nodes=[quality_packaging, logistics_plan]
)
final_processing.order.add_edge(quality_packaging, logistics_plan)

# Full process partial order combining all major parts
root = StrictPartialOrder(
    nodes=[start_to_growth, harvest, final_processing]
)
root.order.add_edge(start_to_growth, harvest)
root.order.add_edge(harvest, final_processing)