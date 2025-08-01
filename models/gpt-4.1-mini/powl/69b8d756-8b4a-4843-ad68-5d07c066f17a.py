# Generated from: 69b8d756-8b4a-4843-ad68-5d07c066f17a.json
# Description: This process outlines the complex and multidisciplinary steps required to establish a sustainable urban rooftop farm. It involves site assessment, structural analysis, soil preparation, ecosystem integration, irrigation system design, seed selection, crop rotation planning, pest management, community engagement, and ongoing monitoring to ensure optimal yield and environmental benefits. The process also incorporates regulatory compliance, safety measures, and logistics coordination for material delivery and waste management, reflecting the unique challenges of transforming urban spaces into productive agricultural sites.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Mix = Transition(label='Soil Mix')
Irrigation_Plan = Transition(label='Irrigation Plan')
Seed_Selection = Transition(label='Seed Selection')
Planting_Grid = Transition(label='Planting Grid')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Schedule = Transition(label='Harvest Schedule')
Waste_Removal = Transition(label='Waste Removal')
Tool_Sterilize = Transition(label='Tool Sterilize')
Water_Testing = Transition(label='Water Testing')
Community_Meet = Transition(label='Community Meet')
Regulation_Check = Transition(label='Regulation Check')
Safety_Drill = Transition(label='Safety Drill')
Logistics_Setup = Transition(label='Logistics Setup')
Crop_Rotation = Transition(label='Crop Rotation')

# Construct partial order for initial assessments and preparation steps
# Site Survey -> Load Test -> Soil Mix
# Soil Mix -> Water Testing (soil quality)
# Then branching into irrigation plan and seed selection in parallel (no order)
# Additionally, Regulation Check and Safety Drill can happen after Load Test in parallel
# Logistics Setup occurs after Safety Drill and Regulation Check

# Growth and plant related steps: Seed Selection -> Planting Grid -> Pest Control -> Growth Monitor
# Crop Rotation plans follow Growth Monitor -> Harvest Schedule
# Waste Removal and Tool Sterilize happen after Harvest Schedule
# Community Meet can happen concurrently after Planting Grid
# Irrigation_Plan happens concurrent with Seed Selection

root = StrictPartialOrder(nodes=[
    Site_Survey, Load_Test, Soil_Mix, Water_Testing, 
    Irrigation_Plan, Seed_Selection, Planting_Grid, Pest_Control, Growth_Monitor, Crop_Rotation,
    Harvest_Schedule, Waste_Removal, Tool_Sterilize, Community_Meet,
    Regulation_Check, Safety_Drill, Logistics_Setup
])

# add edges for serial dependencies
root.order.add_edge(Site_Survey, Load_Test)
root.order.add_edge(Load_Test, Soil_Mix)
root.order.add_edge(Soil_Mix, Water_Testing)

# Regulation and safety after Load Test (concurrent)
root.order.add_edge(Load_Test, Regulation_Check)
root.order.add_edge(Load_Test, Safety_Drill)

# Logistics after regulation and safety (both must complete before logistics)
root.order.add_edge(Regulation_Check, Logistics_Setup)
root.order.add_edge(Safety_Drill, Logistics_Setup)

# Irrigation and Seed Selection depend on Soil Mix (and Water Testing done)
root.order.add_edge(Soil_Mix, Irrigation_Plan)
root.order.add_edge(Soil_Mix, Seed_Selection)
root.order.add_edge(Water_Testing, Irrigation_Plan)
root.order.add_edge(Water_Testing, Seed_Selection)

# Planting Grid after Seed Selection
root.order.add_edge(Seed_Selection, Planting_Grid)

# Community Meet can happen after Planting Grid (engagement)
root.order.add_edge(Planting_Grid, Community_Meet)

# Pest Control after Planting Grid
root.order.add_edge(Planting_Grid, Pest_Control)

# Growth Monitor after Pest Control
root.order.add_edge(Pest_Control, Growth_Monitor)

# Crop Rotation after Growth Monitor
root.order.add_edge(Growth_Monitor, Crop_Rotation)

# Harvest Schedule after Crop Rotation
root.order.add_edge(Crop_Rotation, Harvest_Schedule)

# Waste Removal and Tool Sterilize after Harvest Schedule (parallel)
root.order.add_edge(Harvest_Schedule, Waste_Removal)
root.order.add_edge(Harvest_Schedule, Tool_Sterilize)