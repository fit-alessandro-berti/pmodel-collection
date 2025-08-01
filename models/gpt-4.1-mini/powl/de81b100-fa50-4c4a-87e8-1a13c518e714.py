# Generated from: de81b100-fa50-4c4a-87e8-1a13c518e714.json
# Description: This process describes the establishment of a sustainable urban vertical farming system within a repurposed city warehouse. It involves steps such as environmental assessment, modular rack design, nutrient solution formulation, automated lighting calibration, and integration of IoT sensors for real-time monitoring. The process also includes obtaining necessary permits, recruiting specialized agronomists, establishing supply chains for organic seeds, implementing waste recycling protocols, and training staff on hydroponic and aeroponic techniques. The goal is to create a scalable, energy-efficient food production system that reduces urban food deserts and promotes local sourcing with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Site_Survey = Transition(label='Site Survey')
Permit_Acquire = Transition(label='Permit Acquire')
Rack_Design = Transition(label='Rack Design')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Setup = Transition(label='Lighting Setup')
Sensor_Install = Transition(label='Sensor Install')
System_Test = Transition(label='System Test')
Staff_Hire = Transition(label='Staff Hire')
Training_Lead = Transition(label='Training Lead')
Waste_Manage = Transition(label='Waste Manage')
Supply_Chain = Transition(label='Supply Chain')
Crop_Cycle = Transition(label='Crop Cycle')
Data_Monitor = Transition(label='Data Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Distribution = Transition(label='Distribution')

# Phase 1: Initial assessments and permits (Site Survey then Permit Acquire)
initial_phase = StrictPartialOrder(nodes=[Site_Survey, Permit_Acquire])
initial_phase.order.add_edge(Site_Survey, Permit_Acquire)

# Phase 2: Design and preparation (Rack Design and Seed Selection can be concurrent, but both before Nutrient Mix)
design_seed_phase = StrictPartialOrder(nodes=[Rack_Design, Seed_Selection, Nutrient_Mix])
design_seed_phase.order.add_edge(Rack_Design, Nutrient_Mix)
design_seed_phase.order.add_edge(Seed_Selection, Nutrient_Mix)

# Phase 3: Setup and installation (Lighting Setup and Sensor Install can be concurrent, both before System Test)
setup_phase = StrictPartialOrder(nodes=[Lighting_Setup, Sensor_Install, System_Test])
setup_phase.order.add_edge(Lighting_Setup, System_Test)
setup_phase.order.add_edge(Sensor_Install, System_Test)

# Phase 4: Staffing and training (Staff Hire before Training Lead)
staff_phase = StrictPartialOrder(nodes=[Staff_Hire, Training_Lead])
staff_phase.order.add_edge(Staff_Hire, Training_Lead)

# Phase 5: Waste management and supply chain can be concurrent with staffing/training
waste_supply_phase = StrictPartialOrder(nodes=[Waste_Manage, Supply_Chain])

# Phase 6: Crop cycle loop with monitoring and harvest planning
# Loop definition: 
# A = Crop Cycle (main activity)
# B = Data Monitor + Harvest Plan in partial order before looping back

data_and_harvest = StrictPartialOrder(nodes=[Data_Monitor, Harvest_Plan])
data_and_harvest.order.add_edge(Data_Monitor, Harvest_Plan)

loop_crop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Cycle, data_and_harvest])

# Phase 7: Distribution after loop completed
# Distribution happens after loop_crop finishes

# Compose everything into main partial order

# All phases to be ordered according to a natural process flow:
# initial_phase -> design_seed_phase -> setup_phase -> staff_phase & waste_supply_phase (concurrent) -> loop_crop -> Distribution

# Merge staff_phase and waste_supply_phase concurrently
staff_and_waste = StrictPartialOrder(nodes=[staff_phase, waste_supply_phase])

# Build main model nodes
nodes = [
    initial_phase,
    design_seed_phase,
    setup_phase,
    staff_and_waste,
    loop_crop,
    Distribution
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges between phases
root.order.add_edge(initial_phase, design_seed_phase)
root.order.add_edge(design_seed_phase, setup_phase)
root.order.add_edge(setup_phase, staff_and_waste)
root.order.add_edge(staff_and_waste, loop_crop)
root.order.add_edge(loop_crop, Distribution)