# Generated from: 42431d01-b3a1-4f13-ac68-fa1aa5d636f3.json
# Description: This process involves systematically integrating breakthrough ideas from unrelated industries into a company’s product development framework. It begins with scanning diverse sectors for emerging trends, followed by ideation sessions where cross-disciplinary teams reinterpret these insights. The process includes rapid prototyping, iterative feedback loops with external experts, and scenario testing under variable market conditions. Risk assessments and intellectual property evaluations are conducted before finalizing scalable solutions. The process concludes with strategic launch planning, knowledge transfer workshops, and continuous monitoring of innovation impact across business units to ensure sustainable competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Cross_Team_Sync = Transition(label='Cross-Team Sync')
Concept_Sketch = Transition(label='Concept Sketch')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Scenario_Test = Transition(label='Scenario Test')
Risk_Assess = Transition(label='Risk Assess')
IP_Review = Transition(label='IP Review')
Scale_Design = Transition(label='Scale Design')
Launch_Plan = Transition(label='Launch Plan')
Knowledge_Share = Transition(label='Knowledge Share')
Market_Monitor = Transition(label='Market Monitor')
Feedback_Loop = Transition(label='Feedback Loop')
Impact_Audit = Transition(label='Impact Audit')

# Loop for iterative feedback: (Prototype Build, Feedback Loop)
# Loop body: Feedback_Loop
# After Feedback_Loop go to Prototype_Build again, else exit.
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Feedback_Loop])

# Partial Order for ideation and prototyping:
# Trend Scan --> Idea Harvest --> Cross-Team Sync --> Concept Sketch --> feedback_loop --> Expert Review --> Scenario Test --> Risk Assess --> IP Review --> Scale Design
po_main_part_nodes = [
    Trend_Scan, Idea_Harvest, Cross_Team_Sync, Concept_Sketch, feedback_loop,
    Expert_Review, Scenario_Test, Risk_Assess, IP_Review, Scale_Design
]
root_main_po = StrictPartialOrder(nodes=po_main_part_nodes)
root_main_po.order.add_edge(Trend_Scan, Idea_Harvest)
root_main_po.order.add_edge(Idea_Harvest, Cross_Team_Sync)
root_main_po.order.add_edge(Cross_Team_Sync, Concept_Sketch)
root_main_po.order.add_edge(Concept_Sketch, feedback_loop)
root_main_po.order.add_edge(feedback_loop, Expert_Review)
root_main_po.order.add_edge(Expert_Review, Scenario_Test)
root_main_po.order.add_edge(Scenario_Test, Risk_Assess)
root_main_po.order.add_edge(Risk_Assess, IP_Review)
root_main_po.order.add_edge(IP_Review, Scale_Design)

# Final phase partial order:
# Launch Plan --> Knowledge Share --> Market Monitor --> Impact Audit
po_final_nodes = [Launch_Plan, Knowledge_Share, Market_Monitor, Impact_Audit]
po_final = StrictPartialOrder(nodes=po_final_nodes)
po_final.order.add_edge(Launch_Plan, Knowledge_Share)
po_final.order.add_edge(Knowledge_Share, Market_Monitor)
po_final.order.add_edge(Market_Monitor, Impact_Audit)

# Combine main process and final phase in a partial order:
root = StrictPartialOrder(nodes=[root_main_po, po_final])
root.order.add_edge(root_main_po, po_final)