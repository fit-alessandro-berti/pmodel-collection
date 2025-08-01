# Generated from: cbc6659f-413a-4a87-9778-fd663670fed5.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts before acquisition by a museum. It includes provenance research, material analysis, expert consultations, and legal compliance checks. The workflow ensures that each artifact's origin is verified, authenticity confirmed through scientific and historical methods, and ownership legally cleared. Detailed documentation is maintained throughout, with cross-departmental reviews involving curators, legal advisors, and conservation specialists. The process concludes with final approval and cataloging for exhibit or storage, safeguarding heritage and minimizing acquisition risks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
provenance_check   = Transition(label='Provenance Check')
material_scan      = Transition(label='Material Scan')
carbon_dating      = Transition(label='Carbon Dating')
historical_match   = Transition(label='Historical Match')
expert_review      = Transition(label='Expert Review')
condition_report   = Transition(label='Condition Report')
restoration_plan   = Transition(label='Restoration Plan')
legal_audit        = Transition(label='Legal Audit')
ownership_verify   = Transition(label='Ownership Verify')
customs_clearance  = Transition(label='Customs Clearance')
risk_assessment    = Transition(label='Risk Assessment')
ethics_approval    = Transition(label='Ethics Approval')
final_approval     = Transition(label='Final Approval')
catalog_entry      = Transition(label='Catalog Entry')
exhibit_prep       = Transition(label='Exhibit Prep')

# Build a LOOP for repeated restoration and re‐reporting until no more restoration is needed
loop_repair = OperatorPOWL(
    operator=Operator.LOOP,
    children=[condition_report, restoration_plan]
)

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    carbon_dating,
    historical_match,
    expert_review,
    loop_repair,
    legal_audit,
    ownership_verify,
    customs_clearance,
    risk_assessment,
    ethics_approval,
    final_approval,
    catalog_entry,
    exhibit_prep
])

# Define the ordering
# Sequential workflow up to the repair loop
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, carbon_dating)
root.order.add_edge(carbon_dating, historical_match)
root.order.add_edge(historical_match, expert_review)
root.order.add_edge(expert_review, loop_repair)

# After the loop, legal chain vs. risk & ethics run in parallel, all converge to final approval
root.order.add_edge(loop_repair, legal_audit)
root.order.add_edge(loop_repair, risk_assessment)
root.order.add_edge(loop_repair, ethics_approval)

# Legal chain
root.order.add_edge(legal_audit, ownership_verify)
root.order.add_edge(ownership_verify, customs_clearance)
root.order.add_edge(customs_clearance, final_approval)

# Risk & ethics join final approval
root.order.add_edge(risk_assessment, final_approval)
root.order.add_edge(ethics_approval, final_approval)

# Final steps
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_prep)