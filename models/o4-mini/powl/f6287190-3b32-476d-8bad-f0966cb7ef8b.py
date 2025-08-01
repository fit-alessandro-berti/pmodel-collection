# Generated from: f6287190-3b32-476d-8bad-f0966cb7ef8b.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm that integrates IoT sensors, automated nutrient delivery, and AI-driven growth optimization. Beginning with seed selection tailored to local climate data, the cycle includes environmental monitoring, pest anomaly detection, adaptive lighting adjustment, and precise water recycling. Harvesting is coordinated with market demand forecasts, followed by quality grading and packaging. The process concludes with waste composting and data analytics feedback loops to refine future crop cycles. This atypical yet realistic workflow combines agriculture technology, sustainability, and urban supply chain management in a continuous, adaptive system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_select    = Transition(label='Seed Select')
climate_map    = Transition(label='Climate Map')
iot_setup      = Transition(label='IoT Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
sensor_check   = Transition(label='Sensor Check')
light_adjust   = Transition(label='Light Adjust')
water_cycle    = Transition(label='Water Cycle')
pest_scan      = Transition(label='Pest Scan')
growth_audit   = Transition(label='Growth Audit')
harvest_plan   = Transition(label='Harvest Plan')
demand_sync    = Transition(label='Demand Sync')
quality_grade  = Transition(label='Quality Grade')
pack_items     = Transition(label='Pack Items')
waste_compost  = Transition(label='Waste Compost')
data_review    = Transition(label='Data Review')
cycle_reset    = Transition(label='Cycle Reset')

# Main workflow partial order
po_main = StrictPartialOrder(nodes=[
    seed_select, climate_map, iot_setup, nutrient_mix,
    sensor_check, light_adjust, water_cycle, pest_scan,
    growth_audit, harvest_plan, demand_sync,
    quality_grade, pack_items, waste_compost
])
po_main.order.add_edge(seed_select,    climate_map)
po_main.order.add_edge(climate_map,    iot_setup)
po_main.order.add_edge(iot_setup,      nutrient_mix)
po_main.order.add_edge(nutrient_mix,   sensor_check)
po_main.order.add_edge(nutrient_mix,   light_adjust)
po_main.order.add_edge(nutrient_mix,   water_cycle)
po_main.order.add_edge(nutrient_mix,   pest_scan)
po_main.order.add_edge(sensor_check,   growth_audit)
po_main.order.add_edge(light_adjust,   growth_audit)
po_main.order.add_edge(water_cycle,    growth_audit)
po_main.order.add_edge(pest_scan,      growth_audit)
po_main.order.add_edge(growth_audit,   harvest_plan)
po_main.order.add_edge(harvest_plan,   demand_sync)
po_main.order.add_edge(demand_sync,    quality_grade)
po_main.order.add_edge(quality_grade,  pack_items)
po_main.order.add_edge(pack_items,     waste_compost)

# Reset/feedback partial order
po_reset = StrictPartialOrder(nodes=[data_review, cycle_reset])
po_reset.order.add_edge(data_review, cycle_reset)

# Loop: execute the main cycle, then optionally do reset and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[po_main, po_reset])