# Generated from: 08bb6001-eed6-4912-9a6f-2d021676389a.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm that integrates hydroponics, automated climate control, and AI-driven crop optimization. It begins with seed selection based on market trends and genetic traits, followed by nutrient solution preparation and precise planting. Environmental sensors continuously monitor temperature, humidity, and light, triggering climate adjustments. AI algorithms analyze growth data to optimize resource use and predict harvest times. Concurrently, pest detection systems activate targeted biocontrol measures. Harvested crops undergo quality sorting and packaging before distribution. Waste biomass is composted or converted to bioenergy, closing the sustainability loop. The process culminates with performance analysis and strategic planning for the next cycle, ensuring efficiency and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Seed_Select = Transition(label='Seed Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Plant_Setup = Transition(label='Plant Setup')
Climate_Adjust = Transition(label='Climate Adjust')
Sensor_Monitor = Transition(label='Sensor Monitor')
AI_Analyze = Transition(label='AI Analyze')
Growth_Track = Transition(label='Growth Track')
Pest_Detect = Transition(label='Pest Detect')
Bio_Control = Transition(label='Bio Control')
Harvest_Crop = Transition(label='Harvest Crop')
Quality_Sort = Transition(label='Quality Sort')
Package_Goods = Transition(label='Package Goods')
Distribute = Transition(label='Distribute')
Waste_Process = Transition(label='Waste Process')
Cycle_Review = Transition(label='Cycle Review')

# Sensor monitoring runs concurrently and triggers climate adjustments
# Model Climate_Adjust loop:
# Loop body A: Climate_Adjust
# Loop condition B: Sensor_Monitor (then back to Climate_Adjust)
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Adjust, Sensor_Monitor])

# Pest detection and biocontrol are concurrent (partial order with no order between them)
pest_seq = StrictPartialOrder(nodes=[Pest_Detect, Bio_Control])
pest_seq.order.add_edge(Pest_Detect, Bio_Control)  # pest detection before biocontrol

# Harvest flow
harvest_seq = StrictPartialOrder(nodes=[Harvest_Crop, Quality_Sort, Package_Goods, Distribute])
harvest_seq.order.add_edge(Harvest_Crop, Quality_Sort)
harvest_seq.order.add_edge(Quality_Sort, Package_Goods)
harvest_seq.order.add_edge(Package_Goods, Distribute)

# Growth tracking and AI analyze run concurrently (no ordering between)
growth_ai = StrictPartialOrder(nodes=[Growth_Track, AI_Analyze])

# Waste process and cycle review happen after harvesting and packaging
final_seq = StrictPartialOrder(nodes=[Waste_Process, Cycle_Review])
final_seq.order.add_edge(Waste_Process, Cycle_Review)

# Initial setup sequence
initial_seq = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Prep, Plant_Setup])
initial_seq.order.add_edge(Seed_Select, Nutrient_Prep)
initial_seq.order.add_edge(Nutrient_Prep, Plant_Setup)

# Combine growth_ai, pest_seq, and climate_loop concurrently
# No ordering edges between them (fully concurrent)
concurrent_monitoring = StrictPartialOrder(nodes=[growth_ai, pest_seq, climate_loop])

# Build the main partial order
root = StrictPartialOrder(
    nodes=[initial_seq, concurrent_monitoring, harvest_seq, final_seq]
)

# Define ordering between stages
root.order.add_edge(initial_seq, concurrent_monitoring)
root.order.add_edge(concurrent_monitoring, harvest_seq)
root.order.add_edge(harvest_seq, final_seq)