# Generated from: f6287190-3b32-476d-8bad-f0966cb7ef8b.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm that integrates IoT sensors, automated nutrient delivery, and AI-driven growth optimization. Beginning with seed selection tailored to local climate data, the cycle includes environmental monitoring, pest anomaly detection, adaptive lighting adjustment, and precise water recycling. Harvesting is coordinated with market demand forecasts, followed by quality grading and packaging. The process concludes with waste composting and data analytics feedback loops to refine future crop cycles. This atypical yet realistic workflow combines agriculture technology, sustainability, and urban supply chain management in a continuous, adaptive system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Climate_Map = Transition(label='Climate Map')
IoT_Setup = Transition(label='IoT Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Check = Transition(label='Sensor Check')
Light_Adjust = Transition(label='Light Adjust')
Water_Cycle = Transition(label='Water Cycle')
Pest_Scan = Transition(label='Pest Scan')
Growth_Audit = Transition(label='Growth Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Demand_Sync = Transition(label='Demand Sync')
Quality_Grade = Transition(label='Quality Grade')
Pack_Items = Transition(label='Pack Items')
Waste_Compost = Transition(label='Waste Compost')
Data_Review = Transition(label='Data Review')
Cycle_Reset = Transition(label='Cycle Reset')

# Partial order for the environment preparation and monitoring steps
prep_monitor = StrictPartialOrder(nodes=[
    Seed_Select,
    Climate_Map,
    IoT_Setup,
    Nutrient_Mix,
    Sensor_Check,
    Pest_Scan,
    Light_Adjust,
    Water_Cycle,
    Growth_Audit
])
prep_monitor.order.add_edge(Seed_Select, Climate_Map)
prep_monitor.order.add_edge(Climate_Map, IoT_Setup)
prep_monitor.order.add_edge(IoT_Setup, Nutrient_Mix)
prep_monitor.order.add_edge(Nutrient_Mix, Sensor_Check)
prep_monitor.order.add_edge(Sensor_Check, Pest_Scan)
prep_monitor.order.add_edge(Pest_Scan, Light_Adjust)
prep_monitor.order.add_edge(Light_Adjust, Water_Cycle)
prep_monitor.order.add_edge(Water_Cycle, Growth_Audit)

# Partial order for Harvest and packaging
harvest_pack = StrictPartialOrder(nodes=[
    Harvest_Plan,
    Demand_Sync,
    Quality_Grade,
    Pack_Items
])
harvest_pack.order.add_edge(Harvest_Plan, Demand_Sync)
harvest_pack.order.add_edge(Demand_Sync, Quality_Grade)
harvest_pack.order.add_edge(Quality_Grade, Pack_Items)

# Partial order for the closing activities
close = StrictPartialOrder(nodes=[
    Waste_Compost,
    Data_Review
])
close.order.add_edge(Waste_Compost, Data_Review)

# Partial order combining harvest-pack and close activities (sequential)
harvest_close = StrictPartialOrder(nodes=[harvest_pack, close])
harvest_close.order.add_edge(harvest_pack, close)

# Loop body: from prep_monitor through harvest_close, then reset cycle
# Loop operator: execute prep_monitor + harvest_close, then either exit (Cycle_Reset) or loop again
body = StrictPartialOrder(nodes=[prep_monitor, harvest_close])
body.order.add_edge(prep_monitor, harvest_close)

loop = OperatorPOWL(operator=Operator.LOOP, children=[body, Cycle_Reset])

root = loop