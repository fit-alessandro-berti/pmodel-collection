# Generated from: 670ae353-6fb7-453a-b125-b305a747eb14.json
# Description: This process outlines the establishment of a vertical urban farm within a repurposed industrial building, integrating advanced hydroponics, IoT monitoring, and renewable energy systems. It begins with site evaluation and structural assessment, followed by modular rack installation and environment calibration. Subsequent steps include nutrient solution formulation, seed selection, and automated planting. Continuous monitoring leverages sensor data for climate adjustments and pest detection, while energy management optimizes solar and battery usage. Harvest scheduling coordinates with local distribution logistics. The process concludes with waste recycling and system maintenance planning, ensuring sustainability and scalability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Rack_Install = Transition(label='Rack Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Automated_Plant = Transition(label='Automated Plant')
Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Monitor = Transition(label='Data Monitor')
Pest_Detect = Transition(label='Pest Detect')
Energy_Balance = Transition(label='Energy Balance')
Harvest_Plan = Transition(label='Harvest Plan')
Logistics_Sync = Transition(label='Logistics Sync')
Waste_Process = Transition(label='Waste Process')
System_Review = Transition(label='System Review')

# Build partial orders based on the process description

# 1) Site evaluation and structural assessment sequential
site_eval = StrictPartialOrder(nodes=[Site_Survey, Structure_Check])
site_eval.order.add_edge(Site_Survey, Structure_Check)

# 2) Modular rack installation and environment calibration sequential after structure check
install_and_calibrate = StrictPartialOrder(nodes=[Rack_Install, Climate_Setup])
install_and_calibrate.order.add_edge(Rack_Install, Climate_Setup)

# Link site eval to install_and_calibrate
phase1 = StrictPartialOrder(nodes=[site_eval, install_and_calibrate])
phase1.order.add_edge(site_eval, install_and_calibrate)

# 3) Nutrient solution formulation, seed selection, automated planting sequential after calibration
planting_sequence = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Selection, Automated_Plant])
planting_sequence.order.add_edge(Nutrient_Mix, Seed_Selection)
planting_sequence.order.add_edge(Seed_Selection, Automated_Plant)

# Link install_and_calibrate to planting_sequence
phase2 = StrictPartialOrder(nodes=[phase1, planting_sequence])
phase2.order.add_edge(phase1, planting_sequence)

# 4) Continuous monitoring with sensor deploy, data monitor, pest detect - all sequential after automated planting
monitoring_sequence = StrictPartialOrder(nodes=[Sensor_Deploy, Data_Monitor, Pest_Detect])
monitoring_sequence.order.add_edge(Sensor_Deploy, Data_Monitor)
monitoring_sequence.order.add_edge(Data_Monitor, Pest_Detect)

# 5) Energy management (Energy Balance) can be concurrent with monitoring
# So parallel nodes: monitoring_sequence and Energy_Balance
monitoring_and_energy = StrictPartialOrder(nodes=[monitoring_sequence, Energy_Balance])
# no order edges - concurrency

# Link planting_sequence to monitoring_and_energy
phase3 = StrictPartialOrder(nodes=[phase2, monitoring_and_energy])
phase3.order.add_edge(phase2, monitoring_and_energy)

# 6) Harvest scheduling and local distribution logistics sequential after monitoring and energy management
harvest_and_logistics = StrictPartialOrder(nodes=[Harvest_Plan, Logistics_Sync])
harvest_and_logistics.order.add_edge(Harvest_Plan, Logistics_Sync)

# Link monitoring_and_energy to harvest_and_logistics
phase4 = StrictPartialOrder(nodes=[phase3, harvest_and_logistics])
phase4.order.add_edge(phase3, harvest_and_logistics)

# 7) Waste recycling and system maintenance planning sequential after logistics sync
closing_sequence = StrictPartialOrder(nodes=[Waste_Process, System_Review])
closing_sequence.order.add_edge(Waste_Process, System_Review)

# Link harvest_and_logistics to closing_sequence
root = StrictPartialOrder(nodes=[phase4, closing_sequence])
root.order.add_edge(phase4, closing_sequence)