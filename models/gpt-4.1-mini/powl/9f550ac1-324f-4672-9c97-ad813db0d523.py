# Generated from: 9f550ac1-324f-4672-9c97-ad813db0d523.json
# Description: This process outlines the complex cycle of managing an urban vertical farm that integrates hydroponics, automated nutrient delivery, environmental monitoring, and crop harvesting within a multi-level indoor facility. The workflow begins with seed selection and germination in controlled chambers, followed by transplanting seedlings to vertical growth racks. Continuous monitoring of light intensity, humidity, and nutrient concentration is performed via IoT sensors, enabling real-time adjustments by the central control system. Periodic pest detection and bio-control deployment maintain plant health without chemicals. Harvesting is scheduled based on growth analytics, after which produce undergoes quality inspection and packaging. The process also includes waste recycling to optimize sustainability and data logging for performance analysis and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Select = Transition(label='Seed Select')
Germinate_Start = Transition(label='Germinate Start')
Chamber_Setup = Transition(label='Chamber Setup')
Seedling_Move = Transition(label='Seedling Move')
Rack_Install = Transition(label='Rack Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Irrigation_On = Transition(label='Irrigation On')
Light_Adjust = Transition(label='Light Adjust')
Sensor_Check = Transition(label='Sensor Check')
Pest_Scan = Transition(label='Pest Scan')
Bio_Control_Deploy = Transition(label='Bio-Control Deploy')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Package_Final = Transition(label='Package Final')
Waste_Sort = Transition(label='Waste Sort')
Data_Log = Transition(label='Data Log')

# Define the continuous monitoring partial order:
# Nutrient_Mix, Irrigation_On, Light_Adjust, Sensor_Check, Growth_Monitor run in parallel (concurrently)
monitoring_nodes = [Nutrient_Mix, Irrigation_On, Light_Adjust, Sensor_Check, Growth_Monitor]
monitoring = StrictPartialOrder(nodes=monitoring_nodes)  # no order edges => concurrent

# Define periodic pest handling loop: loop of Pest_Scan then Bio_Control_Deploy repeatedly
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Scan, Bio_Control_Deploy])

# After Seed selection and germination chamber setup:
# Order:
# Seed_Select --> Germinate_Start --> Chamber_Setup --> Seedling_Move --> Rack_Install
initial_seq_nodes = [Seed_Select, Germinate_Start, Chamber_Setup, Seedling_Move, Rack_Install]
initial_seq = StrictPartialOrder(nodes=initial_seq_nodes)
initial_seq.order.add_edge(Seed_Select, Germinate_Start)
initial_seq.order.add_edge(Germinate_Start, Chamber_Setup)
initial_seq.order.add_edge(Chamber_Setup, Seedling_Move)
initial_seq.order.add_edge(Seedling_Move, Rack_Install)

# Monitoring and pest_loop happen after Rack_Install (concurrently)
# So we combine monitoring and pest_loop in a parallel PO with no order edges between them
monitor_pest_parallel = StrictPartialOrder(nodes=monitoring_nodes + [pest_loop])
# no edges => concurrent

# After monitoring+pest_loop, Harvest_Plan
# Harvest_Plan --> Quality_Check --> Package_Final
harvest_seq_nodes = [Harvest_Plan, Quality_Check, Package_Final]
harvest_seq = StrictPartialOrder(nodes=harvest_seq_nodes)
harvest_seq.order.add_edge(Harvest_Plan, Quality_Check)
harvest_seq.order.add_edge(Quality_Check, Package_Final)

# After packaging, Waste_Sort and Data_Log happen concurrently
waste_data = StrictPartialOrder(nodes=[Waste_Sort, Data_Log])  # concurrent, no edges

# Compose the full process partial order with all nodes:
all_nodes = []
all_nodes.extend(initial_seq_nodes)
all_nodes.extend(monitoring_nodes)
all_nodes.append(pest_loop)
all_nodes.extend(harvest_seq_nodes)
all_nodes.extend([Waste_Sort, Data_Log])

root = StrictPartialOrder(nodes=all_nodes)

# Add ordering edges for initial sequence
root.order.add_edge(Seed_Select, Germinate_Start)
root.order.add_edge(Germinate_Start, Chamber_Setup)
root.order.add_edge(Chamber_Setup, Seedling_Move)
root.order.add_edge(Seedling_Move, Rack_Install)

# Rack_Install precedes monitoring and pest_loop (both concurrent)
root.order.add_edge(Rack_Install, Nutrient_Mix)
root.order.add_edge(Rack_Install, Irrigation_On)
root.order.add_edge(Rack_Install, Light_Adjust)
root.order.add_edge(Rack_Install, Sensor_Check)
root.order.add_edge(Rack_Install, Growth_Monitor)
root.order.add_edge(Rack_Install, pest_loop)

# Monitoring activities run concurrently with pest_loop, so no edges between those

# All monitoring nodes and pest_loop precede Harvest_Plan
root.order.add_edge(Nutrient_Mix, Harvest_Plan)
root.order.add_edge(Irrigation_On, Harvest_Plan)
root.order.add_edge(Light_Adjust, Harvest_Plan)
root.order.add_edge(Sensor_Check, Harvest_Plan)
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(pest_loop, Harvest_Plan)

# Harvest sequence edges
root.order.add_edge(Harvest_Plan, Quality_Check)
root.order.add_edge(Quality_Check, Package_Final)

# Package_Final precedes Waste_Sort and Data_Log (concurrent)
root.order.add_edge(Package_Final, Waste_Sort)
root.order.add_edge(Package_Final, Data_Log)