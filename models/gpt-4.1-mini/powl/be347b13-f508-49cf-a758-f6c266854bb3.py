# Generated from: be347b13-f508-49cf-a758-f6c266854bb3.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, modular system installation, nutrient solution calibration, environmental control programming, crop selection based on market trends, integration of robotics for planting and harvesting, real-time data monitoring for growth optimization, waste recycling protocols, and supply chain coordination for distribution. The process ensures sustainability, maximizes yield in limited space, and adapts dynamically to urban agricultural demands while complying with city regulations and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Module_Setup = Transition(label='Module Setup')
Nutrient_Prep = Transition(label='Nutrient Prep')
Env_Control = Transition(label='Env Control')
Crop_Selection = Transition(label='Crop Selection')
Sensor_Install = Transition(label='Sensor Install')
Robot_Config = Transition(label='Robot Config')
Plant_Seeding = Transition(label='Plant Seeding')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Market_Sync = Transition(label='Market Sync')
Logistics_Prep = Transition(label='Logistics Prep')

# Phase 1: Site survey leads to design and setup phases
# Site Survey --> System Design --> Module Setup
phase1 = StrictPartialOrder(nodes=[Site_Survey, System_Design, Module_Setup])
phase1.order.add_edge(Site_Survey, System_Design)
phase1.order.add_edge(System_Design, Module_Setup)

# Phase 2: Nutrient prep and env control run in parallel after Module Setup
# Module Setup --> Nutrient Prep and Env Control (concurrent)
phase2 = StrictPartialOrder(nodes=[Module_Setup, Nutrient_Prep, Env_Control])
phase2.order.add_edge(Module_Setup, Nutrient_Prep)
phase2.order.add_edge(Module_Setup, Env_Control)

# Phase 3: Crop Selection depends on completed design & setup, concurrent with Sensor install and Robot config
# Crop Selection --> (Sensor Install + Robot Config) concurrent
phase3 = StrictPartialOrder(nodes=[Crop_Selection, Sensor_Install, Robot_Config])
# Crop Selection leads to Sensor Install and Robot Config concurrently
phase3.order.add_edge(Crop_Selection, Sensor_Install)
phase3.order.add_edge(Crop_Selection, Robot_Config)

# Phase 4: After Sensor Install and Robot Config, Plant Seeding occurs
# Sensor Install --> Plant Seeding
# Robot Config --> Plant Seeding
phase4 = StrictPartialOrder(nodes=[Sensor_Install, Robot_Config, Plant_Seeding])
phase4.order.add_edge(Sensor_Install, Plant_Seeding)
phase4.order.add_edge(Robot_Config, Plant_Seeding)

# Phase 5: Growth monitoring and waste recycling run concurrently after Plant Seeding and Nutrient Prep
# Plant Seeding and Nutrient Prep --> Growth Monitor and Waste Recycle concurrently
phase5 = StrictPartialOrder(nodes=[Plant_Seeding, Nutrient_Prep, Growth_Monitor, Waste_Recycle])
phase5.order.add_edge(Plant_Seeding, Growth_Monitor)
phase5.order.add_edge(Plant_Seeding, Waste_Recycle)
phase5.order.add_edge(Nutrient_Prep, Growth_Monitor)
phase5.order.add_edge(Nutrient_Prep, Waste_Recycle)

# Phase 6: Data Analysis after Growth Monitor
phase6 = StrictPartialOrder(nodes=[Growth_Monitor, Data_Analysis])
phase6.order.add_edge(Growth_Monitor, Data_Analysis)

# Phase 7: Harvest Planning and Quality Check after Data Analysis and Waste Recycling
# Both Data Analysis and Waste Recycle lead to Harvest Plan
phase7 = StrictPartialOrder(nodes=[Data_Analysis, Waste_Recycle, Harvest_Plan, Quality_Check])
phase7.order.add_edge(Data_Analysis, Harvest_Plan)
phase7.order.add_edge(Waste_Recycle, Harvest_Plan)
# Harvest Plan leads to Quality Check
phase7.order.add_edge(Harvest_Plan, Quality_Check)

# Phase 8: Market sync and logistics prep after Quality Check and Crop Selection
# Quality Check and Crop Selection --> Market Sync --> Logistics Prep
phase8 = StrictPartialOrder(
    nodes=[Quality_Check, Crop_Selection, Market_Sync, Logistics_Prep]
)
phase8.order.add_edge(Quality_Check, Market_Sync)
phase8.order.add_edge(Crop_Selection, Market_Sync)
phase8.order.add_edge(Market_Sync, Logistics_Prep)

# Compose the full process in partial order
# Connect phases respecting their dependencies:
# phase1 -> phase2 -> phase3 -> phase4 -> phase5 -> phase6 -> phase7 -> phase8

# We'll put all nodes and edges together in a single StrictPartialOrder:

all_nodes = [
    Site_Survey, System_Design, Module_Setup, Nutrient_Prep, Env_Control,
    Crop_Selection, Sensor_Install, Robot_Config, Plant_Seeding,
    Growth_Monitor, Waste_Recycle, Data_Analysis, Harvest_Plan,
    Quality_Check, Market_Sync, Logistics_Prep
]

root = StrictPartialOrder(nodes=all_nodes)

# Phase 1 edges
root.order.add_edge(Site_Survey, System_Design)
root.order.add_edge(System_Design, Module_Setup)

# Phase 2 edges
root.order.add_edge(Module_Setup, Nutrient_Prep)
root.order.add_edge(Module_Setup, Env_Control)

# Phase 3 edges
root.order.add_edge(Crop_Selection, Sensor_Install)
root.order.add_edge(Crop_Selection, Robot_Config)

# The connection from Phase1/2 to Phase3: Crop Selection depends on System Design and Module Setup completion
root.order.add_edge(Module_Setup, Crop_Selection)
root.order.add_edge(System_Design, Crop_Selection)

# Phase 4 edges
root.order.add_edge(Sensor_Install, Plant_Seeding)
root.order.add_edge(Robot_Config, Plant_Seeding)

# Phase 5 edges
root.order.add_edge(Plant_Seeding, Growth_Monitor)
root.order.add_edge(Plant_Seeding, Waste_Recycle)
root.order.add_edge(Nutrient_Prep, Growth_Monitor)
root.order.add_edge(Nutrient_Prep, Waste_Recycle)

# Phase 6 edges
root.order.add_edge(Growth_Monitor, Data_Analysis)

# Phase 7 edges
root.order.add_edge(Data_Analysis, Harvest_Plan)
root.order.add_edge(Waste_Recycle, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Quality_Check)

# Phase 8 edges
root.order.add_edge(Quality_Check, Market_Sync)
root.order.add_edge(Crop_Selection, Market_Sync)
root.order.add_edge(Market_Sync, Logistics_Prep)