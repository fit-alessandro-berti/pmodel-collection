# Generated from: 930a521e-2cc4-48bc-9e0f-7d35e879280f.json
# Description: This process outlines the comprehensive cycle of urban vertical farming where crops are grown in stacked layers within controlled indoor environments. It involves site assessment, modular installation, seed selection, nutrient preparation, climate calibration, automated seeding, growth monitoring, pest control, adaptive lighting, water recycling, data analytics, crop harvesting, quality inspection, packaging automation, and distribution logistics. The process integrates IoT sensors and AI-driven analytics to optimize yield while minimizing resource consumption, addressing urban space constraints and sustainability goals in agriculture. Continuous feedback loops ensure adjustments to environmental factors and operational parameters for maximum productivity and minimal waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site        = Transition(label='Site Assess')
module      = Transition(label='Module Install')
seed        = Transition(label='Seed Select')
nutrient    = Transition(label='Nutrient Prep')
initial_cal = Transition(label='Climate Calibrate')

auto_seed   = Transition(label='Auto Seed')
growth      = Transition(label='Growth Monitor')
pest        = Transition(label='Pest Control')
light       = Transition(label='Light Adjust')
water       = Transition(label='Water Recycle')

analyze     = Transition(label='Data Analyze')
loop_cal    = Transition(label='Climate Calibrate')

harvest     = Transition(label='Crop Harvest')
inspect     = Transition(label='Quality Inspect')
pack        = Transition(label='Package Auto')
logistics   = Transition(label='Logistics Plan')

# Define the growth cycle (A part of the loop)
growth_cycle = StrictPartialOrder(nodes=[auto_seed, growth, pest, light, water])
growth_cycle.order.add_edge(auto_seed, growth)
growth_cycle.order.add_edge(growth, pest)
growth_cycle.order.add_edge(pest, light)
growth_cycle.order.add_edge(light, water)

# Define the loop body (B part): analyze data and recalibrate
loop_body = StrictPartialOrder(nodes=[analyze, loop_cal])
loop_body.order.add_edge(analyze, loop_cal)

# Define the loop: repeat growth_cycle, optionally perform loop_body then growth_cycle again
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, loop_body])

# Assemble the full process
root = StrictPartialOrder(nodes=[
    site, module, seed, nutrient, initial_cal,
    loop_node,
    harvest, inspect, pack, logistics
])
# Initial setup ordering
root.order.add_edge(site, module)
root.order.add_edge(module, seed)
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, initial_cal)
# Enter loop after initial calibration
root.order.add_edge(initial_cal, loop_node)
# After finishing loop exit, proceed to harvesting and final steps
root.order.add_edge(loop_node, harvest)
root.order.add_edge(harvest, inspect)
root.order.add_edge(inspect, pack)
root.order.add_edge(pack, logistics)