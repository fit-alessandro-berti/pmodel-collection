# Generated from: a16839c9-d764-4c74-8ec9-203fef8b4a3a.json
# Description: This complex process involves the verification and authentication of rare cultural artifacts intended for international exhibition. It begins with provenance research, followed by multi-tiered physical inspection using advanced imaging technologies. Expert historians and material scientists collaborate to assess authenticity, while legal compliance teams verify export regulations. Concurrently, a digital ledger records all findings for transparency. After validation, the items undergo preservation treatment tailored to their material composition. Finally, secure packaging and logistics coordination ensure safe delivery to exhibit venues while maintaining chain-of-custody documentation throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
provenance_check   = Transition(label='Provenance Check')
image_scan         = Transition(label='Image Scan')
material_test      = Transition(label='Material Test')
expert_review      = Transition(label='Expert Review')
legal_audit        = Transition(label='Legal Audit')
ledger_update      = Transition(label='Ledger Update')
condition_report   = Transition(label='Condition Report')
preservation_plan  = Transition(label='Preservation Plan')
treatment_apply    = Transition(label='Treatment Apply')
packaging_prep     = Transition(label='Packaging Prep')
logistics_plan     = Transition(label='Logistics Plan')
custom_clearance   = Transition(label='Custom Clearance')
chain_verify       = Transition(label='Chain Verify')
exhibit_setup      = Transition(label='Exhibit Setup')
final_approval     = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance_check, image_scan, material_test, expert_review, legal_audit,
    ledger_update, condition_report, preservation_plan, treatment_apply,
    packaging_prep, logistics_plan, custom_clearance, chain_verify,
    exhibit_setup, final_approval
])

# Sequence of research, inspection, review, audit
root.order.add_edge(provenance_check, image_scan)
root.order.add_edge(image_scan, material_test)
root.order.add_edge(material_test, expert_review)
root.order.add_edge(expert_review, legal_audit)

# Ledger and chain-of-custody run concurrently after provenance
root.order.add_edge(provenance_check, ledger_update)
root.order.add_edge(provenance_check, chain_verify)

# Preservation treatment after validation
root.order.add_edge(legal_audit, condition_report)
root.order.add_edge(condition_report, preservation_plan)
root.order.add_edge(preservation_plan, treatment_apply)

# Packaging and logistics
root.order.add_edge(treatment_apply, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)

# Clearance, setup, final approval
root.order.add_edge(logistics_plan, custom_clearance)
root.order.add_edge(custom_clearance, exhibit_setup)
root.order.add_edge(exhibit_setup, final_approval)