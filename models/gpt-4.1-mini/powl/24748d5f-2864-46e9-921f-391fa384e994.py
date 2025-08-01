# Generated from: 24748d5f-2864-46e9-921f-391fa384e994.json
# Description: This process describes the adaptive urban farming cycle designed to optimize crop yield in constrained city environments by integrating sensor data, real-time environmental analysis, and community feedback. Starting with soil prep and seed selection, the cycle involves continuous monitoring, nutrient balancing, pest detection, and automated irrigation adjustments. It incorporates periodic crop rotation based on predictive analytics, waste recycling into compost, and community workshops to educate urban farmers. The process dynamically adapts to weather patterns and urban pollution levels, ensuring sustainable produce with minimal resource waste while fostering local engagement and resilience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Soil_Prep = Transition(label='Soil Prep')
Seed_Select = Transition(label='Seed Select')
Plant_Setup = Transition(label='Plant Setup')
Sensor_Install = Transition(label='Sensor Install')

Env_Monitor = Transition(label='Env Monitor')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Detect = Transition(label='Pest Detect')

Crop_Rotate = Transition(label='Crop Rotate')

Waste_Collect = Transition(label='Waste Collect')
Compost_Make = Transition(label='Compost Make')

Data_Analyze = Transition(label='Data Analyze')

Weather_Check = Transition(label='Weather Check')
Pollution_Assess = Transition(label='Pollution Assess')

Community_Meet = Transition(label='Community Meet')
Feedback_Loop = Transition(label='Feedback Loop')

# Build the cycle loop body:
# cycle involves: Env Monitor, Nutrient Mix, Pest Detect, Irrigation Adjust
cycle_body_nodes = [Env_Monitor, Nutrient_Mix, Pest_Detect, Irrigation_Adjust]
cycle_body = StrictPartialOrder(nodes=cycle_body_nodes)
cycle_body.order.add_edge(Env_Monitor, Nutrient_Mix)
cycle_body.order.add_edge(Nutrient_Mix, Pest_Detect)
cycle_body.order.add_edge(Pest_Detect, Irrigation_Adjust)

# Feedback loop after cycle (like community meet and feedback)
feedback_body_nodes = [Community_Meet, Feedback_Loop]
feedback_body = StrictPartialOrder(nodes=feedback_body_nodes)
# Community Meet then Feedback Loop
feedback_body.order.add_edge(Community_Meet, Feedback_Loop)

# After Feedback Loop, data analyze for adapting (weather and pollution)
data_analyze_nodes = [Data_Analyze, Weather_Check, Pollution_Assess]
data_analyze = StrictPartialOrder(nodes=data_analyze_nodes)
# Data Analyze -> Weather Check and Pollution Assess concurrently
data_analyze.order.add_edge(Data_Analyze, Weather_Check)
data_analyze.order.add_edge(Data_Analyze, Pollution_Assess)

# Waste processing parallel: Waste Collect and Compost Make (Compost Make after Waste Collect)
waste_nodes = [Waste_Collect, Compost_Make]
waste_process = StrictPartialOrder(nodes=waste_nodes)
waste_process.order.add_edge(Waste_Collect, Compost_Make)

# Crop rotation triggered periodically based on predictive analytics (modeled as choice of Crop Rotate or silent skip)
skip = SilentTransition()

crop_rotation_choice = OperatorPOWL(operator=Operator.XOR, children=[Crop_Rotate, skip])

# Loop body = cycle_body then feedback + data analyze + waste + crop rotation choice

# Combine feedback, data analyze, waste and crop rotation as concurrent (partial order with no edges)
post_cycle_nodes = [feedback_body, data_analyze, waste_process, crop_rotation_choice]

post_cycle = StrictPartialOrder(nodes=post_cycle_nodes)
# no edges - concurrent execution of post_cycle parts

# Loop operator: A=cycle_body, B= post_cycle with cycle repeating
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, post_cycle])

# Initial partial order:
# 1. Prep steps sequential: Soil Prep -> Seed Select -> Plant Setup -> Sensor Install
prep = StrictPartialOrder(nodes=[Soil_Prep, Seed_Select, Plant_Setup, Sensor_Install])
prep.order.add_edge(Soil_Prep, Seed_Select)
prep.order.add_edge(Seed_Select, Plant_Setup)
prep.order.add_edge(Plant_Setup, Sensor_Install)

# After prep, start the loop
root = StrictPartialOrder(nodes=[prep, loop])
root.order.add_edge(prep, loop)