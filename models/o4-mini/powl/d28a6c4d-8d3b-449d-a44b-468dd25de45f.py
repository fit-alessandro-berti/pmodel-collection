# Generated from: d28a6c4d-8d3b-449d-a44b-468dd25de45f.json
# Description: This process describes a complex cycle where a company integrates insights from unrelated industries to drive breakthrough product innovation. It begins with trend sensing across multiple sectors, followed by ideation sessions that combine disparate knowledge domains. Prototypes are then rapidly developed using adaptive methodologies, incorporating continuous feedback from external expert panels and real-world testing environments. Intellectual property is strategically evaluated to ensure cross-border compliance, and partnerships are formed with niche suppliers and technology incubators. The cycle concludes with market launch readiness reviews focusing on atypical user segments and iterative scaling strategies to capture emerging demand patterns while minimizing operational risks and maximizing agile responsiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
TS = Transition(label='Trend Sensing')
IF = Transition(label='Idea Fusion')
PB = Transition(label='Prototype Build')
ER = Transition(label='Expert Review')
FT = Transition(label='Field Testing')
FL = Transition(label='Feedback Loop')
IP = Transition(label='IP Analysis')
CC = Transition(label='Compliance Check')
PS = Transition(label='Partner Setup')
UP = Transition(label='User Profiling')
LP = Transition(label='Launch Prep')
SP = Transition(label='Scale Planning')
DS = Transition(label='Demand Scan')
RS = Transition(label='Risk Assess')
AA = Transition(label='Agile Adjust')

# Loop for prototype-build feedback cycle
feedback_cycle = StrictPartialOrder(nodes=[ER, FT, FL])
feedback_cycle.order.add_edge(ER, FL)
feedback_cycle.order.add_edge(FT, FL)
loop_prototype = OperatorPOWL(operator=Operator.LOOP, children=[PB, feedback_cycle])

# Loop for scaling and agile adjustment cycle
scaling_cycle = StrictPartialOrder(nodes=[DS, RS, AA])
scaling_cycle.order.add_edge(DS, RS)
scaling_cycle.order.add_edge(DS, AA)
scaling_cycle.order.add_edge(RS, AA)
loop_scaling = OperatorPOWL(operator=Operator.LOOP, children=[SP, scaling_cycle])

# Build the full process partial order
root = StrictPartialOrder(
    nodes=[TS, IF, loop_prototype, IP, CC, PS, UP, LP, loop_scaling]
)
root.order.add_edge(TS, IF)
root.order.add_edge(IF, loop_prototype)
root.order.add_edge(loop_prototype, IP)
root.order.add_edge(IP, CC)
root.order.add_edge(CC, PS)
root.order.add_edge(PS, UP)
root.order.add_edge(UP, LP)
root.order.add_edge(LP, loop_scaling)