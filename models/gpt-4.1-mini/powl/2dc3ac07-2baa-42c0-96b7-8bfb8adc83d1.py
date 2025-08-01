# Generated from: 2dc3ac07-2baa-42c0-96b7-8bfb8adc83d1.json
# Description: This process involves designing and executing a multi-sensory marketing campaign that integrates tactile, olfactory, auditory, and visual stimuli to enhance consumer engagement across physical and digital channels. The process starts with sensory research to identify optimal stimuli combinations, followed by prototype development where physical samples and digital assets are created. Next, a pilot test is conducted in select markets to measure sensory impact and consumer response using biometric feedback and surveys. Data from the pilot feeds into optimization cycles refining stimuli intensity, timing, and channel synchronization. After final adjustments, the campaign is launched simultaneously across retail stores, mobile apps, social media, and experiential events. Post-launch, ongoing monitoring collects real-time sensory engagement metrics, enabling adaptive modulation of stimuli based on consumer mood and environmental factors. The process concludes with comprehensive performance analysis and lessons learned to inform future sensory marketing initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions for activities
Sensory_Research = Transition(label='Sensory Research')
Stimuli_Design = Transition(label='Stimuli Design')
Prototype_Build = Transition(label='Prototype Build')
Pilot_Testing = Transition(label='Pilot Testing')
Data_Analysis = Transition(label='Data Analysis')
Stimuli_Adjust = Transition(label='Stimuli Adjust')
Channel_Sync = Transition(label='Channel Sync')
Asset_Production = Transition(label='Asset Production')
Market_Launch = Transition(label='Market Launch')
Engagement_Track = Transition(label='Engagement Track')
Feedback_Gather = Transition(label='Feedback Gather')
Adaptive_Tuning = Transition(label='Adaptive Tuning')
Experience_Event = Transition(label='Experience Event')
Performance_Review = Transition(label='Performance Review')
Lessons_Learned = Transition(label='Lessons Learned')

# Stage 1: Sensory Research
# Stage 2: Stimuli Design and Asset Production are concurrent after Sensory Research and before Prototype Build
# Prototype Build follows Stimuli Design and Asset Production
# Stage 3: Pilot Testing after Prototype Build
# Stage 4: Optimization cycles: loop of (Data Analysis -> (Stimuli Adjust & Channel Sync concurrently))
# Stage 5: After loop, Market Launch and Experience Event concurrent
# Stage 6: Post-launch monitoring loop of (Engagement Track -> Feedback Gather -> Adaptive Tuning)
# Stage 7: Final Performance Review then Lessons Learned

# Concurrent PO for Stimuli Design and Asset Production
stimuli_asset_po = StrictPartialOrder(nodes=[Stimuli_Design, Asset_Production])

# Prototype Build follows both Stimuli Design and Asset Production
proto_po = StrictPartialOrder(nodes=[Stimuli_Design, Asset_Production, Prototype_Build])
proto_po.order.add_edge(Stimuli_Design, Prototype_Build)
proto_po.order.add_edge(Asset_Production, Prototype_Build)

# Combine stimuli_asset_po and Prototype_Build into proto_po for clarity later:
# Note: stimuli_asset_po is embedded in proto_po already

# Optimization cycle loop:
# Loop body is: Data Analysis -> (Stimuli Adjust, Channel Sync concurrent)

# Concurrent stimuli adjust and channel sync
adjust_sync_po = StrictPartialOrder(nodes=[Stimuli_Adjust, Channel_Sync])

# Add edges Data Analysis -> Adjust, Data Analysis -> Channel Sync
adjust_sync_po.order.add_edge(Stimuli_Adjust, Channel_Sync)  # no order between the two is stated, but allow both concurrent, no edge here
adjust_sync_po.order.remove_edge(Stimuli_Adjust, Channel_Sync) if (Stimuli_Adjust, Channel_Sync) in adjust_sync_po.order.edges else None  # make sure none
# We'll keep them concurrent by not adding edges between them

# But we do have Data Analysis before both, so we create a PO for Data Analysis and adjust_sync_po

# Create PO for Data Analysis and adjust_sync_po nodes
data_adjust_sync_po = StrictPartialOrder(nodes=[Data_Analysis, Stimuli_Adjust, Channel_Sync])
data_adjust_sync_po.order.add_edge(Data_Analysis, Stimuli_Adjust)
data_adjust_sync_po.order.add_edge(Data_Analysis, Channel_Sync)

# Loop cycle:
optim_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analysis, OperatorPOWL(operator=Operator.XOR, children=[
    # exit choice = silent transition
    SilentTransition(),
    StrictPartialOrder(nodes=[Stimuli_Adjust, Channel_Sync])
])])

