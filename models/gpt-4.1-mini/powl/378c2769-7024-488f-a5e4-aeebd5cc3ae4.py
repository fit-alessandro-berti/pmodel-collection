# Generated from: 378c2769-7024-488f-a5e4-aeebd5cc3ae4.json
# Description: This process involves the authentication and validation of unique cultural artifacts destined for international auction. It begins with initial provenance research followed by multi-expert verification, material composition analysis, and advanced imaging inspections. Concurrently, legal compliance checks for cross-border transfers are conducted. If discrepancies arise, iterative consultations with historians occur. Once authenticated, the artifact undergoes secure packaging, insurance valuation, and digitized certification. Finally, the artifact is logged into a blockchain registry to ensure immutable provenance records before shipment to the auction house, ensuring transparency, security, and authenticity verification throughout the entire lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ProvenanceCheck = Transition(label='Provenance Check')
ExpertReview = Transition(label='Expert Review')
MaterialScan = Transition(label='Material Scan')
ImagingAnalysis = Transition(label='Imaging Analysis')
LegalAudit = Transition(label='Legal Audit')
DiscrepancyFlag = Transition(label='Discrepancy Flag')
HistoriansConsult = Transition(label='Historians Consult')
ReVerification = Transition(label='Re-Verification')
SecurePacking = Transition(label='Secure Packing')
InsuranceQuote = Transition(label='Insurance Quote')
ValueAssessment = Transition(label='Value Assessment')
CertificationIssue = Transition(label='Certification Issue')
BlockchainEntry = Transition(label='Blockchain Entry')
ShipmentPrep = Transition(label='Shipment Prep')
FinalLogging = Transition(label='Final Logging')

skip = SilentTransition()

# Loop for discrepancy consultation and re-verification
# Loop body: first: DiscrepancyFlag, then choice exit or (HistoriansConsult + ReVerification)
# Loop structure: *(DiscrepancyFlag, PO(HistoriansConsult-->ReVerification))
loop_body = StrictPartialOrder(nodes=[HistoriansConsult, ReVerification])
loop_body.order.add_edge(HistoriansConsult, ReVerification)
exit_or_loop = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_body])
discrepancy_loop = OperatorPOWL(operator=Operator.LOOP, children=[DiscrepancyFlag, exit_or_loop])

# Concurrent multi-expert verification: ExpertReview, MaterialScan, ImagingAnalysis (concurrent)
multi_expert = StrictPartialOrder(nodes=[ExpertReview, MaterialScan, ImagingAnalysis])

# Include LegalAudit concurrent with multi-expert phase
concurrent_checks = StrictPartialOrder(nodes=[multi_expert, LegalAudit])
# No order between multi_expert and LegalAudit => concurrent

# Sequencing ProvenanceCheck --> concurrent_checks --> discrepancy_loop
phase1 = StrictPartialOrder(nodes=[ProvenanceCheck, concurrent_checks])
phase1.order.add_edge(ProvenanceCheck, concurrent_checks)

phase2 = StrictPartialOrder(nodes=[phase1, discrepancy_loop])
phase2.order.add_edge(phase1, discrepancy_loop)

# After loop, re-verification synchronizes again before the next phase
# The loop ends when discrepancy resolved; next phase starts after loop

# Next phase: secure packing, insurance quote, value assessment, certification issue (all sequential)
pack_insure_seq = StrictPartialOrder(nodes=[
    SecurePacking,
    InsuranceQuote,
    ValueAssessment,
    CertificationIssue
])
pack_insure_seq.order.add_edge(SecurePacking, InsuranceQuote)
pack_insure_seq.order.add_edge(InsuranceQuote, ValueAssessment)
pack_insure_seq.order.add_edge(ValueAssessment, CertificationIssue)

# Final sequence: after pack_insure_seq:
# BlockchainEntry --> ShipmentPrep --> FinalLogging
final_seq = StrictPartialOrder(nodes=[BlockchainEntry, ShipmentPrep, FinalLogging])
final_seq.order.add_edge(BlockchainEntry, ShipmentPrep)
final_seq.order.add_edge(ShipmentPrep, FinalLogging)

# Combine packaging and final sequence sequentially
post_auth_seq = StrictPartialOrder(nodes=[pack_insure_seq, final_seq])
post_auth_seq.order.add_edge(pack_insure_seq, final_seq)

# Full process ordering: phase2 --> post_auth_seq
root = StrictPartialOrder(nodes=[phase2, post_auth_seq])
root.order.add_edge(phase2, post_auth_seq)