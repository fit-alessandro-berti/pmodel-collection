# Generated from: 7cc14e09-a736-4d18-90b0-966d6e46d20a.json
# Description: This process outlines the integration of urban beekeeping into municipal green initiatives, combining environmental sustainability with local community engagement. It begins with site identification and environmental assessment, followed by regulatory compliance checks and stakeholder consultations. Hive installation and bee colony introduction are coordinated alongside educational workshops for residents. Continuous monitoring of hive health and data collection on pollination impact are conducted, integrating insights into urban planning. Maintenance routines and crisis management protocols ensure bee welfare and public safety. Finally, feedback loops from community and environmental data guide iterative improvements, fostering a harmonious balance between urban development and ecological preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
Site_Survey = Transition(label='Site Survey')
Env_Assessment = Transition(label='Env Assessment')

Reg_Check = Transition(label='Reg Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Permit_Apply = Transition(label='Permit Apply')

Hive_Setup = Transition(label='Hive Setup')
Colony_Introduce = Transition(label='Colony Introduce')
Workshop_Host = Transition(label='Workshop Host')

Health_Monitor = Transition(label='Health Monitor')
Data_Collect = Transition(label='Data Collect')
Impact_Analyze = Transition(label='Impact Analyze')

Maintenance = Transition(label='Maintenance')
Crisis_Manage = Transition(label='Crisis Manage')

Feedback_Gather = Transition(label='Feedback Gather')
Plan_Update = Transition(label='Plan Update')

# Loop children: body A, condition B
# Loop models "feedback loops from community and environmental data guide iterative improvements"
# So B includes Feedback_Gather + Plan_Update

# Loop condition: Feedback_Gather then Plan_Update
feedback_loop_condition = StrictPartialOrder(nodes=[Feedback_Gather, Plan_Update])
feedback_loop_condition.order.add_edge(Feedback_Gather, Plan_Update)

# Loop body: monitor, collect & analyze impact
monitoring = StrictPartialOrder(nodes=[Health_Monitor, Data_Collect, Impact_Analyze])
monitoring.order.add_edge(Health_Monitor, Data_Collect)
monitoring.order.add_edge(Data_Collect, Impact_Analyze)

loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, feedback_loop_condition])

# Maintenance and Crisis manage run parallel after monitoring loop
maint_crisis = StrictPartialOrder(nodes=[Maintenance, Crisis_Manage])
# concurrent, no edges

# After loop and maintenance/crisis -> integration into planning
# So we build a PO combining loop and maint_crisis in parallel, no order edges between them
# So monitoring loop and maintenance/crisis are concurrent

monitoring_and_maintenance = StrictPartialOrder(
    nodes=[loop, maint_crisis]
)
# No edges, fully concurrent of loop and maintenance/crisis

# Educational workshops run alongside hive setup and colony introduce
# We group these three in parallel

educational = StrictPartialOrder(nodes=[Workshop_Host])
setup_and_colony = StrictPartialOrder(nodes=[Hive_Setup, Colony_Introduce])
# Hive_Setup -> Colony_Introduce order
setup_and_colony.order.add_edge(Hive_Setup, Colony_Introduce)

workshops_and_setup = StrictPartialOrder(
    nodes=[setup_and_colony, educational]
)
# No edges between these two, so concurrent

# Regulatory compliance checks and stakeholder consultations can be done in parallel, but Permit Apply must come after Reg Check
regulation = StrictPartialOrder(nodes=[Reg_Check, Stakeholder_Meet, Permit_Apply])
regulation.order.add_edge(Reg_Check, Permit_Apply)
# Stakeholder_Meet concurrent with both

# Initial steps: Site Survey and Env Assessment in sequence
initial = StrictPartialOrder(nodes=[Site_Survey, Env_Assessment])
initial.order.add_edge(Site_Survey, Env_Assessment)

# Combine initial -> regulation -> workshops_and_setup -> monitoring_and_maintenance
root = StrictPartialOrder(
    nodes=[initial, regulation, workshops_and_setup, monitoring_and_maintenance]
)
# Adding ordering edges between these phases
root.order.add_edge(initial, regulation)
root.order.add_edge(regulation, workshops_and_setup)
root.order.add_edge(workshops_and_setup, monitoring_and_maintenance)