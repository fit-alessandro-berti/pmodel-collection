# Generated from: 40b2e441-0b67-4a24-9e17-2d521d0867e9.json
# Description: This process outlines the end-to-end establishment of an urban vertical farm in a densely populated city environment. It involves site analysis, modular structure design, hydroponic system installation, climate control calibration, crop selection, seedling propagation, nutrient solution preparation, automated monitoring setup, pest management integration, waste recycling, harvest scheduling, quality assessment, packaging design, distribution logistics, and community engagement to ensure sustainable urban agriculture with optimized yield, minimal environmental impact, and strong local support.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Structure_Design = Transition(label='Structure Design')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Crop_Select = Transition(label='Crop Select')
Seedling_Grow = Transition(label='Seedling Grow')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Waste_Process = Transition(label='Waste Process')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Packaging_Dev = Transition(label='Packaging Dev')
Logistics_Plan = Transition(label='Logistics Plan')
Community_Meet = Transition(label='Community Meet')

# Structure the POWL model:
# First: Site Analysis -> Structure Design -> System Install -> Climate Setup
# Then, parallel crop related (Crop Select, Seedling Grow, Nutrient Mix)
crop_related = StrictPartialOrder(nodes=[Crop_Select, Seedling_Grow, Nutrient_Mix])
# No order inside crop related: these three can run concurrently

# Sensor Deploy then Pest Control then Waste Process in order
sensor_and_pest = StrictPartialOrder(nodes=[Sensor_Deploy, Pest_Control, Waste_Process])
sensor_and_pest.order.add_edge(Sensor_Deploy, Pest_Control)
sensor_and_pest.order.add_edge(Pest_Control, Waste_Process)

# Harvest Plan -> Quality Check -> Packaging Dev -> Logistics Plan
harvest_flow = StrictPartialOrder(nodes=[Harvest_Plan, Quality_Check, Packaging_Dev, Logistics_Plan])
harvest_flow.order.add_edge(Harvest_Plan, Quality_Check)
harvest_flow.order.add_edge(Quality_Check, Packaging_Dev)
harvest_flow.order.add_edge(Packaging_Dev, Logistics_Plan)

# Community Meet is final, after logistics plan
final_flow = StrictPartialOrder(nodes=[harvest_flow, Community_Meet])
final_flow.order.add_edge(harvest_flow, Community_Meet)

# Partial order for crop_related and sensor_and_pest (can be concurrent)
mid_parallel = StrictPartialOrder(nodes=[crop_related, sensor_and_pest])

# Full sequential order:
root = StrictPartialOrder(
    nodes=[Site_Analysis, Structure_Design, System_Install, Climate_Setup, mid_parallel, final_flow]
)

root.order.add_edge(Site_Analysis, Structure_Design)
root.order.add_edge(Structure_Design, System_Install)
root.order.add_edge(System_Install, Climate_Setup)
root.order.add_edge(Climate_Setup, mid_parallel)
root.order.add_edge(mid_parallel, final_flow)