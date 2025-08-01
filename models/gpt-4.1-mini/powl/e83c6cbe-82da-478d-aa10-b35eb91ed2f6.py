# Generated from: e83c6cbe-82da-478d-aa10-b35eb91ed2f6.json
# Description: This process involves the multi-layered verification and authentication of ancient artifacts before acquisition or exhibition. It begins with initial provenance research, followed by scientific material analysis, stylistic comparison, and expert consultations. Legal clearance and ethical sourcing checks are conducted alongside insurance valuation and risk assessment. The process also includes digital archiving, replica creation for display, and preparation for transport under controlled conditions. Finally, the artifact undergoes a final review meeting before formal cataloging and public announcement, ensuring authenticity, legality, and preservation standards are met comprehensively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ProvenanceCheck = Transition(label='Provenance Check')
MaterialTesting = Transition(label='Material Testing')
StylisticReview = Transition(label='Stylistic Review')
ExpertPanel = Transition(label='Expert Panel')
LegalClearance = Transition(label='Legal Clearance')
EthicsAudit = Transition(label='Ethics Audit')
InsuranceQuote = Transition(label='Insurance Quote')
RiskAssess = Transition(label='Risk Assess')
DigitalArchive = Transition(label='Digital Archive')
ReplicaBuild = Transition(label='Replica Build')
TransportPrep = Transition(label='Transport Prep')
FinalReview = Transition(label='Final Review')
CatalogEntry = Transition(label='Catalog Entry')
PublicNotice = Transition(label='Public Notice')
ConditionReport = Transition(label='Condition Report')

# Step 1: Initial provenance research
# Step 2: Scientific material analysis, stylistic comparison, expert consultations in parallel
step2 = StrictPartialOrder(nodes=[MaterialTesting, StylisticReview, ExpertPanel])

# Step 3: Legal clearance and ethics audit in parallel
legal_ethics = StrictPartialOrder(nodes=[LegalClearance, EthicsAudit])

# Step 4: Insurance quotation and risk assessment in parallel
insurance_risk = StrictPartialOrder(nodes=[InsuranceQuote, RiskAssess])

# Step 5: Legal clearance + ethics audit must complete before insurance + risk start
legal_and_beyond = StrictPartialOrder(nodes=[legal_ethics, insurance_risk])
legal_and_beyond.order.add_edge(legal_ethics, insurance_risk)

# Step 6: Digital archiving, replica build, transport prep in parallel
post_checks = StrictPartialOrder(nodes=[DigitalArchive, ReplicaBuild, TransportPrep])

# Step 7: Final review meeting before formal cataloging and public notice
final_sequence = StrictPartialOrder(nodes=[FinalReview, CatalogEntry, PublicNotice])
final_sequence.order.add_edge(FinalReview, CatalogEntry)
final_sequence.order.add_edge(CatalogEntry, PublicNotice)

# Step 8: Condition report (integrity check) presumably near final steps, 
# place it concurrent with final review but before cataloging?
# More reasonable: Condition Report just before Final Review (like final check)
cond_and_final = StrictPartialOrder(nodes=[ConditionReport, FinalReview])
cond_and_final.order.add_edge(ConditionReport, FinalReview)

# Step 9: Compose the first block:
# Provenance Check then parallel step2 (material, stylistic, expert)
first_part = StrictPartialOrder(nodes=[ProvenanceCheck, step2])
first_part.order.add_edge(ProvenanceCheck, step2)

# Step 10: Compose after step2 the legal and ethics checks flows:
first_part_2 = StrictPartialOrder(nodes=[first_part, legal_and_beyond])
first_part_2.order.add_edge(first_part, legal_and_beyond)

# Step 11: After insurance_risk (part of legal_and_beyond) finish, then post_checks run
# Since legal_and_beyond is a partial order combining legal_ethics and insurance_risk,
# and legal_and_beyond.order has legal_ethics --> insurance_risk
# We add that post_checks depends on insurance_risk to finish.
# To keep dependencies simple, for the entire legal_and_beyond completion
# post_checks depends on insurance_risk (last activity)
legal_and_beyond_last = insurance_risk  # after insurance_risk finishes

first_and_post = StrictPartialOrder(nodes=[first_part_2, post_checks])
first_and_post.order.add_edge(first_part_2, post_checks)

# Step 12: Then condition report + final review + catalog + public notice in order
final_part = StrictPartialOrder(nodes=[cond_and_final, CatalogEntry, PublicNotice])
# cond_and_final = ConditionReport -> FinalReview
# Add FinalReview -> CatalogEntry and CatalogEntry -> PublicNotice
final_part.order.add_edge(cond_and_final, CatalogEntry)
final_part.order.add_edge(CatalogEntry, PublicNotice)

# Step 13: Link post_checks to cond_and_final (i.e. final checks start after post checks)
final_full = StrictPartialOrder(nodes=[post_checks, cond_and_final, CatalogEntry, PublicNotice])
final_full.order.add_edge(post_checks, cond_and_final)
final_full.order.add_edge(cond_and_final, CatalogEntry)
final_full.order.add_edge(CatalogEntry, PublicNotice)

# To avoid duplication, we use final_full as last sequence.

# Final root: ProvenanceCheck->step2->legal_and_beyond->post_checks->final sequence

root = StrictPartialOrder(nodes=[
    ProvenanceCheck,
    step2,
    legal_and_beyond,
    post_checks,
    cond_and_final,
    CatalogEntry,
    PublicNotice
])

root.order.add_edge(ProvenanceCheck, step2)
root.order.add_edge(step2, legal_and_beyond)
root.order.add_edge(legal_and_beyond, post_checks)
root.order.add_edge(post_checks, cond_and_final)
root.order.add_edge(cond_and_final, CatalogEntry)
root.order.add_edge(CatalogEntry, PublicNotice)