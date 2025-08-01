# Generated from: dee43d2b-459b-4866-b006-fda69289f150.json
# Description: This process outlines the end-to-end management of a vertical urban farm, integrating advanced hydroponics, climate control, and AI-driven crop monitoring to optimize yield in limited city spaces. It involves seed selection, nutrient mixing, environmental adjustments, pest detection, harvest scheduling, and distribution logistics tailored for high-density urban environments. Continuous feedback loops with real-time data ensure sustainability and efficient resource usage, while compliance with urban agricultural regulations is maintained throughout the cycle. The process supports rapid adaptation to changing weather patterns and market demands, promoting local food security and minimizing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Setup = Transition(label='Planting Setup')
Climate_Control = Transition(label='Climate Control')
Water_Cycling = Transition(label='Water Cycling')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Detection = Transition(label='Pest Detection')
Light_Adjustment = Transition(label='Light Adjustment')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Planning = Transition(label='Harvest Planning')
Crop_Harvest = Transition(label='Crop Harvest')
Yield_Sorting = Transition(label='Yield Sorting')
Packaging_Prep = Transition(label='Packaging Prep')
Distribution_Plan = Transition(label='Distribution Plan')
Regulation_Check = Transition(label='Regulation Check')
Waste_Recycling = Transition(label='Waste Recycling')
System_Maintenance = Transition(label='System Maintenance')

# Initial preparation sequence: Seed Selection -> Nutrient Mix -> Planting Setup
prep = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, Planting_Setup])
prep.order.add_edge(Seed_Selection, Nutrient_Mix)
prep.order.add_edge(Nutrient_Mix, Planting_Setup)

# Growing environment control partial order:
# Climate Control and Water Cycling run concurrently, both before Light Adjustment
env_control = StrictPartialOrder(nodes=[Climate_Control, Water_Cycling, Light_Adjustment])
env_control.order.add_edge(Climate_Control, Light_Adjustment)
env_control.order.add_edge(Water_Cycling, Light_Adjustment)

# Monitoring and pest detection partial order, concurrent, both before Data Analysis
monitoring = StrictPartialOrder(nodes=[Growth_Monitoring, Pest_Detection, Data_Analysis])
monitoring.order.add_edge(Growth_Monitoring, Data_Analysis)
monitoring.order.add_edge(Pest_Detection, Data_Analysis)

# Harvest-related activities sequence: Harvest Planning -> Crop Harvest -> Yield Sorting -> Packaging Prep
harvest_seq = StrictPartialOrder(nodes=[Harvest_Planning, Crop_Harvest, Yield_Sorting, Packaging_Prep])
harvest_seq.order.add_edge(Harvest_Planning, Crop_Harvest)
harvest_seq.order.add_edge(Crop_Harvest, Yield_Sorting)
harvest_seq.order.add_edge(Yield_Sorting, Packaging_Prep)

# Distribution and compliance partial order: Distribution Plan and Regulation Check concurrently both before Waste Recycling
dist_reg = StrictPartialOrder(nodes=[Distribution_Plan, Regulation_Check, Waste_Recycling])
dist_reg.order.add_edge(Distribution_Plan, Waste_Recycling)
dist_reg.order.add_edge(Regulation_Check, Waste_Recycling)

# Maintenance performed regularly - will form a loop with the growing environment and monitoring
# Loop body:
#  1) env_control and monitoring concurrently (partial order)
#  2) data analysis (part of monitoring)
#  3) Maintenance or skip (choice)
maintenance_xor = OperatorPOWL(operator=Operator.XOR, children=[System_Maintenance, SilentTransition()])

# Loop cycle: (env_control + monitoring) as partial order
# Combine env_control and monitoring as concurrent (unconnected)
grow_phase = StrictPartialOrder(nodes=[env_control, monitoring])
# No order edges between env_control and monitoring, so concurrent

# Loop is: execute grow_phase, then choose to exit or do maintenance and grow_phase again
loop = OperatorPOWL(operator=Operator.LOOP, children=[grow_phase, maintenance_xor])

# Build the overall workflow partial order:
# prep -> loop -> harvest_seq -> dist_reg
root = StrictPartialOrder(nodes=[prep, loop, harvest_seq, dist_reg])
root.order.add_edge(prep, loop)
root.order.add_edge(loop, harvest_seq)
root.order.add_edge(harvest_seq, dist_reg)