# Generated from: 8a7df71f-a28d-4a1d-a7b5-269e26562a33.json
# Description: This process involves the systematic identification, acquisition, and transformation of obsolete corporate artifacts such as outdated technology hardware, legacy software modules, and discontinued branded materials. The objective is to creatively repurpose these assets into new, value-generating products or services that align with current market demands. The process encompasses cross-departmental collaboration, including asset auditing, feasibility analysis, design prototyping, regulatory compliance checks, and stakeholder approvals. It further integrates sustainability assessments to ensure environmental impact is minimized. The final phase involves pilot testing, market feedback incorporation, and scaled production rollout, thereby extending the lifecycle of corporate assets while fostering innovation and reducing waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Asset_Audit = Transition(label='Asset Audit')
Market_Scan = Transition(label='Market Scan')
Feasibility_Study = Transition(label='Feasibility Study')
Design_Concept = Transition(label='Design Concept')
Prototype_Build = Transition(label='Prototype Build')
Compliance_Check = Transition(label='Compliance Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Sustainability_Eval = Transition(label='Sustainability Eval')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Review = Transition(label='Feedback Review')
Iterate_Design = Transition(label='Iterate Design')
Scale_Plan = Transition(label='Scale Plan')
Production_Setup = Transition(label='Production Setup')
Launch_Campaign = Transition(label='Launch Campaign')
Post_Launch = Transition(label='Post Launch')

# Model the design iteration loop: after Feedback_Review, either finish or Iterate_Design + then back to Design_Concept
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Review, Iterate_Design]
)

# Model the main partial order with correct sequencing and concurrency

# Initial audit and scan can be done in parallel (Asset Audit and Market Scan)
# Then Feasibility Study
# Then Design Concept

# After Design Concept, Prototype Build
# Then Compliance Check and Stakeholder Meet can run in parallel (cross-departmental collaboration)
# Then Sustainability Eval and Risk Assess can run in parallel (sustainability assessments and risk)
# Then Pilot Launch
# Then Feedback Review and loop back to iterate design if needed (design_loop)
# After exiting design_loop, proceed to Scale Plan, Production Setup, Launch Campaign, Post Launch

root = StrictPartialOrder(nodes=[
    Asset_Audit, Market_Scan, Feasibility_Study, Design_Concept, Prototype_Build,
    Compliance_Check, Stakeholder_Meet, Sustainability_Eval, Risk_Assess,
    Pilot_Launch, design_loop, Scale_Plan, Production_Setup, Launch_Campaign, Post_Launch
])

# Add edges for the main control flow

# Initial concurrency: Asset Audit and Market Scan can be concurrent (no order needed)

# Both must finish before Feasibility Study starts
root.order.add_edge(Asset_Audit, Feasibility_Study)
root.order.add_edge(Market_Scan, Feasibility_Study)

# Feasibility Study -> Design Concept -> Prototype Build
root.order.add_edge(Feasibility_Study, Design_Concept)
root.order.add_edge(Design_Concept, Prototype_Build)

# Prototype Build -> Compliance Check and Stakeholder Meet concurrent
root.order.add_edge(Prototype_Build, Compliance_Check)
root.order.add_edge(Prototype_Build, Stakeholder_Meet)

# Both Compliance Check and Stakeholder Meet must finish before Sustainability Eval and Risk Assess
root.order.add_edge(Compliance_Check, Sustainability_Eval)
root.order.add_edge(Compliance_Check, Risk_Assess)
root.order.add_edge(Stakeholder_Meet, Sustainability_Eval)
root.order.add_edge(Stakeholder_Meet, Risk_Assess)

# Sustainability Eval and Risk Assess concurrent, both before Pilot Launch
root.order.add_edge(Sustainability_Eval, Pilot_Launch)
root.order.add_edge(Risk_Assess, Pilot_Launch)

# Pilot Launch -> design_loop (Feedback Review + Iterate Design)
root.order.add_edge(Pilot_Launch, design_loop)

# After design_loop completes, go to Scale Plan -> Production Setup -> Launch Campaign -> Post Launch sequentially
root.order.add_edge(design_loop, Scale_Plan)
root.order.add_edge(Scale_Plan, Production_Setup)
root.order.add_edge(Production_Setup, Launch_Campaign)
root.order.add_edge(Launch_Campaign, Post_Launch)