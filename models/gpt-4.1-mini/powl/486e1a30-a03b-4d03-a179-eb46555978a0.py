# Generated from: 486e1a30-a03b-4d03-a179-eb46555978a0.json
# Description: This process involves launching a new product specifically tailored for emerging markets where infrastructure, consumer behavior, and regulatory environments differ significantly from developed regions. It starts with localized market research and cultural adaptation, followed by modular product design to accommodate varying supply chain constraints. Parallel activities include securing local partnerships, navigating complex import regulations, and performing risk assessments on geopolitical factors. Marketing strategies are co-created with regional influencers and pilot campaigns are run in select urban and rural areas. Continuous feedback loops ensure iterative product refinement. The process culminates in scalable distribution network setup, compliance audits, and cross-border payment integration, ensuring a sustainable entry and growth within these dynamic markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Market_Research = Transition(label='Market Research')
Cultural_Study = Transition(label='Cultural Study')
Design_Adaptation = Transition(label='Design Adaptation')
Supply_Analysis = Transition(label='Supply Analysis')
Partner_Sourcing = Transition(label='Partner Sourcing')
Regulatory_Check = Transition(label='Regulatory Check')
Risk_Review = Transition(label='Risk Review')
Influencer_Setup = Transition(label='Influencer Setup')
Pilot_Launch = Transition(label='Pilot Launch')
Feedback_Loop = Transition(label='Feedback Loop')
Product_Tuning = Transition(label='Product Tuning')
Distribution_Map = Transition(label='Distribution Map')
Compliance_Audit = Transition(label='Compliance Audit')
Payment_Setup = Transition(label='Payment Setup')
Growth_Planning = Transition(label='Growth Planning')

# First phase: localized market research and cultural adaptation
phase1 = StrictPartialOrder(nodes=[Market_Research, Cultural_Study, Design_Adaptation, Supply_Analysis])
phase1.order.add_edge(Market_Research, Cultural_Study)
phase1.order.add_edge(Cultural_Study, Design_Adaptation)
phase1.order.add_edge(Cultural_Study, Supply_Analysis)

# Parallel activities after phase1: partner sourcing, regulatory check, risk review
phase2 = StrictPartialOrder(nodes=[Partner_Sourcing, Regulatory_Check, Risk_Review])
# all parallel, no edges

# Marketing strategies co-created with influencers and pilot launch
marketing = StrictPartialOrder(nodes=[Influencer_Setup, Pilot_Launch])
marketing.order.add_edge(Influencer_Setup, Pilot_Launch)

# Continuous feedback loop: Feedback Loop followed by Product Tuning, repeated until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Product_Tuning])

# The feedback loop happens after the pilot launch
phase3 = StrictPartialOrder(nodes=[marketing, loop])
phase3.order.add_edge(marketing, loop)

# Final phase: Distribution Map, Compliance Audit, Payment Setup, then Growth Planning
final_phase = StrictPartialOrder(nodes=[Distribution_Map, Compliance_Audit, Payment_Setup, Growth_Planning])
final_phase.order.add_edge(Distribution_Map, Compliance_Audit)
final_phase.order.add_edge(Distribution_Map, Payment_Setup)
final_phase.order.add_edge(Compliance_Audit, Growth_Planning)
final_phase.order.add_edge(Payment_Setup, Growth_Planning)

# Compose the entire process in their partial order
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, final_phase]
)

# Order edges linking phases:
root.order.add_edge(phase1, phase2)     # phase2 after phase1
root.order.add_edge(phase1, phase3)     # phase3 after phase1 (can start marketing after initial phases)
root.order.add_edge(phase2, phase3)     # marketing after partner sourcing/reg check/risk review
root.order.add_edge(phase3, final_phase) # final after marketing + loop