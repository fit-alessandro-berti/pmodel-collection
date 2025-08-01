# Generated from: e209ef5f-0b28-49f8-93ad-c3bad34b6d72.json
# Description: This process outlines a complex and atypical adaptive urban farming cycle designed for maximizing crop yield in limited city spaces while integrating real-time environmental data and community input. It begins with soil analysis and urban site mapping, followed by modular bed setup and crop selection optimized for microclimates. Continuous sensor monitoring informs automated irrigation and nutrient delivery, while manual pest scouting combines with AI-driven pest prediction. Community workshops guide seasonal crop rotation planning and resource sharing. Waste composting and water recycling close the loop, enhancing sustainability. Data analytics assess productivity and help refine future cycles, ensuring resilience and scalability in urban agriculture amidst fluctuating environmental conditions and social dynamics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Soil_Analyze = Transition(label='Soil Analyze')
Site_Mapping = Transition(label='Site Mapping')
Bed_Setup = Transition(label='Bed Setup')
Crop_Select = Transition(label='Crop Select')
Sensor_Deploy = Transition(label='Sensor Deploy')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Scouting = Transition(label='Pest Scouting')
Pest_Predict = Transition(label='Pest Predict')
Workshop_Host = Transition(label='Workshop Host')
Crop_Rotate = Transition(label='Crop Rotate')
Waste_Compost = Transition(label='Waste Compost')
Water_Recycle = Transition(label='Water Recycle')
Data_Analyze = Transition(label='Data Analyze')
Cycle_Refine = Transition(label='Cycle Refine')
Resource_Share = Transition(label='Resource Share')
Yield_Report = Transition(label='Yield Report')

# Early phase partial order:
# Soil Analyze --> Site Mapping --> Bed Setup --> Crop Select
early_phase = StrictPartialOrder(nodes=[Soil_Analyze, Site_Mapping, Bed_Setup, Crop_Select])
early_phase.order.add_edge(Soil_Analyze, Site_Mapping)
early_phase.order.add_edge(Site_Mapping, Bed_Setup)
early_phase.order.add_edge(Bed_Setup, Crop_Select)

# Sensor Monitoring partial order:
# Sensor Deploy --> (Irrigation Adjust and Nutrient Feed in parallel)
sensor_monitor = StrictPartialOrder(nodes=[Sensor_Deploy, Irrigation_Adjust, Nutrient_Feed])
sensor_monitor.order.add_edge(Sensor_Deploy, Irrigation_Adjust)
sensor_monitor.order.add_edge(Sensor_Deploy, Nutrient_Feed)
# Irrigation Adjust and Nutrient Feed are concurrent as no order edge between them

# Pest handling choice (manual scouting combined with AI prediction)
pest_manual = Pest_Scouting
pest_ai = Pest_Predict
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_manual, pest_ai])

# Community workshops guiding crop rotation and resource sharing can occur concurrently, with Crop Rotate depending on Workshop Host
community_workshop = StrictPartialOrder(nodes=[Workshop_Host, Crop_Rotate, Resource_Share])
community_workshop.order.add_edge(Workshop_Host, Crop_Rotate)
# Resource Share concurrent with Workshop Host and Crop Rotate

# Sustainability closing the loop partial order
closing_loop = StrictPartialOrder(nodes=[Waste_Compost, Water_Recycle])
# Waste Compost and Water Recycle concurrent (no edges)

# Data analytics and cycle refinement partial order (sequential)
data_refine = StrictPartialOrder(nodes=[Data_Analyze, Cycle_Refine])
data_refine.order.add_edge(Data_Analyze, Cycle_Refine)

# Yield Report occurs after cycle refinement and community workshop (so after data_refine and community_workshop)
# for concurrency, define a PO that includes yield_report with edges from cycle_refine and community_workshop nodes

# Combine phases stepwise:

# Phase 1: early phase + sensor monitoring (early_phase --> sensor_monitor)
phase1 = StrictPartialOrder(nodes=[early_phase, sensor_monitor])
phase1.order.add_edge(early_phase, sensor_monitor)

# Phase 2: pest choice after sensor_monitor (sensor_monitor --> pest_choice)
phase2 = StrictPartialOrder(nodes=[phase1, pest_choice])
phase2.order.add_edge(phase1, pest_choice)

# Phase 3: community workshop after pest_choice
phase3 = StrictPartialOrder(nodes=[phase2, community_workshop])
phase3.order.add_edge(phase2, community_workshop)

# Phase 4: closing loop after community workshop (community_workshop --> closing_loop)
phase4 = StrictPartialOrder(nodes=[phase3, closing_loop])
phase4.order.add_edge(phase3, closing_loop)

# Phase 5: data analytics and refinement after closing loop (closing_loop --> data_refine)
phase5 = StrictPartialOrder(nodes=[phase4, data_refine])
phase5.order.add_edge(phase4, data_refine)

# Final: Yield Report after data_refine and community_workshop
root = StrictPartialOrder(
    nodes=[phase5, Yield_Report]
)
root.order.add_edge(phase5, Yield_Report)

# The final model 'root' reflects the complex partial order with concurrency and choice as per the description.