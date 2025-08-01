# Generated from: 3c8ff18c-dd47-4e82-b620-b54ce0113d1d.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site analysis, modular rack installation, climate system calibration, nutrient solution preparation, seed selection, automated planting, lighting optimization, pest monitoring, data analytics integration, crop harvesting, waste recycling, packaging, and distribution logistics. The process ensures sustainable, high-yield crop production with minimal environmental impact, leveraging IoT sensors and AI-driven adjustments to maximize efficiency in a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey    = Transition(label='Site Survey')
rack_setup     = Transition(label='Rack Setup')
climate_adjust = Transition(label='Climate Adjust')
nutrient_mix   = Transition(label='Nutrient Mix')
seed_select    = Transition(label='Seed Select')
auto_plant     = Transition(label='Auto Plant')
light_tune     = Transition(label='Light Tune')
pest_check     = Transition(label='Pest Check')
sensor_sync    = Transition(label='Sensor Sync')
data_review    = Transition(label='Data Review')
growth_scan    = Transition(label='Growth Scan')
harvest_crop   = Transition(label='Harvest Crop')
waste_sort     = Transition(label='Waste Sort')
pack_goods     = Transition(label='Pack Goods')
distribute     = Transition(label='Distribute')

# Build the growth‐cycle partial order: Light Tune → Pest Check → Sensor Sync → Data Review → Growth Scan
cycle = StrictPartialOrder(nodes=[
    light_tune, pest_check, sensor_sync, data_review, growth_scan
])
cycle.order.add_edge(light_tune, pest_check)
cycle.order.add_edge(pest_check, sensor_sync)
cycle.order.add_edge(sensor_sync, data_review)
cycle.order.add_edge(data_review, growth_scan)

# Wrap the monitoring cycle in a LOOP: do 'cycle', then either exit or silent‐step and repeat
skip = SilentTransition()
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Main process: sequence from site survey up to distribution
root = StrictPartialOrder(nodes=[
    site_survey,
    rack_setup,
    climate_adjust,
    nutrient_mix,
    seed_select,
    auto_plant,
    growth_loop,
    harvest_crop,
    waste_sort,
    pack_goods,
    distribute
])
root.order.add_edge(site_survey,    rack_setup)
root.order.add_edge(rack_setup,     climate_adjust)
root.order.add_edge(climate_adjust, nutrient_mix)
root.order.add_edge(nutrient_mix,   seed_select)
root.order.add_edge(seed_select,    auto_plant)
root.order.add_edge(auto_plant,     growth_loop)
root.order.add_edge(growth_loop,    harvest_crop)
root.order.add_edge(harvest_crop,   waste_sort)
root.order.add_edge(waste_sort,     pack_goods)
root.order.add_edge(pack_goods,     distribute)