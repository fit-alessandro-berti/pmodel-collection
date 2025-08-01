# Generated from: 05bc3c3e-1fa9-4008-8c38-a3afd15ba456.json
# Description: This process governs the complex lifecycle of negotiating, drafting, and executing patent licenses across multiple jurisdictions with varying legal frameworks. It involves initial patent portfolio analysis, competitive landscape mapping, jurisdiction-specific compliance checks, risk assessments, drafting multi-region agreements, coordinating with local counsel, managing translation and localization of documents, handling royalty tracking and audit processes, and ensuring timely renewals and dispute resolutions. The process demands continuous collaboration between legal, technical, and financial teams to ensure alignment with global IP strategies while mitigating infringement risks and maximizing licensing revenue streams. It concludes with post-license performance reviews and adaptation to evolving regulatory environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
PortfolioReview = Transition(label='Portfolio Review')
MarketScan = Transition(label='Market Scan')
ComplianceCheck = Transition(label='Compliance Check')
RiskAssess = Transition(label='Risk Assess')
DraftTerms = Transition(label='Draft Terms')
LocalCounsel = Transition(label='Local Counsel')
DocumentTranslate = Transition(label='Document Translate')
AgreementReview = Transition(label='Agreement Review')
NegotiationMeet = Transition(label='Negotiation Meet')
RoyaltySetup = Transition(label='Royalty Setup')
AuditPlan = Transition(label='Audit Plan')
PaymentTrack = Transition(label='Payment Track')
RenewalAlert = Transition(label='Renewal Alert')
DisputeManage = Transition(label='Dispute Manage')
PerformanceReview = Transition(label='Performance Review')
RegulationUpdate = Transition(label='Regulation Update')

# Model initial analysis phase in partial order
initial_analysis = StrictPartialOrder(nodes=[PortfolioReview, MarketScan])
# These two activities can run concurrently (no order edges)

# Compliance and risk assessment sequential after initial analysis but parallel among themselves
comp_risk = StrictPartialOrder(nodes=[ComplianceCheck, RiskAssess])
# ComplianceCheck and RiskAssess can run concurrently

# Connect initial analysis to compliance/risk (both must start after initial analysis)
initial_to_comp_risk = StrictPartialOrder(
    nodes=[initial_analysis, comp_risk]
)
# Connect initial analysis to both ComplianceCheck and RiskAssess
initial_to_comp_risk.order.add_edge(initial_analysis, comp_risk)  # Must execute initial_analysis before comp_risk

# Because initial_analysis and comp_risk are themselves StrictPartialOrders, we only connect their nodes appropriately below.

# But pm4py’s POWL expects nodes as Transition or OperatorPOWL, so we flatten the nested PO to single PO
# So instead, let's model a full PO for these steps:

# Define partial order for first steps:
# Portfolio Review and Market Scan concurrent
# Then Compliance Check and Risk Assess concurrent but after both initial activities
first_phase_nodes = [PortfolioReview, MarketScan, ComplianceCheck, RiskAssess]

first_phase = StrictPartialOrder(nodes=first_phase_nodes)
first_phase.order.add_edge(PortfolioReview, ComplianceCheck)
first_phase.order.add_edge(PortfolioReview, RiskAssess)
first_phase.order.add_edge(MarketScan, ComplianceCheck)
first_phase.order.add_edge(MarketScan, RiskAssess)
# So Compliance Check and Risk Assess both depend on Portfolio Review and Market Scan

# Drafting and review phase:
# Draft Terms, Local Counsel, Document Translate
# Likely Draft Terms first, followed by Local Counsel and Document Translate in parallel, then Agreement Review

draft_and_review = StrictPartialOrder(
    nodes=[DraftTerms, LocalCounsel, DocumentTranslate, AgreementReview]
)
draft_and_review.order.add_edge(DraftTerms, LocalCounsel)
draft_and_review.order.add_edge(DraftTerms, DocumentTranslate)
draft_and_review.order.add_edge(LocalCounsel, AgreementReview)
draft_and_review.order.add_edge(DocumentTranslate, AgreementReview)

# Negotiation phase: Negotiation Meet after Agreement Review
negotiation = StrictPartialOrder(
    nodes=[AgreementReview, NegotiationMeet]
)
negotiation.order.add_edge(AgreementReview, NegotiationMeet)

# Royalty and audit management phase:
# Royalty Setup -> Audit Plan -> Payment Track (sequential)
royalty_audit = StrictPartialOrder(
    nodes=[RoyaltySetup, AuditPlan, PaymentTrack]
)
royalty_audit.order.add_edge(RoyaltySetup, AuditPlan)
royalty_audit.order.add_edge(AuditPlan, PaymentTrack)

# Renewal and dispute management phase (could be concurrent)
renewal_dispute = StrictPartialOrder(
    nodes=[RenewalAlert, DisputeManage]
)
# No order edges: concurrent activities

# Post-license review and regulation update: Performance Review and Regulation Update concurrent
post_license = StrictPartialOrder(
    nodes=[PerformanceReview, RegulationUpdate]
)

# Define the main process partial order that coordinates the phases:
# Ordering main phases as:
# first_phase --> draft_and_review --> negotiation --> royalty_audit --> renewal_dispute --> post_license

root = StrictPartialOrder(
    nodes=[
        first_phase,
        draft_and_review,
        negotiation,
        royalty_audit,
        renewal_dispute,
        post_license
    ]
)

root.order.add_edge(first_phase, draft_and_review)
root.order.add_edge(draft_and_review, negotiation)
root.order.add_edge(negotiation, royalty_audit)
root.order.add_edge(royalty_audit, renewal_dispute)
root.order.add_edge(renewal_dispute, post_license)