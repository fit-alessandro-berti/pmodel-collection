# Generated from: aa004019-3106-4022-b2a3-0bdb5ea46f8e.json
# Description: This process involves the meticulous verification and authentication of ancient artifacts sourced from various archaeological sites before they are approved for museum exhibitions or private collections. It begins with initial provenance research, followed by multi-disciplinary scientific analysis, including radiocarbon dating and material composition tests. Expert consultations are held to evaluate stylistic and cultural attributes. The findings are compiled into a detailed report, which undergoes peer review. If discrepancies arise, further investigative activities such as microscopic imaging and comparative historical analysis are conducted. Once the artifact passes all authentication phases, legal documentation is prepared to certify its authenticity and ownership. Finally, the artifact is cataloged into the digital archive system and prepared for secure transportation to its display location, ensuring compliance with international cultural heritage laws and ethical guidelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
ProvenanceCheck = Transition(label='Provenance Check')
VisualInspection = Transition(label='Visual Inspection')
RadiocarbonTest = Transition(label='Radiocarbon Test')
MaterialAnalysis = Transition(label='Material Analysis')
StylisticReview = Transition(label='Stylistic Review')
ExpertConsult = Transition(label='Expert Consult')
ReportDraft = Transition(label='Report Draft')
PeerReview = Transition(label='Peer Review')
MicroscopicScan = Transition(label='Microscopic Scan')
HistoricalCompare = Transition(label='Historical Compare')
DiscrepancyAudit = Transition(label='Discrepancy Audit')
LegalPrepare = Transition(label='Legal Prepare')
CertificationIssue = Transition(label='Certification Issue')
CatalogEntry = Transition(label='Catalog Entry')
SecureTransport = Transition(label='Secure Transport')
ComplianceVerify = Transition(label='Compliance Verify')

# Scientific analysis parallel activities after Visual Inspection (RadiocarbonTest, MaterialAnalysis)
scientific_analysis = StrictPartialOrder(nodes=[RadiocarbonTest, MaterialAnalysis])

# Order: no ordering between these two, so concurrent.

# ExpertConsult and StylisticReview occur after scientific analysis
# But StylisticReview and ExpertConsult seem at same level
# Sequence looks like:
# ProvenanceCheck -> VisualInspection -> (RadiocarbonTest, MaterialAnalysis) concurrent
# -> StylisticReview -> ExpertConsult

# Construct the first part Partial Order
initial_po = StrictPartialOrder(nodes=[
    ProvenanceCheck, VisualInspection, scientific_analysis, StylisticReview, ExpertConsult
])
# Set order edges accordingly
initial_po.order.add_edge(ProvenanceCheck, VisualInspection)
initial_po.order.add_edge(VisualInspection, scientific_analysis)
initial_po.order.add_edge(scientific_analysis, StylisticReview)
initial_po.order.add_edge(StylisticReview, ExpertConsult)

# After ExpertConsult, go to ReportDraft and then PeerReview
report_po = StrictPartialOrder(nodes=[ReportDraft, PeerReview])
report_po.order.add_edge(ReportDraft, PeerReview)

# Discrepancy handling: if discrepancies arise after PeerReview:
# loop node of: execute DiscrepancyAudit,
# then decision to exit or execute microscopic imaging + historical compare and repeat.

# Discrepancy investigation partial order (concurrent):
discrepancy_investigation = StrictPartialOrder(nodes=[MicroscopicScan, HistoricalCompare])

# Loop node (* (DiscrepancyAudit, discrepancy_investigation))
discrepancy_loop = OperatorPOWL(operator=Operator.LOOP, children=[DiscrepancyAudit, discrepancy_investigation])

# So the structure after PeerReview:
# choice:
# - exit (continue workflow)
# - loop discrepancy_loop

# But the loop defines: execute DiscrepancyAudit, then choose to exit or perform discrepancy_investigation then DiscrepancyAudit again.

# So PeerReview -> discrepancy_loop
# after loop exits, proceed to LegalPrepare, CertificationIssue, CatalogEntry, SecureTransport, ComplianceVerify

# Sequence after loop exit:
final_po = StrictPartialOrder(nodes=[
    LegalPrepare, CertificationIssue, CatalogEntry, SecureTransport, ComplianceVerify
])
final_po.order.add_edge(LegalPrepare, CertificationIssue)
final_po.order.add_edge(CertificationIssue, CatalogEntry)
final_po.order.add_edge(CatalogEntry, SecureTransport)
final_po.order.add_edge(SecureTransport, ComplianceVerify)

# Connect PeerReview to discrepancy_loop and final_po
root_nodes = [initial_po, report_po, discrepancy_loop, final_po]

# Because initial_po ends at ExpertConsult
# report_po starts after ExpertConsult, so ExpertConsult -> ReportDraft
# report_po is ReportDraft -> PeerReview
# PeerReview -> discrepancy_loop and final_po

# We must link all sub-po and operators accordingly with StrictPartialOrder and edges

root = StrictPartialOrder(nodes=root_nodes)

# Set partial order edges between subcomponents:

# initial_po ends ExpertConsult; next is report_po's start ReportDraft
root.order.add_edge(initial_po, report_po)

# report_po ends at PeerReview, which goes to discrepancy_loop
root.order.add_edge(report_po, discrepancy_loop)

# discrepancy_loop ends loop exit, goes to final_po
root.order.add_edge(discrepancy_loop, final_po)