# The loop syntax expects the loop to be *(A, B)
# A: Data Analysis (execute)
# B: Stimuli Adjust & Channel Sync concurrent as one node to execute before A again

# We need to define B = concurrent Stimuli Adjust and Channel Sync
stimuli_channel_po = StrictPartialOrder(nodes=[Stimuli_Adjust, Channel_Sync])

# Loop node
optim_loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analysis, stimuli_channel_po])

# Post-optimization: Market Launch and Experience Event concurrent
launch_exp_po = StrictPartialOrder(nodes=[Market_Launch, Experience_Event])

# Post-launch monitoring loop: Engagement Track -> Feedback Gather -> Adaptive Tuning, repeated
# We'll model the monitoring as loop with body: Adaptive Tuning and B: Engagement Track -> Feedback Gather

# Monitoring cycle: loop over Engagement Track then Feedback Gather then Adaptive Tuning

# Because loop requires two children, conventionally A = do part, B = repeat part
# We model: A = Engagement Track, B = Feedback Gather -> Adaptive Tuning

feedback_adaptive_po = StrictPartialOrder(nodes=[Feedback_Gather, Adaptive_Tuning])
feedback_adaptive_po.order.add_edge(Feedback_Gather, Adaptive_Tuning)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Engagement_Track, feedback_adaptive_po])

# Final order:
# Sensory Research -> Stimuli Design & Asset Production (concurrent) -> Prototype Build -> Pilot Testing -> Loop(Optimization) -> Launch & Experience concurrent -> Loop(Monitoring) -> Performance Review -> Lessons Learned

# Build each partial order from bottom to top:

# Stimuli Design and Asset Production concurrent after Sensory Research
sd_ap_po = StrictPartialOrder(nodes=[Sensory_Research, Stimuli_Design, Asset_Production])
sd_ap_po.order.add_edge(Sensory_Research, Stimuli_Design)
sd_ap_po.order.add_edge(Sensory_Research, Asset_Production)

# Add Prototype Build after both Stimuli Design and Asset Production
sd_ap_pb_po = StrictPartialOrder(nodes=[Sensory_Research, Stimuli_Design, Asset_Production, Prototype_Build])
sd_ap_pb_po.order.add_edge(Sensory_Research, Stimuli_Design)
sd_ap_pb_po.order.add_edge(Sensory_Research, Asset_Production)
sd_ap_pb_po.order.add_edge(Stimuli_Design, Prototype_Build)
sd_ap_pb_po.order.add_edge(Asset_Production, Prototype_Build)

# After Prototype Build -> Pilot Testing
proto_pilot_po = StrictPartialOrder(nodes=[Sensory_Research, Stimuli_Design, Asset_Production, Prototype_Build, Pilot_Testing])
proto_pilot_po.order.add_edge(Sensory_Research, Stimuli_Design)
proto_pilot_po.order.add_edge(Sensory_Research, Asset_Production)
proto_pilot_po.order.add_edge(Stimuli_Design, Prototype_Build)
proto_pilot_po.order.add_edge(Asset_Production, Prototype_Build)
proto_pilot_po.order.add_edge(Prototype_Build, Pilot_Testing)

# After Pilot Testing the optimization loop starts
# We build a PO with proto_pilot_po nodes + optimization loop node
# optimization loop is a single child node after Pilot Testing

# For the optimization loop's concurrent nodes (Stimuli Adjust & Channel Sync), let’s just keep them in the loop structure we defined

main_above_optimization = StrictPartialOrder(
    nodes=[proto_pilot_po, optim_loop]
)

# But StrictPartialOrder nodes cannot be other PO or operators directly, so we embed all nodes individually:

# Let's flatten all nodes for main PO before optimization loop:
main_nodes = [
    Sensory_Research,
    Stimuli_Design,
    Asset_Production,
    Prototype_Build,
    Pilot_Testing,
    optim_loop,
    launch_exp_po,
    monitoring_loop,
    Performance_Review,
    Lessons_Learned
]

root = StrictPartialOrder(nodes=main_nodes)

# Add edges
root.order.add_edge(Sensory_Research, Stimuli_Design)
root.order.add_edge(Sensory_Research, Asset_Production)
root.order.add_edge(Stimuli_Design, Prototype_Build)
root.order.add_edge(Asset_Production, Prototype_Build)
root.order.add_edge(Prototype_Build, Pilot_Testing)
root.order.add_edge(Pilot_Testing, optim_loop)
root.order.add_edge(optim_loop, launch_exp_po)
root.order.add_edge(launch_exp_po, monitoring_loop)
root.order.add_edge(monitoring_loop, Performance_Review)
root.order.add_edge(Performance_Review, Lessons_Learned)

# launch_exp_po nodes concurrency is captured inside launch_exp_po definition
# monitoring_loop nodes concurrency/order captured inside monitoring_loop

# Final root defined.
