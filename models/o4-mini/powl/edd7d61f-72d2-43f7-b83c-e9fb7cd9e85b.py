# Generated from: edd7d61f-72d2-43f7-b83c-e9fb7cd9e85b.json
# Description: This process involves the intricate verification and authentication of antique artifacts for museums, collectors, and auction houses. It includes provenance research, material analysis, and expert consultations to ensure the artifact's legitimacy and historical significance. The workflow requires coordination between historians, chemists, and appraisers, often involving cross-border documentation verification and advanced imaging techniques. The process culminates in a detailed certification report, which is critical for insurance, sale, or exhibition purposes, ensuring the artifact’s value and authenticity are thoroughly established through multidisciplinary validation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
InitialReview      = Transition(label='Initial Review')
ProvenanceCheck    = Transition(label='Provenance Check')
DocumentationVerify= Transition(label='Documentation Verify')
CrossBorderCheck   = Transition(label='Cross-Border Check')
MaterialScan       = Transition(label='Material Scan')
ChemicalTest       = Transition(label='Chemical Test')
ImagingCapture     = Transition(label='Imaging Capture')
ExpertConsult      = Transition(label='Expert Consult')
HistoricalMatch    = Transition(label='Historical Match')
ForgeryDetect      = Transition(label='Forgery Detect')
ConditionAssess    = Transition(label='Condition Assess')
ValueEstimate      = Transition(label='Value Estimate')
ReportDraft        = Transition(label='Report Draft')
ReportReview       = Transition(label='Report Review')
ClientApproval     = Transition(label='Client Approval')
CertificationIssue = Transition(label='Certification Issue')
ArchiveRecord      = Transition(label='Archive Record')

# Choice after expert consultation: match vs. detect
auth_choice = OperatorPOWL(operator=Operator.XOR, children=[HistoricalMatch, ForgeryDetect])

# Loop for drafting and reviewing the report until approval
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[ReportDraft, ReportReview])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    InitialReview, ProvenanceCheck,
    DocumentationVerify, CrossBorderCheck,
    MaterialScan, ChemicalTest, ImagingCapture,
    ExpertConsult, auth_choice,
    ConditionAssess, ValueEstimate,
    report_loop, ClientApproval,
    CertificationIssue, ArchiveRecord
])

# Define ordering constraints
root.order.add_edge(InitialReview, ProvenanceCheck)

# Provenance research and material analysis can proceed in parallel
root.order.add_edge(ProvenanceCheck, DocumentationVerify)
root.order.add_edge(ProvenanceCheck, CrossBorderCheck)
root.order.add_edge(ProvenanceCheck, MaterialScan)
root.order.add_edge(ProvenanceCheck, ChemicalTest)
root.order.add_edge(ProvenanceCheck, ImagingCapture)

# All analysis results feed into expert consultation
root.order.add_edge(DocumentationVerify, ExpertConsult)
root.order.add_edge(CrossBorderCheck, ExpertConsult)
root.order.add_edge(MaterialScan, ExpertConsult)
root.order.add_edge(ChemicalTest, ExpertConsult)
root.order.add_edge(ImagingCapture, ExpertConsult)

# Expert consult leads to exclusive choice
root.order.add_edge(ExpertConsult, auth_choice)

# After authenticity outcome, assess condition and estimate value
root.order.add_edge(auth_choice, ConditionAssess)
root.order.add_edge(ConditionAssess, ValueEstimate)

# Loop for drafting/review until ready for client approval
root.order.add_edge(ValueEstimate, report_loop)
root.order.add_edge(report_loop, ClientApproval)

# Finalization steps
root.order.add_edge(ClientApproval, CertificationIssue)
root.order.add_edge(CertificationIssue, ArchiveRecord)