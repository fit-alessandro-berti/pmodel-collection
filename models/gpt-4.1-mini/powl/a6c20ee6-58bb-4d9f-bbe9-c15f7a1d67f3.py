# Generated from: a6c20ee6-58bb-4d9f-bbe9-c15f7a1d67f3.json
# Description: This process involves the thorough authentication and provenance verification of rare historical artifacts intended for museum acquisition or private collection. It includes multi-disciplinary expert evaluations, scientific testing like radiocarbon dating and spectrography, cross-referencing archival records, and secure chain-of-custody documentation. Additionally, it incorporates risk assessment related to forgery, legal ownership verification, and final certification issuance. The process requires coordination between curators, forensic scientists, historians, legal advisors, and logistics teams to ensure authenticity and compliance with international cultural heritage laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities as transitions
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Expert_Consult = Transition(label='Expert Consult')
Scientific_Test = Transition(label='Scientific Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Spectrograph_Scan = Transition(label='Spectrograph Scan')
Forgery_Assessment = Transition(label='Forgery Assessment')
Record_Crossref = Transition(label='Record Crossref')
Legal_Verify = Transition(label='Legal Verify')
Custody_Chain = Transition(label='Custody Chain')
Risk_Evaluate = Transition(label='Risk Evaluate')
Condition_Report = Transition(label='Condition Report')
Final_Approval = Transition(label='Final Approval')
Certification = Transition(label='Certification')
Secure_Transport = Transition(label='Secure Transport')
Archive_Update = Transition(label='Archive Update')

# Scientific_Test partial order: Radiocarbon_Date and Spectrograph_Scan concurrent inside Scientific_Test step
scientific_test_po = StrictPartialOrder(nodes=[Radiocarbon_Date, Spectrograph_Scan])
# no order edges between Radiocarbon_Date and Spectrograph_Scan (concurrent)

# The Scientific_Test activity is decomposed into these two concurrent tests, 
# model them as a partial order node
scientific_test_complex = StrictPartialOrder(nodes=[Scientific_Test, scientific_test_po])
# But this is not standard: Scientific_Test is the parent activity, we can model it as a PO with Radiocarbon_Date and Spectrograph_Scan concurrently after it:

# Instead, better to model:
# Scientific_Test is first, then Radiocarbon_Date and Spectrograph_Scan concurrently

scientific_test_subpo = StrictPartialOrder(nodes=[Radiocarbon_Date, Spectrograph_Scan])
# No order edges; concurrent

scientific_test_full_po = StrictPartialOrder(nodes=[Scientific_Test, Radiocarbon_Date, Spectrograph_Scan])
scientific_test_full_po.order.add_edge(Scientific_Test, Radiocarbon_Date)
scientific_test_full_po.order.add_edge(Scientific_Test, Spectrograph_Scan)

# The provenance verification involves Provenance_Check, Expert_Consult, Scientific_Test (with its subtasks), Record_Crossref
# Let's model the provenance verification subprocess as a partial order:
# Provenance_Check --> Expert_Consult --> Scientific_Test subtree --> Record_Crossref
# Radiocarbon_Date and Spectrograph_Scan concurrent as above.

# Let's integrate the Scientific_Test subtree in the order after Expert_Consult.

provenance_nodes = [Provenance_Check, Expert_Consult, scientific_test_full_po, Record_Crossref]
provenance_po = StrictPartialOrder(nodes=provenance_nodes)
provenance_po.order.add_edge(Provenance_Check, Expert_Consult)
provenance_po.order.add_edge(Expert_Consult, scientific_test_full_po)
provenance_po.order.add_edge(scientific_test_full_po, Record_Crossref)

# Risk assessment subprocess: Forgery_Assessment, Legal_Verify, Custody_Chain, Risk_Evaluate
# We can assume linear or partially ordered, let's assume:
# Forgery_Assessment and Legal_Verify concurrent
# Then both lead to Custody_Chain
# Then Risk_Evaluate after Custody_Chain

risk_nodes = [Forgery_Assessment, Legal_Verify, Custody_Chain, Risk_Evaluate]
risk_po = StrictPartialOrder(nodes=risk_nodes)
# add concurrency between Forgery_Assessment and Legal_Verify => no edge between them
risk_po.order.add_edge(Forgery_Assessment, Custody_Chain)
risk_po.order.add_edge(Legal_Verify, Custody_Chain)
risk_po.order.add_edge(Custody_Chain, Risk_Evaluate)

# Final steps partial order:
# Condition_Report --> Final_Approval --> Certification --> Secure_Transport --> Archive_Update

final_nodes = [Condition_Report, Final_Approval, Certification, Secure_Transport, Archive_Update]
final_po = StrictPartialOrder(nodes=final_nodes)
final_po.order.add_edge(Condition_Report, Final_Approval)
final_po.order.add_edge(Final_Approval, Certification)
final_po.order.add_edge(Certification, Secure_Transport)
final_po.order.add_edge(Secure_Transport, Archive_Update)

# The overall process:
# Initial_Review --> provenance_po & risk_po concurrent
# Both provenance_po and risk_po end before Condition_Report starts

# So, Initial_Review before Provenance and Risk
# Provenance and Risk parallel (no order between provenance_po and risk_po)
# Both provenance_po and risk_po before Condition_Report

root_nodes = [
    Initial_Review,
    provenance_po,
    risk_po,
    final_po
]

root = StrictPartialOrder(nodes=root_nodes)
# Initial_Review before provenance and risk
root.order.add_edge(Initial_Review, provenance_po)
root.order.add_edge(Initial_Review, risk_po)
# Provenance and risk before final steps starting with Condition_Report (which is first in final_po)
root.order.add_edge(provenance_po, final_po)
root.order.add_edge(risk_po, final_po)