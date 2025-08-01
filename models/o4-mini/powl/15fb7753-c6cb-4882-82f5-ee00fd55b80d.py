# Generated from: 15fb7753-c6cb-4882-82f5-ee00fd55b80d.json
# Description: This process outlines the detailed verification and authentication workflow for custom-made historical artifacts intended for museum acquisition. It involves multidisciplinary collaboration among historians, material scientists, forensic analysts, and legal advisors to ensure the artifact's origin, age, and ownership are accurately documented and verified. The steps include preliminary research, sample testing, chain-of-custody validation, provenance documentation, legal clearance, and final certification. The process ensures authenticity while adhering to international cultural property laws, minimizing risks of forgery and illicit trade. The workflow integrates both physical analysis and archival investigation, including interviews with previous owners and cross-referencing with historical databases, culminating in a comprehensive provenance report for museum curators and acquisition committees.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
InitialResearch    = Transition(label='Initial Research')
SampleTesting      = Transition(label='Sample Testing')
MaterialAnalysis   = Transition(label='Material Analysis')
ForensicImaging    = Transition(label='Forensic Imaging')
ForgeryScan        = Transition(label='Forgery Scan')
ConditionReport    = Transition(label='Condition Report')
HistoricalCheck    = Transition(label='Historical Check')
InterviewOwners    = Transition(label='Interview Owners')
DatabaseCrossref   = Transition(label='Database Crossref')
ChainValidation    = Transition(label='Chain Validation')
OwnershipAudit     = Transition(label='Ownership Audit')
ProvenanceDraft    = Transition(label='Provenance Draft')
ComplianceCheck    = Transition(label='Compliance Check')
LegalReview        = Transition(label='Legal Review')
FinalCertification = Transition(label='Final Certification')
ReportDelivery     = Transition(label='Report Delivery')

# Physical‐analysis loop: do Sample Testing, then either exit or perform Material Analysis → Forensic Imaging → Forgery Scan and repeat
loop_body = StrictPartialOrder(nodes=[MaterialAnalysis, ForensicImaging, ForgeryScan])
loop_body.order.add_edge(MaterialAnalysis, ForensicImaging)
loop_body.order.add_edge(ForensicImaging, ForgeryScan)

physical_loop = OperatorPOWL(operator=Operator.LOOP, children=[SampleTesting, loop_body])

# Archival investigation: Historical Check, Interview Owners, Database Crossref in parallel
archival = StrictPartialOrder(nodes=[HistoricalCheck, InterviewOwners, DatabaseCrossref])
# (no edges → fully concurrent)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    InitialResearch,
    physical_loop,
    ConditionReport,
    HistoricalCheck,
    InterviewOwners,
    DatabaseCrossref,
    ChainValidation,
    OwnershipAudit,
    ProvenanceDraft,
    ComplianceCheck,
    LegalReview,
    FinalCertification,
    ReportDelivery
])

# Define the control‐flow dependencies
root.order.add_edge(InitialResearch,    physical_loop)
root.order.add_edge(physical_loop,      ConditionReport)

root.order.add_edge(ConditionReport,    ChainValidation)
root.order.add_edge(ChainValidation,    OwnershipAudit)

# Provenance draft waits for both ownership audit and all archival tasks
root.order.add_edge(OwnershipAudit,     ProvenanceDraft)
root.order.add_edge(HistoricalCheck,    ProvenanceDraft)
root.order.add_edge(InterviewOwners,    ProvenanceDraft)
root.order.add_edge(DatabaseCrossref,   ProvenanceDraft)

root.order.add_edge(ProvenanceDraft,    ComplianceCheck)
root.order.add_edge(ComplianceCheck,    LegalReview)
root.order.add_edge(LegalReview,        FinalCertification)
root.order.add_edge(FinalCertification, ReportDelivery)