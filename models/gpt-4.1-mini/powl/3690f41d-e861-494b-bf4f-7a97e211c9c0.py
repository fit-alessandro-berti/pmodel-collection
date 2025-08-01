# Generated from: 3690f41d-e861-494b-bf4f-7a97e211c9c0.json
# Description: This process outlines the establishment of a commercial urban vertical farm that integrates advanced hydroponics, AI-driven climate control, and sustainable resource management. It begins with site evaluation, followed by modular rack installation and nutrient system calibration. Subsequent steps include AI sensor deployment to monitor plant health, automated seeding, and growth pattern analysis. The process also involves waste recycling integration and energy optimization. Harvest scheduling is dynamically adjusted based on real-time data, ensuring peak yield. Finally, the produce undergoes quality inspection before packaging and local distribution, emphasizing minimal environmental impact while maximizing urban space utilization and food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Evaluate = Transition(label='Site Evaluate')
Rack_Install = Transition(label='Rack Install')
Nutrient_Setup = Transition(label='Nutrient Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Seed_Automate = Transition(label='Seed Automate')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Climate_Adjust = Transition(label='Climate Adjust')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Produce_Package = Transition(label='Produce Package')
Local_Dispatch = Transition(label='Local Dispatch')
Data_Analyze = Transition(label='Data Analyze')
System_Maintain = Transition(label='System Maintain')

# From the description, a mostly sequential process but with some parallel parts and loops:
# Observe the flow:
# Site Evaluate -> Rack Install -> Nutrient Setup
# Then Sensor Deploy -> Seed Automate -> Growth Monitor
# Also Data Analyze and System Maintain seem concerning dynamic adjustment and upkeep
# Waste Recycle and Energy Optimize can be concurrent sustainability steps
# Climate Adjust likely related to AI-driven climate control can be concurrent with sustainability 
# Harvest Plan is dynamically adjusted based on data analyze, so after Data Analyze
# Quality Check -> Produce Package -> Local Dispatch linear final steps

# Construct partial orders to reflect this:

# First part: Site Evaluate -> Rack Install -> Nutrient Setup
initial_seq = StrictPartialOrder(nodes=[Site_Evaluate, Rack_Install, Nutrient_Setup])
initial_seq.order.add_edge(Site_Evaluate, Rack_Install)
initial_seq.order.add_edge(Rack_Install, Nutrient_Setup)

# Second part: Sensor Deploy -> Seed Automate -> Growth Monitor
monitor_seq = StrictPartialOrder(nodes=[Sensor_Deploy, Seed_Automate, Growth_Monitor])
monitor_seq.order.add_edge(Sensor_Deploy, Seed_Automate)
monitor_seq.order.add_edge(Seed_Automate, Growth_Monitor)

# Sustainability parallel activities: Waste Recycle, Energy Optimize, Climate Adjust
sustain_nodes = [Waste_Recycle, Energy_Optimize, Climate_Adjust]
sustain = StrictPartialOrder(nodes=sustain_nodes)  # no order = concurrent

# Data Analyze and System Maintain (continuous system monitoring and maintenance)
# System Maintain likely a loop with Data Analyze? Approximate loop:
# loop = * (Data Analyze, System Maintain)
data_analyze = Data_Analyze
system_maintain = System_Maintain
loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, system_maintain])

# Harvest Plan depends on Data Analyze (for dynamic adjustment)
# So Harvest Plan after loop_maintenance (which contains Data Analyze)
harvest_and_after = StrictPartialOrder(
    nodes=[loop_maintenance, Harvest_Plan, Quality_Check, Produce_Package, Local_Dispatch]
)
harvest_and_after.order.add_edge(loop_maintenance, Harvest_Plan)
harvest_and_after.order.add_edge(Harvest_Plan, Quality_Check)
harvest_and_after.order.add_edge(Quality_Check, Produce_Package)
harvest_and_after.order.add_edge(Produce_Package, Local_Dispatch)

