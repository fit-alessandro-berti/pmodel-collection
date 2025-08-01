# Generated from: d03a3ac1-01fb-43f7-9e51-df1f5bd17820.json
# Description: This process outlines the intricate cycle of managing a dynamic urban farming system integrating IoT sensors, AI-driven crop monitoring, community feedback loops, and adaptive resource allocation. The workflow begins with site analysis and sensor deployment, followed by continuous data collection and AI-based growth prediction. Community members provide feedback on crop preferences and environmental impact, which informs real-time adjustments in irrigation, nutrient delivery, and pest control. The process also includes periodic soil regeneration through biochar application and microbial inoculation, ensuring sustainable productivity. Harvesting is coordinated via automated systems, while post-harvest analysis feeds into future planting strategies. This atypical farming cycle merges technology, ecology, and social input for optimized urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis    = Transition(label='Site Analysis')
sensor_setup     = Transition(label='Sensor Setup')
data_capture     = Transition(label='Data Capture')
ai_prediction    = Transition(label='AI Prediction')
community_poll   = Transition(label='Community Poll')
irrigation_adjust= Transition(label='Irrigation Adjust')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
soil_testing     = Transition(label='Soil Testing')
biochar_apply    = Transition(label='Biochar Apply')
microbial_add    = Transition(label='Microbial Add')
automated_harvest= Transition(label='Automated Harvest')
yield_review     = Transition(label='Yield Review')
waste_process    = Transition(label='Waste Process')
feedback_loop    = Transition(label='Feedback Loop')

# A-block: Data Capture -> AI Prediction
A = StrictPartialOrder(nodes=[data_capture, ai_prediction])
A.order.add_edge(data_capture, ai_prediction)

# Adjustments block: Irrigation, Nutrient, Pest (concurrent)
adjustments = StrictPartialOrder(nodes=[irrigation_adjust, nutrient_mix, pest_control])

# Soil regeneration block: Soil Testing -> Biochar Apply -> Microbial Add
regeneration = StrictPartialOrder(nodes=[soil_testing, biochar_apply, microbial_add])
regeneration.order.add_edge(soil_testing, biochar_apply)
regeneration.order.add_edge(biochar_apply, microbial_add)

# B-block: Community Poll -> (adjustments and regeneration in parallel)
B = StrictPartialOrder(nodes=[community_poll, adjustments, regeneration])
B.order.add_edge(community_poll, adjustments)
B.order.add_edge(community_poll, regeneration)

# Loop: * (A, B)
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Root workflow: Site Analysis -> Sensor Setup -> loop -> Automated Harvest -> Yield Review -> Waste Process -> Feedback Loop
root = StrictPartialOrder(nodes=[
    site_analysis, sensor_setup, loop,
    automated_harvest, yield_review, waste_process, feedback_loop
])
root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, loop)
root.order.add_edge(loop, automated_harvest)
root.order.add_edge(automated_harvest, yield_review)
root.order.add_edge(yield_review, waste_process)
root.order.add_edge(waste_process, feedback_loop)