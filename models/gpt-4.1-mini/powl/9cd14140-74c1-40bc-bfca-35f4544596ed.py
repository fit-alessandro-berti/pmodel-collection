# Generated from: 9cd14140-74c1-40bc-bfca-35f4544596ed.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating IoT sensors, AI-driven nutrient management, and automated harvesting. Starting from seed selection based on real-time climate data, the farm adjusts lighting, humidity, and irrigation through predictive analytics. Concurrently, waste organic matter is converted via bio-digesters to generate energy for internal use. Employees coordinate maintenance drones for pest control and monitor crop health via augmented reality interfaces. Finally, harvested produce undergoes automated quality sorting and packaging before real-time distribution scheduling to local markets, ensuring minimal waste and maximum freshness in a fully sustainable urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Seed_Select = Transition(label='Seed Select')
Climate_Scan = Transition(label='Climate Scan')
Light_Adjust = Transition(label='Light Adjust')
Irrigation_Set = Transition(label='Irrigation Set')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Sync = Transition(label='Sensor Sync')
Waste_Digest = Transition(label='Waste Digest')
Energy_Store = Transition(label='Energy Store')
Drone_Deploy = Transition(label='Drone Deploy')
Pest_Control = Transition(label='Pest Control')
Crop_Monitor = Transition(label='Crop Monitor')
Data_Analyze = Transition(label='Data Analyze')
Harvest_Auto = Transition(label='Harvest Auto')
Quality_Sort = Transition(label='Quality Sort')
Package_Item = Transition(label='Package Item')
Dispatch_Plan = Transition(label='Dispatch Plan')
Market_Link = Transition(label='Market Link')

# Partial Order 1: Seed Select --> Climate Scan --> (Light Adjust, Irrigation Set, Nutrient Mix, Sensor Sync) concurrent
initial_seq = StrictPartialOrder(
    nodes=[Seed_Select, Climate_Scan, Light_Adjust, Irrigation_Set, Nutrient_Mix, Sensor_Sync]
)
initial_seq.order.add_edge(Seed_Select, Climate_Scan)
initial_seq.order.add_edge(Climate_Scan, Light_Adjust)
initial_seq.order.add_edge(Climate_Scan, Irrigation_Set)
initial_seq.order.add_edge(Climate_Scan, Nutrient_Mix)
initial_seq.order.add_edge(Climate_Scan, Sensor_Sync)
# Light_Adjust, Irrigation_Set, Nutrient_Mix, Sensor_Sync are concurrent after Climate_Scan (no edges between them)

# Partial Order 2: Waste Digest --> Energy Store
bio_energy_seq = StrictPartialOrder(
    nodes=[Waste_Digest, Energy_Store]
)
bio_energy_seq.order.add_edge(Waste_Digest, Energy_Store)

# Partial Order 3: Drone Deploy --> Pest Control and Crop Monitor --> Data Analyze
drone_maintenance = StrictPartialOrder(
    nodes=[Drone_Deploy, Pest_Control, Crop_Monitor, Data_Analyze]
)
drone_maintenance.order.add_edge(Drone_Deploy, Pest_Control)
drone_maintenance.order.add_edge(Drone_Deploy, Crop_Monitor)
drone_maintenance.order.add_edge(Pest_Control, Data_Analyze)
drone_maintenance.order.add_edge(Crop_Monitor, Data_Analyze)
# Pest_Control and Crop_Monitor are concurrent after Drone_Deploy

# Partial Order 4: Harvest Auto --> Quality Sort --> Package Item --> Dispatch Plan --> Market Link
harvest_distribution = StrictPartialOrder(
    nodes=[Harvest_Auto, Quality_Sort, Package_Item, Dispatch_Plan, Market_Link]
)
harvest_distribution.order.add_edge(Harvest_Auto, Quality_Sort)
harvest_distribution.order.add_edge(Quality_Sort, Package_Item)
harvest_distribution.order.add_edge(Package_Item, Dispatch_Plan)
harvest_distribution.order.add_edge(Dispatch_Plan, Market_Link)

# Combine the big partial orders concurrent:
# initial_seq, bio_energy_seq, drone_maintenance, harvest_distribution can run concurrently, 
# but we need to impose some ordering between them: 
# We assume the farm operations steps proceed linearly in main sequence except for the waste digestion and drone maintenance happening concurrently with adjustments and scanning.

# So ordering:
# initial_seq --> bio_energy_seq (they run concurrently, but let's keep them concurrent)
# initial_seq --> drone_maintenance (also concurrent)
# initial_seq --> harvest_distribution (harvest after monitoring and data analyze)
# drone_maintenance --> harvest_distribution (harvest depends on data analyze, so drone_maintenance before harvest_distribution)
# bio_energy_seq concurrent with drone_maintenance and harvest_distribution, no dependencies

# Let's combine initial_seq, bio_energy_seq, drone_maintenance in a PO with concurrent nodes

root = StrictPartialOrder(
    nodes=[initial_seq, bio_energy_seq, drone_maintenance, harvest_distribution]
)

# initial_seq finishes before harvest_distribution starts
root.order.add_edge(initial_seq, harvest_distribution)
# drone_maintenance finishes before harvest_distribution starts
root.order.add_edge(drone_maintenance, harvest_distribution)
# initial_seq, bio_energy_seq and drone_maintenance concurrent except above constraints
# bio_energy_seq concurrent with initial_seq and drone_maintenance: no edges

# This models:
# - Seed selection and environment adjustment
# - Waste digestion and energy storing concurrent to environmental ops and monitoring
# - Drone deployment and monitoring concurrent with initial seq
# - Harvest and distribution follow initial operations and monitoring
