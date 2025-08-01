# Generated from: 3fc477e3-a8db-4b7b-9583-8dac73b0b7c1.json
# Description: This process outlines the intricate operations involved in managing an urban vertical farming facility that integrates hydroponics, automated climate control, and AI-driven crop monitoring to maximize yield within limited city spaces. It begins with seed selection and genetic optimization, followed by nutrient mixing tailored for specific plant species. Environmental sensors continuously feed data for real-time adjustments in lighting, humidity, and temperature. Automated robotic arms handle planting, pruning, and harvesting to reduce labor costs and increase precision. Waste recycling converts organic byproducts into compost or bioenergy, maintaining sustainability. The process also includes market demand analysis to adjust crop varieties seasonally and logistics coordination for timely urban distribution, ensuring freshness and minimal carbon footprint throughout the cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection   = Transition(label='Seed Selection')
genetic_optimize = Transition(label='Genetic Optimize')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_update    = Transition(label='Sensor Update')
climate_adjust   = Transition(label='Climate Adjust')
light_control    = Transition(label='Light Control')
humidity_set     = Transition(label='Humidity Set')
temp_monitor     = Transition(label='Temp Monitor')
robotic_plant    = Transition(label='Robotic Plant')
prune_cycle      = Transition(label='Prune Cycle')
harvest_pick     = Transition(label='Harvest Pick')
waste_recycle    = Transition(label='Waste Recycle')
compost_process  = Transition(label='Compost Process')
market_analyze   = Transition(label='Market Analyze')
logistics_plan   = Transition(label='Logistics Plan')
data_review      = Transition(label='Data Review')

# Partial order for climate adjustment sub‐process
climate_po = StrictPartialOrder(nodes=[climate_adjust,
                                       light_control,
                                       humidity_set,
                                       temp_monitor])
climate_po.order.add_edge(climate_adjust, light_control)
climate_po.order.add_edge(climate_adjust, humidity_set)
climate_po.order.add_edge(climate_adjust, temp_monitor)

# Loop: sensor update then either exit or climate adjustment sub‐process and repeat
env_loop = OperatorPOWL(operator=Operator.LOOP,
                       children=[sensor_update, climate_po])

# Root partial order
root = StrictPartialOrder(nodes=[seed_selection,
                                 genetic_optimize,
                                 nutrient_mix,
                                 env_loop,
                                 robotic_plant,
                                 prune_cycle,
                                 harvest_pick,
                                 waste_recycle,
                                 compost_process,
                                 market_analyze,
                                 logistics_plan,
                                 data_review])

# Define the main sequence
root.order.add_edge(seed_selection,   genetic_optimize)
root.order.add_edge(genetic_optimize, nutrient_mix)
root.order.add_edge(nutrient_mix,     env_loop)
root.order.add_edge(env_loop,         robotic_plant)
root.order.add_edge(robotic_plant,    prune_cycle)
root.order.add_edge(prune_cycle,      harvest_pick)
root.order.add_edge(harvest_pick,     waste_recycle)
root.order.add_edge(waste_recycle,    compost_process)
root.order.add_edge(compost_process,  market_analyze)
root.order.add_edge(market_analyze,   logistics_plan)
root.order.add_edge(logistics_plan,   data_review)