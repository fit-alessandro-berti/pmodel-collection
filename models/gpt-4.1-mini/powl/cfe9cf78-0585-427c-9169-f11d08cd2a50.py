# Generated from: cfe9cf78-0585-427c-9169-f11d08cd2a50.json
# Description: This process outlines the end-to-end setup and operational launch of an urban vertical farming facility. It begins with site analysis and environmental assessment, followed by modular system design tailored to urban constraints. Procurement of specialized hydroponic equipment and organic seeds is followed by installation, calibration, and testing of climate control systems. Staff training emphasizes sustainable farming techniques and technology use. Once operational, crop cycles are monitored through IoT sensors, with data analytics optimizing nutrient delivery and light exposure. Regular maintenance and pest management ensure crop health, while direct-to-consumer logistics and marketing strategies complete the process, ensuring fresh produce efficiently reaches urban markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Analysis = Transition(label='Site Analysis')
Env_Assessment = Transition(label='Env Assessment')
System_Design = Transition(label='System Design')
Equipment_Order = Transition(label='Equipment Order')
Seed_Selection = Transition(label='Seed Selection')
Install_Modules = Transition(label='Install Modules')
Calibrate_Systems = Transition(label='Calibrate Systems')
Staff_Training = Transition(label='Staff Training')
Plant_Seeding = Transition(label='Plant Seeding')
IoT_Monitoring = Transition(label='IoT Monitoring')
Data_Analytics = Transition(label='Data Analytics')
Nutrient_Adjust = Transition(label='Nutrient Adjust')
Pest_Control = Transition(label='Pest Control')
Maintenance_Check = Transition(label='Maintenance Check')
Market_Launch = Transition(label='Market Launch')
Logistics_Setup = Transition(label='Logistics Setup')

# Phase 1: Initial Analysis
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Env_Assessment])
phase1.order.add_edge(Site_Analysis, Env_Assessment)

# Phase 2: Design (after analysis)
phase2 = StrictPartialOrder(nodes=[System_Design])
# no internal order, single activity

# Phase 3: Procurement (Equipment Order and Seed Selection concurrent)
phase3 = StrictPartialOrder(nodes=[Equipment_Order, Seed_Selection])
# no edges, they happen concurrently

# Phase 4: Installation & Calibration
phase4 = StrictPartialOrder(nodes=[Install_Modules, Calibrate_Systems])
phase4.order.add_edge(Install_Modules, Calibrate_Systems)

# Phase 5: Staff Training (after install & calib)
phase5 = StrictPartialOrder(nodes=[Staff_Training])

# Phase 6: Planting
phase6 = StrictPartialOrder(nodes=[Plant_Seeding])

# Phase 7: Monitoring & Analysis loop of IoT Monitoring then Data Analytics then Nutrient Adjust
# This is logically a loop: 
# Execute IoT Monitoring, then loop on Data Analytics + Nutrient Adjust repeating until done

# To model the loop, break down:
# Loop body: B = PO(Data Analytics, Nutrient Adjust)
# A = IoT Monitoring
# Loop = *(A,B)

B_monitoring_loop = StrictPartialOrder(nodes=[Data_Analytics, Nutrient_Adjust])
# no order between Data Analytics and Nutrient Adjust - assume concurrent; 
# if logic suggests order, can add edge (e.g. Data Analytics -> Nutrient Adjust)
# Ordering Nutrient Adjust depends on Data Analytics results, so Data Analytics --> Nutrient Adjust
B_monitoring_loop.order.add_edge(Data_Analytics, Nutrient_Adjust)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[IoT_Monitoring, B_monitoring_loop])

# Phase 8: Maintenance and Pest Control parallel after monitoring loop
phase8 = StrictPartialOrder(nodes=[Pest_Control, Maintenance_Check])
# no order between Pest Control and Maintenance Check, assume concurrent

# Phase 9: Market Launch and Logistics Setup concurrent after maintenance
phase9 = StrictPartialOrder(nodes=[Market_Launch, Logistics_Setup])
# no order assumed

# Now build the overall partial order linking phases with proper ordering edges:
# Sequence: phase1 -> phase2 -> phase3 -> phase4 -> phase5 -> phase6 -> monitoring_loop -> phase8 -> phase9

root = StrictPartialOrder(
    nodes=[
        phase1, phase2, phase3, phase4, phase5, phase6, monitoring_loop, phase8, phase9
    ]
)

# Add edges between phases (these edges create partial order between phase modules)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, monitoring_loop)
root.order.add_edge(monitoring_loop, phase8)
root.order.add_edge(phase8, phase9)