# Combine monitoring sequence and sustainability in parallel, then join with harvest_and_after
# Also Nutrient Setup must finish before Sensor Deploy (monitor_seq)
# So initial_seq -> Sensor Deploy start, i.e. initial_seq -> monitor_seq
# We'll connect Nutrient_Setup --> Sensor_Deploy

# Create combined monitor+sustain partial order (concurrent)
monitor_sustain = StrictPartialOrder(nodes=[monitor_seq, sustain])
# No edge between monitor_seq and sustain => concurrent

# Now combine initial_seq with monitor_sustain (sequential: initial_seq -> monitor_seq)
# Because monitor_seq inside monitor_sustain, must link from initial_seq to monitor_seq's first node Sensor_Deploy
initial_plus_monitorSustain = StrictPartialOrder(
    nodes=[initial_seq, monitor_sustain]
)
# Add order edges:
# From initial_seq to monitor_seq: map from Nutrient_Setup to monitor_seq(Sensor_Deploy)
# monitor_seq is a StrictPartialOrder object, so linking nodes inside is unconventional:
# Instead, let's flatten monitor_sustain before combining with initial_seq for clarity.

# Flatten monitor_sustain to a PO with following nodes:

# monitor_seq nodes = [Sensor_Deploy, Seed_Automate, Growth_Monitor]
# sustain nodes = [Waste_Recycle, Energy_Optimize, Climate_Adjust]

monitor_sustain_flat_nodes = [
    Sensor_Deploy, Seed_Automate, Growth_Monitor,
    Waste_Recycle, Energy_Optimize, Climate_Adjust
]
monitor_sustain_flat = StrictPartialOrder(nodes=monitor_sustain_flat_nodes)
monitor_sustain_flat.order.add_edge(Sensor_Deploy, Seed_Automate)
monitor_sustain_flat.order.add_edge(Seed_Automate, Growth_Monitor)
# sustain parallel: no edges between Waste_Recycle, Energy_Optimize, Climate_Adjust

# Combine initial_seq and monitor_sustain_flat with ordering Nutrient_Setup --> Sensor_Deploy
initial_monitor = StrictPartialOrder(nodes=[Site_Evaluate, Rack_Install, Nutrient_Setup] + monitor_sustain_flat_nodes)
# Add initial edges
initial_monitor.order.add_edge(Site_Evaluate, Rack_Install)
initial_monitor.order.add_edge(Rack_Install, Nutrient_Setup)
# Add monitor_seq edges
initial_monitor.order.add_edge(Sensor_Deploy, Seed_Automate)
initial_monitor.order.add_edge(Seed_Automate, Growth_Monitor)
# Add Nutrient_Setup --> Sensor_Deploy 
initial_monitor.order.add_edge(Nutrient_Setup, Sensor_Deploy)
# sustain parallel: no order edges needed

# Finally, combine initial_monitor with loop_maintenance and harvest_and_after sequences

# Note: harvest_and_after nodes = [loop_maintenance, Harvest_Plan, Quality_Check, Produce_Package, Local_Dispatch]
# loop_maintenance is a loop, followed by Harvest_Plan and rest sequentially

final_root = StrictPartialOrder(
    nodes=[initial_monitor, loop_maintenance, Harvest_Plan, Quality_Check, Produce_Package, Local_Dispatch]
)

# Add orders connecting initial_monitor to loop_maintenance
# Data Analyze is inside loop_maintenance but not directly accessible for edge
# Just put edge initial_monitor -> loop_maintenance
final_root.order.add_edge(initial_monitor, loop_maintenance)
final_root.order.add_edge(loop_maintenance, Harvest_Plan)
final_root.order.add_edge(Harvest_Plan, Quality_Check)
final_root.order.add_edge(Quality_Check, Produce_Package)
final_root.order.add_edge(Produce_Package, Local_Dispatch)

# Assign to root
root = final_root