# Generated from: 5a16a6c9-707a-427f-8a4a-2a7ba5cce5c5.json
# Description: This process involves the complex and meticulous steps required to authenticate rare historical artifacts before acquisition by a museum or private collector. It includes provenance verification, material analysis, expert consultations, and risk assessments to ensure authenticity and legal compliance. The workflow integrates interdisciplinary collaboration between historians, scientists, legal advisors, and logistics teams. Each phase requires specialized tools and documentation, culminating in a final appraisal and certification for acquisition or rejection. The process is atypical due to its reliance on diverse expertise and the high stakes involved in verifying unique cultural heritage items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Initial_Review     = Transition(label='Initial Review')
Provenance_Check   = Transition(label='Provenance Check')
Database_Search    = Transition(label='Database Search')
Historical_Compare = Transition(label='Historical Compare')
Material_Scan      = Transition(label='Material Scan')
Xray_Analysis      = Transition(label='Xray Analysis')
Chemical_Test      = Transition(label='Chemical Test')
Condition_Report   = Transition(label='Condition Report')
Photograph_Item    = Transition(label='Photograph Item')
Expert_Consult     = Transition(label='Expert Consult')
Legal_Audit        = Transition(label='Legal Audit')
Risk_Assess        = Transition(label='Risk Assess')
Appraisal_Draft    = Transition(label='Appraisal Draft')
Final_Certification= Transition(label='Final Certification')
Logistics_Plan     = Transition(label='Logistics Plan')
Acquisition_Approval = Transition(label='Acquisition Approval')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    Initial_Review,
    Provenance_Check, Database_Search, Historical_Compare,
    Material_Scan, Xray_Analysis, Chemical_Test, Condition_Report, Photograph_Item,
    Expert_Consult,
    Legal_Audit, Risk_Assess,
    Appraisal_Draft, Final_Certification, Logistics_Plan, Acquisition_Approval
])

# Initial Review precedes all analysis/verification phases
root.order.add_edge(Initial_Review, Provenance_Check)
root.order.add_edge(Initial_Review, Material_Scan)
root.order.add_edge(Initial_Review, Expert_Consult)
root.order.add_edge(Initial_Review, Legal_Audit)

# Provenance verification branch
root.order.add_edge(Provenance_Check, Database_Search)
root.order.add_edge(Provenance_Check, Historical_Compare)

# Material analysis branch: scan → x‐ray → chemical
root.order.add_edge(Material_Scan, Xray_Analysis)
root.order.add_edge(Xray_Analysis, Chemical_Test)

# Condition reporting depends on chemical test
root.order.add_edge(Chemical_Test, Condition_Report)
root.order.add_edge(Chemical_Test, Photograph_Item)

# Legal compliance branch: audit → risk assessment
root.order.add_edge(Legal_Audit, Risk_Assess)

# All deliverables feed into the appraisal draft
for predecessor in [
    Database_Search, Historical_Compare,
    Expert_Consult, Risk_Assess,
    Condition_Report, Photograph_Item
]:
    root.order.add_edge(predecessor, Appraisal_Draft)

# Final stages: draft → certification → logistics → approval
root.order.add_edge(Appraisal_Draft, Final_Certification)
root.order.add_edge(Final_Certification, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Acquisition_Approval)