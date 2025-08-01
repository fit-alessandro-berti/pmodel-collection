# Generated from: c1cdf878-4398-451b-b236-c6f11a2a51d3.json
# Description: This process outlines the complex operational cycle of an urban vertical farm integrating IoT sensor data, AI-driven climate control, and automated harvesting robots. It begins with seed selection optimized by genetic algorithms, followed by nutrient solution formulation tailored per crop type. Environmental sensors continuously feed data to AI modules that adjust lighting, humidity, and airflow in real-time. Periodic pest detection triggers targeted biocontrol deployment. Harvesting robots identify mature crops via computer vision, ensuring selective picking without damaging plants. Post-harvest, produce undergoes automated quality grading and packaging. Waste biomass is recycled into organic compost through an on-site bio-reactor. Finally, logistics coordination ensures timely delivery to local markets and restaurants, optimizing freshness and reducing carbon footprint. This atypical process demands seamless integration of advanced technologies and sustainable practices to maximize yield within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Seed_Select = Transition(label='Seed Select')
Genetic_Optimize = Transition(label='Genetic Optimize')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Monitor = Transition(label='Data Monitor')
Climate_Adjust = Transition(label='Climate Adjust')
Pest_Detect = Transition(label='Pest Detect')
Biocontrol_Release = Transition(label='Biocontrol Release')
Growth_Analyze = Transition(label='Growth Analyze')
Harvest_Identify = Transition(label='Harvest Identify')
Crop_Pick = Transition(label='Crop Pick')
Quality_Grade = Transition(label='Quality Grade')
Pack_Produce = Transition(label='Pack Produce')
Waste_Process = Transition(label='Waste Process')
Compost_Cycle = Transition(label='Compost Cycle')
Logistics_Plan = Transition(label='Logistics Plan')
Delivery_Schedule = Transition(label='Delivery Schedule')

# Continuous environment monitoring cycle with sensor deployment, data monitoring and climate adjustment
# Considering Data_Monitor feeds Climate_Adjust, which loops after Pest detection and biocontrol release

# Define loop body:
# Loop pattern: * (A,B):
# A = Sensor_Deploy --> Data_Monitor --> Climate_Adjust
# B = Choice: Either Pest_Detect + Biocontrol_Release + Growth_Analyze (detection triggers biocontrol, then analyze growth)
# or skip (no pest detected)
# After B, loop back to A or exit the loop.

# Build A as partial order: Sensor_Deploy --> Data_Monitor --> Climate_Adjust
A_nodes = [Sensor_Deploy, Data_Monitor, Climate_Adjust]
A = StrictPartialOrder(nodes=A_nodes)
A.order.add_edge(Sensor_Deploy, Data_Monitor)
A.order.add_edge(Data_Monitor, Climate_Adjust)

# Build B as choice:
# Sequence Pest_Detect --> Biocontrol_Release --> Growth_Analyze
pest_seq = StrictPartialOrder(nodes=[Pest_Detect, Biocontrol_Release, Growth_Analyze])
pest_seq.order.add_edge(Pest_Detect, Biocontrol_Release)
pest_seq.order.add_edge(Biocontrol_Release, Growth_Analyze)

skip = SilentTransition()

B = OperatorPOWL(operator=Operator.XOR, children=[pest_seq, skip])

# Create loop node: * (A, B)
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Main sequence before loop: Seed Select --> Genetic Optimize --> Nutrient Mix
seq1 = StrictPartialOrder(nodes=[Seed_Select, Genetic_Optimize, Nutrient_Mix])
seq1.order.add_edge(Seed_Select, Genetic_Optimize)
seq1.order.add_edge(Genetic_Optimize, Nutrient_Mix)

# After loop: Harvest Identify --> Crop Pick --> Quality Grade --> Pack Produce
harvest_seq = StrictPartialOrder(nodes=[Harvest_Identify, Crop_Pick, Quality_Grade, Pack_Produce])
harvest_seq.order.add_edge(Harvest_Identify, Crop_Pick)
harvest_seq.order.add_edge(Crop_Pick, Quality_Grade)
harvest_seq.order.add_edge(Quality_Grade, Pack_Produce)

# Waste Process --> Compost Cycle (can be concurrent or after packing? Logically after packing)
waste_seq = StrictPartialOrder(nodes=[Waste_Process, Compost_Cycle])
waste_seq.order.add_edge(Waste_Process, Compost_Cycle)

# Logistics Plan --> Delivery Schedule
logistics_seq = StrictPartialOrder(nodes=[Logistics_Plan, Delivery_Schedule])
logistics_seq.order.add_edge(Logistics_Plan, Delivery_Schedule)

# Compose final partial order:
# seq1 --> loop --> harvest_seq
# harvest_seq --> waste_seq and logistics_seq concurrently
nodes_final = [seq1, loop, harvest_seq, waste_seq, logistics_seq]

root = StrictPartialOrder(nodes=nodes_final)

# Adding edges to define order of main flow:
root.order.add_edge(seq1, loop)
root.order.add_edge(loop, harvest_seq)
root.order.add_edge(harvest_seq, waste_seq)
root.order.add_edge(harvest_seq, logistics_seq)