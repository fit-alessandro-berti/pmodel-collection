# Generated from: 233ee11d-dff2-45f1-baf0-26206fa1f6e2.json
# Description: This process involves the orchestration of remotely managing and harvesting digital assets from decentralized networks while ensuring compliance with dynamic regulatory frameworks. It includes activities such as asset discovery, risk evaluation, automated bidding, extraction scheduling, encrypted transfer, multi-node verification, and post-harvest analytics. The process must adapt to fluctuating network conditions and maintain security protocols throughout. Additionally, continuous feedback loops are integrated to optimize harvesting parameters based on performance data and emerging threats, making it a robust and adaptive system for maximizing asset recovery in volatile environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Asset_Scan = Transition(label='Asset Scan')
Risk_Assess = Transition(label='Risk Assess')
Bid_Submit = Transition(label='Bid Submit')
Schedule_Extract = Transition(label='Schedule Extract')
Encrypt_Data = Transition(label='Encrypt Data')
Transfer_Init = Transition(label='Transfer Init')
Node_Verify = Transition(label='Node Verify')
Compliance_Check = Transition(label='Compliance Check')
Threat_Monitor = Transition(label='Threat Monitor')
Performance_Log = Transition(label='Performance Log')
Parameter_Adjust = Transition(label='Parameter Adjust')
Feedback_Loop = Transition(label='Feedback Loop')
Data_Merge = Transition(label='Data Merge')
Report_Generate = Transition(label='Report Generate')
Archive_Assets = Transition(label='Archive Assets')

# Modeling feedback loop:
# Feedback loop: after initial scan -> risk -> bid -> scheduling -> extraction -> encrypt -> transfer -> verify -> compliance
# Then loop to performance evaluation which may adjust parameters and continue monitoring threats,
# introducing a loop for ongoing optimization.

# Define the inner loop body:
# Loop(A,B) where A is the main execution sequence and B is the feedback adjustment process

# Main sequence before feedback:
# Asset Scan -> Risk Assess -> Bid Submit -> Schedule Extract -> Encrypt Data -> Transfer Init -> Node Verify -> Compliance Check
main_sequence_nodes = [
    Asset_Scan, Risk_Assess, Bid_Submit, Schedule_Extract,
    Encrypt_Data, Transfer_Init, Node_Verify, Compliance_Check
]

main_sequence = StrictPartialOrder(nodes=main_sequence_nodes)
for i in range(len(main_sequence_nodes) - 1):
    main_sequence.order.add_edge(main_sequence_nodes[i], main_sequence_nodes[i+1])

# Feedback process nodes:
# Threat Monitor and Performance Log run concurrently (partial order with no edges)
# Parameter Adjust depends on both Threat Monitor and Performance Log
# Feedback Loop after Parameter Adjust

feedback_nodes = [Threat_Monitor, Performance_Log, Parameter_Adjust, Feedback_Loop]

feedback = StrictPartialOrder(nodes=feedback_nodes)
# Threat Monitor and Performance Log concurrent - no edges
feedback.order.add_edge(Threat_Monitor, Parameter_Adjust)
feedback.order.add_edge(Performance_Log, Parameter_Adjust)
feedback.order.add_edge(Parameter_Adjust, Feedback_Loop)

# Define the loop with main_sequence as A and feedback as B
# Meaning: execute main_sequence, then choose to exit or execute feedback then main_sequence again

loop = OperatorPOWL(operator=Operator.LOOP, children=[main_sequence, feedback])

# After looping, the process continues with Data Merge, Report Generate, Archive Assets

post_loop_nodes = [Data_Merge, Report_Generate, Archive_Assets]
post_loop = StrictPartialOrder(nodes=post_loop_nodes)
post_loop.order.add_edge(Data_Merge, Report_Generate)
post_loop.order.add_edge(Report_Generate, Archive_Assets)

# Final model connects loop to post_loop

root = StrictPartialOrder(nodes=[loop, post_loop])
root.order.add_edge(loop, post_loop)