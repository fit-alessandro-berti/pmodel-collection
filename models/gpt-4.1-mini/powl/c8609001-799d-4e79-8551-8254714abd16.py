# Generated from: c8609001-799d-4e79-8551-8254714abd16.json
# Description: This process involves the detailed authentication and verification of antique assets before acquisition or sale. It includes provenance research, material analysis, expert consultations, and risk assessment to ensure the asset's legitimacy and value. The process incorporates cross-referencing historical databases, coordinating with multiple stakeholders, and finalizing legal documentation to mitigate fraud and optimize investment decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Test = Transition(label='Material Test')
Expert_Consult = Transition(label='Expert Consult')
Database_Search = Transition(label='Database Search')
Condition_Report = Transition(label='Condition Report')
Risk_Assess = Transition(label='Risk Assess')
Market_Analysis = Transition(label='Market Analysis')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Legal_Review = Transition(label='Legal Review')
Insurance_Quote = Transition(label='Insurance Quote')
Price_Negotiation = Transition(label='Price Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Final_Approval = Transition(label='Final Approval')
Asset_Registration = Transition(label='Asset Registration')

# First partial order: initial verifications in parallel or partially ordered
# Provenance_Check and Material_Test and Expert_Consult are part of detailed authentication
# Provenance_Check includes Database_Search and Condition_Report as predecessors

# Order: Initial_Review -> Provenance_Check -> {Database_Search, Condition_Report (concurrent)} -> Material_Test + Expert_Consult (concurrent)
# Risk_Assess after these
# Market_Analysis and Stakeholder_Meet concurrent after Risk_Assess
# Then Legal_Review and Insurance_Quote concurrent
# Price_Negotiation after them
# Contract_Draft after Price_Negotiation
# Final_Approval after Contract_Draft
# Asset_Registration last

# Build PO for Provenance_Check dependencies:
pc_sub = StrictPartialOrder(nodes=[Provenance_Check, Database_Search, Condition_Report])
pc_sub.order.add_edge(Provenance_Check, Database_Search)
pc_sub.order.add_edge(Provenance_Check, Condition_Report)

# Authentication partial order includes pc_sub, Material_Test and Expert_Consult
auth_nodes = [pc_sub, Material_Test, Expert_Consult]
auth_po = StrictPartialOrder(nodes=auth_nodes)
# Provenance_Check(path) must finish before Material_Test and Expert_Consult
auth_po.order.add_edge(pc_sub, Material_Test)
auth_po.order.add_edge(pc_sub, Expert_Consult)

# Risk assessment after authentication
risk_part = StrictPartialOrder(nodes=[auth_po, Risk_Assess])
risk_part.order.add_edge(auth_po, Risk_Assess)

# Market_Analysis and Stakeholder_Meet concurrent after Risk_Assess
market_stake = StrictPartialOrder(nodes=[Market_Analysis, Stakeholder_Meet])

# After Risk_Assess -> market_stake concurrent
post_risk = StrictPartialOrder(nodes=[risk_part, market_stake])
post_risk.order.add_edge(risk_part, market_stake)

# Legal_Review and Insurance_Quote concurrent after market_stake
legal_ins = StrictPartialOrder(nodes=[Legal_Review, Insurance_Quote])

# Order: market_stake -> legal_ins
legal_part = StrictPartialOrder(nodes=[post_risk, legal_ins])
legal_part.order.add_edge(post_risk, legal_ins)

# Price negotiation after legal and insurance
price_neg = StrictPartialOrder(nodes=[legal_part, Price_Negotiation])
price_neg.order.add_edge(legal_part, Price_Negotiation)

# Contract draft after price negotiation
contract_part = StrictPartialOrder(nodes=[price_neg, Contract_Draft])
contract_part.order.add_edge(price_neg, Contract_Draft)

# Final approval after contract draft
final_approval_part = StrictPartialOrder(nodes=[contract_part, Final_Approval])
final_approval_part.order.add_edge(contract_part, Final_Approval)

# Asset registration last
root = StrictPartialOrder(nodes=[Initial_Review, final_approval_part, Asset_Registration])

# Initial_Review before everything else
root.order.add_edge(Initial_Review, final_approval_part)
# Final_Approval before Asset_Registration
root.order.add_edge(final_approval_part, Asset_Registration)