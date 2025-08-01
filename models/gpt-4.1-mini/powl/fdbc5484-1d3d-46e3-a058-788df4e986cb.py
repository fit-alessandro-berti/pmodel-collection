# Generated from: fdbc5484-1d3d-46e3-a058-788df4e986cb.json
# Description: This process involves the systematic valuation, negotiation, transfer, and legal safeguarding of intellectual assets between multiple corporate entities and individual creators. It begins with asset identification followed by detailed appraisal and risk assessment. Next, parties engage in multi-round negotiations facilitated by automated workflows and AI-driven market analysis. Upon agreement, contracts are drafted and digitally signed, incorporating dynamic royalty structures and usage restrictions. Post-transfer, continuous monitoring ensures compliance, and periodic audits verify asset integrity and usage rights. The process concludes with strategic adjustments based on market feedback and evolving intellectual property laws to maximize long-term value and minimize disputes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Asset_ID = Transition(label='Asset ID')
Value_Assess = Transition(label='Value Assess')
Risk_Scan = Transition(label='Risk Scan')
Market_Review = Transition(label='Market Review')
Initial_Offer = Transition(label='Initial Offer')
Counter_Offer = Transition(label='Counter Offer')
Negotiation = Transition(label='Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Legal_Review = Transition(label='Legal Review')
Digital_Sign = Transition(label='Digital Sign')
Royalty_Setup = Transition(label='Royalty Setup')
Transfer_Record = Transition(label='Transfer Record')
Compliance_Check = Transition(label='Compliance Check')
Audit_Schedule = Transition(label='Audit Schedule')
Market_Feedback = Transition(label='Market Feedback')
Strategy_Update = Transition(label='Strategy Update')

# Define negotiation loop as LOOP:
# Do (Initial Offer + Market Review + Negotiation)
# Then choose to exit or do Counter Offer again before the loop restarts
# But since also multi-round negotiation is "Initial Offer -> Counter Offer -> Negotiation" repeated

# Model multi-round negotiation:
# Body A: Initial_Offer -> Market_Review -> Negotiation
# Body B: Counter_Offer

body_A = StrictPartialOrder(nodes=[Initial_Offer, Market_Review, Negotiation])
body_A.order.add_edge(Initial_Offer, Market_Review)
body_A.order.add_edge(Market_Review, Negotiation)

body_B = Counter_Offer

negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_A, body_B])

# Contracting steps after negotiation_loop
contracting = StrictPartialOrder(nodes=[Contract_Draft, Legal_Review, Digital_Sign, Royalty_Setup])
contracting.order.add_edge(Contract_Draft, Legal_Review)
contracting.order.add_edge(Legal_Review, Digital_Sign)
contracting.order.add_edge(Digital_Sign, Royalty_Setup)

# Post transfer steps: Transfer_Record -> Compliance_Check -> Audit_Schedule
post_transfer = StrictPartialOrder(nodes=[Transfer_Record, Compliance_Check, Audit_Schedule])
post_transfer.order.add_edge(Transfer_Record, Compliance_Check)
post_transfer.order.add_edge(Compliance_Check, Audit_Schedule)

# Feedback and strategy after audits: Market_Feedback -> Strategy_Update
feedback_strategy = StrictPartialOrder(nodes=[Market_Feedback, Strategy_Update])
feedback_strategy.order.add_edge(Market_Feedback, Strategy_Update)

# Initial appraisal partial order: Asset_ID -> Value_Assess & Risk_Scan (concurrent)
appraisal = StrictPartialOrder(nodes=[Asset_ID, Value_Assess, Risk_Scan])
appraisal.order.add_edge(Asset_ID, Value_Assess)
appraisal.order.add_edge(Asset_ID, Risk_Scan)
# Value Assess and Risk Scan concurrent (no edge between them)

# Assemble main flow partial order:
# appraisal -> negotiation_loop -> contracting -> post_transfer -> feedback_strategy

root = StrictPartialOrder(nodes=[appraisal, negotiation_loop, contracting, post_transfer, feedback_strategy])
root.order.add_edge(appraisal, negotiation_loop)
root.order.add_edge(negotiation_loop, contracting)
root.order.add_edge(contracting, post_transfer)
root.order.add_edge(post_transfer, feedback_strategy)