# Generated from: 5a16a6c9-707a-427f-8a4a-2a7ba5cce5c5.json
# Description: This process involves the complex and meticulous steps required to authenticate rare historical artifacts before acquisition by a museum or private collector. It includes provenance verification, material analysis, expert consultations, and risk assessments to ensure authenticity and legal compliance. The workflow integrates interdisciplinary collaboration between historians, scientists, legal advisors, and logistics teams. Each phase requires specialized tools and documentation, culminating in a final appraisal and certification for acquisition or rejection. The process is atypical due to its reliance on diverse expertise and the high stakes involved in verifying unique cultural heritage items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Initial_Review = Transition(label='Initial Review')

# Provenance verification partial order and choices
Provenance_Check = Transition(label='Provenance Check')
Database_Search = Transition(label='Database Search')
Historical_Compare = Transition(label='Historical Compare')
Expert_Consult = Transition(label='Expert Consult')

# Material analysis partial order
Material_Scan = Transition(label='Material Scan')
Xray_Analysis = Transition(label='Xray Analysis')
Chemical_Test = Transition(label='Chemical Test')

# Legal and risk partial order
Legal_Audit = Transition(label='Legal Audit')
Risk_Assess = Transition(label='Risk Assess')

# Documentation partial order
Condition_Report = Transition(label='Condition Report')
Photograph_Item = Transition(label='Photograph Item')

# Final appraisal and certification partial order and choice
Appraisal_Draft = Transition(label='Appraisal Draft')
Final_Certification = Transition(label='Final Certification')

# Logistics and acquisition partial order and choice
Logistics_Plan = Transition(label='Logistics Plan')
Acquisition_Approval = Transition(label='Acquisition Approval')

# --- Build provenance verification subtree ---
# Expert_Consult depends on Historical_Compare
prov_po = StrictPartialOrder(nodes=[Provenance_Check, Database_Search, Historical_Compare, Expert_Consult])
prov_po.order.add_edge(Provenance_Check, Database_Search)
prov_po.order.add_edge(Database_Search, Historical_Compare)
prov_po.order.add_edge(Historical_Compare, Expert_Consult)

# --- Build material analysis subtree ---
material_po = StrictPartialOrder(nodes=[Material_Scan, Xray_Analysis, Chemical_Test])
material_po.order.add_edge(Material_Scan, Xray_Analysis)
material_po.order.add_edge(Xray_Analysis, Chemical_Test)

# --- Legal and risk subtree ---
legal_risk_po = StrictPartialOrder(nodes=[Legal_Audit, Risk_Assess])
# Assume Legal_Audit and Risk_Assess can run concurrently (no order)

# --- Documentation subtree ---
doc_po = StrictPartialOrder(nodes=[Condition_Report, Photograph_Item])
# Assume can be concurrent

# --- Final appraisal and certification choice ---
# Either proceed to Final Certification or loop back to Appraisal Draft for revision
appraisal_loop = OperatorPOWL(operator=Operator.LOOP, children=[Appraisal_Draft, SilentTransition()]) # permit skip revising draft
final_cert_choice = OperatorPOWL(operator=Operator.XOR, children=[Final_Certification, appraisal_loop])

# --- Logistics and acquisition choice ---
# Either approve acquisition or stop (skip)
acquisition_choice = OperatorPOWL(operator=Operator.XOR, children=[Acquisition_Approval, SilentTransition()])

# --- Combine all major phases as a partial order ---
root = StrictPartialOrder(nodes=[
    Initial_Review,
    prov_po,
    material_po,
    legal_risk_po,
    doc_po,
    final_cert_choice,
    Logistics_Plan,
    acquisition_choice
])

# Define order/dependencies between phases:

# Initial Review precedes provenance verification and material analysis in parallel
root.order.add_edge(Initial_Review, prov_po)
root.order.add_edge(Initial_Review, material_po)

# Provenance verification and material analysis must complete before legal & risk and documentation (concurrent)
root.order.add_edge(prov_po, legal_risk_po)
root.order.add_edge(material_po, legal_risk_po)
root.order.add_edge(prov_po, doc_po)
root.order.add_edge(material_po, doc_po)

# Legal & risk and documentation must complete before final appraisal and certification choice
root.order.add_edge(legal_risk_po, final_cert_choice)
root.order.add_edge(doc_po, final_cert_choice)

# Final appraisal/certification must complete before logistics plan
root.order.add_edge(final_cert_choice, Logistics_Plan)

# Logistics plan must complete before acquisition choice
root.order.add_edge(Logistics_Plan, acquisition_choice)