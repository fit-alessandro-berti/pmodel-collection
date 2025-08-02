# Generated from: d03a3ac1-01fb-43f7-9e51-df1f5bd17820.json
# Description: This process outlines the intricate cycle of managing a dynamic urban farming system integrating IoT sensors, AI-driven crop monitoring, community feedback loops, and adaptive resource allocation. The workflow begins with site analysis and sensor deployment, followed by continuous data collection and AI-based growth prediction. Community members provide feedback on crop preferences and environmental impact, which informs real-time adjustments in irrigation, nutrient delivery, and pest control. The process also includes periodic soil regeneration through biochar application and microbial inoculation, ensuring sustainable productivity. Harvesting is coordinated via automated systems, while post-harvest analysis feeds into future planting strategies. This atypical farming cycle merges technology, ecology, and social input for optimized urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
site_analysis = Transition(label='Site Analysis')
sensor_setup = Transition(label='Sensor Setup')
data_capture = Transition(label='Data Capture')
ai_prediction = Transition(label='AI Prediction')
community_poll = Transition(label='Community Poll')
irrigation_adjust = Transition(label='Irrigation Adjust')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
soil_testing = Transition(label='Soil Testing')
biochar_apply = Transition(label='Biochar Apply')
microbial_add = Transition(label='Microbial Add')
automated_harvest = Transition(label='Automated Harvest')
yield_review = Transition(label='Yield Review')
waste_process = Transition(label='Waste Process')
feedback_loop = Transition(label='Feedback Loop')

# Partial order for soil regeneration (soil testing → biochar apply + microbial add concurrently)
soil_regen = StrictPartialOrder(nodes=[soil_testing, biochar_apply, microbial_add])
soil_regen.order.add_edge(soil_testing, biochar_apply)
soil_regen.order.add_edge(soil_testing, microbial_add)

# Partial order for resource allocation adjustments (irrigation, nutrient, pest control concurrent)
resource_adjust = StrictPartialOrder(nodes=[irrigation_adjust, nutrient_mix, pest_control])

# Partial order for post-harvest analysis (yield review → waste process)
post_harvest = StrictPartialOrder(nodes=[yield_review, waste_process])
post_harvest.order.add_edge(yield_review, waste_process)

# Define feedback partial order: community poll and feedback loop concurrent, feeding into resource adjustments
feedback = StrictPartialOrder(nodes=[community_poll, feedback_loop, resource_adjust])
feedback.order.add_edge(community_poll, resource_adjust)
feedback.order.add_edge(feedback_loop, resource_adjust)

# Main cycle:
# Site Analysis → Sensor Setup → Data Capture → AI Prediction → feedback → automated harvest → post-harvest → loop soil regeneration and data capture cycles

# Define the cycle of: data capture + prediction + feedback + resource adjust + automated harvest + post harvest + soil regeneration, 
# looping continuously after site analysis and sensor setup done once.

# First define the cycle body:
cycle_body_nodes = [data_capture, ai_prediction, feedback, automated_harvest, post_harvest, soil_regen]

# Because feedback is already a PO, post_harvest and soil_regen are POs, resource_adjust included in feedback PO.

# Let's define the order edges inside the cycle:
cycle = StrictPartialOrder(nodes=cycle_body_nodes)

# data_capture -> ai_prediction
cycle.order.add_edge(data_capture, ai_prediction)

# ai_prediction -> feedback
cycle.order.add_edge(ai_prediction, feedback)
# feedback includes resource_adjust (which is after community_poll and feedback_loop)

# feedback -> automated_harvest
cycle.order.add_edge(feedback, automated_harvest)

# automated_harvest -> post_harvest
cycle.order.add_edge(automated_harvest, post_harvest)

# post_harvest -> soil_regen
cycle.order.add_edge(post_harvest, soil_regen)

# soil_regen loops back to data_capture (to represent continuous cycles)
# Use the LOOP operator: LOOP(body=cycle, redo=???

# LOOP structure: LOOP(body, redo)
# In the process description, after soil regeneration, we redo data capture and onwards.

# Use a silent transition as "redo" to represent loop back to cycle start (data_capture)
# But redo child in LOOP executes before body on repetition

# Here, the redo segment would be the resource adjustment steps or the starting point of the cycle (data_capture).
# However, to precisely loop on cycle, we'll separate cycle into body = data_capture and the rest as redo to better fit LOOP concept.

# Let's split cycle as body = data_capture,
# redo = PartialOrder of the rest (ai_prediction, feedback, automated_harvest, post_harvest, soil_regen)
redo_nodes = [ai_prediction, feedback, automated_harvest, post_harvest, soil_regen]
redo = StrictPartialOrder(nodes=redo_nodes)

redo.order.add_edge(ai_prediction, feedback)
redo.order.add_edge(feedback, automated_harvest)
redo.order.add_edge(automated_harvest, post_harvest)
redo.order.add_edge(post_harvest, soil_regen)

# soil_regen loops back to data_capture FOR NEXT CYCLE, so LOOP(body, redo) means execute body once,
# then on each repeat execute redo plus body, etc.

# The LOOP here:
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, redo])

# Entire process order after initial site analysis and sensor setup:
root = StrictPartialOrder(nodes=[site_analysis, sensor_setup, loop])

root.order.add_edge(site_analysis, sensor_setup)
root.order.add_edge(sensor_setup, loop)