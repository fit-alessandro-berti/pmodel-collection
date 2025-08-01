# Generated from: 50cd576d-d3fa-4938-a50a-903ca2c2f1c5.json
# Description: This process involves the systematic integration of emerging technologies from diverse industries to foster breakthrough product development. It begins with trend scouting across sectors, followed by multi-disciplinary brainstorming sessions to ideate novel applications. Prototyping includes rapid iteration with cross-functional teams, incorporating feedback from external experts and end-users. Subsequent steps focus on regulatory alignment, intellectual property mapping, and pilot testing in controlled environments. The cycle concludes with strategic scaling and continuous post-launch innovation monitoring, ensuring sustained competitive advantage in rapidly evolving markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Trend_Scouting = Transition(label='Trend Scouting')
Idea_Harvest = Transition(label='Idea Harvest')
Concept_Screening = Transition(label='Concept Screening')

Tech_Mapping = Transition(label='Tech Mapping')
Cross_Teams = Transition(label='Cross Teams')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
User_Testing = Transition(label='User Testing')

Regulatory_Check = Transition(label='Regulatory Check')
IP_Analysis = Transition(label='IP Analysis')
Pilot_Launch = Transition(label='Pilot Launch')

Data_Capture = Transition(label='Data Capture')
Scale_Planning = Transition(label='Scale Planning')
Market_Rollout = Transition(label='Market Rollout')
Innovation_Audit = Transition(label='Innovation Audit')

# Prototyping loop:
# "Prototyping includes rapid iteration with cross-functional teams,
# incorporating feedback from external experts and end-users."
# This would be: Build prototype, then Expert Review and User Testing,
# then iterate on prototype build again or exit loop
# We'll model B = "Expert Review + User Testing" in parallel as PO, A = Prototype_Build

# Parallel steps Expert Review and User Testing
expert_user_PO = StrictPartialOrder(nodes=[Expert_Review, User_Testing])

# Loop: Prototype_Build -> (exit or Expert_Review+User_Testing -> Prototype_Build)
loop_prototyping = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Prototype_Build, expert_user_PO]
)

# Integration of feedback and cross teams work is before prototype build.
# The "Cross Teams" and "Tech Mapping" are part of prototyping preparation
# Model "Tech Mapping" and "Cross Teams" in parallel and before prototype build loop
pre_prototype_PO = StrictPartialOrder(nodes=[Tech_Mapping, Cross_Teams])
# no order edges: concurrent

# Now the main process ordering:

# Start:
# Trend Scouting -> Idea Harvest -> Concept Screening

# Then Integration prep (Tech Mapping and Cross Teams concurrent),
# which leads to prototyping loop.

# After prototyping loop, next steps:
# Regulatory Check -> IP Analysis -> Pilot Launch

# Then Data Capture -> Scale Planning -> Market Rollout -> Innovation Audit

# Create the top level PO and add ordering edges accordingly

nodes_top = [
    Trend_Scouting,
    Idea_Harvest,
    Concept_Screening,
    pre_prototype_PO,
    loop_prototyping,
    Regulatory_Check,
    IP_Analysis,
    Pilot_Launch,
    Data_Capture,
    Scale_Planning,
    Market_Rollout,
    Innovation_Audit
]

root = StrictPartialOrder(nodes=nodes_top)

# Add ordering edges according to process description

# From start:
root.order.add_edge(Trend_Scouting, Idea_Harvest)
root.order.add_edge(Idea_Harvest, Concept_Screening)

# Concept Screening precedes pre-prototype work (Tech Mapping + Cross Teams concurrent)
root.order.add_edge(Concept_Screening, pre_prototype_PO)

# Pre prototype concurrent activities precede prototyping loop
root.order.add_edge(pre_prototype_PO, loop_prototyping)

# After prototyping loop follows Regulatory Check etc.
root.order.add_edge(loop_prototyping, Regulatory_Check)
root.order.add_edge(Regulatory_Check, IP_Analysis)
root.order.add_edge(IP_Analysis, Pilot_Launch)

# Then next phase: Data Capture, Scale Planning, Market Rollout, Innovation Audit sequential
root.order.add_edge(Pilot_Launch, Data_Capture)
root.order.add_edge(Data_Capture, Scale_Planning)
root.order.add_edge(Scale_Planning, Market_Rollout)
root.order.add_edge(Market_Rollout, Innovation_Audit)