# Generated from: b0b1dd53-ffaf-4cf9-9604-1a4a1040874a.json
# Description: This process involves a systematic approach to generating novel solutions by integrating insights from diverse industries. It starts with environmental scanning to identify emerging trends, followed by cross-sector brainstorming sessions. Ideas are then prototyped rapidly using agile methods and tested through simulated market environments. Feedback loops include stakeholder validation and cross-disciplinary peer reviews. The process culminates in iterative refinement and strategic alignment before final deployment, ensuring innovation is both disruptive and viable across multiple markets and regulatory frameworks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions with exact labels
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Sector_Sync = Transition(label='Sector Sync')
Brainstorm = Transition(label='Brainstorm')
Concept_Map = Transition(label='Concept Map')
Rapid_Proto = Transition(label='Rapid Proto')
Simulate_Test = Transition(label='Simulate Test')
Stakeholder_Review = Transition(label='Stakeholder Review')
Peer_Assess = Transition(label='Peer Assess')
Feedback_Loop = Transition(label='Feedback Loop')
Iterate_Design = Transition(label='Iterate Design')
Risk_Align = Transition(label='Risk Align')
Compliance_Check = Transition(label='Compliance Check')
Strategic_Fit = Transition(label='Strategic Fit')
Final_Deploy = Transition(label='Final Deploy')
Post_Launch = Transition(label='Post Launch')

# The process flow:

# 1. Start: Trend Scan
# 2. Concurrent after Trend Scan: Idea Harvest and Sector Sync
# 3. After both Idea Harvest and Sector Sync: Brainstorm and Concept Map in parallel (partial order - concurrent)
# 4. After Brainstorm and Concept Map: Rapid Proto
# 5. Then Simulate Test
# 6. Feedback loop: Stakeholder Review and Peer Assess (concurrent) --> Feedback Loop (loop)
#    Loop is: execute Feedback Loop, then choose to repeat Stakeholder Review + Peer Assess again and Feedback Loop,
#    or exit loop
# 7. After loop exit: Iterate Design
# 8. Then three activities in concurrency: Risk Align, Compliance Check, Strategic Fit
# 9. After these three: Final Deploy
# 10. Then Post Launch

# Model the feedback loop as a LOOP:
# Loop structure: LOOP(body=Feedback_Loop, redo=StrictPartialOrder(nodes=[Stakeholder_Review, Peer_Assess]))
# That means execute Feedback Loop then either exit or execute Stakeholder Review & Peer Assess then Feedback Loop again.

# Build nodes for feedback loop redo branch (Stakeholder Review and Peer Assess concurrent):
redo_nodes = [Stakeholder_Review, Peer_Assess]
redo_po = StrictPartialOrder(nodes=redo_nodes)

# Feedback loop as LOOP operator
loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, redo_po])

# Concurrency of Brainstorm and Concept Map
brainstorm_concept = StrictPartialOrder(nodes=[Brainstorm, Concept_Map])

# Concurrency of Risk Align, Compliance Check, Strategic Fit
risk_compliance_strategic = StrictPartialOrder(nodes=[Risk_Align, Compliance_Check, Strategic_Fit])

# Concurrency of Idea Harvest and Sector Sync
idea_sector = StrictPartialOrder(nodes=[Idea_Harvest, Sector_Sync])

# Build overall partial order nodes including all major stages:
# Nodes:
# Trend Scan --> idea_sector --> brainstorm_concept --> Rapid Proto --> Simulate Test --> loop --> Iterate Design --> risk_compliance_strategic --> Final Deploy --> Post Launch

nodes = [
    Trend_Scan,
    idea_sector,
    brainstorm_concept,
    Rapid_Proto,
    Simulate_Test,
    loop,
    Iterate_Design,
    risk_compliance_strategic,
    Final_Deploy,
    Post_Launch,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges respecting described flow:

root.order.add_edge(Trend_Scan, idea_sector)

root.order.add_edge(idea_sector, brainstorm_concept)

root.order.add_edge(brainstorm_concept, Rapid_Proto)

root.order.add_edge(Rapid_Proto, Simulate_Test)

root.order.add_edge(Simulate_Test, loop)

root.order.add_edge(loop, Iterate_Design)

root.order.add_edge(Iterate_Design, risk_compliance_strategic)

root.order.add_edge(risk_compliance_strategic, Final_Deploy)

root.order.add_edge(Final_Deploy, Post_Launch)