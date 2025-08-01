# Generated from: 69a3dd4b-090a-48de-8e00-313f840f4e68.json
# Description: This process outlines the sequential steps for establishing a fully operational urban vertical farm within a repurposed industrial space. It includes site assessment, modular system design, climate control calibration, hydroponic nutrient formulation, automated lighting programming, pest management integration, workforce training, crop scheduling, yield monitoring, waste recycling implementation, and market distribution planning. The process is complex due to the integration of advanced technology, sustainability requirements, and urban logistics, requiring interdisciplinary coordination and continuous optimization to maximize crop output while minimizing environmental impact in a constrained urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Space_Planning = Transition(label='Space Planning')
System_Design = Transition(label='System Design')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Config = Transition(label='Lighting Config')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Crop_Schedule = Transition(label='Crop Schedule')
Yield_Tracking = Transition(label='Yield Tracking')
Waste_Sort = Transition(label='Waste Sort')
Water_Recycling = Transition(label='Water Recycling')
Energy_Audit = Transition(label='Energy Audit')
Market_Prep = Transition(label='Market Prep')
Distribution = Transition(label='Distribution')

# Construct the workflow partial order reflecting sequential and concurrent dependencies
# The sequence roughly:
# Site Survey -> Space Planning -> System Design
# Then parallel calibration steps: Climate Setup, Nutrient Mix, Lighting Config, Pest Control
# Then Staff Training and Crop Scheduling in parallel after calibrations
# Then Yield Tracking, Waste Sort, Water Recycling, Energy Audit (some can be concurrent)
# Finally Market Prep and Distribution sequentially

# We model parallelism with concurrent nodes (no edges between them), sequential with edges

nodes = [
    Site_Survey,
    Space_Planning,
    System_Design,
    Climate_Setup,
    Nutrient_Mix,
    Lighting_Config,
    Pest_Control,
    Staff_Training,
    Crop_Schedule,
    Yield_Tracking,
    Waste_Sort,
    Water_Recycling,
    Energy_Audit,
    Market_Prep,
    Distribution
]

root = StrictPartialOrder(nodes=nodes)

# Sequential dependencies
root.order.add_edge(Site_Survey, Space_Planning)
root.order.add_edge(Space_Planning, System_Design)

# After System Design, 4 activities in parallel:
# Climate Setup, Nutrient Mix, Lighting Config, Pest Control
root.order.add_edge(System_Design, Climate_Setup)
root.order.add_edge(System_Design, Nutrient_Mix)
root.order.add_edge(System_Design, Lighting_Config)
root.order.add_edge(System_Design, Pest_Control)

# After calibrations, Staff Training and Crop Schedule in parallel
# They depend on all 4 calibration tasks completing
root.order.add_edge(Climate_Setup, Staff_Training)
root.order.add_edge(Nutrient_Mix, Staff_Training)
root.order.add_edge(Lighting_Config, Staff_Training)
root.order.add_edge(Pest_Control, Staff_Training)

root.order.add_edge(Climate_Setup, Crop_Schedule)
root.order.add_edge(Nutrient_Mix, Crop_Schedule)
root.order.add_edge(Lighting_Config, Crop_Schedule)
root.order.add_edge(Pest_Control, Crop_Schedule)

# After training and scheduling, Yield Tracking, Waste Sort, Water Recycling, Energy Audit run concurrently
root.order.add_edge(Staff_Training, Yield_Tracking)
root.order.add_edge(Crop_Schedule, Yield_Tracking)

root.order.add_edge(Staff_Training, Waste_Sort)
root.order.add_edge(Crop_Schedule, Waste_Sort)

root.order.add_edge(Staff_Training, Water_Recycling)
root.order.add_edge(Crop_Schedule, Water_Recycling)

root.order.add_edge(Staff_Training, Energy_Audit)
root.order.add_edge(Crop_Schedule, Energy_Audit)

# Finally Market Prep depends on completion of these four
root.order.add_edge(Yield_Tracking, Market_Prep)
root.order.add_edge(Waste_Sort, Market_Prep)
root.order.add_edge(Water_Recycling, Market_Prep)
root.order.add_edge(Energy_Audit, Market_Prep)

# Distribution last, after Market Prep
root.order.add_edge(Market_Prep, Distribution)