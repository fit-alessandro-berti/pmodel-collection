# Generated from: 0b4e8ea1-a440-4817-a9cd-470d5e04d44c.json
# Description: Dynamic Talent Allocation is a multifaceted process designed to optimize workforce distribution across multiple projects in real-time by leveraging predictive analytics and continuous feedback loops. The process starts with skill profiling and project requirement mapping, followed by availability forecasting using AI-driven models. Concurrently, employee preferences and historical performance metrics are analyzed to match talents with evolving project demands. Throughout the project lifecycle, dynamic reassignment and upskilling initiatives are executed based on emerging skill gaps and shifting priorities. Continuous performance monitoring and stakeholder feedback ensure alignment with organizational goals while minimizing downtime and maximizing productivity. The process concludes with post-project evaluation and knowledge retention activities to enhance future allocation cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
SP = Transition(label='Skill Profiling')
RM = Transition(label='Requirement Map')
AC = Transition(label='Availability Check')
DF = Transition(label='Demand Forecast')
PS = Transition(label='Preference Survey')
PR = Transition(label='Performance Review')
TM = Transition(label='Talent Match')
AN = Transition(label='Assignment Notify')
OB = Transition(label='Onboard Brief')
PM = Transition(label='Progress Monitor')
GI = Transition(label='Gap Identify')
UP = Transition(label='Upskill Plan')
RT = Transition(label='Reassign Talent')
FG = Transition(label='Feedback Gather')
PC = Transition(label='Project Closeout')
KA = Transition(label='Knowledge Archive')

# Build the loop body: Gap Identify -> Upskill Plan -> Reassign Talent -> Feedback Gather
loop_body = StrictPartialOrder(nodes=[GI, UP, RT, FG])
loop_body.order.add_edge(GI, UP)
loop_body.order.add_edge(UP, RT)
loop_body.order.add_edge(RT, FG)

# Build the loop: first Progress Monitor, then zero-or-more executions of the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[PM, loop_body])

# Build the root partial order with all components
root = StrictPartialOrder(nodes=[
    SP, RM,
    AC,
    DF, PS, PR,
    TM,
    AN, OB,
    loop,
    PC, KA
])

# Define the control‐flow relations
root.order.add_edge(SP, AC)
root.order.add_edge(RM, AC)

# After availability check, three analyses run in parallel:
root.order.add_edge(AC, DF)
root.order.add_edge(AC, PS)
root.order.add_edge(AC, PR)

# Once analyses complete, perform the talent match
root.order.add_edge(DF, TM)
root.order.add_edge(PS, TM)
root.order.add_edge(PR, TM)

# Sequence the assignment and onboarding
root.order.add_edge(TM, AN)
root.order.add_edge(AN, OB)

# Then enter the monitoring/upskilling loop
root.order.add_edge(OB, loop)

# After the loop, close out and archive knowledge
root.order.add_edge(loop, PC)
root.order.add_edge(PC, KA)