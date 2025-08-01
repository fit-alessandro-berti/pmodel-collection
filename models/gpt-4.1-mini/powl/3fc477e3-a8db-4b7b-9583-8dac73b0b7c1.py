# Generated from: 3fc477e3-a8db-4b7b-9583-8dac73b0b7c1.json
# Description: This process outlines the intricate operations involved in managing an urban vertical farming facility that integrates hydroponics, automated climate control, and AI-driven crop monitoring to maximize yield within limited city spaces. It begins with seed selection and genetic optimization, followed by nutrient mixing tailored for specific plant species. Environmental sensors continuously feed data for real-time adjustments in lighting, humidity, and temperature. Automated robotic arms handle planting, pruning, and harvesting to reduce labor costs and increase precision. Waste recycling converts organic byproducts into compost or bioenergy, maintaining sustainability. The process also includes market demand analysis to adjust crop varieties seasonally and logistics coordination for timely urban distribution, ensuring freshness and minimal carbon footprint throughout the cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Genetic_Optimize = Transition(label='Genetic Optimize')
Nutrient_Mix = Transition(label='Nutrient Mix')

Climate_Adjust = Transition(label='Climate Adjust')
Light_Control = Transition(label='Light Control')
Humidity_Set = Transition(label='Humidity Set')
Temp_Monitor = Transition(label='Temp Monitor')
Sensor_Update = Transition(label='Sensor Update')

Robotic_Plant = Transition(label='Robotic Plant')
Prune_Cycle = Transition(label='Prune Cycle')
Harvest_Pick = Transition(label='Harvest Pick')

Waste_Recycle = Transition(label='Waste Recycle')
Compost_Process = Transition(label='Compost Process')

Market_Analyze = Transition(label='Market Analyze')
Logistics_Plan = Transition(label='Logistics Plan')
Data_Review = Transition(label='Data Review')

# Compose environment sensor updates and climate controls as partial order (concurrent but in order within themselves where needed)
# Sensor update must happen before Climate Adjust, Light Control, Humidity Set, Temp Monitor (continuous monitoring)
sensor_po = StrictPartialOrder(
    nodes=[Sensor_Update, Climate_Adjust, Light_Control, Humidity_Set, Temp_Monitor]
)
sensor_po.order.add_edge(Sensor_Update, Climate_Adjust)
sensor_po.order.add_edge(Sensor_Update, Light_Control)
sensor_po.order.add_edge(Sensor_Update, Humidity_Set)
sensor_po.order.add_edge(Sensor_Update, Temp_Monitor)

# Robotic arms handling planting, pruning and harvesting are sequential
robotic_po = StrictPartialOrder(
    nodes=[Robotic_Plant, Prune_Cycle, Harvest_Pick]
)
robotic_po.order.add_edge(Robotic_Plant, Prune_Cycle)
robotic_po.order.add_edge(Prune_Cycle, Harvest_Pick)

# Waste recycling and compost processing flow sequentially
waste_po = StrictPartialOrder(
    nodes=[Waste_Recycle, Compost_Process]
)
waste_po.order.add_edge(Waste_Recycle, Compost_Process)

# Market analysis leads to data review and logistics planning sequentially
market_po = StrictPartialOrder(
    nodes=[Market_Analyze, Data_Review, Logistics_Plan]
)
market_po.order.add_edge(Market_Analyze, Data_Review)
market_po.order.add_edge(Data_Review, Logistics_Plan)

# Initial seed selection and optimization followed by nutrient mixing
seed_po = StrictPartialOrder(nodes=[Seed_Selection, Genetic_Optimize, Nutrient_Mix])
seed_po.order.add_edge(Seed_Selection, Genetic_Optimize)
seed_po.order.add_edge(Genetic_Optimize, Nutrient_Mix)

# Define the core processing cycle loop:
# Loop around the following:
#   - Sensor updates & climate adjustments (sensor_po)
#   - Robotic processing (robotic_po)
#   - Waste processing (waste_po)
#   - Market/logistics (market_po)
# The loop input node is the sensor update monitored continuously, leading through the cycle again

# Build partial order for the loop body, all four major parts are concurrent except market_po must happen after waste_po (market depends on product availability)
loop_body_po = StrictPartialOrder(
    nodes=[sensor_po, robotic_po, waste_po, market_po]
)
# Market analysis depends on waste recycling finishing (waste cycle done before market adjusts)
loop_body_po.order.add_edge(waste_po, market_po)

# Partial orders sensor_po, robotic_po and waste_po are concurrent (no order between them)
# Add edges within loop_body_po - nodes are partial orders themselves

# Loop operator: first execute loop_body_po, then choose to exit or repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[seed_po, loop_body_po])