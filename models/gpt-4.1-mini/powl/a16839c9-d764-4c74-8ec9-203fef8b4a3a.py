# Generated from: a16839c9-d764-4c74-8ec9-203fef8b4a3a.json
# Description: This complex process involves the verification and authentication of rare cultural artifacts intended for international exhibition. It begins with provenance research, followed by multi-tiered physical inspection using advanced imaging technologies. Expert historians and material scientists collaborate to assess authenticity, while legal compliance teams verify export regulations. Concurrently, a digital ledger records all findings for transparency. After validation, the items undergo preservation treatment tailored to their material composition. Finally, secure packaging and logistics coordination ensure safe delivery to exhibit venues while maintaining chain-of-custody documentation throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')
Image_Scan = Transition(label='Image Scan')
Material_Test = Transition(label='Material Test')
Expert_Review = Transition(label='Expert Review')
Legal_Audit = Transition(label='Legal Audit')
Ledger_Update = Transition(label='Ledger Update')
Condition_Report = Transition(label='Condition Report')
Preservation_Plan = Transition(label='Preservation Plan')
Treatment_Apply = Transition(label='Treatment Apply')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Custom_Clearance = Transition(label='Custom Clearance')
Chain_Verify = Transition(label='Chain Verify')
Exhibit_Setup = Transition(label='Exhibit Setup')
Final_Approval = Transition(label='Final Approval')

# Multi-tiered physical inspection as partial order:
# Image Scan -> Material Test
inspect_PO = StrictPartialOrder(nodes=[Image_Scan, Material_Test])
inspect_PO.order.add_edge(Image_Scan, Material_Test)

# Expert historians and material scientists assessment as parallel tasks after inspection:
# Expert Review and Legal Audit concurrent, but both after Material Test
# Ledger Update concurrent with Expert Review and Legal Audit
# So group Expert Review, Legal Audit, Ledger Update as PO, all after Material Test
assessment_PO = StrictPartialOrder(nodes=[Expert_Review, Legal_Audit, Ledger_Update])
# No order edges between these three => concurrent

# After Material Test, start assessment_PO concurrently with Ledger Update (Ledger Update included in assessment_PO)
# So Material Test --> assessment_PO concurrently

# Condition Report happens after Expert Review and Legal Audit (assuming they complete)
# So edges Expert Review -> Condition Report, Legal Audit -> Condition Report
condition_PO = StrictPartialOrder(nodes=[Condition_Report])
condition_PO_order = condition_PO.order
# To connect edges, condition_PO only one node, edges will be added in the root PO edges.

# Preservation Plan after Condition Report
# Treatment Apply after Preservation Plan
preservation_PO = StrictPartialOrder(nodes=[Preservation_Plan, Treatment_Apply])
preservation_PO.order.add_edge(Preservation_Plan, Treatment_Apply)

# Packaging Prep and Logistics Plan in parallel after Treatment Apply
packaging_logistics_PO = StrictPartialOrder(nodes=[Packaging_Prep, Logistics_Plan])
# No edges -> concurrent

# Custom Clearance and Chain Verify concurrent after Logistics Plan and Packaging Prep
custom_chain_PO = StrictPartialOrder(nodes=[Custom_Clearance, Chain_Verify])
# No edges -> concurrent

# Exhibit Setup and Final Approval sequential
final_PO = StrictPartialOrder(nodes=[Exhibit_Setup, Final_Approval])
final_PO.order.add_edge(Exhibit_Setup, Final_Approval)

# Build main PO root combining all parts
# Nodes in root:
nodes = [
    Provenance_Check,
    inspect_PO,
    assessment_PO,
    Condition_Report,
    preservation_PO,
    packaging_logistics_PO,
    custom_chain_PO,
    final_PO
]

root = StrictPartialOrder(nodes=nodes)

order = root.order
# Provenance Check -> inspect_PO (Image Scan + Material Test)
order.add_edge(Provenance_Check, inspect_PO)

# inspect_PO ends with Material Test, which triggers assessment_PO (Expert Review, Legal Audit, Ledger Update)
order.add_edge(inspect_PO, assessment_PO)

# Expert Review -> Condition Report, Legal Audit -> Condition Report
order.add_edge(assessment_PO, Condition_Report)
# Ledger Update is concurrent, no direct edge to Condition Report

# Condition Report -> Preservation Plan (part of preservation_PO)
order.add_edge(Condition_Report, preservation_PO)

# preservation_PO edges already connect Preservation Plan -> Treatment Apply inside preservation_PO,
# so no need to add edge here for that.

# Treatment Apply (part of preservation_PO) -> packaging_logistics_PO
order.add_edge(preservation_PO, packaging_logistics_PO)

# packaging_logistics_PO -> custom_chain_PO
order.add_edge(packaging_logistics_PO, custom_chain_PO)

# custom_chain_PO -> final_PO
order.add_edge(custom_chain_PO, final_PO)