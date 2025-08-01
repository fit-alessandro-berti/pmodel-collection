# Generated from: 778cb7b4-3125-47f0-89a0-37031c55e91b.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It covers site assessment, modular rack installation, environmental control calibration, hydroponic nutrient solution preparation, seedling propagation, automated monitoring setup, and integration with local food distribution networks. The process requires coordination between agricultural experts, engineers, and logistics teams to ensure sustainable crop yield, energy efficiency, and rapid market delivery. Continuous data analysis and system optimization follow initial deployment to adapt to seasonal variations and urban constraints, maximizing productivity within limited space while minimizing resource consumption and waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Rack_Setup = Transition(label='Rack Setup')
Lighting_Install = Transition(label='Lighting Install')
Env_Calibration = Transition(label='Env Calibration')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seedling_Plant = Transition(label='Seedling Plant')
Sensor_Deploy = Transition(label='Sensor Deploy')
System_Sync = Transition(label='System Sync')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Link = Transition(label='Market Link')
Waste_Manage = Transition(label='Waste Manage')
Data_Review = Transition(label='Data Review')
Energy_Audit = Transition(label='Energy Audit')

# Stage 1: Site assessment and structural check (sequential)
stage1 = StrictPartialOrder(nodes=[Site_Survey, Structural_Check])
stage1.order.add_edge(Site_Survey, Structural_Check)

# Stage 2: Modular rack installation and lighting install in parallel, but both after structural check
stage2 = StrictPartialOrder(nodes=[Rack_Setup, Lighting_Install])
# no order inside stage2, they are concurrent

# Stage 3: Environmental calibration after lighting install
stage3 = Env_Calibration

# Stage 4: Hydroponic nutrient solution and water testing in parallel
stage4 = StrictPartialOrder(nodes=[Water_Testing, Nutrient_Mix])
# no order inside stage4, concurrent

# Stage 5: Seedling propagation after nutrient and water testing
stage5 = Seedling_Plant

# Stage 6: Automated monitoring setup (sensor deploy + system sync sequential)
stage6 = StrictPartialOrder(nodes=[Sensor_Deploy, System_Sync])
stage6.order.add_edge(Sensor_Deploy, System_Sync)

# Stage 7: Growth monitor and pest inspect in parallel after system sync
stage7 = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Inspect])
# no order inside stage7, concurrent

# Stage 8: Harvest planning and packaging prep sequential
stage8 = StrictPartialOrder(nodes=[Harvest_Plan, Packaging_Prep])
stage8.order.add_edge(Harvest_Plan, Packaging_Prep)

# Stage 9: Market link and waste manage concurrent after packaging prep
stage9 = StrictPartialOrder(nodes=[Market_Link, Waste_Manage])
# no order inside stage9, concurrent

# Stage 10: Continuous data review and energy audit loop after initial deployment
# Loop: Execute (Data Review and Energy Audit) and then choose to exit or repeat
loop_body = StrictPartialOrder(nodes=[Data_Review, Energy_Audit])
loop_body.order.add_edge(Data_Review, Energy_Audit)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Construct the overall partial order by stages:

# Define compound sequential stages as nodes
# We'll create compound nodes for stages where needed

# Stage 2 + stage3 + stage4 + stage5 + stage6 + stage7 + stage8 + stage9 as one compound partial order to simplify
# Stage 2 after stage1.structural check, Stage3 after lighting install (part of stage2), and so on.

# For ordering, key transitions:
# Structural_Check -> Rack_Setup & Lighting_Install (stage2 concurrent nodes)
# Lighting_Install -> Env_Calibration (stage3)
# Env_Calibration -> Water_Testing & Nutrient_Mix (stage4 concurrent)
# Water_Testing & Nutrient_Mix -> Seedling_Plant (stage5)
# Seedling_Plant -> Sensor_Deploy (stage6)
# System_Sync after Sensor_Deploy (stage6)
# System_Sync -> Growth_Monitor & Pest_Inspect (stage7 concurrent)
# Growth_Monitor & Pest_Inspect -> Harvest_Plan (stage8)
# Harvest_Plan -> Packaging_Prep (stage8)
# Packaging_Prep -> Market_Link & Waste_Manage (stage9 concurrent)
# Market_Link & Waste_Manage -> loop (continuous data review and energy audit)

# To capture this precisely, break down as a StrictPartialOrder with all involved nodes

all_nodes = [
    Site_Survey, Structural_Check, Rack_Setup, Lighting_Install, Env_Calibration,
    Water_Testing, Nutrient_Mix, Seedling_Plant,
    Sensor_Deploy, System_Sync, Growth_Monitor, Pest_Inspect,
    Harvest_Plan, Packaging_Prep, Market_Link, Waste_Manage,
    loop
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for the flows described:

# Stage 1
root.order.add_edge(Site_Survey, Structural_Check)

# Stage 1 to Stage 2
root.order.add_edge(Structural_Check, Rack_Setup)
root.order.add_edge(Structural_Check, Lighting_Install)  # concurrent after structural check

# Stage 2 to Stage 3
root.order.add_edge(Lighting_Install, Env_Calibration)
# Rack_Setup and Env_Calibration can be concurrent since no direct dependency between Rack_Setup and Env_Calibration stated

# Stage 3 to Stage 4
root.order.add_edge(Env_Calibration, Water_Testing)
root.order.add_edge(Env_Calibration, Nutrient_Mix)

# Stage 4 to Stage 5
root.order.add_edge(Water_Testing, Seedling_Plant)
root.order.add_edge(Nutrient_Mix, Seedling_Plant)

# Stage 5 to Stage 6
root.order.add_edge(Seedling_Plant, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, System_Sync)

# Stage 6 to Stage 7
root.order.add_edge(System_Sync, Growth_Monitor)
root.order.add_edge(System_Sync, Pest_Inspect)  # concurrent after system sync

# Stage 7 to Stage 8
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(Pest_Inspect, Harvest_Plan)

root.order.add_edge(Harvest_Plan, Packaging_Prep)

# Stage 8 to Stage 9
root.order.add_edge(Packaging_Prep, Market_Link)
root.order.add_edge(Packaging_Prep, Waste_Manage)  # concurrent after packaging prep

# Stage 9 to loop (continuous optimization)
root.order.add_edge(Market_Link, loop)
root.order.add_edge(Waste_Manage, loop)

# Final model in 'root'