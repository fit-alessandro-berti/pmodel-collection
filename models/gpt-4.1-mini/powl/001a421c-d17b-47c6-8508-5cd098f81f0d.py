# Generated from: 001a421c-d17b-47c6-8508-5cd098f81f0d.json
# Description: This process involves transforming underutilized urban rooftop spaces into productive, sustainable farms. It includes structural assessment to ensure load-bearing capacity, environmental analysis for sunlight and wind patterns, selection of appropriate soil and hydroponic systems, installation of automated irrigation and nutrient delivery, integration of sensor networks for real-time monitoring, community engagement for education and maintenance, and finally, planning for seasonal crop rotation and pest management strategies. The process is designed to maximize green space in cities while promoting local food production and reducing carbon footprints through innovative urban agriculture techniques.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Check = Transition(label='Load Check')
Sun_Mapping = Transition(label='Sun Mapping')
Wind_Study = Transition(label='Wind Study')
Soil_Select = Transition(label='Soil Select')
Hydro_Setup = Transition(label='Hydro Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Network = Transition(label='Sensor Network')
Nutrient_Plan = Transition(label='Nutrient Plan')
Crop_Choice = Transition(label='Crop Choice')
Community_Meet = Transition(label='Community Meet')
Training_Session = Transition(label='Training Session')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Season_Switch = Transition(label='Season Switch')

# Step 1: Structural assessment: Site Survey -> Load Check
structural_assessment = StrictPartialOrder(nodes=[Site_Survey, Load_Check])
structural_assessment.order.add_edge(Site_Survey, Load_Check)

# Step 2: Environmental analysis partly concurrent: Sun Mapping and Wind Study concurrent after Load Check
env_analysis = StrictPartialOrder(nodes=[Sun_Mapping, Wind_Study])
# No order edges: they are concurrent

env_after_structural = StrictPartialOrder(nodes=[structural_assessment, env_analysis])
env_after_structural.order.add_edge(structural_assessment, env_analysis)

# Step 3: Selection of soil and hydroponic systems: Soil Select and Hydro Setup concurrent after env_analysis
soil_hydro = StrictPartialOrder(nodes=[Soil_Select, Hydro_Setup])
# concurrent, no edges

selection_after_env = StrictPartialOrder(nodes=[env_after_structural, soil_hydro])
selection_after_env.order.add_edge(env_after_structural, soil_hydro)

# Step 4: Installation of irrigation and nutrient plan concurrent
installation = StrictPartialOrder(nodes=[Irrigation_Install, Nutrient_Plan])
# concurrent

installation_after_selection = StrictPartialOrder(nodes=[selection_after_env, installation])
installation_after_selection.order.add_edge(selection_after_env, installation)

# Step 5: Sensor network integration concurrent with installation? More likely after installation
sensor_after_installation = StrictPartialOrder(nodes=[installation_after_selection, Sensor_Network])
sensor_after_installation.order.add_edge(installation_after_selection, Sensor_Network)

# Step 6: Crop choice after sensor network
crop_choice_flow = StrictPartialOrder(nodes=[sensor_after_installation, Crop_Choice])
crop_choice_flow.order.add_edge(sensor_after_installation, Crop_Choice)

# Step 7: Community engagement: Community Meet then Training Session sequentially
community_engagement = StrictPartialOrder(nodes=[Community_Meet, Training_Session])
community_engagement.order.add_edge(Community_Meet, Training_Session)

# Step 8: Pest Control, Harvest Plan, Waste Recycle concurrent after crop choice and community engagement
post_crop = StrictPartialOrder(nodes=[crop_choice_flow, community_engagement])
# concurrent branches after crop choice and community engagement start after crop_choice_flow is ready and community_engagement ready?
# To simplify, we assume pest, harvest, waste start after both crop_choice and training_session done

# So first we combine crop_choice_flow and community_engagement so that pest, harvest, waste depend on both
before_post_crop = StrictPartialOrder(nodes=[crop_choice_flow, community_engagement])
# No edge between crop_choice_flow and community_engagement - they run independently

post_crop_steps = StrictPartialOrder(nodes=[Pest_Control, Harvest_Plan, Waste_Recycle])
# concurrent

post_crop_flow = StrictPartialOrder(nodes=[before_post_crop, post_crop_steps])
post_crop_flow.order.add_edge(before_post_crop, post_crop_steps)

# Step 9: Seasonal crop rotation and pest management strategies: modeled as loop with Pest_Control and Season_Switch
# The loop body: Pest_Control + Seasonal Switch
# The model: * (Pest_Control + Season_Switch) - but Pest_Control and Season_Switch sequential? Or concurrent? 
# Likely sequential: Pest_Control --> Season_Switch

loop_body = StrictPartialOrder(nodes=[Pest_Control, Season_Switch])
loop_body.order.add_edge(Pest_Control, Season_Switch)

# Loop: execute loop_body and then optionally repeat or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[Season_Switch, Pest_Control])

# However, the classical LOOP operator expects: LOOP(childA=body, childB=loopback)
# Per pm4py docs: LOOP(A,B): execute A, then either exit or do B then A again

# We want a loop: execute Pest_Control, then Season_Switch, then optionally repeat
# So set A = loop_body (Pest_Control->Season_Switch), B = SilentTransition (means no additional step before looping again)
# But this means after loop_body, either exit or do B then loop_body again
# Alternatively, set B = SilentTransition to allow looping

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Final assembly:
# The loop (crop rotation & pest management) happens after post_crop_flow without Pest_Control (to avoid duplication)
# Since Pest_Control appears already in post_crop_flow, let's replace that with loop
# So post_crop_steps without Pest_Control = Harvest_Plan and Waste_Recycle concurrent

post_crop_steps_without_pest = StrictPartialOrder(nodes=[Harvest_Plan, Waste_Recycle])
# concurrent

post_crop_flow_final = StrictPartialOrder(nodes=[before_post_crop, post_crop_steps_without_pest])
post_crop_flow_final.order.add_edge(before_post_crop, post_crop_steps_without_pest)

# Now finish flow is post_crop_flow_final --> loop
root = StrictPartialOrder(nodes=[post_crop_flow_final, loop])
root.order.add_edge(post_crop_flow_final, loop)

# Compose all:
# structural_assessment -> env_analysis -> soil_hydro -> installation -> sensor -> crop_choice -> community_engagement
# For better clarity, assemble chain from structural_assessment to community_engagement

# Chain all previous partial orders in sequence:

s1 = StrictPartialOrder(nodes=[structural_assessment, env_analysis])
s1.order.add_edge(structural_assessment, env_analysis)

s2 = StrictPartialOrder(nodes=[s1, soil_hydro])
s2.order.add_edge(s1, soil_hydro)

s3 = StrictPartialOrder(nodes=[s2, installation])
s3.order.add_edge(s2, installation)

s4 = StrictPartialOrder(nodes=[s3, Sensor_Network])
s4.order.add_edge(s3, Sensor_Network)

s5 = StrictPartialOrder(nodes=[s4, Crop_Choice])
s5.order.add_edge(s4, Crop_Choice)

s6 = StrictPartialOrder(nodes=[s5, community_engagement])
s6.order.add_edge(s5, community_engagement)

s7 = StrictPartialOrder(nodes=[s6, post_crop_steps_without_pest])
s7.order.add_edge(s6, post_crop_steps_without_pest)

root = StrictPartialOrder(nodes=[s7, loop])
root.order.add_edge(s7, loop)