# Generated from: 66a6bf7c-b061-4443-acda-c5bc40d25a12.json
# Description: This process governs the end-to-end management of an urban vertical farm that integrates IoT monitoring, automated nutrient delivery, and AI-driven crop optimization. Starting from seed selection, the system adapts environmental controls dynamically based on sensor feedback to maximize yield while minimizing water and energy consumption. The workflow includes pest detection via image recognition, real-time growth analytics, and coordinated harvest scheduling. Post-harvest, produce undergoes automated quality grading and packaging before distribution to local markets and restaurants, ensuring freshness and traceability. The cycle concludes with system maintenance, data archiving, and continuous improvement through machine learning insights derived from operational data.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
IoT_Setup = Transition(label='IoT Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Check = Transition(label='Sensor Check')
Climate_Adjust = Transition(label='Climate Adjust')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Water_Control = Transition(label='Water Control')
AI_Analysis = Transition(label='AI Analysis')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Scan = Transition(label='Quality Scan')
Auto_Package = Transition(label='Auto Package')
Market_Dispatch = Transition(label='Market Dispatch')
Data_Archive = Transition(label='Data Archive')
System_Maintain = Transition(label='System Maintain')
Feedback_Loop = Transition(label='Feedback Loop')

# Stage 1: start - Seed Selection -> IoT Setup -> Nutrient Mix
stage1 = StrictPartialOrder(nodes=[Seed_Selection, IoT_Setup, Nutrient_Mix])
stage1.order.add_edge(Seed_Selection, IoT_Setup)
stage1.order.add_edge(IoT_Setup, Nutrient_Mix)

# Stage 2: Sensor check and adjustments (Sensor Check -> Climate Adjust and Water Control in parallel)
sensor_adjust = StrictPartialOrder(nodes=[Sensor_Check, Climate_Adjust, Water_Control])
sensor_adjust.order.add_edge(Sensor_Check, Climate_Adjust)
sensor_adjust.order.add_edge(Sensor_Check, Water_Control)
# Climate Adjust and Water Control concurrent (no edge between them)

# Stage 3: Growth and pest detection
growth_pest = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Detect])
# These can be concurrent, so no order edges

# Stage 4: AI analysis and harvest planning
ai_harvest = StrictPartialOrder(nodes=[AI_Analysis, Harvest_Plan])
ai_harvest.order.add_edge(AI_Analysis, Harvest_Plan)

# Stage 5: Quality Scan, Auto Package (in order)
quality_pack = StrictPartialOrder(nodes=[Quality_Scan, Auto_Package])
quality_pack.order.add_edge(Quality_Scan, Auto_Package)

# Stage 6: Market Dispatch after packaging
market = Market_Dispatch

# Stage 7: Post-harvest maintenance and archiving
post_harvest = StrictPartialOrder(nodes=[Data_Archive, System_Maintain])
post_harvest.order.add_edge(Data_Archive, System_Maintain)

# Next: Feedback Loop with loop on adjustments and analysis
# Loop structure: 
#   A = Sensor Check -> (Climate Adjust | Water Control) -> Growth Monitor -> Pest Detect -> AI Analysis -> Harvest Plan
#   B = Feedback Loop
# So break the process into loop head and body

# Define loop head A:
head_nodes = [
    Sensor_Check, Climate_Adjust, Water_Control,
    Growth_Monitor, Pest_Detect,
    AI_Analysis, Harvest_Plan
]
head = StrictPartialOrder(nodes=head_nodes)
head.order.add_edge(Sensor_Check, Climate_Adjust)
head.order.add_edge(Sensor_Check, Water_Control)
head.order.add_edge(Climate_Adjust, Growth_Monitor)
head.order.add_edge(Water_Control, Growth_Monitor)
# Growth_Monitor and Pest_Detect concurrent?
# Described as concurrent in growth_pest above, but here for loop use order to ensure proper sequencing:
head.order.add_edge(Growth_Monitor, Pest_Detect)
head.order.add_edge(Pest_Detect, AI_Analysis)
head.order.add_edge(AI_Analysis, Harvest_Plan)

# Define loop body B (Feedback Loop)
feedback = Feedback_Loop

# Create the loop operator
loop = OperatorPOWL(operator=Operator.LOOP, children=[head, feedback])

# Now compose the entire process in proper order:
# Seed Selection -> IoT Setup -> Nutrient Mix -> loop -> Quality Scan -> Auto Package -> Market Dispatch -> Data Archive -> System Maintain

pre_loop = stage1  # Seed Selection -> IoT Setup -> Nutrient Mix

post_loop_quality = StrictPartialOrder(nodes=[Quality_Scan, Auto_Package])
post_loop_quality.order.add_edge(Quality_Scan, Auto_Package)

market_dispatch = Market_Dispatch

post_harvest_seq = StrictPartialOrder(nodes=[Data_Archive, System_Maintain])
post_harvest_seq.order.add_edge(Data_Archive, System_Maintain)

# Compose post-loop partial order: Quality packaging -> Market Dispatch -> Data Archive -> System Maintain
post_loop_nodes = [post_loop_quality, market_dispatch, post_harvest_seq]

# Create a StrictPartialOrder for all post-loop sequential execution
post_loop = StrictPartialOrder(nodes=[post_loop_quality, market_dispatch, post_harvest_seq])
post_loop.order.add_edge(post_loop_quality, market_dispatch)
post_loop.order.add_edge(market_dispatch, post_harvest_seq)

# Finally compose the root partial order with:
# pre_loop -> loop -> post_loop

root = StrictPartialOrder(nodes=[pre_loop, loop, post_loop])
root.order.add_edge(pre_loop, loop)
root.order.add_edge(loop, post_loop)