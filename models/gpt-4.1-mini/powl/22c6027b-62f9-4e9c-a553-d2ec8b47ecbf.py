# Generated from: 22c6027b-62f9-4e9c-a553-d2ec8b47ecbf.json
# Description: This process outlines an adaptive urban farming cycle designed to optimize crop yield within constrained city environments by integrating real-time environmental monitoring, dynamic resource allocation, and community engagement. Initially, sensor data is collected and analyzed to determine microclimate variations. Based on these insights, planting schedules and nutrient delivery are adjusted dynamically to suit specific crop requirements. Community volunteers participate in maintenance and harvesting, while waste products undergo bio-conversion to generate compost and energy. The entire system undergoes continuous feedback loops involving AI-driven predictions and manual expert interventions, ensuring sustainable production, minimal waste, and enhanced social cohesion in urban neighborhoods.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Capture = Transition(label='Data Capture')
Microclimate_Map = Transition(label='Microclimate Map')
Analyze_Trends = Transition(label='Analyze Trends')
Adjust_Schedule = Transition(label='Adjust Schedule')
Allocate_Nutrients = Transition(label='Allocate Nutrients')
Plant_Crops = Transition(label='Plant Crops')
Volunteer_Brief = Transition(label='Volunteer Brief')
Maintenance_Round = Transition(label='Maintenance Round')
Harvest_Crops = Transition(label='Harvest Crops')
Waste_Collect = Transition(label='Waste Collect')
Bio_Convert_Waste = Transition(label='Bio-Convert Waste')
Compost_Apply = Transition(label='Compost Apply')
Energy_Store = Transition(label='Energy Store')
Feedback_Review = Transition(label='Feedback Review')
Expert_Consult = Transition(label='Expert Consult')

# Construct community tasks partial order (Volunteer Brief -> Maintenance Round & Harvest Crops concurrent)
community_po = StrictPartialOrder(nodes=[Volunteer_Brief, Maintenance_Round, Harvest_Crops])
community_po.order.add_edge(Volunteer_Brief, Maintenance_Round)
community_po.order.add_edge(Volunteer_Brief, Harvest_Crops)

# Construct waste processing partial order (Waste Collect -> Bio-Convert Waste -> Compost Apply and Energy Store concurrent)
waste_processing_po = StrictPartialOrder(
    nodes=[Waste_Collect, Bio_Convert_Waste, Compost_Apply, Energy_Store])
waste_processing_po.order.add_edge(Waste_Collect, Bio_Convert_Waste)
waste_processing_po.order.add_edge(Bio_Convert_Waste, Compost_Apply)
waste_processing_po.order.add_edge(Bio_Convert_Waste, Energy_Store)

# Planting adjustment partial order (Adjust Schedule and Allocate Nutrients concurrent)
adjustment_po = StrictPartialOrder(nodes=[Adjust_Schedule, Allocate_Nutrients])
# no edges - concurrent

# Initial data gathering partial order: Sensor Deploy -> Data Capture -> Microclimate Map -> Analyze Trends
initial_data_po = StrictPartialOrder(nodes=[Sensor_Deploy, Data_Capture, Microclimate_Map, Analyze_Trends])
initial_data_po.order.add_edge(Sensor_Deploy, Data_Capture)
initial_data_po.order.add_edge(Data_Capture, Microclimate_Map)
initial_data_po.order.add_edge(Microclimate_Map, Analyze_Trends)

# After analysis: analyze trends -> adjust schedule & allocate nutrients -> plant crops
after_analysis_po = StrictPartialOrder(nodes=[Analyze_Trends, adjustment_po, Plant_Crops])
after_analysis_po.order.add_edge(Analyze_Trends, adjustment_po)
after_analysis_po.order.add_edge(adjustment_po, Plant_Crops)

# Combine community_po and waste_processing_po concurrently - no order between them
community_waste_po = StrictPartialOrder(
    nodes=[community_po, waste_processing_po])

# Combine planting with community + waste (all concurrent except planting partial order is before community+waste)
# Actually, per description: plant crops then community participation and waste processing are concurrent
plant_then_community_waste_po = StrictPartialOrder(
    nodes=[after_analysis_po, community_waste_po])
plant_then_community_waste_po.order.add_edge(after_analysis_po, community_waste_po)

# Feedback loop: loop node with body = community_waste_po, and condition = feedback
# Loop form: LOOP(A=plant_then_community_waste_po, B=feedback + expert consult)
Feedback_Review_and_Expert_Consult = StrictPartialOrder(
    nodes=[Feedback_Review, Expert_Consult])
# Feedback and expert consult concurrent, no edge needed

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[plant_then_community_waste_po, Feedback_Review_and_Expert_Consult]
)

root = StrictPartialOrder(nodes=[initial_data_po, after_analysis_po, adjustment_po, community_po,
                                waste_processing_po, community_waste_po, plant_then_community_waste_po, feedback_loop])

# But the above root is not properly structured - we want the root to be the full process as one POWL structure.
# Simplify to correct modeling:

# Step 1: Initial data partial order
# Step 2: After analysis partial order (which includes adjustment partial order concurrent) then plant crops
# Step 3: Community and waste concurrently 
# Step 4: Feedback loop (* (Step 3, Feedback_Review + Expert_Consult))

# Construct Step 2 as partial order:
step2_po = StrictPartialOrder(nodes=[Adjust_Schedule, Allocate_Nutrients, Plant_Crops])
step2_po.order.add_edge(Adjust_Schedule, Plant_Crops)
step2_po.order.add_edge(Allocate_Nutrients, Plant_Crops)

# Combine Step1 and Step2:
initial_and_adjust_plant = StrictPartialOrder(
    nodes=[Sensor_Deploy, Data_Capture, Microclimate_Map, Analyze_Trends, step2_po])
initial_and_adjust_plant.order.add_edge(Sensor_Deploy, Data_Capture)
initial_and_adjust_plant.order.add_edge(Data_Capture, Microclimate_Map)
initial_and_adjust_plant.order.add_edge(Microclimate_Map, Analyze_Trends)
initial_and_adjust_plant.order.add_edge(Analyze_Trends, step2_po)

# Combine community and waste concurrently:
community_and_waste = StrictPartialOrder(nodes=[community_po, waste_processing_po])
# No edges between community_po and waste_processing_po means concurrent

# Combine initial_and_adjust_plant -> community_and_waste:
before_loop = StrictPartialOrder(
    nodes=[initial_and_adjust_plant, community_and_waste])
before_loop.order.add_edge(initial_and_adjust_plant, community_and_waste)

# Feedback loop:
feedback_body = community_and_waste
feedback_condition = StrictPartialOrder(nodes=[Feedback_Review, Expert_Consult])
# They are concurrent, no edge needed.

loop = OperatorPOWL(operator=Operator.LOOP, children=[before_loop, feedback_condition])

root = loop