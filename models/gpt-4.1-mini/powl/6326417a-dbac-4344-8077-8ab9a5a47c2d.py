# Generated from: 6326417a-dbac-4344-8077-8ab9a5a47c2d.json
# Description: This process involves the authentication of rare cultural artifacts through a multi-step approach integrating scientific analysis, provenance verification, expert consultation, and legal compliance checks. Initially, the artifact undergoes non-invasive material scanning to detect composition and condition. Concurrently, provenance data is gathered from historical records and previous ownership chains. Specialists in art history and archaeology review the combined data to assess authenticity. Legal teams verify export and import permissions to ensure compliance with international heritage laws. Finally, a digital certificate of authenticity is generated and archived, while stakeholders receive a comprehensive report. This atypical workflow ensures the artifact's legitimacy, protects cultural heritage, and supports collectors' and institutions' trust in acquisitions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
Initial_Scan = Transition(label='Initial Scan')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Ownership_Trace = Transition(label='Ownership Trace')
Historical_Review = Transition(label='Historical Review')
Expert_Consult = Transition(label='Expert Consult')
Condition_Report = Transition(label='Condition Report')
Legal_Verify = Transition(label='Legal Verify')
Export_Audit = Transition(label='Export Audit')
Import_Audit = Transition(label='Import Audit')
Fraud_Screening = Transition(label='Fraud Screening')
Data_Consolidate = Transition(label='Data Consolidate')
Certificate_Gen = Transition(label='Certificate Gen')
Report_Draft = Transition(label='Report Draft')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Archive_Record = Transition(label='Archive Record')

# Material scanning branch: Initial Scan --> Material Test
material_branch = StrictPartialOrder(nodes=[Initial_Scan, Material_Test])
material_branch.order.add_edge(Initial_Scan, Material_Test)

# Provenance branch: Provenance Check --> Ownership Trace
provenance_branch = StrictPartialOrder(nodes=[Provenance_Check, Ownership_Trace])
provenance_branch.order.add_edge(Provenance_Check, Ownership_Trace)

# Combine scanning and provenance branches concurrently
scan_and_provenance = StrictPartialOrder(
    nodes=[material_branch, provenance_branch]
)
# no order edges - these two are concurrent

# Specialist review branch: Historical Review --> Expert Consult
specialist_review = StrictPartialOrder(nodes=[Historical_Review, Expert_Consult])
specialist_review.order.add_edge(Historical_Review, Expert_Consult)

# Condition report (after material test)
condition_report = Condition_Report

# Legal branch: Legal Verify --> Export Audit --> Import Audit --> Fraud Screening
legal_branch = StrictPartialOrder(
    nodes=[Legal_Verify, Export_Audit, Import_Audit, Fraud_Screening]
)
legal_branch.order.add_edge(Legal_Verify, Export_Audit)
legal_branch.order.add_edge(Export_Audit, Import_Audit)
legal_branch.order.add_edge(Import_Audit, Fraud_Screening)

# Data Consolidation follows specialist_review, condition report, and legal checks
# So, these three must complete before Data_Consolidate

# We build a PO where specialist_review, condition_report, legal_branch are concurrent,
# Data_Consolidate after them all

# Put specialist_review, condition_report, legal_branch concurrent:
pre_consolidate = StrictPartialOrder(
    nodes=[specialist_review, condition_report, legal_branch]
)
# no order edges among these 3 - concurrency

# Create the full order: scan_and_provenance --> pre_consolidate --> Data_Consolidate
# So Data_Consolidate depends on all three (specialist_review, condition_report, legal_branch)
# and pre_consolidate depends on scan_and_provenance

# We'll combine all in one root PO:
# Nodes: scan_and_provenance, pre_consolidate, Data_Consolidate, Certificate_Gen, Report_Draft, Stakeholder_Notify, Archive_Record

root = StrictPartialOrder(
    nodes=[
        scan_and_provenance,
        pre_consolidate,
        Data_Consolidate,
        Certificate_Gen,
        Report_Draft,
        Stakeholder_Notify,
        Archive_Record,
    ]
)

# Define edges:

# scan_and_provenance before pre_consolidate
root.order.add_edge(scan_and_provenance, pre_consolidate)
# pre_consolidate before Data_Consolidate
root.order.add_edge(pre_consolidate, Data_Consolidate)
# Data_Consolidate before Certificate_Gen and Report_Draft (these two concurrent)
root.order.add_edge(Data_Consolidate, Certificate_Gen)
root.order.add_edge(Data_Consolidate, Report_Draft)
# Certificate_Gen and Report_Draft before Stakeholder_Notify and Archive_Record (both concurrent)
root.order.add_edge(Certificate_Gen, Stakeholder_Notify)
root.order.add_edge(Certificate_Gen, Archive_Record)
root.order.add_edge(Report_Draft, Stakeholder_Notify)
root.order.add_edge(Report_Draft, Archive_Record)