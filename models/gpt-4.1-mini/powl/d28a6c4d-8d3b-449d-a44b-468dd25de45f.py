# Generated from: d28a6c4d-8d3b-449d-a44b-468dd25de45f.json
# Description: This process describes a complex cycle where a company integrates insights from unrelated industries to drive breakthrough product innovation. It begins with trend sensing across multiple sectors, followed by ideation sessions that combine disparate knowledge domains. Prototypes are then rapidly developed using adaptive methodologies, incorporating continuous feedback from external expert panels and real-world testing environments. Intellectual property is strategically evaluated to ensure cross-border compliance, and partnerships are formed with niche suppliers and technology incubators. The cycle concludes with market launch readiness reviews focusing on atypical user segments and iterative scaling strategies to capture emerging demand patterns while minimizing operational risks and maximizing agile responsiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
Trend_Sensing = Transition(label='Trend Sensing')
Idea_Fusion = Transition(label='Idea Fusion')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Field_Testing = Transition(label='Field Testing')
IP_Analysis = Transition(label='IP Analysis')
Compliance_Check = Transition(label='Compliance Check')
Partner_Setup = Transition(label='Partner Setup')
User_Profiling = Transition(label='User Profiling')
Launch_Prep = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')
Scale_Planning = Transition(label='Scale Planning')
Risk_Assess = Transition(label='Risk Assess')
Demand_Scan = Transition(label='Demand Scan')
Agile_Adjust = Transition(label='Agile Adjust')

# The cycle involved is that after Trend Sensing and Idea Fusion,
# Prototype Build happens, then Expert Review and Field Testing feed continuous feedback.
# This feedback loop is then incorporated into Prototype Build again.
# After the build cycle:
# IP Analysis and Compliance Check (sequential)
# Then Partner Setup (single step)
# Then Market Launch readiness: User Profiling and Launch Prep in sequence
# Followed by an iterative scaling strategy including Feedback Loop (feedback),
# Scale Planning, Risk Assess, Demand Scan, Agile Adjust.
#
# The description suggests a loop from Prototype Build incorporating Expert Review and Field Testing feedback,
# and another loop (cycle) towards scaling and adjusting responsiveness with Feedback Loop repeated.

# Build the inner feedback loop after Prototype Build
feedback_loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Prototype_Build,  # body to execute initially
        StrictPartialOrder(nodes=[Expert_Review, Field_Testing])  # repeatedly execute these (feedback providers) before going back
    ]
)

# Sequence of IP Analysis and Compliance Check
ip_compliance = StrictPartialOrder(nodes=[IP_Analysis, Compliance_Check])
ip_compliance.order.add_edge(IP_Analysis, Compliance_Check)

# Sequence for Market Launch readiness: User Profiling -> Launch Prep
launch_readiness = StrictPartialOrder(nodes=[User_Profiling, Launch_Prep])
launch_readiness.order.add_edge(User_Profiling, Launch_Prep)

# Iterative scaling strategy loop:
# Start with Feedback Loop, then linear Scale Planning -> Risk Assess -> Demand Scan -> Agile Adjust
scaling_sequence = StrictPartialOrder(
    nodes=[Scale_Planning, Risk_Assess, Demand_Scan, Agile_Adjust]
)
scaling_sequence.order.add_edge(Scale_Planning, Risk_Assess)
scaling_sequence.order.add_edge(Risk_Assess, Demand_Scan)
scaling_sequence.order.add_edge(Demand_Scan, Agile_Adjust)

scaling_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Feedback_Loop,
        scaling_sequence
    ]
)

# Partner setup stands alone after compliance
# Build full sequence before scaling loop:
# IP sequence -> Partner setup -> Launch readiness -> scaling loop

pre_scaling_seq = StrictPartialOrder(
    nodes=[ip_compliance, Partner_Setup, launch_readiness]
)
pre_scaling_seq.order.add_edge(ip_compliance, Partner_Setup)
pre_scaling_seq.order.add_edge(Partner_Setup, launch_readiness)

# Because ip_compliance and launch_readiness are themselves StrictPartialOrder instances,
# they count as nodes in pre_scaling_seq, so we add the sub-models as nodes

# Trend Sensing -> Idea Fusion -> feedback_loop_cycle -> pre_scaling_seq -> scaling_loop

first_seq = StrictPartialOrder(
    nodes=[Trend_Sensing, Idea_Fusion, feedback_loop_cycle, pre_scaling_seq, scaling_loop]
)
first_seq.order.add_edge(Trend_Sensing, Idea_Fusion)
first_seq.order.add_edge(Idea_Fusion, feedback_loop_cycle)
first_seq.order.add_edge(feedback_loop_cycle, pre_scaling_seq)
first_seq.order.add_edge(pre_scaling_seq, scaling_loop)

# Final root
root = first_seq