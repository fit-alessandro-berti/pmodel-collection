# Generated from: 55f34aba-595d-4319-9d1c-d1e418ed4ed9.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site analysis for structural integrity, environmental impact review, modular hydroponic system design, nutrient solution formulation, advanced lighting configuration, climate control integration, crop selection based on local demand, IoT sensor deployment for real-time monitoring, staff training on automated systems, community engagement for urban agriculture education, regulatory compliance checks, waste recycling protocols, yield data analytics setup, and finally, continuous optimization for energy efficiency and crop productivity to ensure sustainable urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with exact labels
Site_Survey = Transition(label='Site Survey')
Structure_Test = Transition(label='Structure Test')
Impact_Review = Transition(label='Impact Review')
System_Design = Transition(label='System Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Light_Setup = Transition(label='Light Setup')
Climate_Sync = Transition(label='Climate Sync')
Crop_Select = Transition(label='Crop Select')
Sensor_Deploy = Transition(label='Sensor Deploy')
Staff_Train = Transition(label='Staff Train')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Waste_Cycle = Transition(label='Waste Cycle')
Data_Analyze = Transition(label='Data Analyze')
Optimize_Run = Transition(label='Optimize Run')

# Build partial order based on logically implied sequence from description

# Structural & environmental analysis phase
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structure_Test, Impact_Review])
phase1.order.add_edge(Site_Survey, Structure_Test)
phase1.order.add_edge(Structure_Test, Impact_Review)

# System design and setup phase
phase2 = StrictPartialOrder(nodes=[System_Design, Nutrient_Mix, Light_Setup, Climate_Sync])
phase2.order.add_edge(System_Design, Nutrient_Mix)
phase2.order.add_edge(Nutrient_Mix, Light_Setup)
phase2.order.add_edge(Light_Setup, Climate_Sync)

# Crop preparation and sensor deployment phase (can start after system design)
phase3 = StrictPartialOrder(nodes=[Crop_Select, Sensor_Deploy])
phase3.order.add_edge(Crop_Select, Sensor_Deploy)

# Staff training and community engagement in parallel, but after sensors deployed
phase4 = StrictPartialOrder(nodes=[Staff_Train, Community_Meet])
# No order between these two (concurrent)

# Regulatory, waste, data, and optimization phases in sequence
phase5 = StrictPartialOrder(nodes=[Compliance_Check, Waste_Cycle, Data_Analyze, Optimize_Run])
phase5.order.add_edge(Compliance_Check, Waste_Cycle)
phase5.order.add_edge(Waste_Cycle, Data_Analyze)
phase5.order.add_edge(Data_Analyze, Optimize_Run)

# Combine phases in a global partial order
# Start with phase1 --> phase2
# phase3 can start after System_Design (part of phase2)
# phase4 after phase3
# phase5 after phase4

# Create a root partial order containing all phases and add edges between them accordingly

nodes = [Site_Survey, Structure_Test, Impact_Review,
         System_Design, Nutrient_Mix, Light_Setup, Climate_Sync,
         Crop_Select, Sensor_Deploy,
         Staff_Train, Community_Meet,
         Compliance_Check, Waste_Cycle, Data_Analyze, Optimize_Run]

root = StrictPartialOrder(nodes=nodes)

# Add intra-phase edges for phase1
root.order.add_edge(Site_Survey, Structure_Test)
root.order.add_edge(Structure_Test, Impact_Review)

# Add intra-phase edges for phase2
root.order.add_edge(System_Design, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Light_Setup)
root.order.add_edge(Light_Setup, Climate_Sync)

# Add intra-phase edges for phase3
root.order.add_edge(Crop_Select, Sensor_Deploy)

# phase4 concurrency means no edges between Staff_Train and Community_Meet

# Add intra-phase edges for phase5
root.order.add_edge(Compliance_Check, Waste_Cycle)
root.order.add_edge(Waste_Cycle, Data_Analyze)
root.order.add_edge(Data_Analyze, Optimize_Run)

# Add inter-phase edges
# phase1 -> phase2: last of phase1 to first of phase2
root.order.add_edge(Impact_Review, System_Design)

# phase2 -> phase3: System_Design (phase2) -> Crop_Select (phase3)
root.order.add_edge(System_Design, Crop_Select)

# phase3 -> phase4: Sensor_Deploy -> Staff_Train and Sensor_Deploy -> Community_Meet
root.order.add_edge(Sensor_Deploy, Staff_Train)
root.order.add_edge(Sensor_Deploy, Community_Meet)

# phase4 -> phase5: both Staff_Train and Community_Meet -> Compliance_Check
root.order.add_edge(Staff_Train, Compliance_Check)
root.order.add_edge(Community_Meet, Compliance_Check)