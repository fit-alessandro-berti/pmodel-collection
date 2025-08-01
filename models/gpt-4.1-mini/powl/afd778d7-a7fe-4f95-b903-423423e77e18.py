# Generated from: afd778d7-a7fe-4f95-b903-423423e77e18.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban rooftop farm on a commercial building. It begins with structural assessment and environmental analysis, followed by sourcing sustainable materials and soil alternatives. The process includes modular bed assembly, installation of automated irrigation systems, and integration of renewable energy sources. Crop selection is based on microclimate data and market demand, with seed procurement aligned accordingly. Subsequent activities cover planting schedules, pest management using organic methods, and periodic nutrient supplementation. The farm incorporates real-time monitoring via IoT sensors, data analysis for yield optimization, and community engagement initiatives to promote urban agriculture awareness. Finally, harvest logistics and distribution channels are managed to ensure fresh produce reaches local markets efficiently, completing a cycle that supports sustainability and urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Assess_Structure = Transition(label='Assess Structure')
Analyze_Climate = Transition(label='Analyze Climate')
Source_Materials = Transition(label='Source Materials')
Prepare_Soil = Transition(label='Prepare Soil')
Assemble_Beds = Transition(label='Assemble Beds')
Install_Irrigation = Transition(label='Install Irrigation')
Set_Energy = Transition(label='Set Energy')
Select_Crops = Transition(label='Select Crops')
Procure_Seeds = Transition(label='Procure Seeds')
Schedule_Planting = Transition(label='Schedule Planting')
Manage_Pests = Transition(label='Manage Pests')
Supplement_Nutrients = Transition(label='Supplement Nutrients')
Monitor_Sensors = Transition(label='Monitor Sensors')
Analyze_Data = Transition(label='Analyze Data')
Engage_Community = Transition(label='Engage Community')
Plan_Harvest = Transition(label='Plan Harvest')
Distribute_Produce = Transition(label='Distribute Produce')

# Build the partial order according to the description
# Step 1: Assess Structure and Analyze Climate in sequence
# Step 2: Source Materials and Prepare Soil are sequential, both depend on Analyze Climate
# Step 3: Assemble Beds after Prepare Soil
# Step 4: Install Irrigation and Set Energy concurrent after Assemble Beds
# Step 5: Select Crops after Analyze Climate and Source Materials
# Step 6: Procure Seeds after Select Crops
# Step 7: Schedule Planting after Procure Seeds
# Step 8: Manage Pests and Supplement Nutrients in sequence after Schedule Planting
# Step 9: Monitor Sensors, Analyze Data, Engage Community concurrent after Supplement Nutrients and Manage Pests
# Step 10: Plan Harvest after Analyze Data and Engage Community
# Step 11: Distribute Produce after Plan Harvest

root = StrictPartialOrder(nodes=[
    Assess_Structure,
    Analyze_Climate,
    Source_Materials,
    Prepare_Soil,
    Assemble_Beds,
    Install_Irrigation,
    Set_Energy,
    Select_Crops,
    Procure_Seeds,
    Schedule_Planting,
    Manage_Pests,
    Supplement_Nutrients,
    Monitor_Sensors,
    Analyze_Data,
    Engage_Community,
    Plan_Harvest,
    Distribute_Produce
])

# Add edges according to dependencies
root.order.add_edge(Assess_Structure, Analyze_Climate)

root.order.add_edge(Analyze_Climate, Source_Materials)
root.order.add_edge(Analyze_Climate, Prepare_Soil)

root.order.add_edge(Prepare_Soil, Assemble_Beds)

root.order.add_edge(Assemble_Beds, Install_Irrigation)
root.order.add_edge(Assemble_Beds, Set_Energy)

root.order.add_edge(Analyze_Climate, Select_Crops)
root.order.add_edge(Source_Materials, Select_Crops)

root.order.add_edge(Select_Crops, Procure_Seeds)

root.order.add_edge(Procure_Seeds, Schedule_Planting)

root.order.add_edge(Schedule_Planting, Manage_Pests)
root.order.add_edge(Manage_Pests, Supplement_Nutrients)

root.order.add_edge(Supplement_Nutrients, Monitor_Sensors)
root.order.add_edge(Manage_Pests, Monitor_Sensors)

root.order.add_edge(Supplement_Nutrients, Analyze_Data)
root.order.add_edge(Manage_Pests, Analyze_Data)

root.order.add_edge(Supplement_Nutrients, Engage_Community)
root.order.add_edge(Manage_Pests, Engage_Community)

root.order.add_edge(Analyze_Data, Plan_Harvest)
root.order.add_edge(Engage_Community, Plan_Harvest)

root.order.add_edge(Plan_Harvest, Distribute_Produce)